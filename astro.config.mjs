// @ts-check
import { defineConfig, fontProviders } from "astro/config";

import astroBrokenLinksChecker from 'astro-broken-link-checker';
import expressiveCode from 'astro-expressive-code';
import icon from 'astro-icon';
import pagefind from "astro-pagefind";
import sitemap from '@astrojs/sitemap';
import { visualizer } from "rollup-plugin-visualizer";

import remarkDirective from 'remark-directive'; // required for CalloutDirectives
import remarkCalloutDirectives from '@microflash/remark-callout-directives';
import remarkMath from 'remark-math'; // with rehype-katex

import { remarkDiagram } from './remark-plugins/mermaid.mjs'; // Custom plugin -- Force loading Mermaid
import { remarkModifiedTime } from './remark-plugins/modified-time.mjs'; // Custom plugin -- last time file was modified

import rehypeSlug from 'rehype-slug'; // dependency of AutoLinkHeadings
import rehypeAutolinkHeadings from 'rehype-autolink-headings';
import rehypeExternalLinks from 'rehype-external-links';
import rehypeSanitize from 'rehype-sanitize' // TODO
import rehypeKatex from 'rehype-katex'; // with remark-math



// Set default Layout for Markdown files
const defaultLayout = () => {
	return function (_, file) {
		file.data.astro.frontmatter.layout =
			file.data.astro.frontmatter.layout || "@layouts/CourseLayout.astro";
	};
};

const remarkCalloutConfig = {
	aliases: {
		exo: "note",
		tip: "commend",
		link: "assert",
		warning: "warn",
		strong: "deter",
	},
	callouts: {
		note: {
			title: "Exercice"
		},
		commend: {
			title: "Tip"
		},
		assert: {
			title: "Lien"
		},
		deter: {
			title: "Important"
		},
		correction: {
			title: "Correction",
			// hint: `<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"><path d="M4.7 6.5h.01m8.49-2.8h.01m4.29 15.6h.01m2.79-8.5h.01m-6.41-.7 2.2-.7V6.5h2.8V3.7L21 3m-6.253 10.767c1.676-.175 2.93-.38 3.739-.064 1.234.483 1.497 1.529 1.409 3.008m-9.723-7.519c.175-1.676.38-2.93.064-3.739-.483-1.234-1.529-1.497-3.008-1.409M6.5 10.4l7.1 7.1L3 21z"/></svg>`
		}
	}
};

// https://astro.build/config
export default defineConfig({
	site: 'https://www.avenel.pro',
	output: 'static',

	markdown: {
		// remark: Markdown processing
		remarkPlugins: [
			defaultLayout,
			remarkDiagram, // TODO
			remarkMath,
			remarkModifiedTime,
			remarkDirective, // required for remarkCalloutDirectives - must be before
			[remarkCalloutDirectives, remarkCalloutConfig],
		],
		// rehype: HTML processing (uses remark)
		rehypePlugins: [
			rehypeSlug, // dependency of AutoLinkHeadings
			[
				// add a link to h1, h2, …
				rehypeAutolinkHeadings,
				{
					behavior: 'append',
					properties: { ariaHidden: true, tabIndex: -1, class: ['add-bookmark'] },
				}
			],
			[rehypeExternalLinks, { content: { type: 'text', value: ' 🌎' } }], // external links have this symbol
			// rehypeSanitize, // sanitize and cleanup HTML // TODO
			rehypeKatex, // latex and math. Lazy-loaded, only if needed.
		],
	},

	integrations: [
		astroBrokenLinksChecker({
			checkExternalLinks: false
		}),
		expressiveCode({
			themes: [
				'andromeeda',
				'aurora-x',
				'ayu-dark',
				'catppuccin-mocha',
				'dark-plus',
				'dracula',
				'everforest-light',
				'github-light',
				'gruvbox-dark-medium',
				'gruvbox-light-medium',
				'houston',
				'kanagawa-dragon',
				'nord',
				'one-light',
				'poimandres',
				'rose-pine',
				'synthwave-84',
				'tokyo-night',
			],
		}),
		icon(),
		sitemap(),
		// must be last to search in fully bundled
		pagefind()
	],

	vite: {
		plugins: [
			visualizer({ // analyse bundle size
				emitFile: true,
				filename: "stats.html",
			})
		]
	},

	experimental: {
		fonts: [
			{
				name: "Inter",
				cssVariable: "--font-main",
				provider: fontProviders.fontsource(),
				// Download only font files for characters used on the page
				subsets: ["latin"],
			},
		]
	}

})
