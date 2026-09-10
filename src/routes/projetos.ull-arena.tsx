import { createFileRoute, Link } from "@tanstack/react-router";

export const Route = createFileRoute("/projetos/ull-arena")({
  component: UllArenaPage,
});

const tipoLabel: Record<string, string> = {
  lab: "Laboratório",
  game: "Jogo",
  topologia: "Topologia",
  modelo: "Modelo",
};

// Dados injetados diretamente na página para evitar erros de importação
const p = {
  titulo: "ULL Arena - HFT & Exchange Connectivity",
  subtitulo: "Arquitetura de rede de ultra-baixa latência",
  chamada: "Otimização da camada de rede para tempos de execução na casa dos microssegundos para aplicações críticas do mercado financeiro conectadas à B3.",
  trilha: "HFT",
  nivel: "Avançado",
  idiomas: ["PT-BR", "EN-US"],
  href: "/ull-arena/index.html",
  resumo: [
    "Implementação de switching cut-through de altíssima performance.",
    "Ajuste fino de buffers de rede para mitigação de microbursts.",
    "Roteamento determinístico e sincronização de tempo via PTP."
  ],
  modulos: [
    { n: "01", titulo: "Topologia Nexus", tipo: "topologia", descricao: "Desenho lógico da conexão HFT." },
    { n: "02", titulo: "Tuning de Buffer", tipo: "lab", descricao: "Mitigação de microbursts e análise de descarte." }
  ],
  paraQuem: ["Engenheiros de Rede HFT", "Arquitetos de Infraestrutura Financeira", "C-Level de Tecnologia"],
  stack: ["Cisco Nexus", "PTP", "BGP", "Multicast"],
  aviso: "Ambiente de demonstração focado em estabilidade sob volatilidade do mercado."
};

function UllArenaPage() {
  return (
    <article className="mx-auto max-w-4xl px-6 py-12">
      <nav className="mb-8 text-sm text-muted-foreground">
        <Link to="/projetos" className="hover:text-foreground">Projetos</Link>
        <span className="mx-2">/</span>
        <span className="text-foreground">{p.titulo}</span>
      </nav>

      <header className="mb-10">
        <div className="mb-4 flex flex-wrap items-center gap-2">
          <span className="rounded-full bg-sky-500/10 px-3 py-1 text-xs font-semibold text-sky-600 dark:text-sky-400">{p.trilha}</span>
          <span className="rounded-full border px-3 py-1 text-xs font-medium text-muted-foreground">{p.nivel}</span>
          {p.idiomas.map((i) => (
            <span key={i} className="rounded-full border px-2.5 py-1 text-xs font-medium text-muted-foreground">{i}</span>
          ))}
        </div>
        <h1 className="text-4xl font-bold tracking-tight sm:text-5xl">{p.titulo}</h1>
        <p className="mt-2 text-xl text-muted-foreground">{p.subtitulo}</p>
        <p className="mt-6 max-w-2xl text-lg leading-relaxed">{p.chamada}</p>
        <div className="mt-8 flex flex-wrap gap-3">
          <a href={p.href} target="_blank" rel="noreferrer" className="inline-flex items-center gap-2 rounded-xl bg-sky-600 px-6 py-3 text-base font-semibold text-white transition hover:bg-sky-700">Abrir a Arena <span aria-hidden>→</span></a>
        </div>
      </header>

      <section className="mb-12">
        <h2 className="mb-4 text-2xl font-bold tracking-tight">A tese</h2>
        <div className="space-y-4 border-l-2 border-sky-500 pl-6">
          {p.resumo.map((t, i) => (<p key={i} className="leading-relaxed text-muted-foreground">{t}</p>))}
        </div>
      </section>

      <section className="mb-12">
        <h2 className="mb-1 text-2xl font-bold tracking-tight">Módulos</h2>
        <div className="divide-y rounded-xl border">
          {p.modulos.map((m) => (
            <div key={m.n} className="flex gap-4 p-4">
              <span className="w-10 shrink-0 pt-0.5 font-mono text-sm font-semibold text-sky-600 dark:text-sky-400">{m.n}</span>
              <div className="min-w-0">
                <div className="flex flex-wrap items-baseline gap-2">
                  <h3 className="font-semibold">{m.titulo}</h3>
                  <span className="rounded border px-1.5 py-0.5 text-[10px] font-medium uppercase tracking-wide text-muted-foreground">{tipoLabel[m.tipo]}</span>
                </div>
                <p className="mt-1 text-sm leading-relaxed text-muted-foreground">{m.descricao}</p>
              </div>
            </div>
          ))}
        </div>
      </section>

      <section className="mb-12 grid gap-8 sm:grid-cols-2">
        <div>
          <h2 className="mb-3 text-lg font-bold tracking-tight">Para quem é</h2>
          <ul className="space-y-2">{p.paraQuem.map((t, i) => (<li key={i} className="flex gap-2 text-sm text-muted-foreground"><span className="mt-1.5 h-1.5 w-1.5 shrink-0 rounded-sm bg-sky-500" />{t}</li>))}</ul>
        </div>
        <div>
          <h2 className="mb-3 text-lg font-bold tracking-tight">Stack</h2>
          <ul className="space-y-2">{p.stack.map((t, i) => (<li key={i} className="flex gap-2 text-sm text-muted-foreground"><span className="mt-1.5 h-1.5 w-1.5 shrink-0 rounded-sm bg-sky-500" />{t}</li>))}</ul>
        </div>
      </section>
    </article>
  );
}
