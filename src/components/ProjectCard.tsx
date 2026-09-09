import { Link } from "@tanstack/react-router";
import { useI18n } from "@/lib/i18n";
import type { Project } from "@/data/projects";

export function ProjectCard({ project }: { project: Project }) {
  const { lang } = useI18n();
  return (
    <Link
      to={`/projetos/${project.slug}`}
      className="card-hover group flex flex-col overflow-hidden rounded-xl border border-border bg-card"
    >
      <img
        src={project.cover}
        alt={project.title[lang]}
        loading="lazy"
        width={1280}
        height={720}
        className="aspect-video w-full object-cover opacity-90 transition-opacity group-hover:opacity-100"
      />
      <div className="flex flex-1 flex-col gap-3 p-5">
        <h3 className="text-lg font-semibold">{project.title[lang]}</h3>
        <p className="flex-1 text-sm leading-relaxed text-muted-foreground">
          {project.summary[lang]}
        </p>
        <div className="flex flex-wrap gap-1.5">
          {project.tags.map((tag) => (
            <span
              key={tag}
              className="rounded border border-border bg-secondary px-2 py-0.5 font-mono text-[11px] text-muted-foreground"
            >
              {tag}
            </span>
          ))}
        </div>
      </div>
    </Link>
  );
}
