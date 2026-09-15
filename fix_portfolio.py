#!/usr/bin/env python3
"""
fix_portfolio.py — caitano1985.github.io

Tres ajustes em uma execucao:

  1. "Newcomer" -> "Rookie" no ensaio (EN). ES mantem "el Novato",
     PT mantem "O Novato".
  2. Favicon proprio: substitui o icone padrao do scaffold pelo
     logotipo de barras da marca (SVG) e remove o reporter de erros
     da ferramenta de geracao.
  3. Remove o formulario de contato quebrado, deixando a coluna de
     contatos diretos (email / LinkedIn / YouTube) em largura total.

Uso:
    python fix_portfolio.py --dry-run
    python fix_portfolio.py
    python fix_portfolio.py --restore
"""

import argparse
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ESSAY = (ROOT / "public" / "perspective" /
         "network-architect-to-trading-specialist" / "index.html")
INDEX = ROOT / "src" / "routes" / "index.tsx"
ROOT_TSX = ROOT / "src" / "routes" / "__root.tsx"
FAVICON_SVG = ROOT / "public" / "favicon.svg"
FAVICON_ICO = ROOT / "public" / "favicon.ico"

C = {"ok": "\033[92m", "warn": "\033[93m", "err": "\033[91m",
     "info": "\033[96m", "bold": "\033[1m", "end": "\033[0m"}


def log(tag, msg):
    color = {"OK": "ok", "!!": "warn", "XX": "err", "->": "info"}.get(tag, "info")
    print(f"{C[color]}[{tag}]{C['end']} {msg}")


# ---------------------------------------------------------------- favicon
FAVICON = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">
  <rect width="32" height="32" rx="7" fill="#08213E"/>
  <g stroke-linecap="round">
    <line x1="6"  y1="22" x2="6"  y2="16" stroke="#00BCEB" stroke-width="3"/>
    <line x1="11" y1="22" x2="11" y2="12" stroke="#0B5CD5" stroke-width="3"/>
    <line x1="16" y1="22" x2="16" y2="8"  stroke="#FFFFFF" stroke-width="3"/>
    <line x1="21" y1="22" x2="21" y2="12" stroke="#0B5CD5" stroke-width="3"/>
    <line x1="26" y1="22" x2="26" y2="16" stroke="#00BCEB" stroke-width="3"/>
  </g>
</svg>
'''

# --------------------------------------------------------- 1. ROOKIE (EN)
ROOKIE = [
    ("The Advantage of the Newcomer", "The Advantage of the Rookie"),
    ("The Newcomer is not an intruder. He is the professional",
     "The Rookie is not an intruder. He is the professional"),
    ("The Newcomer does not accept", "The Rookie does not accept"),
    ("The Newcomer experiences this not as humiliation",
     "The Rookie experiences this not as humiliation"),
    ("The Newcomer retains an advantage", "The Rookie retains an advantage"),
    ("AUTHOR\u2019S NOTE \u2014 THE NEWCOMER", "AUTHOR\u2019S NOTE \u2014 THE ROOKIE"),
    ("Throughout this piece I call myself <strong>\u201cthe Newcomer\u201d</strong>",
     "Throughout this piece I call myself <strong>\u201cthe Rookie\u201d</strong>"),
    ("taught me about the value of the newcomer.",
     "taught me about the value of the rookie."),
]

# ------------------------------------------------- 3. contato sem formulario
CONTACT_OLD_GRID = '''        <div className="grid gap-10 md:grid-cols-2">
          <div>
            <p className="leading-relaxed text-muted-foreground">{t("contact.desc")}</p>'''
CONTACT_NEW_GRID = '''        <div className="max-w-2xl">
          <div>
            <p className="leading-relaxed text-muted-foreground">{t("contact.desc")}</p>'''

ONSUBMIT = re.compile(
    r"\n  const onSubmit = async \(e: FormEvent\) => \{.*?\n  \};\n", re.S)
FORM_BLOCK = re.compile(
    r"\n\n          <form onSubmit=\{onSubmit\}.*?\n          </form>\n", re.S)


def patch_essay(res):
    if not ESSAY.exists():
        res.append(("!!", "ensaio nao encontrado, pulando"))
        return None
    # o ensaio e entregue ja corrigido; esta etapa e apenas rede de seguranca
    h = ESSAY.read_text(encoding="utf-8")
    if "Rookie" in h:
        res.append(("!!", "ensaio: ja usa Rookie, pulando"))
        return None
    n = 0
    for old, new in ROOKIE:
        if old in h:
            h = h.replace(old, new)
            n += 1
    if n == 0:
        res.append(("!!", "ensaio: nada a trocar (ja corrigido), pulando"))
        return None
    res.append(("OK", f"ensaio: {n}/{len(ROOKIE)} trechos EN -> Rookie"))
    if "Newcomer" in h or "newcomer" in h:
        res.append(("!!", "ensaio: ainda restam ocorrencias de Newcomer"))
    return h


def patch_root(res):
    h = ROOT_TSX.read_text(encoding="utf-8")
    before = h

    h = h.replace(
        '      { rel: "icon", href: "/favicon.ico", type: "image/x-icon" },\n',
        '      { rel: "icon", href: "/favicon.svg", type: "image/svg+xml" },\n')
    if h != before:
        res.append(("OK", "root: favicon apontado para /favicon.svg"))
    else:
        res.append(("!!", "root: link do favicon nao encontrado"))

    h2 = h.replace(
        'import { reportLovableError } from "../lib/lovable-error-reporting";\n', "")
    h2 = re.sub(
        r"  useEffect\(\(\) => \{\n"
        r'    reportLovableError\(error, \{ boundary: "tanstack_root_error_component" \}\);\n'
        r"  \}, \[error\]\);\n\n", "", h2)
    if h2 != h:
        res.append(("OK", "root: reporter da ferramenta de geracao removido"))
        h = h2
    else:
        res.append(("!!", "root: reporter ja removido ou nao encontrado"))

    # useEffect pode ficar sem uso apos a remocao
    if "useEffect" not in h.split("import")[-1] and h.count("useEffect") == 1:
        h = re.sub(r"import \{ useEffect \} from \"react\";\n", "", h)
        h = h.replace("{ useEffect, ", "{ ").replace(", useEffect }", " }")
        res.append(("OK", "root: import useEffect nao utilizado removido"))
    return h


def patch_index(res):
    h = INDEX.read_text(encoding="utf-8")
    if "onSubmit" not in h:
        res.append(("!!", "index: formulario ja removido, pulando"))
        return None

    h2, n1 = ONSUBMIT.subn("\n", h, count=1)
    res.append(("OK" if n1 else "XX", "index: handler onSubmit removido"))

    h3, n2 = FORM_BLOCK.subn("\n", h2, count=1)
    res.append(("OK" if n2 else "XX", "index: bloco <form> removido"))

    if CONTACT_OLD_GRID in h3:
        h3 = h3.replace(CONTACT_OLD_GRID, CONTACT_NEW_GRID)
        res.append(("OK", "index: contatos em coluna unica"))
    else:
        res.append(("!!", "index: grid de contato nao encontrado"))

    # estado e imports orfaos
    h3 = h3.replace("  const [sent, setSent] = useState(false);\n", "")
    h3 = h3.replace("  const [sending, setSending] = useState(false);\n", "")
    h3 = h3.replace('import { useState, type FormEvent } from "react";\n', "")
    res.append(("OK", "index: estado e imports orfaos removidos"))

    if "useState" in h3 or "FormEvent" in h3:
        res.append(("!!", "index: ainda ha referencia a useState/FormEvent \u2014 revise"))
    return h3


TARGETS = [ESSAY, INDEX, ROOT_TSX]


def preflight():
    if not (ROOT / ".git").exists():
        log("XX", f"nao e um repositorio git: {ROOT}")
        sys.exit(1)
    for f in (INDEX, ROOT_TSX):
        if not f.exists():
            log("XX", f"nao encontrado: {f.relative_to(ROOT)}")
            sys.exit(1)
    log("OK", "alvos localizados")


def restore():
    n = 0
    for f in TARGETS:
        bak = f.with_suffix(f.suffix + ".bak")
        if bak.exists():
            shutil.copy2(bak, f)
            bak.unlink()
            log("OK", f"restaurado {f.relative_to(ROOT)}")
            n += 1
    if FAVICON_SVG.exists():
        FAVICON_SVG.unlink()
        log("OK", "favicon.svg removido")
    log("OK" if n else "!!", f"{n} arquivo(s) restaurado(s)")


def run(dry_run=False):
    buffers, hard = {}, False

    for label, fn, target in (
        ("1. Rookie (EN)", patch_essay, ESSAY),
        ("2. Identidade visual", patch_root, ROOT_TSX),
        ("3. Formulario de contato", patch_index, INDEX),
    ):
        print(f"\n  {C['bold']}{label}{C['end']}")
        res = []
        out = fn(res)
        for tag, msg in res:
            log(tag, f"    {msg}")
            if tag == "XX":
                hard = True
        if out is not None:
            buffers[target] = out

    if hard:
        print()
        log("XX", "erro critico \u2014 nada foi gravado")
        return False
    if not buffers and FAVICON_SVG.exists():
        log("!!", "nada a fazer")
        return False
    if dry_run:
        print()
        log("!!", f"dry-run: {len(buffers)} arquivo(s) validado(s), nada gravado")
        return False

    print()
    FAVICON_SVG.parent.mkdir(parents=True, exist_ok=True)
    FAVICON_SVG.write_text(FAVICON, encoding="utf-8")
    log("OK", "criado public/favicon.svg")

    if FAVICON_ICO.exists():
        FAVICON_ICO.rename(FAVICON_ICO.with_suffix(".ico.bak"))
        log("OK", "favicon.ico antigo movido para favicon.ico.bak")

    for f, content in buffers.items():
        shutil.copy2(f, f.with_suffix(f.suffix + ".bak"))
        f.write_text(content, encoding="utf-8")
        log("OK", f"gravado {f.relative_to(ROOT)}")
    return True


def main():
    ap = argparse.ArgumentParser(description="Tres ajustes de credibilidade")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--restore", action="store_true")
    args = ap.parse_args()

    print(f"\n{C['bold']}Portfolio \u2014 ajustes{C['end']}")
    print(f"{'-' * 62}")

    if args.restore:
        restore()
        return

    preflight()
    ok = run(dry_run=args.dry_run)

    print(f"\n{C['bold']}{'=' * 62}{C['end']}")
    if args.dry_run:
        print("  DRY-RUN concluido. Rode sem --dry-run para gravar.")
    elif ok:
        print(f"{C['bold']}  AJUSTES APLICADOS{C['end']}")
        print(f"{'=' * 62}")
        print("  Testar:\n")
        print("    bun run dev        # confira o icone na aba do navegador")
        print("    bun run build\n")
        print("  Publicar:\n")
        print("    git add src/ public/")
        print('    git commit -m "fix: own favicon, remove broken contact form,'
              ' rename Newcomer to Rookie"')
        print("    git push origin main\n")
        print("  Desfazer:  python fix_portfolio.py --restore")
    print(f"{'=' * 62}\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        log("!!", "interrompido")
        sys.exit(130)
