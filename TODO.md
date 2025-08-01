## P1

- check accessiblility : https://wave.webaim.org (/k8s/cours)

## P2

- diagrams mermaid BUG : note class diag (see /test).

## P3

- eco-index
- blog tech. => /wrote/
- W3C
- URL checker
	- break on broken local link
	- improve external links checks

- "favorites" :
	- CSS => RM display: none for add-bookmark
  - link in Menu/
  - delete
  - fix favorites navigation (after astro hydration ?)
  - Favorites.astro => fix TODO

- linter `astro.config.mjs`
  - import remarkLint from 'remark-lint';
  - import remarkPresetLintRecommended from 'remark-preset-lint-recommended';
  - import remarkLintNoDeadUrls from 'remark-lint-no-dead-urls';
  - https://github.com/remarkjs/remark-validate-links
  - remarkPlugins: [ // remarkLint, // remarkPresetLintRecommended, // remarkLintNoDeadUrls, ]

## P4

- seo
  - https://github.com/hellotham/hello-astro/blob/main/src/components/seo.astro
  - https://code.juliancataldo.com/component/astro-seo-metadata/

- CSS => split themes in files and load only on-demand
- "Fix typo" link in footer (or in versioning ?)
- Head.astro => ClientRouter transitions
- tsconfig.json :	"verbatimModuleSyntax": true,
- better `date:`
- "latest" page => git history ?
- <https://adamsimpson.net/writing/openring>
- tags:[] word cloud and links
- Diagrams => RM plantuml library

