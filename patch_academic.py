#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
patch_academy_link.py
=====================
Liga a secao Academy da home ao Trading Network Journal.

Troca o placeholder "Materials available soon" por um card real
apontando para /academy/trading-network-journal/

Mexe em dois arquivos:
    src/lib/i18n.tsx      -> 4 chaves novas em en / es / pt
    src/routes/index.tsx  -> o bloco JSX da secao Academy

Uso:
    python patch_academy_link.py --dry-run   # mostra o que mudaria
    python patch_academy_link.py             # aplica
    python patch_academy_link.py --revert    # volta do .bak

Idempotente. Faz backup .bak antes de gravar.

IMPORTANTE: o link e um <a href>, nao um <Link to>.
O caminho vem de public/, e arquivo estatico, nao rota do router.
"""

import argparse
import re
import shutil
import sys
from pathlib import Path

I18N = "src/lib/i18n.tsx"
ROUTE = "src/routes/index.tsx"

# ── chaves novas, ancoradas no academic.coming de cada idioma ────────

CHAVES = {
    "en": (
        '"academic.coming": "Materials available soon",',
        '    "academic.journal.title": "Trading Network Journal",\n'
        '    "academic.journal.desc": "A documented descent from market mechanism to physical infrastructure. One layer per entry, each closing with a lab.",\n'
        '    "academic.journal.meta": "3 entries · interactive labs · EN / ES / PT",\n'
        '    "academic.journal.cta": "Open the Journal",'
    ),
    "es": (
        '"academic.coming": "Materiales disponibles pronto",',
        '    "academic.journal.title": "Diario de Redes de Trading",\n'
        '    "academic.journal.desc": "Un descenso documentado desde el mecanismo de mercado hasta la infraestructura física. Una capa por entrada, cada una con su laboratorio.",\n'
        '    "academic.journal.meta": "3 entradas · laboratorios interactivos · EN / ES / PT",\n'
        '    "academic.journal.cta": "Abrir el Diario",'
    ),
    "pt": (
        '"academic.coming": "Materiais disponíveis em breve",',
        '    "academic.journal.title": "Diário de Redes de Trading",\n'
        '    "academic.journal.desc": "Uma descida documentada do mecanismo de mercado até a infraestrutura física. Uma camada por entrada, cada uma com seu laboratório.",\n'
        '    "academic.journal.meta": "3 entradas · laboratórios interativos · EN / ES / PT",\n'
        '    "academic.journal.cta": "Abrir o Diário",'
    ),
}

# ── o placeholder na home, tolerante a indentacao ────────────────────

PLACEHOLDER = re.compile(
    r'([ \t]*)<div className="rounded-xl border border-dashed[^"]*">\s*'
    r'<p className="[^"]*">\{t\("academic\.coming"\)\}</p>\s*'
    r'</div>',
    re.S,
)

CARD = '''{i}<a
{i}  href="/academy/trading-network-journal/"
{i}  className="group flex flex-col gap-4 rounded-xl border border-border bg-card p-6 transition-colors hover:border-primary sm:flex-row sm:items-center sm:gap-6"
{i}>
{i}  <span className="font-mono text-2xl font-semibold text-primary">01&ndash;03</span>
{i}  <span className="flex-1">
{i}    <span className="block font-semibold">{{t("academic.journal.title")}}</span>
{i}    <span className="mt-1 block text-sm text-muted-foreground">{{t("academic.journal.desc")}}</span>
{i}    <span className="mt-2 block font-mono text-xs text-muted-foreground">{{t("academic.journal.meta")}}</span>
{i}  </span>
{i}  <span className="font-mono text-sm text-primary group-hover:underline">{{t("academic.journal.cta")}} &rarr;</span>
{i}</a>'''


class C:
    OK = "\033[92m"; WARN = "\033[93m"; ERR = "\033[91m"
    DIM = "\033[90m"; B = "\033[1m"; CY = "\033[96m"; END = "\033[0m"


if sys.platform == "win32":
    try:
        import ctypes
        k = ctypes.windll.kernel32
        k.SetConsoleMode(k.GetStdHandle(-11), 7)
    except Exception:
        for n in ("OK", "WARN", "ERR", "DIM", "B", "CY", "END"):
            setattr(C, n, "")


def head(t): print(f"\n{C.B}{C.CY}{t}{C.END}")
def ok(t):   print(f"  {C.OK}OK{C.END}   {t}")
def warn(t): print(f"  {C.WARN}!{C.END}    {t}")
def err(t):  print(f"  {C.ERR}FALHA{C.END} {t}")
def dim(t):  print(f"  {C.DIM}{t}{C.END}")


def patch_i18n(txt: str):
    """Insere as 4 chaves nos tres blocos de idioma."""
    n = 0
    for lang, (ancora, insercao) in CHAVES.items():
        if ancora not in txt:
            err(f"{lang}: nao achei a ancora academic.coming")
            dim(f"  esperava: {ancora}")
            return None, -1
        pos = txt.find(ancora)
        trecho = txt[pos:pos + 700]
        if '"academic.journal.title"' in trecho:
            dim(f"{lang}: chaves ja existem")
            continue
        txt = txt[:pos] + ancora + "\n" + insercao + txt[pos + len(ancora):]
        ok(f"{lang}: 4 chaves inseridas")
        n += 4
    return txt, n


def patch_route(txt: str):
    """Troca o placeholder pelo card."""
    if 'href="/academy/trading-network-journal/"' in txt:
        dim("card ja existe")
        return txt, 0
    m = PLACEHOLDER.search(txt)
    if not m:
        err("nao achei o bloco placeholder da secao Academy")
        dim('  procurei por: <div className="rounded-xl border border-dashed ...">')
        dim('                  <p ...>{t("academic.coming")}</p>')
        dim('                </div>')
        return None, -1
    indent = m.group(1)
    novo = CARD.format(i=indent)
    txt = txt[:m.start()] + novo + txt[m.end():]
    ok("placeholder trocado pelo card do Journal")
    return txt, 1


def main():
    ap = argparse.ArgumentParser(description="Liga a Academy ao Trading Network Journal")
    ap.add_argument("--dry-run", action="store_true", help="mostra sem gravar")
    ap.add_argument("--revert", action="store_true", help="restaura dos .bak")
    a = ap.parse_args()

    raiz = Path(__file__).resolve().parent
    if not (raiz / "src").is_dir():
        raiz = Path.cwd()

    f_i18n, f_route = raiz / I18N, raiz / ROUTE

    print(f"\n{C.B}ACADEMY -> TRADING NETWORK JOURNAL{C.END}")
    dim(f"repo: {raiz}")

    for f, nome in ((f_i18n, I18N), (f_route, ROUTE)):
        if not f.is_file():
            err(f"nao encontrei {nome}")
            dim("rode a partir da raiz do repositorio")
            return 1

    # ── revert ────────────────────────────────────────────────────────
    if a.revert:
        head("RESTAURANDO")
        n = 0
        for f in (f_i18n, f_route):
            bak = Path(str(f) + ".bak")
            if bak.is_file():
                shutil.copy2(bak, f)
                ok(f"{f.name} restaurado")
                n += 1
            else:
                warn(f"{f.name}: sem .bak")
        print(f"\n{C.OK}{n} arquivo(s) restaurado(s){C.END}\n")
        return 0

    # ── i18n ──────────────────────────────────────────────────────────
    head(f"1. {I18N}")
    t_i18n = f_i18n.read_text(encoding="utf-8")
    novo_i18n, n1 = patch_i18n(t_i18n)
    if n1 < 0:
        return 1

    # ── route ─────────────────────────────────────────────────────────
    head(f"2. {ROUTE}")
    t_route = f_route.read_text(encoding="utf-8")
    novo_route, n2 = patch_route(t_route)
    if n2 < 0:
        return 1

    if n1 == 0 and n2 == 0:
        print(f"\n{C.OK}Tudo ja aplicado. Nada a fazer.{C.END}\n")
        return 0

    # ── preview ───────────────────────────────────────────────────────
    if n2 > 0:
        head("3. COMO FICA O JSX")
        m = re.search(r'[ \t]*<a\n[ \t]*href="/academy/trading-network-journal/".*?</a>',
                      novo_route, re.S)
        if m:
            for l in m.group(0).splitlines():
                print(f"  {C.DIM}{l}{C.END}")

    if a.dry_run:
        print(f"\n{C.WARN}dry-run: nada foi gravado.{C.END}\n")
        return 0

    # ── gravar ────────────────────────────────────────────────────────
    head("4. GRAVANDO")
    if n1 > 0:
        shutil.copy2(f_i18n, Path(str(f_i18n) + ".bak"))
        f_i18n.write_text(novo_i18n, encoding="utf-8", newline="\n")
        ok(f"{I18N}  ({n1} chaves)")
    if n2 > 0:
        shutil.copy2(f_route, Path(str(f_route) + ".bak"))
        f_route.write_text(novo_route, encoding="utf-8", newline="\n")
        ok(f"{ROUTE}")

    print(f"""
{C.B}PROXIMO PASSO{C.END}
  {C.DIM}teste local:{C.END}  bun run dev      {C.DIM}(ou npm run dev){C.END}
  {C.DIM}confira:{C.END}      a secao Academy nas 3 bandeiras
  {C.DIM}publique:{C.END}     git add src && git commit -m "Academy: link para o Journal" && git push

  {C.DIM}se algo quebrar:{C.END}  python patch_academy_link.py --revert
""")
    return 0


if __name__ == "__main__":
    sys.exit(main())
