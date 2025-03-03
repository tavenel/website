## Features

- Lazy-load `Mermaid` (diagrams) JS librairies if needed.
- Transform `PlantUML` diagrams into images at build-time using [remark-simple-plantuml](https://github.com/akebifiky/remark-simple-plantuml)
- Search using `PageFind` integrated by [astro-pagefind](https://github.com/shishkin/astro-pagefind/)
- Callouts : `:::tip`, `:::link`, `:::warn`, `:::strong`, `:::exo`, `:::correction` using [remark-callout-directives](https://github.com/Microflash/remark-callout-directives)

## 🧞 Commands

- The main build uses a <https://taskfile.dev> here : <./Taskfile.yml>. Use `task …` 
- `task dev` or `bun run dev` => <http://localhost:4321>
- `bun run astro --help`

## 🔗 Links

- <https://docs.astro.build> and an example : <https://github.com/hellotham/hello-astro/>
- Markdown to HTML : [remark plugins](https://github.com/remarkjs/remark/blob/main/doc/plugins.md#list-of-plugins)
- HTML tranforming : [rehype plugins](https://github.com/rehypejs/rehype/blob/HEAD/doc/plugins.md#list-of-plugins)

## Licenses

<./LICENSE>
