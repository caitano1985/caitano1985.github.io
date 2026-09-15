import { Link, useRouterState } from "@tanstack/react-router";
import { useState } from "react";
import { useI18n } from "@/lib/i18n";

const sections = [
  ["about", "nav.about"],
  ["experiencia", "nav.experience"],
  ["certificacoes", "nav.certs"],
  ["ensino", "nav.teaching"],
  ["academia", "nav.academic"],
  ["projetos", "nav.projects"],
  ["conteudo", "nav.content"],
  ["contato", "nav.contact"],
] as const;

export function SiteHeader() {
  const { t, lang, setLang } = useI18n();
  const [open, setOpen] = useState(false);
  const isHome = useRouterState({ select: (s) => s.location.pathname === "/" });

  const href = (id: string) => (isHome ? `#${id}` : `/#${id}`);

  return (
    <header className="sticky top-0 z-50 border-b border-border/70 bg-background/85 backdrop-blur-md">
      <div className="mx-auto flex max-w-6xl items-center justify-between px-5 py-3">
        <Link to="/" className="flex items-baseline gap-2">
          <span className="font-mono text-base font-bold text-primary">Josimar Caitano</span>
          <span className="hidden text-xs text-muted-foreground sm:inline">じょしまる</span>
        </Link>

        <nav className="hidden items-center gap-5 lg:flex">
          {sections.map(([id, key]) => (
            <a
              key={id}
              href={href(id)}
              className="text-sm text-muted-foreground transition-colors hover:text-primary"
            >
              {t(key)}
            </a>
          ))}
        </nav>

        <div className="flex items-center gap-2">
          <div className="flex overflow-hidden rounded-md border border-border text-sm">
            {([
              { code: "en" as const, flag: "🇺🇸", label: "English (US)" },
              { code: "es" as const, flag: "🇪🇸", label: "Español (ES)" },
              { code: "pt" as const, flag: "🇧🇷", label: "Português (BR)" },
            ]).map(({ code, flag, label }) => (
              <button
                key={code}
                onClick={() => setLang(code)}
                aria-label={label}
                className={`px-2 py-1 transition-colors ${
                  lang === code
                    ? "bg-primary text-primary-foreground"
                    : "text-muted-foreground hover:text-primary"
                }`}
              >
                {flag}
              </button>
            ))}
          </div>
          <button
            className="rounded-md border border-border px-2 py-1 font-mono text-xs text-muted-foreground lg:hidden"
            onClick={() => setOpen((v) => !v)}
            aria-expanded={open}
            aria-label="Menu"
          >
            menu
          </button>
        </div>
      </div>

      {open && (
        <nav className="grid gap-1 border-t border-border px-5 py-3 lg:hidden">
          {sections.map(([id, key]) => (
            <a
              key={id}
              href={href(id)}
              onClick={() => setOpen(false)}
              className="rounded-md px-2 py-2 text-sm text-muted-foreground transition-colors hover:bg-secondary hover:text-primary"
            >
              {t(key)}
            </a>
          ))}
        </nav>
      )}
    </header>
  );
}
