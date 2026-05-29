# CLAUDE.md

## Babysitter

- Project profile: `.a5c/project-profile.json` / `.a5c/project-profile.md`.
- Preferred autonomy: semi-autonomous for low-risk content/code edits; ask before CI/CD, dependency, git commit/push, deploy, destructive operations, or large refactoring.
- Main project commands: `bun run dev`, `bun run build`, `bun run test`.
- Keep course content in French unless explicitly requested otherwise.
- Preserve custom admonition blocks: `:::tip`, `:::link`, `:::warn`, `:::exo`, `:::correction`.
- For content changes, check related `src/pages`, `src/courses`, and `src/assets` references; run targeted build/link checks when useful.
- CI/CD Babysitter integration is intentionally deferred; do not modify GitHub Actions without explicit approval.

Recommended processes/skills:

- `cradle/project-install` for refreshing this profile.
- Technical documentation processes for content strategy, docs testing, and style-guide consistency.
- Web-development processes for technical SEO and performance-sensitive changes.
- `content-research-writer` for accurate technical course content.
- `changelog-generator` for summarizing batches of course/site updates.
