# Playbook: verifier

You did NOT produce this file. Your job is to try to break it.
For every row: open each source URL, confirm it loads and supports the claims. For organizations,
confirm the company exists, is active in 2026 and the website is official. For robots/models,
confirm they exist and the builder is right. Check select values match schemas/notion-schema.md.
Mark each row verified / corrected / rejected with a one-line reason.
Output `reports/verify_<file>.md` and overwrite the JSON with the cleaned version
(rejected rows removed, corrected rows fixed, Status set to "To verify").

## Devin-specific
- You run in your own VM. Clone the repo, work on branch `research/<your-slug>`, commit your output/ and reports/ files and push. Do not push to main.
- When done, reply to the coordinator session with your 5-line summary and the branch name.
- Stay within your ACU limit: if you hit the saturation stop early, stop.
