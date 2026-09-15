#!/usr/bin/env python3
"""
patch_shared_header.py
Migra as paginas estaticas de caitano1985.github.io para um unico
cabecalho canonico: public/_shared/site-header.js

Alvos:
  public/ull-arena/index.html
  public/perspective/network-architect-to-trading-specialist/index.html

O que faz em cada pagina:
  - remove o <nav class="main-nav"> proprio
  - remove o <div class="tb"> proprio (topbar com bandeiras / lente)
  - insere <div id="jc-header" ...> + <script src="/_shared/site-header.js">
  - reconecta o i18n da pagina ao evento "jc:lang"
  - reconecta a lente ao evento "jc:lens" (apenas ULL Arena)

Uso:
    python patch_shared_header.py --dry-run
    python patch_shared_header.py
    python patch_shared_header.py --restore
"""

import argparse
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SHARED_DIR = ROOT / "public" / "_shared"
SHARED_JS = SHARED_DIR / "site-header.js"
SOURCE_JS = ROOT / "site-header.js"

ARENA = ROOT / "public" / "ull-arena" / "index.html"
ESSAY = (ROOT / "public" / "perspective" /
         "network-architect-to-trading-specialist" / "index.html")

C = {"ok": "\033[92m", "warn": "\033[93m", "err": "\033[91m",
     "info": "\033[96m", "bold": "\033[1m", "end": "\033[0m"}


def log(tag, msg):
    color = {"OK": "ok", "!!": "warn", "XX": "err", "->": "info"}.get(tag, "info")
    print(f"{C[color]}[{tag}]{C['end']} {msg}")


MOUNT_ARENA = '''<div id="jc-header"
     data-title="Mercado Financeiro"
     data-lens="true"
     data-sub-en="— Behind the Scenes"
     data-sub-es="— Tras Bastidores"
     data-sub-pt="— Bastidores"></div>
<script src="/_shared/site-header.js"></script>
'''

MOUNT_ESSAY = '''<div id="jc-header"
     data-title="Perspective"
     data-sub-en="— Capital Markets Technology"
     data-sub-es="— Tecnología de Mercados de Capitales"
     data-sub-pt="— Tecnologia de Mercado de Capitais"></div>
<script src="/_shared/site-header.js"></script>
'''

# CSS proprio de cabecalho que deixa de ser necessario nas paginas
CSS_DROP = [
    r"\.main-nav\{[^}]*\}", r"\.main-nav-inner\{[^}]*\}",
    r"\.main-nav-brand\{[^}]*\}", r"\.main-nav-name\{[^}]*\}",
    r"\.main-nav-alias\{[^}]*\}", r"\.main-nav-links\{[^}]*\}",
    r"\.main-nav-links a\{[^}]*\}", r"\.main-nav-links a:hover\{[^}]*\}",
    r"\.main-nav-home\{[^}]*\}", r"\.main-nav-home:hover\{[^}]*\}",
    r"@media\(max-width:900px\)\{\.main-nav-links\{display:none\}\.main-nav-home\{margin-left:auto\}\}",
    r"\.tb\{top:45px !important\}",
]


def strip_block(html, pattern, label, results):
    """Remove um bloco por regex. Registra resultado."""
    new, n = re.subn(pattern, "", html, count=1, flags=re.S)
    if n:
        results.append(("OK", label))
        return new
    results.append(("!!", label + " (ausente, pulado)"))
    return html


def patch_arena(html, results):
    html = strip_block(html, r'<nav class="main-nav">.*?</nav>\n?',
                       "nav propria removida", results)
    html = strip_block(html, r'<div class="tb"><div class="r">.*?</div></div>\n?',
                       "topbar propria removida", results)

    # ponto de insercao: logo apos <body ...>
    m = re.search(r"<body[^>]*>\n?", html)
    if not m:
        results.append(("XX", "tag <body> nao encontrada"))
        return html
    html = html[:m.end()] + MOUNT_ARENA + html[m.end():]
    results.append(("OK", "mount + script inseridos"))

    # reconecta idioma e lente aos eventos do cabecalho
    old_boot = 'applyLang("en");\nsetArch("ull");'
    new_boot = (
        'window.addEventListener("jc:lang", function(e){ applyLang(e.detail.lang); });\n'
        'window.addEventListener("jc:lens", function(){ runModel(); });\n'
        'applyLang((window.jcHeader && window.jcHeader.lang) || "en");\n'
        'setArch("ull");'
    )
    if old_boot in html:
        html = html.replace(old_boot, new_boot)
        results.append(("OK", "i18n e lente reconectados aos eventos"))
    else:
        results.append(("!!", "boot do script nao encontrado (ja migrado?)"))

    for pat in CSS_DROP:
        html = re.sub(pat, "", html, flags=re.S)
    results.append(("OK", "CSS de cabecalho duplicado removido"))
    return html


def patch_essay(html, results):
    html = strip_block(html, r'<nav class="main-nav">.*?</nav>\n?',
                       "nav propria removida", results)
    html = strip_block(html, r'<div class="tb"><div class="r">.*?</div></div>\n?',
                       "topbar propria removida", results)

    m = re.search(r"<body[^>]*>\n?", html)
    if not m:
        results.append(("XX", "tag <body> nao encontrada"))
        return html
    html = html[:m.end()] + MOUNT_ESSAY + html[m.end():]
    results.append(("OK", "mount + script inseridos"))

    # substitui o boot proprio pelo listener do evento
    old = re.search(
        r'Array\.prototype\.forEach\.call\(document\.querySelectorAll\("\.seg\.flags button"\).*?'
        r'applyLang\(saved&&T\[saved\]\?saved:\(saved==="en"\?"en":"en"\)\);',
        html, flags=re.S)
    if old:
        html = html.replace(old.group(0),
            'window.addEventListener("jc:lang", function(e){ applyLang(e.detail.lang); });\n'
            'applyLang((window.jcHeader && window.jcHeader.lang) || "en");')
        results.append(("OK", "i18n reconectado ao evento"))
    else:
        results.append(("!!", "boot do script nao encontrado (ja migrado?)"))

    for pat in CSS_DROP:
        html = re.sub(pat, "", html, flags=re.S)
    results.append(("OK", "CSS de cabecalho duplicado removido"))
    return html


TARGETS = [(ARENA, "ULL Arena", patch_arena), (ESSAY, "Perspective essay", patch_essay)]


def preflight():
    if not (ROOT / ".git").exists():
        log("XX", f"nao e um repositorio git: {ROOT}")
        sys.exit(1)
    if not SOURCE_JS.exists():
        log("XX", "site-header.js nao encontrado na raiz do repositorio")
        log("!!", "baixe o arquivo e coloque ao lado deste script")
        sys.exit(1)
    missing = [n for f, n, _ in TARGETS if not f.exists()]
    if missing:
        log("XX", "paginas nao encontradas: " + ", ".join(missing))
        sys.exit(1)
    log("OK", "origens e alvos localizados")


def restore():
    n = 0
    for f, name, _ in TARGETS:
        bak = f.with_suffix(f.suffix + ".bak")
        if bak.exists():
            shutil.copy2(bak, f)
            bak.unlink()
            log("OK", f"restaurado {name}")
            n += 1
    log("OK" if n else "!!", f"{n} pagina(s) restaurada(s)")


def run(dry_run=False):
    buffers, hard_fail = {}, False

    for f, name, fn in TARGETS:
        html = f.read_text(encoding="utf-8")
        if 'id="jc-header"' in html:
            log("!!", f"{name}: ja migrado, pulando")
            continue
        print(f"\n  {C['bold']}{name}{C['end']}")
        results = []
        buffers[f] = fn(html, results)
        for tag, msg in results:
            log(tag, f"    {msg}")
            if tag == "XX":
                hard_fail = True

    if hard_fail:
        log("XX", "erro critico \u2014 nada foi gravado")
        return False
    if not buffers:
        log("!!", "nenhuma pagina a migrar")
        return False
    if dry_run:
        print()
        log("!!", f"dry-run: {len(buffers)} pagina(s) validada(s), nada gravado")
        return False

    print()
    SHARED_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copy2(SOURCE_JS, SHARED_JS)
    log("OK", f"publicado public/_shared/site-header.js "
               f"({SHARED_JS.stat().st_size / 1024:.1f} KB)")

    for f, content in buffers.items():
        shutil.copy2(f, f.with_suffix(f.suffix + ".bak"))
        f.write_text(content, encoding="utf-8")
        log("OK", f"gravado {f.relative_to(ROOT)}")
    return True


def main():
    ap = argparse.ArgumentParser(description="Migracao para cabecalho compartilhado")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--restore", action="store_true")
    args = ap.parse_args()

    print(f"\n{C['bold']}Cabecalho compartilhado \u2014 migracao{C['end']}")
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
        print(f"{C['bold']}  MIGRACAO CONCLUIDA{C['end']}")
        print(f"{'=' * 62}")
        print("  Testar:\n")
        print("    bun run dev")
        print("    http://localhost:5173/ull-arena/")
        print("    http://localhost:5173/perspective/"
              "network-architect-to-trading-specialist/\n")
        print("  Publicar:\n")
        print("    git add public/")
        print('    git commit -m "refactor: single shared header for static pages"')
        print("    git push origin main\n")
        print("  Desfazer:  python patch_shared_header.py --restore")
    print(f"{'=' * 62}\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        log("!!", "interrompido")
        sys.exit(130)
