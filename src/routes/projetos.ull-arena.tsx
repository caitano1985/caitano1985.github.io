import { createFileRoute, redirect } from "@tanstack/react-router";
export const Route = createFileRoute("/projetos/ull-arena")({
  beforeLoad: () => { throw redirect({ href: "/ull-arena/" }); },
  component: () => null,
});
