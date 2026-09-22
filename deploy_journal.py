#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
deploy_journal.py
=================
Publica o Trading Network Journal em public/academy/trading-network-journal/

Uso:
    python deploy_journal.py              # valida + grava + mostra o que mudou
    python deploy_journal.py --commit     # idem + git add + git commit
    python deploy_journal.py --push       # idem + git push
    python deploy_journal.py --dry-run    # só valida, não escreve nada
    python deploy_journal.py --no-index   # não gera a página índice do Journal

Rode a partir da raiz do repositório caitano1985.github.io
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

# ──────────────────────────────────────────────────────────────────────
# CONFIGURAÇÃO
# ──────────────────────────────────────────────────────────────────────

BASE = "public/academy/trading-network-journal"

CAPITULOS = [
    {
        "src": "01-market-structure.html",
        "slug": "01-market-structure",
        "num": "01",
        "en": ("Market Structure",
               "The market mechanism that every piece of trading infrastructure exists to execute."),
        "es": ("Estructura de Mercado",
               "El mecanismo de mercado que toda infraestructura de trading existe para ejecutar."),
        "pt": ("Estrutura de Mercado",
               "O mecanismo de mercado que toda infraestrutura de trading existe para executar."),
    },
    {
        "src": "02-order-lifecycle.html",
        "slug": "02-order-lifecycle",
        "num": "02",
        "en": ("The Order Lifecycle",
               "One order followed end to end — where latency lives and where an order dies."),
        "es": ("El Ciclo de Vida de la Orden",
               "Una orden seguida de extremo a extremo — dónde vive la latencia y dónde muere una orden."),
        "pt": ("O Ciclo de Vida da Ordem",
               "Uma ordem seguida de ponta a ponta — onde mora a latência e onde uma ordem morre."),
    },
    {
        "src": "03-protocols.html",
        "slug": "03-protocols",
        "num": "03",
        "en": ("Trading Protocols & Connectivity",
               "Sequence, gap detection, recovery and sessions — reliability above an unreliable transport."),
        "es": ("Protocolos de Trading y Conectividad",
               "Secuencia, detección de gaps, recuperación y sesiones — confiabilidad sobre un transporte no confiable."),
        "pt": ("Protocolos de Trading e Conectividade",
               "Sequência, detecção de gap, recuperação e sessões — confiabilidade sobre um transporte não confiável."),
    },
]

COMMIT_MSG = """Academy: publica Trading Network Journal 01-03

Trading Network Journal, tres capitulos com laboratorios interativos
e traducao completa EN/ES/PT no contrato do site:

  01 - Market Structure
  02 - The Order Lifecycle
  03 - Trading Protocols & Connectivity

Servidos em /academy/trading-network-journal/<slug>/

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01BTwXH2ZHPFFpM6GugRMrGg
"""

# ──────────────────────────────────────────────────────────────────────
# SAÍDA
# ──────────────────────────────────────────────────────────────────────

class C:
    OK = "\033[92m"; WARN = "\033[93m"; ERR = "\033[91m"
    DIM = "\033[90m"; B = "\033[1m"; CY = "\033[96m"; END = "\033[0m"

    @classmethod
    def off(cls):
        for k in ("OK", "WARN", "ERR", "DIM", "B", "CY", "END"):
            setattr(cls, k, "")


if sys.platform == "win32":
    try:
        import colorama  # type: ignore
        colorama.just_fix_windows_console()
    except Exception:
        try:
            import ctypes
            k = ctypes.windll.kernel32
            k.SetConsoleMode(k.GetStdHandle(-11), 7)
        except Exception:
            C.off()


def head(t):  print(f"\n{C.B}{C.CY}{t}{C.END}")
def ok(t):    print(f"  {C.OK}OK{C.END}   {t}")
def warn(t):  print(f"  {C.WARN}!{C.END}    {t}")
def err(t):   print(f"  {C.ERR}FALHA{C.END} {t}")
def info(t):  print(f"  {C.DIM}{t}{C.END}")


# ──────────────────────────────────────────────────────────────────────
# VALIDAÇÃO
# ──────────────────────────────────────────────────────────────────────

def validar(html: str, nome: str) -> list:
    """Confere se o arquivo cumpre o contrato do site. Devolve lista de erros."""
    problemas = []

    if 'id="jc-header"' not in html:
        problemas.append('falta a div <div id="jc-header">')
    if '/_shared/site-header.js' not in html:
        problemas.append("falta o <script src='/_shared/site-header.js'>")
    if 'data-title="Academy"' not in html:
        problemas.append('o jc-header nao esta com data-title="Academy"')
    if "DM+Sans" not in html or "IBM+Plex+Mono" not in html:
        problemas.append("faltam as fontes DM Sans / IBM Plex Mono")
    if "--ink:#08213E" not in html:
        problemas.append("a paleta :root do site nao esta presente")

    # cobertura de traducao
    chaves = set(re.findall(r'data-i18n="([^"]+)"', html))
    i_es = html.find("es:{")
    i_pt = html.find("pt:{")
    if i_es == -1 or i_pt == -1:
        problemas.append("nao encontrei os dicionarios es:{ } / pt:{ }")
        return problemas

    fim_pt = html.find("/* ", i_pt)
    if fim_pt == -1:
        fim_pt = len(html)
    bloco_es = html[i_es:i_pt]
    bloco_pt = html[i_pt:fim_pt]

    faltam_es = sorted(k for k in chaves if f'"{k}":' not in bloco_es)
    faltam_pt = sorted(k for k in chaves if f'"{k}":' not in bloco_pt)

    if faltam_es:
        problemas.append(f"{len(faltam_es)} chave(s) sem traducao ES: {', '.join(faltam_es[:6])}")
    if faltam_pt:
        problemas.append(f"{len(faltam_pt)} chave(s) sem traducao PT: {', '.join(faltam_pt[:6])}")

    if not problemas:
        info(f"{nome}: {len(chaves)} chaves i18n, EN/ES/PT completos")

    return problemas


# ──────────────────────────────────────────────────────────────────────
# PÁGINA ÍNDICE DO JOURNAL
# ──────────────────────────────────────────────────────────────────────

def montar_indice() -> str:
    cards, t_es, t_pt = [], [], []

    for c in CAPITULOS:
        n = c["num"]
        cards.append(f'''
   <a class="ch" href="./{c["slug"]}/">
    <div class="chn">{n}</div>
    <div class="chb">
     <h3 data-i18n="c{n}.t">{c["en"][0]}</h3>
     <p data-i18n="c{n}.d">{c["en"][1]}</p>
    </div>
    <div class="cha">&rarr;</div>
   </a>''')
        t_es.append(f'"c{n}.t":{json_str(c["es"][0])},"c{n}.d":{json_str(c["es"][1])}')
        t_pt.append(f'"c{n}.t":{json_str(c["pt"][0])},"c{n}.d":{json_str(c["pt"][1])}')

    return INDEX_TPL.replace("{{CARDS}}", "".join(cards)) \
                    .replace("{{ES}}", ",\n".join(t_es)) \
                    .replace("{{PT}}", ",\n".join(t_pt))


def json_str(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


INDEX_TPL = r'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Trading Network Journal | Josimar Caitano</title>
<meta name="description" content="A documented descent from market mechanism to physical infrastructure, one layer per entry, each closing with an interactive lab.">
<meta property="og:title" content="Trading Network Journal">
<meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>
:root{--ink:#08213E;--tx:#2A3B52;--tx2:#4A5E78;--cy:#00BCEB;--cy2:#0093B8;--bl:#0B5CD5;
 --t1:#F4F9FD;--t2:#E5F1FA;--ln:#DCE7F1;--ln2:#BFD5E8;--mu:#63768E;--mu2:#93A6BB;
 --s2:0 1px 2px rgba(8,33,62,.05),0 16px 40px -26px rgba(8,33,62,.4);--mw:1220px}
*{box-sizing:border-box}
body{margin:0;background:#fff;color:var(--tx);font-family:"DM Sans",system-ui,sans-serif;
 font-size:18px;line-height:1.68;-webkit-font-smoothing:antialiased}
h1,h2,h3{color:var(--ink);letter-spacing:-.02em;font-weight:700;margin:0}
a{color:var(--bl)}
.hero{background:radial-gradient(85% 105% at 90% -12%,#D9EEFA 0%,rgba(255,255,255,0) 60%),linear-gradient(180deg,#FAFDFF,#fff);border-bottom:1px solid var(--ln)}
.hero .r{max-width:var(--mw);margin:0 auto;padding:62px 24px 48px}
.eb{display:inline-flex;align-items:center;gap:10px;font-size:13.5px;font-weight:700;color:var(--bl);margin:0 0 18px}
.eb::before{content:"";width:28px;height:3px;border-radius:3px;background:var(--cy)}
.hero h1{font-size:clamp(32px,5vw,52px);line-height:1.05;max-width:18ch;margin:0 0 20px;letter-spacing:-.032em}
.hero .ld{font-size:clamp(17px,2vw,21px);color:var(--tx2);max-width:60ch;margin:0}
main{max-width:var(--mw);margin:0 auto;padding:44px 24px 20px}
.wrap{max-width:78ch;margin:0 auto}
.lead{font-size:18px;color:var(--tx2);margin:0 0 34px;max-width:64ch}
.ch{display:flex;align-items:center;gap:20px;border:1px solid var(--ln);border-radius:16px;
 padding:20px 24px;margin-bottom:14px;text-decoration:none;background:#fff;transition:.16s;box-shadow:var(--s2)}
.ch:hover{border-color:var(--cy);transform:translateY(-1px)}
.chn{font-family:"IBM Plex Mono",monospace;font-size:26px;font-weight:600;color:var(--cy2);flex:none;width:44px}
.chb{flex:1;min-width:0}
.chb h3{font-size:19px;margin:0 0 5px}
.chb p{margin:0;font-size:15px;color:var(--tx2)}
.cha{font-size:20px;color:var(--mu2);flex:none}
.ch:hover .cha{color:var(--bl)}
.soon{display:flex;align-items:center;gap:20px;border:1px dashed var(--ln2);border-radius:16px;
 padding:20px 24px;margin-bottom:14px;background:var(--t1)}
.soon .chn{color:var(--mu2)}
.soon h3{font-size:19px;margin:0 0 5px;color:var(--mu)}
.soon p{margin:0;font-size:15px;color:var(--mu)}
.note{border-left:3px solid var(--cy);background:var(--t1);border-radius:0 14px 14px 0;padding:18px 22px;margin:34px 0 0}
.note .t{font-family:"IBM Plex Mono",monospace;font-size:11.5px;font-weight:700;color:var(--bl);margin:0 0 7px;letter-spacing:.04em}
.note p{margin:0;font-size:16.5px;color:var(--tx)}
footer{background:var(--ink);color:#BCD0E7;margin-top:60px}
footer .r{max-width:var(--mw);margin:0 auto;padding:50px 24px}
footer h3{color:#fff;font-size:23px;margin:0 0 10px}
footer .cr{font-size:14.5px;color:#92A9C9;line-height:2}
footer .cr b{color:#E4EEFA}
footer .lk{margin-top:18px;display:flex;gap:20px;flex-wrap:wrap}
footer .lk a{color:var(--cy);font-family:"IBM Plex Mono",monospace;font-size:13.5px;text-decoration:none}
footer .lk a:hover{text-decoration:underline}
footer .oep{margin-top:20px;font-size:14px;color:var(--cy);font-weight:700}
footer .mt{margin-top:22px;padding-top:18px;border-top:1px solid #1B3F6C;font-size:12.5px;color:#7590B4;line-height:1.75}
@media(max-width:720px){body{font-size:17px}.ch,.soon{gap:14px;padding:17px 18px}.chn{font-size:22px;width:36px}}
a:focus-visible{outline:2px solid var(--bl);outline-offset:2px;border-radius:6px}
</style>
</head>
<body data-lang="en">
<div id="jc-header"
     data-title="Academy"
     data-sub-en="— Trading Network Journal"
     data-sub-es="— Diario de Redes de Trading"
     data-sub-pt="— Diário de Redes de Trading"></div>
<script src="/_shared/site-header.js"></script>

<header class="hero"><div class="r">
 <p class="eb" data-i18n="h.k">Academy</p>
 <h1 data-i18n="h.t">Trading Network Journal</h1>
 <p class="ld" data-i18n="h.l">A documented descent from market mechanism to physical infrastructure. One layer per entry, each closing with a lab you are expected to solve before moving on.</p>
</div></header>

<main><div class="wrap">
 <p class="lead" data-i18n="m.l">I write this for the engineer I was five years ago — the one who could move a packet faster than almost anyone and could not say what the packet was carrying. Every entry descends one layer, and every technical decision traces back to a market rule established earlier.</p>
{{CARDS}}

 <div class="soon">
  <div class="chn">04</div>
  <div>
   <h3 data-i18n="c04.t">From Wire to Application</h3>
   <p data-i18n="c04.d">NIC, PCIe, kernel, socket, interrupt versus polling, CPU and cache.</p>
  </div>
 </div>

 <div class="note">
  <p class="t" data-i18n="n.t">HOW TO READ THIS</p>
  <p data-i18n="n.b">In order. Each entry assumes the one before it, and the labs get harder because the reasoning compounds. If you skip the lab, you have read the chapter — you have not learned it.</p>
 </div>
</div></main>

<footer><div class="r">
 <h3>Josimar Caitano</h3>
 <p class="cr"><b>Josimar Caitano</b> — Principal Solutions Architect | Capital Markets<br>
  <span data-i18n="ft.1">Cisco Networking Academy instructor since 2006</span><br>
  <span data-i18n="ft.2">High-performance network engineering for capital markets</span></p>
 <div class="lk">
  <a href="https://www.linkedin.com/in/josimar-caitano/" target="_blank" rel="noopener noreferrer">LinkedIn &#8599;</a>
  <a href="https://www.youtube.com/@Josinfo" target="_blank" rel="noopener noreferrer">YouTube &#8599;</a>
  <a href="mailto:josimaru@gmail.com">josimaru@gmail.com</a>
 </div>
 <p class="oep">O.E.P. — <span data-i18n="ft.oep">Order · Strategy · Patience</span></p>
 <p class="mt" data-i18n="ft.legal">Academy · Trading Network Journal · v1.0 — Original didactic material. Figures and logs are illustrative, intended to teach architectural reasoning. They are not investment advice nor a project specification. MIT licence.</p>
</div></footer>

<script>
var T={
es:{
"h.k":"Academia","h.t":"Diario de Redes de Trading",
"h.l":"Un descenso documentado desde el mecanismo de mercado hasta la infraestructura física. Una capa por entrada, cada una cerrando con un laboratorio que se espera que resuelva antes de avanzar.",
"m.l":"Escribo esto para el ingeniero que yo era hace cinco años — el que movía un paquete más rápido que casi cualquiera y no sabía decir qué transportaba ese paquete. Cada entrada desciende una capa, y cada decisión técnica remite a una regla de mercado establecida antes.",
{{ES}},
"c04.t":"Del Cable a la Aplicación","c04.d":"NIC, PCIe, kernel, socket, interrupción versus polling, CPU y caché.",
"n.t":"CÓMO LEER ESTO",
"n.b":"En orden. Cada entrada asume la anterior, y los laboratorios se vuelven más difíciles porque el razonamiento se acumula. Si salta el laboratorio, leyó el capítulo — no lo aprendió.",
"ft.1":"Instructor Cisco Networking Academy desde 2006",
"ft.2":"Ingeniería de redes de alto rendimiento para mercados de capitales",
"ft.oep":"Orden · Estrategia · Paciencia",
"ft.legal":"Academia · Diario de Redes de Trading · v1.0 — Material didáctico original. Las cifras y logs son ilustrativos, destinados a enseñar el razonamiento de arquitectura. No constituyen recomendación de inversión ni especificación de proyecto. Licencia MIT."
},
pt:{
"h.k":"Academia","h.t":"Diário de Redes de Trading",
"h.l":"Uma descida documentada do mecanismo de mercado até a infraestrutura física. Uma camada por entrada, cada uma fechando com um laboratório que você deve resolver antes de seguir.",
"m.l":"Escrevo isto para o engenheiro que eu era cinco anos atrás — aquele que movia um pacote mais rápido que quase todo mundo e não sabia dizer o que aquele pacote carregava. Cada entrada desce uma camada, e toda decisão técnica remete a uma regra de mercado estabelecida antes.",
{{PT}},
"c04.t":"Do Fio à Aplicação","c04.d":"NIC, PCIe, kernel, socket, interrupção versus polling, CPU e cache.",
"n.t":"COMO LER ISTO",
"n.b":"Em ordem. Cada entrada assume a anterior, e os laboratórios ficam mais difíceis porque o raciocínio se acumula. Se pular o laboratório, você leu o capítulo — não aprendeu.",
"ft.1":"Instrutor Cisco Networking Academy desde 2006",
"ft.2":"Engenharia de redes de alta performance para mercado de capitais",
"ft.oep":"Ordem · Estratégia · Paciência",
"ft.legal":"Academia · Diário de Redes de Trading · v1.0 — Material didático original. Números e logs são ilustrativos, destinados ao ensino do raciocínio de arquitetura. Não constituem recomendação de investimento nem especificação de projeto. Licença MIT."
}};
(function(){
"use strict";
var origs=null;
function applyLang(lang){
  document.body.dataset.lang=lang;
  document.documentElement.lang=lang==="pt"?"pt-BR":lang;
  var nodes=document.querySelectorAll("[data-i18n]");
  if(!origs){origs=new Map();nodes.forEach(function(n){origs.set(n,n.innerHTML);});}
  nodes.forEach(function(n){
    var k=n.getAttribute("data-i18n");
    if(lang==="en"){n.innerHTML=origs.get(n);return;}
    var v=T[lang]&&T[lang][k];
    if(v==null)return;
    n.innerHTML=v;
  });
}
window.addEventListener("jc:lang",function(e){applyLang(e.detail.lang);});
setTimeout(function(){applyLang((window.jcHeader&&window.jcHeader.lang)||"en");},0);
})();
</script>
</body>
</html>
'''


# ──────────────────────────────────────────────────────────────────────
# GIT
# ──────────────────────────────────────────────────────────────────────

def git(raiz: Path, *args, check=True):
    return subprocess.run(["git", *args], cwd=str(raiz), check=check,
                          capture_output=True, text=True, encoding="utf-8", errors="replace")


# ──────────────────────────────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser(description="Publica o Trading Network Journal")
    ap.add_argument("--commit", action="store_true", help="git add + git commit")
    ap.add_argument("--push", action="store_true", help="commit e git push")
    ap.add_argument("--dry-run", action="store_true", help="so valida, nao escreve")
    ap.add_argument("--no-index", action="store_true", help="nao gera a pagina indice")
    a = ap.parse_args()

    raiz = Path(__file__).resolve().parent
    if not (raiz / "public").is_dir():
        raiz = Path.cwd()

    print(f"\n{C.B}TRADING NETWORK JOURNAL — deploy{C.END}")
    info(f"repo: {raiz}")

    if not (raiz / "public").is_dir():
        err("nao achei a pasta public/ — rode a partir da raiz do repositorio")
        return 1

    # ── 1. validar ────────────────────────────────────────────────────
    head("1. VALIDANDO OS CAPITULOS")
    conteudo = {}
    falhou = False

    for c in CAPITULOS:
        origem = raiz / c["src"]
        if not origem.is_file():
            err(f'{c["src"]} nao encontrado na raiz do repositorio')
            falhou = True
            continue
        html = origem.read_text(encoding="utf-8")
        problemas = validar(html, c["src"])
        if problemas:
            err(c["src"])
            for p in problemas:
                print(f"         - {p}")
            falhou = True
        else:
            ok(f'{c["src"]}  ({len(html):,} bytes)')
            conteudo[c["slug"]] = html

    if falhou:
        print(f"\n{C.ERR}Deploy abortado. Corrija os itens acima.{C.END}\n")
        return 1

    # ── 2. gravar ─────────────────────────────────────────────────────
    head("2. GRAVANDO EM public/")
    escritos = []

    for c in CAPITULOS:
        destino = raiz / BASE / c["slug"] / "index.html"
        rel = destino.relative_to(raiz).as_posix()
        novo = conteudo[c["slug"]]

        if destino.is_file() and destino.read_text(encoding="utf-8") == novo:
            info(f"{rel}  (sem alteracao)")
            continue

        if a.dry_run:
            warn(f"{rel}  (dry-run, nao gravado)")
            continue

        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text(novo, encoding="utf-8", newline="\n")
        ok(rel)
        escritos.append(rel)

    if not a.no_index:
        idx = raiz / BASE / "index.html"
        rel = idx.relative_to(raiz).as_posix()
        novo = montar_indice()
        if idx.is_file() and idx.read_text(encoding="utf-8") == novo:
            info(f"{rel}  (sem alteracao)")
        elif a.dry_run:
            warn(f"{rel}  (dry-run, nao gravado)")
        else:
            idx.parent.mkdir(parents=True, exist_ok=True)
            idx.write_text(novo, encoding="utf-8", newline="\n")
            ok(rel)
            escritos.append(rel)

    # ── 3. urls ───────────────────────────────────────────────────────
    head("3. URLS APOS O DEPLOY")
    if not a.no_index:
        print(f"  https://caitano1985.github.io/academy/trading-network-journal/")
    for c in CAPITULOS:
        print(f'  https://caitano1985.github.io/academy/trading-network-journal/{c["slug"]}/')

    if a.dry_run:
        print(f"\n{C.WARN}dry-run: nada foi gravado.{C.END}\n")
        return 0

    # ── 4. git ────────────────────────────────────────────────────────
    head("4. GIT")
    try:
        st = git(raiz, "status", "--porcelain", BASE)
        pend = [l for l in st.stdout.splitlines() if l.strip()]
        if not pend:
            info("nada pendente em public/academy/ — arvore ja esta em dia")
        else:
            for l in pend:
                print(f"  {C.DIM}{l}{C.END}")

        if a.commit or a.push:
            if not pend:
                info("nada para commitar")
            else:
                git(raiz, "add", BASE)
                git(raiz, "commit", "-m", COMMIT_MSG)
                ok("commit criado")
            if a.push:
                br = git(raiz, "rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
                r = git(raiz, "push", "origin", br, check=False)
                if r.returncode == 0:
                    ok(f"push para origin/{br}")
                    info("o GitHub Actions vai buildar; aguarde 1-2 min")
                else:
                    err("push falhou")
                    print(r.stderr.strip())
                    return 1
        else:
            print(f"\n  {C.DIM}para publicar:{C.END}  python deploy_journal.py --push")

    except FileNotFoundError:
        warn("git nao encontrado no PATH — arquivos gravados, commit manual")
    except subprocess.CalledProcessError as e:
        err("comando git falhou")
        print((e.stderr or "").strip())
        return 1

    print(f"\n{C.OK}{C.B}Concluido.{C.END}  {len(escritos)} arquivo(s) gravado(s)\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
