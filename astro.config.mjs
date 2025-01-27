// @ts-check
import { defineConfig } from 'astro/config';

import sitemap from '@astrojs/sitemap';
import remarkToc from 'remark-toc';
import { rehypeAccessibleEmojis } from 'rehype-accessible-emojis';

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
		remarkPlugins: [setLayout, [remarkToc, { heading: 'Chapitres', maxDepth: 3 }]],
		rehypePlugins: [rehypeAccessibleEmojis],
		shikiConfig: {
			// https://shiki.style/themes
			themes: {
				light: 'one-light',
				dark: 'houston', // catpuccin-mocha',
			},
		},
	},

	integrations: [sitemap()]
})
