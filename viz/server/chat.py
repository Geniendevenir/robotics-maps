import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

from viz.server import tools


SERVER_ROOT = Path(__file__).resolve().parent
SYSTEM_PROMPT = (SERVER_ROOT / "prompt.md").read_text(encoding="utf-8")
DEFAULT_MODEL = "claude-sonnet-4-5"
MAX_TOOL_ROUNDS = 8

TOOL_SCHEMAS = [
    {"name": "overview", "description": "Summarize counts and groups in both maps.", "input_schema": {"type": "object", "properties": {}}},
    {"name": "search_nodes", "description": "Search map nodes by text and filters.", "input_schema": {"type": "object", "properties": {"query": {"type": "string"}, "type": {"type": "string"}, "branch": {"type": "string"}, "filters": {"type": "object"}, "limit": {"type": "integer"}}, "required": []}},
    {"name": "get_node", "description": "Get a map node and its linked neighbors.", "input_schema": {"type": "object", "properties": {"id_or_name": {"type": "string"}}, "required": ["id_or_name"]}},
    {"name": "get_neighbors", "description": "Traverse linked nodes around one node.", "input_schema": {"type": "object", "properties": {"id": {"type": "string"}, "depth": {"type": "integer"}}, "required": ["id"]}},
    {"name": "list_groups", "description": "List saved node groups.", "input_schema": {"type": "object", "properties": {}}},
    {"name": "create_group", "description": "Create a saved group of nodes.", "input_schema": {"type": "object", "properties": {"name": {"type": "string"}, "description": {"type": "string"}, "node_ids": {"type": "array", "items": {"type": "string"}}, "color": {"type": "string"}}, "required": ["name"]}},
    {"name": "add_to_group", "description": "Add nodes to a saved group.", "input_schema": {"type": "object", "properties": {"group_id": {"type": "string"}, "node_ids": {"type": "array", "items": {"type": "string"}},}, "required": ["group_id", "node_ids"]}},
    {"name": "remove_from_group", "description": "Remove nodes from a saved group.", "input_schema": {"type": "object", "properties": {"group_id": {"type": "string"}, "node_ids": {"type": "array", "items": {"type": "string"}}}, "required": ["group_id", "node_ids"]}},
    {"name": "rename_group", "description": "Rename a group or change its description.", "input_schema": {"type": "object", "properties": {"group_id": {"type": "string"}, "name": {"type": "string"}, "description": {"type": "string"}}, "required": ["group_id"]}},
    {"name": "delete_group", "description": "Delete a saved group.", "input_schema": {"type": "object", "properties": {"group_id": {"type": "string"}}, "required": ["group_id"]}},
    {"name": "focus_node", "description": "Focus and select a node in the visualizer.", "input_schema": {"type": "object", "properties": {"id": {"type": "string"}}, "required": ["id"]}},
    {"name": "highlight_nodes", "description": "Highlight nodes in the visualizer.", "input_schema": {"type": "object", "properties": {"ids": {"type": "array", "items": {"type": "string"}}}, "required": ["ids"]}},
    {"name": "set_filters", "description": "Replace filters for one map view.", "input_schema": {"type": "object", "properties": {"view": {"type": "string"}, "filters": {"type": "object"}}, "required": ["view", "filters"]}},
    {"name": "show_group", "description": "Filter the current view to a saved group.", "input_schema": {"type": "object", "properties": {"group_id": {"type": "string"}}, "required": ["group_id"]}},
    {"name": "switch_view", "description": "Switch between the graph and map.", "input_schema": {"type": "object", "properties": {"view": {"type": "string"}}, "required": ["view"]}},
]

TOOL_FUNCTIONS = {
    "overview": tools.overview,
    "search_nodes": tools.search_nodes,
    "get_node": tools.get_node,
    "get_neighbors": tools.get_neighbors,
    "list_groups": tools.list_groups,
    "create_group": tools.create_group,
    "add_to_group": tools.add_to_group,
    "remove_from_group": tools.remove_from_group,
    "rename_group": tools.rename_group,
    "delete_group": tools.delete_group,
    "focus_node": tools.focus_node,
    "highlight_nodes": tools.highlight_nodes,
    "set_filters": tools.set_filters,
    "show_group": tools.show_group,
    "switch_view": tools.switch_view,
}


def backend_info():
    if os.environ.get("ANTHROPIC_API_KEY"):
        return "anthropic", os.environ.get("VIZ_CHAT_MODEL", DEFAULT_MODEL)
    if shutil.which("claude"):
        return "claude-cli", "Claude Code CLI"
    return "none", "none"


def _contextual_messages(messages, context):
    result = [{"role": item["role"], "content": item["content"]} for item in messages]
    context_text = "View context:\n" + json.dumps(context or {}, ensure_ascii=False) + "\n\n"
    for item in reversed(result):
        if item["role"] == "user":
            item["content"] = context_text + item["content"]
            break
    return result


def _tool_result(name, arguments):
    try:
        return TOOL_FUNCTIONS[name](**arguments)
    except Exception as error:
        return {"error": str(error)}


def _summary(result):
    if isinstance(result, dict) and result.get("error"):
        return result["error"][:240]
    if isinstance(result, list):
        return f"{len(result)} result(s)"
    if isinstance(result, dict) and result.get("id"):
        return f"{result.get('name', result['id'])} updated"
    return "completed"


def _sse(payload):
    return "data: " + json.dumps(payload, ensure_ascii=False) + "\n\n"


def anthropic_stream(messages, context, model):
    import anthropic

    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    history = _contextual_messages(messages, context)
    for _ in range(MAX_TOOL_ROUNDS):
        tool_uses = []
        with client.messages.stream(
            model=model,
            max_tokens=1400,
            system=SYSTEM_PROMPT,
            messages=history,
            tools=TOOL_SCHEMAS,
        ) as stream:
            for text in stream.text_stream:
                yield _sse({"type": "text", "text": text})
            response = stream.get_final_message()
        for block in response.content:
            if getattr(block, "type", None) == "tool_use":
                tool_uses.append(block)
        if not tool_uses:
            yield _sse({"type": "done"})
            return

        results = []
        for call in tool_uses:
            result = _tool_result(call.name, call.input)
            results.append({
                "type": "tool_result",
                "tool_use_id": call.id,
                "content": json.dumps(result, ensure_ascii=False),
            })
            yield _sse({
                "type": "tool",
                "name": call.name,
                "input": call.input,
                "result_summary": _summary(result),
            })
        history.append({"role": "assistant", "content": response.content})
        history.append({"role": "user", "content": results})
    yield _sse({"type": "error", "message": f"Stopped after {MAX_TOOL_ROUNDS} tool-use rounds."})
    yield _sse({"type": "done"})


def _tool_result_text(block):
    content = block.get("content", "")
    if isinstance(content, list):
        content = " ".join(item.get("text", "") for item in content if isinstance(item, dict))
    return str(content)[:240]


def cli_stream(messages, context):
    config_file = None
    process = None
    try:
        config = {"mcpServers": {"maps": {"type": "http", "url": "http://127.0.0.1:8765/mcp"}}}
        handle = tempfile.NamedTemporaryFile(mode="w", suffix=".json", encoding="utf-8", delete=False)
        config_file = handle.name
        json.dump(config, handle)
        handle.close()
        flattened = ["System instructions:\n" + SYSTEM_PROMPT]
        flattened.extend(
            f"{item['role'].upper()}:\n{item['content']}"
            for item in _contextual_messages(messages, context)
        )
        prompt = "\n\n".join(flattened)
        command = [
            shutil.which("claude"),
            "-p",
            "--output-format",
            "stream-json",
            "--verbose",
            "--mcp-config",
            config_file,
            "--allowedTools",
            "mcp__maps",
        ]
        process = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
        )
        process.stdin.write(prompt)
        process.stdin.close()
        pending = {}
        emitted_text = False
        for line in process.stdout:
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue
            event_type = event.get("type")
            message = event.get("message", {})
            blocks = message.get("content", []) if isinstance(message, dict) else []
            if event_type == "stream_event":
                delta = event.get("event", {}).get("delta", {})
                if delta.get("type") == "text_delta" and delta.get("text"):
                    emitted_text = True
                    yield _sse({"type": "text", "text": delta["text"]})
            elif event_type == "assistant":
                for block in blocks:
                    if block.get("type") == "text" and block.get("text"):
                        emitted_text = True
                        yield _sse({"type": "text", "text": block["text"]})
                    elif block.get("type") == "tool_use":
                        pending[block.get("id")] = {
                            "name": block.get("name", "tool"),
                            "input": block.get("input", {}),
                        }
            elif event_type == "user":
                for block in blocks:
                    if block.get("type") == "tool_result":
                        call = pending.pop(block.get("tool_use_id"), {"name": "tool", "input": {}})
                        yield _sse({
                            "type": "tool",
                            "name": call["name"],
                            "input": call["input"],
                            "result_summary": _tool_result_text(block),
                        })
            elif event_type == "result" and event.get("result"):
                if not emitted_text:
                    yield _sse({"type": "text", "text": event["result"]})
        stderr = process.stderr.read()
        return_code = process.wait()
        if return_code:
            yield _sse({"type": "error", "message": stderr.strip() or f"claude exited with status {return_code}"})
        yield _sse({"type": "done"})
    except Exception as error:
        if process and process.poll() is None:
            process.kill()
        yield _sse({"type": "error", "message": str(error)})
        yield _sse({"type": "done"})
    finally:
        if config_file:
            try:
                os.unlink(config_file)
            except OSError:
                pass


def stream_chat(messages, context):
    backend, model = backend_info()
    try:
        if backend == "anthropic":
            yield from anthropic_stream(messages, context, model)
        elif backend == "claude-cli":
            yield from cli_stream(messages, context)
        else:
            yield _sse({
                "type": "error",
                "message": "Chat is not configured. Set ANTHROPIC_API_KEY or install the Claude Code CLI and put `claude` on PATH.",
            })
            yield _sse({"type": "done"})
    except Exception as error:
        yield _sse({"type": "error", "message": str(error)})
        yield _sse({"type": "done"})
