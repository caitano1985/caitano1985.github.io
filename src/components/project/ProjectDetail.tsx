import { Link } from "@tanstack/react-router";
import { useI18n } from "@/lib/i18n";
import type { Project } from "@/data/projects";

function Section({ title, children }: { title: string; children: React.ReactNode }) {
  return (
    <section className="mt-10">
      <h2 className="mono-label">{title}</h2>
      <div className="mt-3 space-y-3 text-muted-foreground">{children}</div>
    </section>
  );
}

export function ProjectDetail({ project }: { project: Project }) {
  const { t, lang } = useI18n();

  return (
    <main className="mx-auto max-w-3xl px-5 py-16">
      <Link to="/projetos" className="font-mono text-sm text-primary transition-opacity hover:opacity-80">
        ← {t("projects.back")}
      </Link>

      <h1 className="mt-6 text-3xl font-bold sm:text-4xl">{project.title[lang]}</h1>
      <p className="mt-3 text-lg text-muted-foreground">{project.summary[lang]}</p>

      <img
        src={project.cover}
        alt={project.title[lang]}
        loading="lazy"
        width={1280}
        height={720}
        className="mt-8 w-full rounded-xl border border-border object-cover"
      />

      <Section title={t("projects.context")}>
        <p className="leading-relaxed">{project.context[lang]}</p>
      </Section>

      <Section title={t("projects.tech")}>
        <div className="flex flex-wrap gap-2">
          {project.tags.map((tag) => (
            <span key={tag} className="rounded border border-border bg-secondary px-2 py-1 font-mono text-xs">
              {tag}
            </span>
          ))}
        </div>
      </Section>

      <Section title={t("projects.solution")}>
        <ul className="space-y-2">
          {project.solution[lang].map((item) => (
            <li key={item} className="flex gap-3 leading-relaxed">
              <span className="mt-2 h-1.5 w-1.5 shrink-0 rounded-full bg-primary" />
              {item}
            </li>
          ))}
        </ul>
      </Section>

      <Section title={t("projects.diagram")}>
        <div className="grid-bg flex min-h-40 items-center justify-center rounded-xl border border-dashed border-border p-6 text-center font-mono text-xs">
          {project.diagramNote[lang]}
        </div>
      </Section>

      <Section title={t("projects.results")}>
        <ul className="space-y-2">
          {project.results[lang].map((item) => (
            <li key={item} className="flex gap-3 leading-relaxed">
              <span className="mt-2 h-1.5 w-1.5 shrink-0 rounded-full bg-neon" />
              {item}
            </li>
          ))}
        </ul>
      </Section>

      <Link
        to="/projetos"
        className="mt-12 inline-flex items-center rounded-md border border-primary/50 px-4 py-2 font-mono text-sm text-primary transition-colors hover:bg-primary hover:text-primary-foreground"
      >
        ← {t("projects.back")}
      </Link>
    </main>
  );
}