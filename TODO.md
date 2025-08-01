
## P1

- playwright
  - https://status.avenel.pro/

- eslint

[![Super-Linter](https://github.com/<OWNER>/<REPOSITORY>/actions/workflows/<WORKFLOW_FILE_NAME>/badge.svg)](https://github.com/marketplace/actions/super-linter)

```sh
# Run playwright server in a Docker container
docker run -p 3000:3000 --rm --init -it mcr.microsoft.com/playwright:v1.54.2 /bin/sh -c "cd /home/pwuser && npx -y playwright@1.54.2 run-server --port 3000 --host 0.0.0.0"
```

```js
// playwright.config.ts

export default defineConfig({

	use: {

		connectOptions: {
			wsEndpoint: 'ws://localhost:3000',
		},

	},
})
```

- https://www.emgoto.com/react-table-of-contents/#making-your-anchor-links-update
- https://github.com/futuraprime/rehype-figure-title
- https://web.dev/articles/browser-level-image-lazy-loading?hl=fr

- check accessiblility : https://wave.webaim.org (/k8s/cours)
- ShowCorrection => in :::exo

## P2

- diagrams mermaid BUG : note class diag (see /test).

## P3

- eco-index
- blog tech. => /wrote/
  - fusion links, liens
  - tech/
    - /fun
	  - /vim
  - faq/
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

- sanitize
  - rss.xml.js
  - package.json & astro.config
    - "@types/sanitize-html": "^2.13.0",
    - "rehype-sanitize": "^6.0.0",
    - "sanitize-html": "^2.14.0"

## P4

- CSS => split themes in files and load only on-demand
- "Fix typo" link in footer (or in versioning ?)
- Head.astro => ClientRouter transitions
- tsconfig.json :	"verbatimModuleSyntax": true,
- better `date:`
- "latest" page => git history ?
- <https://adamsimpson.net/writing/openring>
- tags:[] word cloud and links

