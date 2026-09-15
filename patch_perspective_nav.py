#!/usr/bin/env python3
"""
patch_perspective_nav.py
Aplica no portfolio caitano1985.github.io:
  1. Menu reduzido a 5 links (About / Academy / Projects / Perspective / Contact)
  2. Chaves i18n novas em EN, ES e PT-BR
  3. Secao "Content" substituida por "Perspective" com o card do ensaio

Uso:
    python patch_perspective_nav.py --dry-run
    python patch_perspective_nav.py
    python patch_perspective_nav.py --restore     # desfaz usando os .bak
"""

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HEADER = ROOT / "src" / "components" / "SiteHeader.tsx"
I18N = ROOT / "src" / "lib" / "i18n.tsx"
INDEX = ROOT / "src" / "routes" / "index.tsx"

C = {"ok": "\033[92m", "warn": "\033[93m", "err": "\033[91m",
     "info": "\033[96m", "bold": "\033[1m", "end": "\033[0m"}


def log(tag, msg):
    color = {"OK": "ok", "!!": "warn", "XX": "err", "->": "info"}.get(tag, "info")
    print(f"{C[color]}[{tag}]{C['end']} {msg}")


# ------------------------------------------------------------------ PATCHES
# Cada entrada: (arquivo, rotulo, trecho_antigo, trecho_novo)

P_HEADER_SECTIONS = ('''const sections = [
  ["about", "nav.about"],
  ["experiencia", "nav.experience"],
  ["certificacoes", "nav.certs"],
  ["ensino", "nav.teaching"],
  ["academia", "nav.academic"],
  ["projetos", "nav.projects"],
  ["conteudo", "nav.content"],
  ["contato", "nav.contact"],
] as const;''', '''const sections = [
  ["about", "nav.about"],
  ["academia", "nav.academic"],
  ["projetos", "nav.projects"],
  ["perspective", "nav.perspective"],
  ["contato", "nav.contact"],
] as const;''')

NAV = {
    "en": ('''    "nav.about": "About",
    "nav.experience": "Experience",
    "nav.certs": "Certifications",
    "nav.teaching": "Teaching",
    "nav.academic": "Academy",
    "nav.projects": "Projects",
    "nav.content": "Content",
    "nav.contact": "Contact",''', '''    "nav.about": "About",
    "nav.academic": "Academy",
    "nav.projects": "Projects",
    "nav.perspective": "Perspective",
    "nav.contact": "Contact",'''),
    "es": ('''    "nav.about": "Sobre m\u00ed",
    "nav.experience": "Experiencia",
    "nav.certs": "Certificaciones",
    "nav.teaching": "Ense\u00f1anza",
    "nav.academic": "Academia",
    "nav.projects": "Proyectos",
    "nav.content": "Contenido",
    "nav.contact": "Contacto",''', '''    "nav.about": "Sobre m\u00ed",
    "nav.academic": "Academia",
    "nav.projects": "Proyectos",
    "nav.perspective": "Perspectiva",
    "nav.contact": "Contacto",'''),
    "pt": ('''    "nav.about": "Sobre",
    "nav.experience": "Experi\u00eancia",
    "nav.certs": "Certifica\u00e7\u00f5es",
    "nav.teaching": "Ensino",
    "nav.academic": "Academia",
    "nav.projects": "Projetos",
    "nav.content": "Conte\u00fado",
    "nav.contact": "Contato",''', '''    "nav.about": "Sobre",
    "nav.academic": "Academia",
    "nav.projects": "Projetos",
    "nav.perspective": "Perspectiva",
    "nav.contact": "Contato",'''),
}

CONTENT = {
    "en": ('''    "content.title": "Content & Publications",
    "content.yt": "YouTube \u2014 Josinfo",
    "content.ytd": "Technical videos on network architecture, lab walkthroughs, and infrastructure deep-dives.",
    "content.ytLink": "https://www.youtube.com/@Josinfo",
    "content.a1": "HowTo: Cisco StealthWatch",
    "content.a1d": "Practical guide to deployment and flow analysis with StealthWatch for network visibility.",
    "content.link": "Watch on YouTube",
    "content.linkSoon": "Coming soon",''', '''    "content.title": "Perspective",
    "content.sub": "Essays on capital markets technology, infrastructure strategy, and the view from the architect's chair.",
    "content.a1": "From Network Architect to Trading Network Specialist",
    "content.a1d": "Twenty years of infrastructure, three continents, one market that changed everything \u2014 and what crossing that frontier taught me about the value of the outsider.",
    "content.a1Link": "/perspective/network-architect-to-trading-specialist/",
    "content.yt": "YouTube \u2014 Josinfo",
    "content.ytd": "Technical videos on network architecture, lab walkthroughs, and infrastructure deep-dives.",
    "content.ytLink": "https://www.youtube.com/@Josinfo",
    "content.read": "Read the essay",
    "content.link": "Watch on YouTube",
    "content.linkSoon": "Coming soon",'''),
    "es": ('''    "content.title": "Contenido y Publicaciones",
    "content.yt": "YouTube \u2014 Josinfo",
    "content.ytd": "Videos t\u00e9cnicos sobre arquitectura de redes, walkthroughs de laboratorio e inmersiones en infraestructura.",
    "content.ytLink": "https://www.youtube.com/@Josinfo",
    "content.a1": "HowTo: Cisco StealthWatch",
    "content.a1d": "Gu\u00eda pr\u00e1ctica de implementaci\u00f3n y an\u00e1lisis de flujos con StealthWatch para visibilidad de red.",
    "content.link": "Ver en YouTube",
    "content.linkSoon": "Pr\u00f3ximamente",''', '''    "content.title": "Perspectiva",
    "content.sub": "Ensayos sobre tecnolog\u00eda de mercados de capitales, estrategia de infraestructura y la vista desde la silla del arquitecto.",
    "content.a1": "De Arquitecto de Redes a Especialista en Redes de Trading",
    "content.a1d": "Veinte a\u00f1os de infraestructura, tres continentes, un mercado que lo cambi\u00f3 todo \u2014 y lo que cruzar esa frontera me ense\u00f1\u00f3 sobre el valor del forastero.",
    "content.a1Link": "/perspective/network-architect-to-trading-specialist/",
    "content.yt": "YouTube \u2014 Josinfo",
    "content.ytd": "Videos t\u00e9cnicos sobre arquitectura de redes, walkthroughs de laboratorio e inmersiones en infraestructura.",
    "content.ytLink": "https://www.youtube.com/@Josinfo",
    "content.read": "Leer el ensayo",
    "content.link": "Ver en YouTube",
    "content.linkSoon": "Pr\u00f3ximamente",'''),
    "pt": ('''    "content.title": "Conte\u00fado & Publica\u00e7\u00f5es",
    "content.yt": "YouTube \u2014 Josinfo",
    "content.ytd": "V\u00eddeos t\u00e9cnicos sobre arquitetura de redes, walkthroughs de laborat\u00f3rio e deep-dives em infraestrutura.",
    "content.ytLink": "https://www.youtube.com/@Josinfo",
    "content.a1": "HowTo: Cisco StealthWatch",
    "content.a1d": "Guia pr\u00e1tico de implanta\u00e7\u00e3o e an\u00e1lise de fluxos com StealthWatch para visibilidade de rede.",
    "content.link": "Assistir no YouTube",
    "content.linkSoon": "Em breve",''', '''    "content.title": "Perspectiva",
    "content.sub": "Ensaios sobre tecnologia de mercado de capitais, estrat\u00e9gia de infraestrutura e a vis\u00e3o de quem senta na cadeira do arquiteto.",
    "content.a1": "De Arquiteto de Redes a Especialista em Redes de Trading",
    "content.a1d": "Vinte anos de infraestrutura, tr\u00eas continentes, um mercado que mudou tudo \u2014 e o que atravessar essa fronteira me ensinou sobre o valor do novato.",
    "content.a1Link": "/perspective/network-architect-to-trading-specialist/",
    "content.yt": "YouTube \u2014 Josinfo",
    "content.ytd": "V\u00eddeos t\u00e9cnicos sobre arquitetura de redes, walkthroughs de laborat\u00f3rio e deep-dives em infraestrutura.",
    "content.ytLink": "https://www.youtube.com/@Josinfo",
    "content.read": "Ler o ensaio",
    "content.link": "Assistir no YouTube",
    "content.linkSoon": "Em breve",'''),
}

P_INDEX_ARRAY = ('''  const contents: [string, string, string, string][] = [
    ["content.yt", "content.ytd", "youtube", "content.ytLink"],
    ["content.a1", "content.a1d", "article", ""],
  ];''', '''  const perspectives: [string, string, string, string, string][] = [
    ["content.a1", "content.a1d", "essay", "content.a1Link", "content.read"],
    ["content.yt", "content.ytd", "youtube", "content.ytLink", "content.link"],
  ];''')

P_INDEX_SECTION = ('''      {/* CONTENT */}
      <section id="conteudo" className="border-y border-border bg-surface/40">
        <div className="mx-auto max-w-6xl px-5 py-20">
          <SectionHead label="./content" title={t("content.title")} />
          <div className="grid gap-5 sm:grid-cols-2">
            {contents.map(([title, desc, kind, link]) => (
              <div key={title} className="card-hover rounded-xl border border-border bg-card p-6">
                <span className="font-mono text-[11px] uppercase tracking-widest text-neon">{kind}</span>
                <h3 className="mt-2 font-semibold">{t(title)}</h3>
                <p className="mt-2 text-sm leading-relaxed text-muted-foreground">{t(desc)}</p>
                {link ? (
                  <a href={t(link)} target="_blank" rel="noopener noreferrer" className="mt-4 inline-block font-mono text-xs text-primary hover:underline">{t("content.link")} \u2192</a>
                ) : (
                  <span className="mt-4 inline-block font-mono text-xs text-muted-foreground">{t("content.linkSoon")}</span>
                )}
              </div>
            ))}
          </div>
        </div>
      </section>''', '''      {/* PERSPECTIVE */}
      <section id="perspective" className="border-y border-border bg-surface/40">
        <div className="mx-auto max-w-6xl px-5 py-20">
          <SectionHead label="./perspective" title={t("content.title")} />
          <p className="-mt-4 mb-8 max-w-2xl text-sm leading-relaxed text-muted-foreground">
            {t("content.sub")}
          </p>
          <div className="grid gap-5 sm:grid-cols-2">
            {perspectives.map(([title, desc, kind, link, cta]) => (
              <div key={title} className="card-hover rounded-xl border border-border bg-card p-6">
                <span className="font-mono text-[11px] uppercase tracking-widest text-neon">{kind}</span>
                <h3 className="mt-2 font-semibold">{t(title)}</h3>
                <p className="mt-2 text-sm leading-relaxed text-muted-foreground">{t(desc)}</p>
                {link ? (
                  <a
                    href={t(link)}
                    {...(kind === "youtube" ? { target: "_blank", rel: "noopener noreferrer" } : {})}
                    className="mt-4 inline-block font-mono text-xs text-primary hover:underline"
                  >
                    {t(cta)} \u2192
                  </a>
                ) : (
                  <span className="mt-4 inline-block font-mono text-xs text-muted-foreground">{t("content.linkSoon")}</span>
                )}
              </div>
            ))}
          </div>
        </div>
      </section>''')


def build_plan():
    plan = [(HEADER, "menu reduzido a 5 links", *P_HEADER_SECTIONS)]
    for lang in ("en", "es", "pt"):
        plan.append((I18N, f"chaves nav [{lang.upper()}]", *NAV[lang]))
    for lang in ("en", "es", "pt"):
        plan.append((I18N, f"chaves perspective [{lang.upper()}]", *CONTENT[lang]))
    plan.append((INDEX, "array de cards", *P_INDEX_ARRAY))
    plan.append((INDEX, "secao Perspective", *P_INDEX_SECTION))
    return plan


def normalize(s):
    """Tolera CRLF e espacos finais de linha."""
    return "\n".join(line.rstrip() for line in s.replace("\r\n", "\n").split("\n"))


def preflight():
    if not (ROOT / ".git").exists():
        log("XX", f"nao e um repositorio git: {ROOT}")
        sys.exit(1)
    for f in (HEADER, I18N, INDEX):
        if not f.exists():
            log("XX", f"arquivo nao encontrado: {f.relative_to(ROOT)}")
            sys.exit(1)
    log("OK", "arquivos de origem localizados")


def restore():
    n = 0
    for f in (HEADER, I18N, INDEX):
        bak = f.with_suffix(f.suffix + ".bak")
        if bak.exists():
            shutil.copy2(bak, f)
            bak.unlink()
            log("OK", f"restaurado {f.relative_to(ROOT)}")
            n += 1
    log("OK" if n else "!!", f"{n} arquivo(s) restaurado(s)")


def apply(dry_run=False):
    plan = build_plan()
    buffers, applied, failed = {}, [], []

    for f in (HEADER, I18N, INDEX):
        buffers[f] = normalize(f.read_text(encoding="utf-8"))

    for f, label, old, new in plan:
        old_n, new_n = normalize(old), normalize(new)
        count = buffers[f].count(old_n)
        if count == 1:
            buffers[f] = buffers[f].replace(old_n, new_n)
            applied.append(label)
            log("OK", f"  {label}")
        elif count == 0:
            if normalize(new).split("\n")[0].strip() in buffers[f]:
                log("!!", f"  {label} \u2014 ja aplicado, pulando")
            else:
                failed.append(label)
                log("XX", f"  {label} \u2014 trecho original NAO encontrado")
        else:
            failed.append(label)
            log("XX", f"  {label} \u2014 {count} ocorrencias, ambiguo")

    if failed:
        log("!!", f"{len(failed)} patch(es) falharam \u2014 nada foi gravado")
        log("!!", "o arquivo pode ja ter sido editado a mao; revise antes")
        return False

    if not applied:
        log("!!", "nenhuma alteracao necessaria")
        return False

    if dry_run:
        log("!!", f"dry-run: {len(applied)} patch(es) validados, nada gravado")
        return False

    for f, content in buffers.items():
        bak = f.with_suffix(f.suffix + ".bak")
        shutil.copy2(f, bak)
        f.write_text(content + ("\n" if not content.endswith("\n") else ""),
                     encoding="utf-8")
        log("OK", f"gravado {f.relative_to(ROOT)}  (backup: {bak.name})")

    return True


def main():
    ap = argparse.ArgumentParser(description="Patch do menu + secao Perspective")
    ap.add_argument("--dry-run", action="store_true", help="valida sem gravar")
    ap.add_argument("--restore", action="store_true", help="desfaz usando os .bak")
    args = ap.parse_args()

    print(f"\n{C['bold']}Patch \u2014 menu + Perspective{C['end']}")
    print(f"{'-' * 62}\n")

    if args.restore:
        restore()
        return

    preflight()
    log("->", "aplicando patches")
    ok = apply(dry_run=args.dry_run)

    print(f"\n{C['bold']}{'=' * 62}{C['end']}")
    if args.dry_run:
        print("  DRY-RUN concluido. Rode sem --dry-run para gravar.")
    elif ok:
        print(f"{C['bold']}  PATCH APLICADO{C['end']}")
        print(f"{'=' * 62}")
        print("  Proximos passos:\n")
        print("    bun run dev          # testar em http://localhost:5173")
        print("    bun run build        # validar o build")
        print("    git add src/")
        print('    git commit -m "feat(nav): 5-link menu, Content -> Perspective"')
        print("    git push origin main\n")
        print("  Desfazer:  python patch_perspective_nav.py --restore")
    print(f"{'=' * 62}\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        log("!!", "interrompido")
        sys.exit(130)
