import json
import os
from urllib.error import URLError
from urllib.request import Request, urlopen


DEFAULT_SERVER_URL = "http://127.0.0.1:8765"


def make_publishers(server_url=None, opener=None):
    base_url = (server_url or os.environ.get("VIZ_SERVER_URL", DEFAULT_SERVER_URL)).rstrip("/")
    open_request = opener or urlopen
    ui_url = f"{base_url}/api/ui"
    groups_url = f"{base_url}/api/groups/refresh"

    def post(url, payload):
        request = Request(
            url,
            data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with open_request(request, timeout=3) as response:
            response.read()

    def publish_ui(command):
        try:
            post(ui_url, command)
        except (URLError, OSError, TimeoutError) as error:
            raise RuntimeError(
                f"Browser server not reachable at {ui_url}; start it with `python -m viz.server`"
            ) from error

    def publish_groups(_groups):
        try:
            post(groups_url, {})
        except (URLError, OSError, TimeoutError):
            pass

    return publish_ui, publish_groups
