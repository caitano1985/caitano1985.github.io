#!/usr/bin/env python3
"""
deploy_perspective.py
Publica o artigo Perspective no repositorio caitano1985.github.io

Uso:
    python deploy_perspective.py
    python deploy_perspective.py --dry-run
    python deploy_perspective.py --no-push
"""

import argparse
import os
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

# ---------------------------------------------------------------- CONFIG
REPO_ROOT = Path(__file__).resolve().parent
SLUG = "network-architect-to-trading-specialist"
SOURCE_FILE = REPO_ROOT / "perspective-network-architect-to-trading-specialist.html"
TARGET_DIR = REPO_ROOT / "public" / "perspective" / SLUG
TARGET_FILE = TARGET_DIR / "index.html"
BRANCH = "main"
COMMIT_MSG = f"feat(perspective): publish essay '{SLUG}'"

C = {
    "ok": "\033[92m", "warn": "\033[93m", "err": "\033[91m",
    "info": "\033[96m", "bold": "\033[1m", "end": "\033[0m",
}


def log(tag, msg):
    color = {"OK": "ok", "!!": "warn", "XX": "err", "->": "info"}.get(tag, "info")
    print(f"{C[color]}[{tag}]{C['end']} {msg}")


def run(cmd, check=True, capture=False):
    log("->", " ".join(cmd))
    r = subprocess.run(cmd, cwd=REPO_ROOT, check=False,
                       capture_output=capture, text=True)
    if check and r.returncode != 0:
        if capture and r.stderr:
            print(r.stderr)
        log("XX", f"comando falhou (exit {r.returncode})")
        sys.exit(r.returncode)
    return r


def preflight():
    log("->", "verificando ambiente")

    if not (REPO_ROOT / ".git").exists():
        log("XX", f"nao e um repositorio git: {REPO_ROOT}")
        log("!!", "coloque este script na raiz de caitano1985.github.io")
        sys.exit(1)

    if not SOURCE_FILE.exists():
        log("XX", f"arquivo de origem nao encontrado: {SOURCE_FILE.name}")
        log("!!", "coloque o HTML do artigo na raiz do repositorio")
        sys.exit(1)

    size_kb = SOURCE_FILE.stat().st_size / 1024
    log("OK", f"origem encontrada: {SOURCE_FILE.name} ({size_kb:.1f} KB)")

    r = run(["git", "rev-parse", "--abbrev-ref", "HEAD"], capture=True)
    current = r.stdout.strip()
    if current != BRANCH:
        log("!!", f"branch atual e '{current}', esperado '{BRANCH}'")
        if input("    continuar mesmo assim? [s/N] ").strip().lower() != "s":
            sys.exit(0)
    else:
        log("OK", f"branch: {current}")

    return True


def validate_html():
    log("->", "validando HTML")
    html = SOURCE_FILE.read_text(encoding="utf-8")

    checks = [
        ("<!doctype html>", "doctype"),
        ('data-lang="en"', "idioma base EN"),
        ('"es":', "traducao ES") if '"es":' in html else ("es:{", "traducao ES"),
        ("pt:{", "traducao PT-BR"),
        ("pt-only", "bloco O Novato (PT)"),
        ("</html>", "fechamento"),
    ]
    failed = []
    for needle, label in checks:
        if needle in html:
            log("OK", f"  {label}")
        else:
            failed.append(label)
            log("!!", f"  {label} — NAO ENCONTRADO")

    if failed:
        log("!!", f"{len(failed)} verificacao(oes) falharam")
        if input("    continuar? [s/N] ").strip().lower() != "s":
            sys.exit(1)
    return True


def copy_article(dry_run=False):
    log("->", f"destino: public/perspective/{SLUG}/index.html")
    if dry_run:
        log("!!", "dry-run: copia nao executada")
        return
    TARGET_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copy2(SOURCE_FILE, TARGET_FILE)
    log("OK", f"copiado ({TARGET_FILE.stat().st_size / 1024:.1f} KB)")


def git_status():
    r = run(["git", "status", "--porcelain"], capture=True)
    return r.stdout.strip()


def commit_and_push(dry_run=False, push=True):
    changes = git_status()
    if not changes:
        log("!!", "nenhuma alteracao a commitar")
        return False

    print(f"\n{C['bold']}Alteracoes detectadas:{C['end']}")
    for line in changes.splitlines():
        print(f"   {line}")
    print()

    if dry_run:
        log("!!", "dry-run: commit e push nao executados")
        return False

    if input("Confirmar commit e push? [s/N] ").strip().lower() != "s":
        log("!!", "cancelado pelo usuario")
        return False

    run(["git", "add", "public/perspective/"])
    run(["git", "commit", "-m", COMMIT_MSG])
    log("OK", "commit criado")

    if push:
        run(["git", "push", "origin", BRANCH])
        log("OK", "push concluido")
    else:
        log("!!", "--no-push: commit local apenas")
    return True


def summary(pushed):
    url = f"https://caitano1985.github.io/perspective/{SLUG}/"
    print(f"\n{C['bold']}{'=' * 62}{C['end']}")
    print(f"{C['bold']}  DEPLOY — PERSPECTIVE{C['end']}")
    print(f"{'=' * 62}")
    print(f"  Artigo    : {SLUG}")
    print(f"  Data      : {date.today().isoformat()}")
    print(f"  Caminho   : public/perspective/{SLUG}/index.html")
    print(f"  URL       : {url}")
    print(f"  Status    : {'PUBLICADO' if pushed else 'LOCAL'}")
    print(f"{'=' * 62}")
    if pushed:
        print(f"\n  O GitHub Actions leva ~1-2 min para concluir o build.")
        print(f"  Acompanhe: https://github.com/caitano1985/"
              f"caitano1985.github.io/actions\n")


def main():
    ap = argparse.ArgumentParser(description="Deploy do artigo Perspective")
    ap.add_argument("--dry-run", action="store_true",
                    help="simula sem alterar nada")
    ap.add_argument("--no-push", action="store_true",
                    help="commita local, nao envia ao remoto")
    args = ap.parse_args()

    print(f"\n{C['bold']}Perspective — deploy{C['end']}")
    print(f"{'-' * 62}\n")

    preflight()
    validate_html()
    copy_article(dry_run=args.dry_run)
    pushed = commit_and_push(dry_run=args.dry_run, push=not args.no_push)
    summary(pushed)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        log("!!", "interrompido")
        sys.exit(130)
