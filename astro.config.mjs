// @ts-check
import { defineConfig } from 'astro/config';

import sitemap from '@astrojs/sitemap';

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
		remarkPlugins: [setLayout],
	},

	integrations: [sitemap()]
})
