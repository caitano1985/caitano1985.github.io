import { createFileRoute, Link } from "@tanstack/react-router";
import { ProjectCard } from "@/components/ProjectCard";
import { projects } from "@/data/projects";
import { useI18n } from "@/lib/i18n";

export const Route = createFileRoute("/projetos/")({
  head: () => ({
    meta: [
      { title: "Projects | Josimar Caitano — Principal Solutions Architect" },
      {
        name: "description",
        content:
          "Estudos de caso de arquitetura e implementação de redes: Ultra-Baixa Latência (ULL), High-Frequency Trading (HFT) e conectividade B3.",
      },
      { property: "og:title", content: "Projects | Josimar Caitano" },
      {
        property: "og:description",
        content: "Estudos de caso de arquitetura e implementação de redes por Josimar Caitano.",
      },
      { property: "og:type", content: "website" },
      { name: "twitter:card", content: "summary_large_image" },
    ],
  }),
  component: ProjectsPage,
});

function ProjectsPage() {
  const { t } = useI18n();
  return (
    <main className="mx-auto max-w-6xl px-5 py-16">
      <p className="mono-label">./projects</p>
      <h1 className="mt-2 text-3xl font-bold sm:text-4xl">{t("projects.listTitle")}</h1>
      <p className="mt-3 max-w-2xl text-muted-foreground">{t("projects.subtitle")}</p>
      <div className="mt-10 grid gap-6 sm:grid-cols-2">
        {projects.map((p) => (
          <ProjectCard key={p.slug} project={p} />
        ))}
      </div>
      <Link
        to="/"
        className="mt-10 inline-block font-mono text-sm text-primary hover:underline"
      >
        ← home
      </Link>
    </main>
  );
}
