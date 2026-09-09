import { createFileRoute } from "@tanstack/react-router";
import { getProject } from "@/data/projects";
import { ProjectDetail } from "@/components/project/ProjectDetail";

const project = getProject("dna-center")!;

export const Route = createFileRoute("/projetos/dna-center")({
  head: () => ({
    meta: [
      { title: `${project.title.pt} | Projetos — Josinfo` },
      { name: "description", content: project.summary.pt },
      { property: "og:title", content: `${project.title.pt} | Josinfo` },
      { property: "og:description", content: project.summary.pt },
      { property: "og:type", content: "article" },
      { name: "twitter:card", content: "summary_large_image" },
    ],
  }),
  component: () => <ProjectDetail project={project} />,
});