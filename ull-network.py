#!/usr/bin/env python3
"""Fix prerender — exclui /ull-arena do prerender"""
from pathlib import Path
import sys

f = Path("vite.config.ts")
if not f.exists():
    print("ERRO: vite.config.ts não encontrado"); sys.exit(1)

c = f.read_text("utf-8")

old = """    prerender: {
      enabled: true,
    },"""

new = """    prerender: {
      enabled: true,
      ignore: ["/ull-arena", "/ull-arena/"],
    },"""

if old in c:
    c = c.replace(old, new)
    f.write_text(c, "utf-8")
    print("✓ vite.config.ts — prerender ignore adicionado")
elif "ignore" in c:
    print("✓ já corrigido")
else:
    print("✗ trecho não encontrado — verifique manualmente")
