import rss, { pagesGlobToRssItems } from '@astrojs/rss';
// import sanitizeHtml from 'sanitize-html';

export async function GET(context) {
	// const postImportResult = pagesGlobToRssItems(import.meta.glob('./**/*.md', { eager: true }));
	// const posts = Object.values(postImportResult);
	return rss({
		title: 'Tom Avenel',
		description: 'Tech update and courses',
		site: context.site,
		items: await pagesGlobToRssItems(
			import.meta.glob('./**/*.{md,mdx}'),
		),
		stylesheet: '/rss/styles.xsl',
	});
}


