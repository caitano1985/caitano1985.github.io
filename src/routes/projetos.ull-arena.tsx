// src/routes/projetos.ull-arena.tsx
import { createFileRoute, Link } from "@tanstack/react-router";
import { ullArena } from "@/data/ull-arena";

export const Route = createFileRoute("/projetos/ull-arena")({
  component: UllArenaPage,
});

const tipoLabel: Record<string, string> = {
  lab: "Laboratório",
  game: "Jogo",
  topologia: "Topologia",
  modelo: "Modelo",
};

function UllArenaPage() {
  const p = ullArena;

  return (
    <article className="mx-auto max-w-4xl px-6 py-12">
      {/* cabeçalho */}
      <nav className="mb-8 text-sm text-muted-foreground">
        <Link to="/projetos" className="hover:text-foreground">
          Projetos
        </Link>
        <span className="mx-2">/</span>
        <span className="text-foreground">{p.titulo}</span>
      </nav>

      <header className="mb-10">
        <div className="mb-4 flex flex-wrap items-center gap-2">
          <span className="rounded-full bg-sky-500/10 px-3 py-1 text-xs font-semibold text-sky-600 dark:text-sky-400">
            {p.trilha}
          </span>
          <span className="rounded-full border px-3 py-1 text-xs font-medium text-muted-foreground">
            {p.nivel}
          </span>
          {p.idiomas.map((i) => (
            <span
              key={i}
              className="rounded-full border px-2.5 py-1 text-xs font-medium text-muted-foreground"
            >
              {i}
            </span>
          ))}
        </div>

        <h1 className="text-4xl font-bold tracking-tight sm:text-5xl">
          {p.titulo}
        </h1>
        <p className="mt-2 text-xl text-muted-foreground">{p.subtitulo}</p>
        <p className="mt-6 max-w-2xl text-lg leading-relaxed">{p.chamada}</p>

        <div className="mt-8 flex flex-wrap gap-3">
          <a
            href={p.href}
            target="_blank"
            rel="noreferrer"
            className="inline-flex items-center gap-2 rounded-xl bg-sky-600 px-6 py-3 text-base font-semibold text-white transition hover:bg-sky-700"
          >
            Abrir a Arena
            <span aria-hidden>→</span>
          </a>
          <a
            href="https://github.com/caitano1985/caitano1985.github.io/blob/main/public/ull-arena/index.html"
            target="_blank"
            rel="noreferrer"
            className="inline-flex items-center gap-2 rounded-xl border px-6 py-3 text-base font-semibold transition hover:bg-muted"
          >
            Ver o código
          </a>
        </div>
      </header>

      {/* tese */}
      <section className="mb-12">
        <h2 className="mb-4 text-2xl font-bold tracking-tight">A tese</h2>
        <div className="space-y-4 border-l-2 border-sky-500 pl-6">
          {p.resumo.map((t, i) => (
            <p key={i} className="leading-relaxed text-muted-foreground">
              {t}
            </p>
          ))}
        </div>
      </section>

      {/* módulos */}
      <section className="mb-12">
        <h2 className="mb-1 text-2xl font-bold tracking-tight">
          Onze módulos interativos
        </h2>
        <p className="mb-6 text-sm text-muted-foreground">
          Cada um jogável no navegador, sem instalação.
        </p>
        <div className="divide-y rounded-xl border">
          {p.modulos.map((m) => (
            <div key={m.n} className="flex gap-4 p-4">
              <span className="w-10 shrink-0 pt-0.5 font-mono text-sm font-semibold text-sky-600 dark:text-sky-400">
                {m.n}
              </span>
              <div className="min-w-0">
                <div className="flex flex-wrap items-baseline gap-2">
                  <h3 className="font-semibold">{m.titulo}</h3>
                  <span className="rounded border px-1.5 py-0.5 text-[10px] font-medium uppercase tracking-wide text-muted-foreground">
                    {tipoLabel[m.tipo]}
                  </span>
                </div>
                <p className="mt-1 text-sm leading-relaxed text-muted-foreground">
                  {m.descricao}
                </p>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* para quem / stack */}
      <section className="mb-12 grid gap-8 sm:grid-cols-2">
        <div>
          <h2 className="mb-3 text-lg font-bold tracking-tight">Para quem é</h2>
          <ul className="space-y-2">
            {p.paraQuem.map((t, i) => (
              <li key={i} className="flex gap-2 text-sm text-muted-foreground">
                <span className="mt-1.5 h-1.5 w-1.5 shrink-0 rounded-sm bg-sky-500" />
                {t}
              </li>
            ))}
          </ul>
        </div>
        <div>
          <h2 className="mb-3 text-lg font-bold tracking-tight">
            Como foi construído
          </h2>
          <ul className="space-y-2">
            {p.stack.map((t, i) => (
              <li key={i} className="flex gap-2 text-sm text-muted-foreground">
                <span className="mt-1.5 h-1.5 w-1.5 shrink-0 rounded-sm bg-sky-500" />
                {t}
              </li>
            ))}
          </ul>
        </div>
      </section>

      {/* chamada final */}
      <section className="rounded-2xl border bg-muted/40 p-8 text-center">
        <h2 className="text-xl font-bold tracking-tight">
          A Arena roda inteira no navegador
        </h2>
        <p className="mx-auto mt-2 max-w-lg text-sm text-muted-foreground">
          Sem instalação, sem cadastro, sem backend. Alterne entre engenharia e
          board no topo da página.
        </p>
        <a
          href={p.href}
          target="_blank"
          rel="noreferrer"
          className="mt-6 inline-flex items-center gap-2 rounded-xl bg-sky-600 px-6 py-3 text-base font-semibold text-white transition hover:bg-sky-700"
        >
          Abrir a Arena
          <span aria-hidden>→</span>
        </a>
      </section>

      <p className="mt-10 text-xs leading-relaxed text-muted-foreground">
        {p.aviso}
      </p>
    </article>
  );
}
