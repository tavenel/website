import rss, { pagesGlobToRssItems } from '@astrojs/rss';
// import sanitizeHtml from 'sanitize-html';

export async function GET(context) {
	// const postImportResult = pagesGlobToRssItems(import.meta.glob('./**/*.md', { eager: true }));
	// const posts = Object.values(postImportResult);
	return rss({
		title: 'Tom Avenel',
		description: 'Tech update and courses',
		site: context.site,
		// Array of `<item>`s in output xml
		// See "Generating items" section for examples using content collections and glob imports
		// items: posts.map(async (post) => ({
		// 	link: post.url,
		// 	content: sanitizeHtml((await post.compiledContent())),
		// 	...post.frontmatter,
		// })),
		items: await pagesGlobToRssItems(
			import.meta.glob('./**/*.{md,mdx}'),
		),
		stylesheet: '/rss/styles.xsl',
	});
}


