import { execSync } from "child_process";

// Get the last modified date of the file using Git
export function remarkModifiedTime() {
	return function (tree, file) {
		const filepath = file.history[0];
		const result = execSync(`git log -1 --pretty="format:%cI" "${filepath}"`);
		file.data.astro.frontmatter.lastModified = result.toString();
	};
}
