// @ts-check
import { defineConfig } from 'astro/config';

import sitemap from '@astrojs/sitemap';
import remarkToc from 'remark-toc';
import { rehypeAccessibleEmojis } from 'rehype-accessible-emojis';
import rehypeSlug from 'rehype-slug';
import rehypeAutolinkHeadings from 'rehype-autolink-headings';
import rehypeExternalLinks from 'rehype-external-links';
import rehypeSanitize from 'rehype-sanitize'
import { visualizer } from "rollup-plugin-visualizer";

import { remarkModifiedTime } from './remark-modified-time.mjs';

// Set default Layout for Markdown files
const setLayout = () => {
	return function (_, file) {
		file.data.astro.frontmatter.layout =
			file.data.astro.frontmatter.layout || "@layouts/CourseLayout.astro";
	};
};

// https://astro.build/config
export default defineConfig({
	site: 'https://www.avenel.pro',

	markdown: {
		// remark: Markdown processing
		remarkPlugins: [
			setLayout,
			[remarkToc, { heading: 'Chapitres', maxDepth: 3 }],
			remarkModifiedTime,
		],
		// rehype: HTML processing (uses remark)
		rehypePlugins: [
			rehypeAccessibleEmojis, // add a span explaining the emoji
			rehypeSlug, // dependency of AutoLinkHeadings
			[rehypeAutolinkHeadings, { behavior: 'append' }], // add a link to h1, h2, …
			[rehypeExternalLinks, { content: { type: 'text', value: ' 🌎' } }], // mark external links
			 // rehypeSanitize, // sanitize and cleanup HTML
		],
		shikiConfig: { // code highlighter
			// https://shiki.style/themes
			themes: {
				light: 'one-light',
				dark: 'houston', // catpuccin-mocha',
			},
		},
	},

	integrations: [sitemap()],

	vite: {
		plugins: [visualizer({ // analyse bundle size
			emitFile: true,
			filename: "stats.html",
		})]
	}
})
