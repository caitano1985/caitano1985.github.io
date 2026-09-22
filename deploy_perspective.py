#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
patch_journal01_i18n.py
=======================
Insere as 4 chaves de traducao que faltam no capitulo 01 do Journal:

    cmp.ap  cmp.bp   -> blocos ASCII  Trading / Post-Trade
    mk.ap   mk.bp    -> tabelas       Order Flow / Market Data

Sem essas chaves os blocos ficam em ingles quando o leitor troca
a bandeira para ES ou PT.

Uso:
    python patch_journal01_i18n.py

Idempotente: rodar duas vezes nao duplica nada.
Faz backup em 01-market-structure.html.bak antes de gravar.
"""

import re
import shutil
import sys
from pathlib import Path

ALVO = "01-market-structure.html"

# ── o que inserir, e depois de qual ancora ───────────────────────────

PATCH_ES = [
    (
        '"cmp.a":"TRADING","cmp.b":"POST-TRADE",',
        '"cmp.ap":"<b>COMPRAR 100 WIN</b>\\n     ↓\\n   ORDEN\\n     ↓\\n CASAMIENTO\\n     ↓\\n  <b>OPERACIÓN</b>",\n'
        '"cmp.bp":"<b>OPERACIÓN</b>\\n   ↓\\nCLEARING\\n   ↓\\n RIESGO\\n   ↓\\nLIQUIDACIÓN\\n   ↓\\n CUSTODIA",'
    ),
    (
        '"mk.a":"ORDER FLOW · trader → bolsa","mk.b":"MARKET DATA · bolsa → todos",',
        '"mk.ap":"Protocolo  <b>TCP</b>\\nTopología  unicast 1:1\\nVolumen    moderado\\nFalla      caída de sesión\\nTolerancia <b>cero pérdida</b>",\n'
        '"mk.bp":"Protocolo  <b>UDP multicast</b>\\nTopología  1:N simultáneo\\nVolumen    enorme\\nFalla      gap de paquete\\nTolerancia <b>gap + recuperar</b>",'
    ),
]

PATCH_PT = [
    (
        '"cmp.a":"NEGOCIAÇÃO","cmp.b":"PÓS-NEGOCIAÇÃO",',
        '"cmp.ap":"<b>COMPRAR 100 WIN</b>\\n     ↓\\n   ORDEM\\n     ↓\\n CASAMENTO\\n     ↓\\n  <b>NEGÓCIO</b>",\n'
        '"cmp.bp":"<b>NEGÓCIO</b>\\n   ↓\\nCLEARING\\n   ↓\\n  RISCO\\n   ↓\\nLIQUIDAÇÃO\\n   ↓\\n CUSTÓDIA",'
    ),
    (
        '"mk.a":"ORDER FLOW · trader → bolsa","mk.b":"MARKET DATA · bolsa → todos",',
        '"mk.ap":"Protocolo  <b>TCP</b>\\nTopologia  unicast 1:1\\nVolume     moderado\\nFalha      queda de sessão\\nTolância <b>perda zero</b>",\n'
        '"mk.bp":"Protocolo  <b>UDP multicast</b>\\nTopologia  1:N simultâneo\\nVolume     enorme\\nFalha      gap de pacote\\nTolância <b>gap + recuperar</b>",'
    ),
]

# correcao: "Tolerancia" em PT
PATCH_PT = [
    (a, b.replace("Tolância", "Tolerância")) for a, b in PATCH_PT
]


class C:
    OK = "\033[92m"; ERR = "\033[91m"; DIM = "\033[90m"; B = "\033[1m"; END = "\033[0m"


if sys.platform == "win32":
    try:
        import ctypes
        k = ctypes.windll.kernel32
        k.SetConsoleMode(k.GetStdHandle(-11), 7)
    except Exception:
        for n in ("OK", "ERR", "DIM", "B", "END"):
            setattr(C, n, "")


def aplicar(bloco: str, patches, nome: str):
    """Insere cada patch no bloco. Devolve (bloco novo, quantas chaves inseriu)."""
    n = 0
    for ancora, insercao in patches:
        chaves = re.findall(r'^"([^"]+)":', insercao, re.M)   # ex: cmp.ap, cmp.bp
        rotulo = " + ".join(chaves)
        if all(f'"{k}":' in bloco for k in chaves):
            print(f"  {C.DIM}{nome}: {rotulo} ja existem{C.END}")
            continue
        if ancora not in bloco:
            print(f"  {C.ERR}{nome}: ancora nao encontrada para {rotulo}{C.END}")
            print(f"  {C.DIM}  esperava: {ancora[:60]}...{C.END}")
            return bloco, -1
        bloco = bloco.replace(ancora, ancora + "\n" + insercao, 1)
        print(f"  {C.OK}{nome}: {rotulo} inseridas{C.END}")
        n += len(chaves)
    return bloco, n


def main():
    raiz = Path(__file__).resolve().parent
    arq = raiz / ALVO
    if not arq.is_file():
        arq = Path.cwd() / ALVO
    if not arq.is_file():
        print(f"{C.ERR}nao encontrei {ALVO}{C.END}")
        print(f"{C.DIM}rode a partir da raiz do repositorio{C.END}")
        return 1

    print(f"\n{C.B}PATCH i18n — Journal 01{C.END}")
    print(f"  {C.DIM}{arq}{C.END}\n")

    html = arq.read_text(encoding="utf-8")

    i_es = html.find("es:{")
    i_pt = html.find("pt:{")
    if i_es == -1 or i_pt == -1:
        print(f"{C.ERR}nao encontrei os dicionarios es:{{ }} / pt:{{ }}{C.END}")
        return 1

    cabeca = html[:i_es]
    bloco_es = html[i_es:i_pt]
    bloco_pt = html[i_pt:]

    bloco_es, n_es = aplicar(bloco_es, PATCH_ES, "ES")
    if n_es < 0:
        return 1
    bloco_pt, n_pt = aplicar(bloco_pt, PATCH_PT, "PT")
    if n_pt < 0:
        return 1

    total = n_es + n_pt
    if total == 0:
        print(f"\n{C.OK}Arquivo ja esta completo. Nada a fazer.{C.END}\n")
        return 0

    novo = cabeca + bloco_es + bloco_pt

    # verificacao antes de gravar
    chaves = set(re.findall(r'data-i18n="([^"]+)"', novo))
    j_es, j_pt = novo.find("es:{"), novo.find("pt:{")
    b_es, b_pt = novo[j_es:j_pt], novo[j_pt:]
    faltam_es = sorted(k for k in chaves if f'"{k}":' not in b_es)
    faltam_pt = sorted(k for k in chaves if f'"{k}":' not in b_pt)

    print()
    if faltam_es or faltam_pt:
        print(f"{C.ERR}ainda faltam chaves apos o patch — nada foi gravado{C.END}")
        if faltam_es:
            print(f"  ES: {', '.join(faltam_es)}")
        if faltam_pt:
            print(f"  PT: {', '.join(faltam_pt)}")
        return 1

    shutil.copy2(arq, arq.with_suffix(".html.bak"))
    arq.write_text(novo, encoding="utf-8", newline="\n")

    print(f"{C.OK}{C.B}OK{C.END}  {total} chave(s) inserida(s)")
    print(f"  {C.DIM}{len(chaves)} chaves i18n no total, EN/ES/PT completos{C.END}")
    print(f"  {C.DIM}backup: {ALVO}.bak{C.END}")
    print(f"\n  proximo:  python deploy_journal.py --dry-run\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
