import type { CollectionEntry, CollectionKey } from 'astro:content';

export interface Chapter {
  slug: string;
  url: string;
  title: string;
  order: number;
  type: string;
  tags?: string[];
  description?: string;
}

export interface Course {
  slug: string;
  url: string;
  title: string;
  description: string;
  icon?: string;
  chapters: Chapter[];
}

export interface CourseTree {
  courses: Course[];
  getBySlug(slug: string): Course | undefined;
  getChapterBySlug(slug: string): Chapter | undefined;
}

/**
 * Builds a course tree from the Starlight docs collection.
 * Each directory under courses/ = one course, files = chapters,
 * sorted by sidebar.order (or fallback order).
 */
export function buildCourseTree(
  docs: CollectionEntry<'docs'>[],
  getEntry: (collection: CollectionKey, slug: string) => CollectionEntry<'docs'> | undefined,
): CourseTree {
  // Group entries by course directory
  const courseMap = new Map<string, CollectionEntry<'docs'>[]>();

  for (const entry of docs) {
    const parts = entry.id.split('/');
    if (parts.length < 2) continue; // skip non-course entries
    const courseSlug = parts[0]; // e.g. "linux", "git"

    if (courseSlug === 'pages') continue; // skip standalone pages

    if (!courseMap.has(courseSlug)) {
      courseMap.set(courseSlug, []);
    }
    courseMap.get(courseSlug)!.push(entry);
  }

  const courses: Course[] = [];

  for (const [slug, entries] of courseMap) {
    const indexEntry = entries.find((e) => e.id.endsWith('/index'));
    const chapters = entries
      .filter((e) => !e.id.endsWith('/index'))
      .map((e) => ({
        slug: e.id,
        url: `/courses/${e.id.replace(/\/index$/, '')}`,
        title: e.data.title || e.id.split('/').pop() || '',
        order: typeof e.data.sidebar?.order === 'number' ? e.data.sidebar.order : 999,
        type: (e.data as any).type || 'cours',
        tags: (e.data as any).tags || [],
        description: e.data.description || '',
      }))
      .sort((a, b) => a.order - b.order);

    if (chapters.length === 0) {
      // single-file course: the index itself is the only entry
      chapters.push({
        slug: slug,
        url: `/courses/${slug}`,
        title: indexEntry?.data.title || slug,
        order: 1,
        type: 'cours',
        description: indexEntry?.data.description || '',
      });
    }

    courses.push({
      slug,
      url: `/courses/${slug}`,
      title: indexEntry?.data.title || slug,
      description: indexEntry?.data.description || '',
      icon: (indexEntry?.data as any).icon || undefined,
      chapters,
    });
  }

  courses.sort((a, b) => a.title.localeCompare(b.title));

  const tree: CourseTree = {
    courses,
    getBySlug(slug: string) {
      return courses.find((c) => c.slug === slug);
    },
    getChapterBySlug(slug: string) {
      for (const course of courses) {
        const chapter = course.chapters.find((c) => c.slug === slug);
        if (chapter) return chapter;
      }
      return undefined;
    },
  };

  return tree;
}

/**
 * Validates that all slugs in a chapters array exist in the course tree.
 * Returns missing slugs.
 */
export function validateTrackChapters(
  chapters: string[],
  tree: CourseTree,
): string[] {
  return chapters.filter((slug) => !tree.getChapterBySlug(slug));
}