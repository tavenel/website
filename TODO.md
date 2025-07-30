ci => ???
jenkins => ??

devops

tests

---

## P1

- To Mermaid : http://localhost:4321/_image?href=%2F%40fs%2Fmnt%2Fdata%2Fgit%2Fastro%2Fwebsite%2Fsrc%2Fassets%2Fddd%2FDomainDrivenDesignReference.png%3ForigWidth%3D836%26origHeight%3D741%26origFormat%3Dpng&w=836&h=741&f=webp

- mermaid :
  - BUG : note class diag.
  - BUG : diag. seq.

## P2

- CSS layout
  - global layout <https://www.w3schools.com/csS/css_grid.asp>
	- menu layout
	- chapitres always visible
	- main content not too big (/k8s/cours)
- diagrams mermaid
  - KO IN :::correction !!!
  - render images at build time with playwright : <https://agramont.net/blog/diagraming-with-mermaidjs-astro/> =>  NO ? (themes ! or OK if SVG ?)

## P3

- blog tech.
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
- Head.astro => ClientRouter transitions
- tsconfig.json :	"verbatimModuleSyntax": true,
- better `date:`
- "latest" page => git history ?
- <https://adamsimpson.net/writing/openring>
- tags:[] word cloud and links
- Diagrams => RM plantuml library

