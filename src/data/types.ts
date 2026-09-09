import type { Lang } from "@/lib/i18n";

export type LocalizedText = Record<Lang, string>;
export type LocalizedList = Record<Lang, string[]>;

export type Project = {
  slug: string;
  cover: string;
  tags: string[];
  title: LocalizedText;
  summary: LocalizedText;
  context: LocalizedText;
  solution: LocalizedList;
  results: LocalizedList;
  diagramNote: LocalizedText;
};