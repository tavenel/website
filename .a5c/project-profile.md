# Project Profile: website

Site statique Astro https://www.avenel.pro servant de support de cours techniques en français pour étudiants avancés et professionnels IT.

> Last updated: 2026-05-29T22:02:20Z | Version: 1

## Goals

- **content-quality** [high]: Maintenir un corpus de cours techniques exact, cohérent et utile pédagogiquement. (active)
- **static-site** [high]: Garder le site Astro rapide, navigable, buildable et déployable sur GitHub Pages. (active)
- **education** [high]: Favoriser les TP/labs reproductibles et les exemples exécutables pour les apprenants. (active)
- **maintenance** [medium]: Limiter la dérive des liens, dépendances et contenus obsolètes. (active)

## Tech Stack

### Languages

- Markdown (primary educational content)
- Astro (static pages/components/layouts)
- TypeScript/JavaScript (client utilities, config and remark plugins)
- CSS (site styling)

### Frameworks

- Astro v^6.1.5 [static-site-generator]
- Pagefind [static-search]
- Expressive Code [code-rendering]
- remark/rehype [markdown-pipeline]
- KaTeX [math-rendering]

### Infrastructure

- GitHub Pages [hosting]
- GitHub Actions [ci-cd]

**Build tools:** bun, astro, vite, rollup-plugin-visualizer

**Package managers:** bun, npm (.a5c tooling only)

## Architecture

**Pattern:** Astro static website/content monolith
**Data flow:** Markdown/Astro content is transformed by Astro with remark/rehype plugins into a static site, then built with Bun and deployed by GitHub Actions to GitHub Pages.

### Modules

| Module | Path | Description |
|--------|------|-------------|
| pages | `src/pages` | Routed website pages and course/lab pages. |
| courses | `src/courses` | Reusable long-form Markdown course chapters. |
| components | `src/components` | Astro UI components for navigation, TOC, favorites, print, tags and site chrome. |
| layouts | `src/layouts` | Shared layouts for pages and courses. |
| assets | `src/assets` | Images and diagrams organized by teaching domain. |
| remark-plugins | `remark-plugins` | Custom Markdown processing plugins. |

**Entry points:** `astro.config.mjs`, `src/pages/index.astro`, `src/pages/**/*.md`, `src/pages/**/*.astro`, `src/courses/**/*.md`

## Team

- **Tom Avenel** (maintainer/teacher): course content, site maintenance, technical accuracy, deployment decisions
- **External contributors** (occasional contributors): typo fixes, issue reports, pull requests

## Workflows

### Local development

Edit content and preview locally.
**Triggers:** manual

1. bun install
2. bun run dev
3. edit Markdown/Astro
4. bun run build when relevant

### Content update

Update French technical course material while preserving admonitions and links.
**Triggers:** course update, typo fix, new lab

1. identify related src/pages and src/courses files
2. edit content
3. check assets/links
4. run build or targeted checks

### Deploy

Continuous GitHub Pages deploy from main.
**Triggers:** push main, workflow_dispatch

1. push to main
2. GitHub Actions Astro build
3. deploy-pages

### Quality checks

Super-linter/CodeQL on PR/push and scheduled link checking.
**Triggers:** pull_request, push, schedule

1. super-linter
2. CodeQL
3. lychee scheduled/manual

## Tools

### Linting

- GitHub Super-Linter
- remark-lint

### Testing

- Vitest
- Astro build
- Lychee

## Services

- **GitHub Pages** (hosting) - https://www.avenel.pro
- **Vercel Analytics** (analytics)
- **Vercel Speed Insights** (performance monitoring)

## CI/CD

**Provider:** GitHub Actions
**Config files:** `.github/workflows/astro.yml`, `.github/workflows/codeql.yml`, `.github/workflows/links.yml`, `.github/workflows/super-linter.yml`, `.github/dependabot.yml`

### Pipelines

- **Deploy Astro site to Pages** (trigger: push main / workflow_dispatch)
  Stages: build -> deploy
- **CodeQL Advanced** (trigger: push, pull_request, weekly)
  Stages: analyze
- **Links** (trigger: manual, repository_dispatch, weekly)
  Stages: lychee -> issue-on-failure
- **Lint Code Base** (trigger: push, pull_request)
  Stages: super-linter

## Pain Points

- **medium** [documentation]: Maintenir la cohérence d'un gros corpus Markdown français.
  - Remediation: Use targeted reviews for terminology, admonitions and related course/page changes.
- **medium** [content-quality]: Risque de liens externes obsolètes dans les supports de cours.
  - Remediation: Use scheduled lychee and targeted checks for edited pages.
- **medium** [build]: Les évolutions Astro/Bun peuvent casser le build statique.
  - Remediation: Run bun run build after config/component/dependency changes.

## Bottlenecks

- Page d'outils très modifiée avec risque d'accumulation de dette de liens. at src/pages/tools.md (high)
  Impact: medium
- Zone Kubernetes à forte activité nécessitant cohérence et vérification de liens. at src/pages/k8s, src/courses/k8s (high)
  Impact: medium
- Métadonnées .a5c locales à ignorer pour éviter le bruit git. at .a5c (ongoing)
  Impact: low

## Conventions

### Naming

- **components:** PascalCase .astro
- **content:** domain directories; French filenames using cours/tp/projet/exo when relevant
- **commits:** short scope-prefixed messages

### Git

- **mainBranch:** main
- **branchStrategy:** main with occasional topic branches/PRs
- **commitStyle:** short scope-prefixed, not strict conventional commits
- **approvalRequiredFor:** commit, push, destructive operations

**Import order:** Astro/config > integrations > remark plugins > rehype plugins > local plugins

**Error handling:** Prefer build-time validation; fix broken links/build errors before deployment.

**Testing:** Run bun run build for site-impacting changes; use bun run test when TypeScript/plugin logic is touched; rely on CI for CodeQL/super-linter/link schedule.

### Additional Rules

- Prefer concise French communication.
- Prioritize correctness; avoid hallucinated technical claims in course content.
- Ask before CI/CD changes, dependency upgrades, git commit/push, deploy, destructive operations or large refactoring.
- Semi-autonomous mode: content/code edits and local verification are allowed without extra confirmation when low risk.

## Repositories

- **website** - https://github.com/tavenel/website

## CLAUDE.md Instructions

- Use Bun for project commands: bun run dev, bun run build, bun run test.
- Keep course content in French unless explicitly requested otherwise.
- Preserve custom admonition blocks :::tip/link/warn/exo/correction.
- Ask before modifying GitHub Actions, dependencies, git history, commits/pushes or deployment settings.
- For content changes, check related pages/courses/assets and run targeted build/link checks when useful.
- CI/CD Babysitter integration is deferred; do not modify workflows without explicit approval.

## Installed Extensions

- Skills: project-install, content-research-writer, changelog-generator
- Processes: cradle/project-install, specializations/technical-documentation/docs-testing, specializations/technical-documentation/style-guide-enforcement
