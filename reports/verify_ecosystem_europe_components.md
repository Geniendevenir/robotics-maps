# Verification — Europe / Components

Date: 2026-11-13. Followed `devin/playbooks/verifier.md`, `CLAUDE.md` and `schemas/notion-schema.md`, with the explicit no-Notion and existing-branch instructions taking precedence. No Notion reads or writes; no PR or main push.

## Checkpoint

All 36 input rows have been assessed and retained with corrections (20 organizations, 16 products). Every retained row has Status `To verify`. This checkpoint is pushed before the final schema and source-ledger checks; the completed row-by-row report will follow on the same branch.

Principal fixes: replace the incorrect Enact official domain with `enact-intelligence.com`, normalize `Pre-seed/Seed`, omit unknown funding stages, remove `_relationship_reason` and narrative metadata, correct Arduino's location to Monza, distinguish components/tools from complete robots, and separate future rollout/manufacturing commitments from achieved deliveries. Replace the generic Humanoid fleet entry with HMND 01 Alpha, and remove the unsupported RoBee/ST user relation (investment does not imply use).

Unknown numeric release years are omitted rather than guessed. The top-level `organizations` and `robots_models` keys are dataset containers, not Notion row properties. All entity keys must be actual field names. Narrative research summaries and source-consultation metadata are removed from the JSON.
