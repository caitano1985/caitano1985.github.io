#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════════
  MASTER PATCH — Portfolio Josimar Caitano
  Todas as correções do dia em um único script.
  
  Executa: python3 master_patch.py
  Na RAIZ do projeto (onde tem src/ e public/)
  
  PRÉ-REQUISITO: i18n.tsx já substituído pelo novo (3 idiomas)
═══════════════════════════════════════════════════════════════
"""
import sys
from pathlib import Path

def p(file, old, new, label):
    c = file.read_text("utf-8")
    cn = c.replace("\r\n","\n"); on = old.replace("\r\n","\n"); nn = new.replace("\r\n","\n")
    if on not in cn:
        print(f"  ✗ {label}")
        return False
    cn = cn.replace(on, nn, 1)
    if "\r\n" in c: cn = cn.replace("\n","\r\n")
    file.write_text(cn,"utf-8")
    print(f"  ✓ {label}")
    return True

def pa(file, old, new, label):
    c = file.read_text("utf-8")
    cn = c.replace("\r\n","\n"); on = old.replace("\r\n","\n"); nn = new.replace("\r\n","\n")
    n = cn.count(on)
    if n == 0:
        print(f"  ✗ {label}")
        return False
    cn = cn.replace(on, nn)
    if "\r\n" in c: cn = cn.replace("\n","\r\n")
    file.write_text(cn,"utf-8")
    print(f"  ✓ {label} ({n}x)")
    return True

def rm(f, label):
    if f.exists(): f.unlink(); print(f"  🗑  {label}")
    else: print(f"  ·  {label} — já removido")

def inj(file, marker, content, label):
    c = file.read_text("utf-8")
    if content[:30] in c:
        print(f"  ✓ {label} — já presente")
        return True
    if marker not in c:
        print(f"  ✗ {label} — marker ausente")
        return False
    c = c.replace(marker, content + marker, 1)
    file.write_text(c,"utf-8")
    print(f"  ✓ {label}")
    return True

# ═══════════════════════════════════════════════════════════
SR_EN = ','.join([
'"sr.k":"Module 3.1 — the real cage"',
'"sr.h":"B3 Trading Rack: what the exchange demands and what elite does"',
'"sr.p":"B3 leaves no choice: the Trading Rack modality <strong>requires</strong> routed Layer 3 access, dual connections, and BGP with the exchange PEs. No cage without a router. The difference between a common operation and an elite one is not having or not having the CE — it is <strong>where it sits relative to the critical path</strong>."',
'"sr.lab":"B3 compliance × elite configuration"',
'"sr.left":"B3 COMPLIANT — CE IN THE FEED PATH"',
'"sr.right":"ELITE — CE OUT OF THE FEED PATH"',
'"sr.mdrt":"routed market data"',
'"sr.swconv":"Conventional L2/L3 switch"',
'"sr.lt":"TOTAL PATH COST"',
'"sr.lb":"the feed traverses L3 routing before reaching the strategy"',
'"sr.rb":"the CE still exists — it is just not in the market data path"',
'"sr.ctrl":"control plane"',
'"sr.fan":"electrical fanout 1:N"',
'"sr.split":"planes separated"',
'"sr.leak":"leak A15"',
'"sr.mdl1":"market data direct on L1"',
'"sr.ordtx":"TCP orders"',
'"sr.cap":"Trading Rack requirements and how the elite architecture meets them without paying latency"',
'"sr.c1":"B3 requirement"','"sr.c2":"Common implementation"','"sr.c3":"Elite implementation"',
'"sr.r1a":"Routed Layer 3 access"','"sr.r1b":"CE in the feed and order path"','"sr.r1c":"CE only in control plane; data via L1"',
'"sr.r2a":"Dual connections"','"sr.r2b":"FHRP with convergence in seconds"','"sr.r2c":"FHRP + BFD 100 ms × 3 · sub-second"',
'"sr.r3a":"Optimized eBGP routing"','"sr.r3b":"Default timers, no BFD"','"sr.r3c":"Timers 7/21 + BFD + prefix filters"',
'"sr.r4a":"UMDF multicast via PIM sparse"','"sr.r4b":"Join on CE, software replication"','"sr.r4c":"Join on CE, electrical replication on L1"',
'"sr.r5a":"Redundant feeds A and B"','"sr.r5b":"Feed arbitrage in application"','"sr.r5c":"A/B arbitrage in FPGA on the NIC"',
'"sr.eng":"The common misreading of the B3 manual is concluding that because the modality requires Layer 3, the router must sit in the market data path. It does not. The CE exists to establish the eBGP session, announce the Trading Rack block, maintain PIM adjacency, and join the UMDF groups. Once the multicast tree is formed, the traffic can be delivered to the Fusion and electrically replicated to servers without going back through routing processing. The CE stays in the control plane; data runs on Layer 1. This separation is the difference between 156 µs and 294 ns."',
'"sr.board":"Two institutions can be equally compliant with the same exchange manual and operate at latency regimes separated by three orders of magnitude. Regulatory compliance and competitive advantage are independent axes — meeting the requirement is the floor, not the strategy. What separates the two is an architecture decision that costs no additional license or contract: it costs knowing where to place each box."',
])

SR_ES = ','.join([
'"sr.k":"Módulo 3.1 — la jaula real"',
'"sr.h":"Rack Negociación B3: lo que la bolsa exige y lo que la élite hace"',
'"sr.p":"B3 no deja elegir: la modalidad Rack Negociación <strong>obliga</strong> acceso en Capa 3 ruteado, conexiones dualizadas y BGP con los PEs de la bolsa. No existe jaula sin router. La diferencia entre una operación común y una de élite no es tener o no tener el CE — es <strong>dónde queda en relación al camino crítico</strong>."',
'"sr.lab":"Conformidad B3 × configuración de élite"',
'"sr.left":"CONFORME A B3 — CE EN EL CAMINO DEL FEED"',
'"sr.right":"ÉLITE — CE FUERA DEL CAMINO DEL FEED"',
'"sr.mdrt":"market data ruteado"',
'"sr.swconv":"Switch L2/L3 convencional"',
'"sr.lt":"COSTO TOTAL DEL CAMINO"',
'"sr.lb":"el feed atraviesa ruteo L3 antes de llegar a la estrategia"',
'"sr.rb":"el CE sigue existiendo — simplemente no está en el camino del market data"',
'"sr.ctrl":"plano de control"',
'"sr.fan":"fanout eléctrico 1:N"',
'"sr.split":"planos separados"',
'"sr.leak":"leak A15"',
'"sr.mdl1":"market data directo en L1"',
'"sr.ordtx":"órdenes TCP"',
'"sr.cap":"Exigencias del Rack Negociación y cómo la arquitectura de élite las cumple sin pagar latencia"',
'"sr.c1":"Exigencia de B3"','"sr.c2":"Implementación común"','"sr.c3":"Implementación de élite"',
'"sr.r1a":"Acceso en Capa 3 ruteado"','"sr.r1b":"CE en el camino del feed y de las órdenes"','"sr.r1c":"CE solo en plano de control; datos vía L1"',
'"sr.r2a":"Conexiones dualizadas"','"sr.r2b":"FHRP con convergencia en segundos"','"sr.r2c":"FHRP + BFD 100 ms × 3 · sub-segundo"',
'"sr.r3a":"Ruteo eBGP optimizado"','"sr.r3b":"Timers por defecto, sin BFD"','"sr.r3c":"Timers 7/21 + BFD + filtros de prefijo"',
'"sr.r4a":"Multicast UMDF vía PIM sparse"','"sr.r4b":"Join en CE, replicación en software"','"sr.r4c":"Join en CE, replicación eléctrica en L1"',
'"sr.r5a":"Feeds A y B redundantes"','"sr.r5b":"Arbitraje de feed en aplicación"','"sr.r5c":"Arbitraje A/B en FPGA en la NIC"',
'"sr.eng":"La lectura errónea del manual de B3 es concluir que, porque la modalidad exige Capa 3, el router debe estar en el camino del market data. No es así. El CE existe para establecer la sesión eBGP, anunciar el bloque del Rack Negociación, mantener la adyacencia PIM y hacer el join de los grupos UMDF. Una vez formado el árbol multicast, el tráfico puede entregarse al Fusion y replicarse eléctricamente a los servidores sin volver a atravesar procesamiento de ruteo. El CE queda en el plano de control; el dato corre en Capa 1. Esta separación es la diferencia entre 156 µs y 294 ns."',
'"sr.board":"Dos instituciones pueden estar igualmente conformes al mismo manual de la bolsa y operar en regímenes de latencia separados por tres órdenes de magnitud. Conformidad regulatoria y ventaja competitiva son ejes independientes — cumplir el requisito es el piso, no la estrategia. Lo que separa a las dos es una decisión de arquitectura que no cuesta más licencia ni más contrato: cuesta saber dónde colocar cada caja."',
])

NAV_CSS = '''
.main-nav{position:sticky;top:0;z-index:999;background:rgba(255,255,255,.92);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border-bottom:1px solid var(--ln);font-family:"DM Sans",system-ui,sans-serif}
.main-nav-inner{max-width:var(--mw);margin:0 auto;display:flex;align-items:center;gap:1.5rem;padding:.65rem 1.5rem}
.main-nav-brand{display:flex;align-items:baseline;gap:.5rem;text-decoration:none;flex-shrink:0}
.main-nav-name{font-family:"IBM Plex Mono",monospace;font-weight:700;font-size:.9rem;color:var(--bl)}
.main-nav-alias{font-size:.75rem;color:var(--mu2)}
.main-nav-links{display:flex;align-items:center;gap:1.25rem;flex:1}
.main-nav-links a{font-size:.82rem;color:var(--tx2);text-decoration:none;transition:color .15s;white-space:nowrap}
.main-nav-links a:hover{color:var(--bl)}
.main-nav-home{font-family:"IBM Plex Mono",monospace;font-size:.8rem;color:var(--bl);text-decoration:none;white-space:nowrap}
.main-nav-home:hover{text-decoration:underline}
@media(max-width:900px){.main-nav-links{display:none}.main-nav-home{margin-left:auto}}
.tb{top:45px !important}
'''

NAV_HTML = '''<nav class="main-nav"><div class="main-nav-inner">
<a href="/" class="main-nav-brand"><span class="main-nav-name">Josimar Caitano</span><span class="main-nav-alias">じょしまる</span></a>
<div class="main-nav-links"><a href="/#about">About</a><a href="/#experiencia">Experience</a><a href="/#certificacoes">Certifications</a><a href="/#ensino">Teaching</a><a href="/#academia">Academy</a><a href="/#projetos">Projects</a><a href="/#conteudo">Content</a><a href="/#contato">Contact</a></div>
<a href="/" class="main-nav-home">← Home</a>
</div></nav>
'''


def main():
    B = Path(".")
    hdr   = B/"src"/"components"/"SiteHeader.tsx"
    ftr   = B/"src"/"components"/"SiteFooter.tsx"
    card  = B/"src"/"components"/"ProjectCard.tsx"
    idx   = B/"src"/"routes"/"index.tsx"
    pidx  = B/"src"/"routes"/"projetos.index.tsx"
    pts   = B/"src"/"data"/"projects.ts"
    root  = B/"src"/"routes"/"__root.tsx"
    styles= B/"src"/"styles.css"
    ull_rt= B/"src"/"routes"/"projetos.ull-arena.tsx"
    H     = B/"public"/"ull-arena"/"index.html"

    for f in [hdr,ftr,card,idx,pidx,pts,root,styles]:
        if not f.exists():
            print(f"ERRO: {f} não encontrado."); sys.exit(1)

    # ═══════════════════════ SITE HEADER ═══════════════════════
    print(f"\n{'═'*55}\n  SiteHeader.tsx\n{'═'*55}")
    p(hdr, '["about", "nav.about"],\n  ["experiencia", "nav.experience"],\n  ["certificacoes", "nav.certs"],\n  ["ensino", "nav.teaching"],\n  ["projetos", "nav.projects"],',
           '["about", "nav.about"],\n  ["experiencia", "nav.experience"],\n  ["certificacoes", "nav.certs"],\n  ["ensino", "nav.teaching"],\n  ["academia", "nav.academic"],\n  ["projetos", "nav.projects"],',
           "Nav — academia")
    p(hdr, '          <div className="flex overflow-hidden rounded-md border border-border font-mono text-xs">\n            {(["pt", "en"] as const).map((l) => (\n              <button\n                key={l}\n                onClick={() => setLang(l)}\n                aria-label={l === "pt" ? "Português (pt-BR)" : "English (en-US)"}\n                className={`px-2 py-1 transition-colors ${\n                  lang === l\n                    ? "bg-primary text-primary-foreground"\n                    : "text-muted-foreground hover:text-primary"\n                }`}\n              >\n                {l === "pt" ? "PT-BR" : "EN-US"}\n              </button>\n            ))}\n          </div>',
           '          <div className="flex overflow-hidden rounded-md border border-border text-sm">\n            {([\n              { code: "en" as const, flag: "🇺🇸", label: "English (US)" },\n              { code: "es" as const, flag: "🇪🇸", label: "Español (ES)" },\n              { code: "pt" as const, flag: "🇧🇷", label: "Português (BR)" },\n            ]).map(({ code, flag, label }) => (\n              <button\n                key={code}\n                onClick={() => setLang(code)}\n                aria-label={label}\n                className={`px-2 py-1 transition-colors ${\n                  lang === code\n                    ? "bg-primary text-primary-foreground"\n                    : "text-muted-foreground hover:text-primary"\n                }`}\n              >\n                {flag}\n              </button>\n            ))}\n          </div>',
           "Bandeiras 🇺🇸🇪🇸🇧🇷")
    p(hdr, '<span className="font-mono text-base font-bold text-primary">josinfo</span>\n          <span className="hidden text-xs text-muted-foreground sm:inline">Josimar Caitano</span>',
           '<span className="font-mono text-base font-bold text-primary">Josimar Caitano</span>\n          <span className="hidden text-xs text-muted-foreground sm:inline">じょしまる</span>',
           "josinfo → Josimar Caitano")

    # ═══════════════════════ SITE FOOTER ═══════════════════════
    print(f"\n{'═'*55}\n  SiteFooter.tsx\n{'═'*55}")
    p(ftr, 'josinfo // Josimar Caitano — CCIE x2', 'Josimar Caitano // じょしまる', "Footer limpo")

    # ═══════════════════════ INDEX.TSX ═══════════════════════
    print(f"\n{'═'*55}\n  index.tsx\n{'═'*55}")
    p(idx, '{ title: "Josimar Caitano (JOSIMARU) — CCIE x2 | Arquiteto de Redes" }',
           '{ title: "Josimar Caitano — Principal Solutions Architect | Capital Markets & Enterprise Infrastructure" }', "Meta title")
    p(idx, 'content:\n          "Portfólio de Josimar Caitano (Josinfo): CCIE x2, Principal IP Solutions Architect for Financial Services, instrutor de CCNA DevNet, CCNP Encor e labs CCIE.",',
           'content:\n          "Mission-critical network architect specializing in ultra-low latency (ULL/HFT) trading infrastructure, multi-cloud connectivity, and enterprise security governance for capital markets.",', "Meta desc")
    p(idx, '{ property: "og:title", content: "Josimar Caitano (Josinfo) — CCIE x2 | Arquiteto de Redes" }',
           '{ property: "og:title", content: "Josimar Caitano — Principal Solutions Architect | Capital Markets" }', "OG title")
    p(idx, 'content:\n          "Especialista sênior em redes: roteamento avançado, segurança, NOC e arquitetura IP para o setor financeiro.",',
           'content:\n          "Architecting ultra-low latency infrastructure for the world\'s fastest financial markets. Enterprise networking, cybersecurity, and technical leadership.",', "OG desc")
    p(idx, '              Josimar Caitano\n              <span className="block font-mono text-xl text-primary sm:text-2xl">// josinfo</span>',
           '              {t("hero.name")}\n              <span className="block font-mono text-xl text-primary sm:text-2xl">{t("hero.alias")}</span>', "Hero name")
    p(idx, '              <a href="#contato" className="hover:text-primary">\n                linkedin/[placeholder]\n              </a>\n              <a href="#contato" className="hover:text-primary">\n                youtube/[placeholder]\n              </a>',
           '              <a href="https://www.linkedin.com/in/josimar-caitano/" target="_blank" rel="noopener noreferrer" className="hover:text-primary">\n                linkedin/josimar-caitano\n              </a>\n              <a href="https://www.youtube.com/@Josinfo" target="_blank" rel="noopener noreferrer" className="hover:text-primary">\n                youtube/@Josinfo\n              </a>', "Hero social links")
    p(idx, '            <figcaption className="mt-2 text-center font-mono text-[11px] text-muted-foreground">\n              {t("hero.photoNote")}\n            </figcaption>',
           '            {/* photo caption removed */}', "PhotoNote removido")
    p(idx, '    { role: "exp.role3", company: "exp.company3", period: "exp.period3", desc: "exp.desc3", current: false },\n  ];',
           '    { role: "exp.role3", company: "exp.company3", period: "exp.period3", desc: "exp.desc3", current: false },\n    { role: "exp.role4", company: "exp.company4", period: "exp.period4", desc: "exp.desc4", current: false },\n  ];', "4 experiências")
    p(idx, '      <section id="certificacoes" className="mx-auto max-w-6xl px-5 py-20">\n        <SectionHead label="./certifications" title={t("certs.title")} />\n        <div className="grid gap-5 md:grid-cols-3">\n          <div className="glow-ring rounded-xl border border-primary/40 bg-card p-6">\n            <p className="font-mono text-4xl font-bold text-primary">{t("certs.ccie")}</p>\n            <p className="mt-3 text-sm text-muted-foreground">{t("certs.ccieDesc")}</p>\n          </div>\n          {[0, 1].map((i) => (\n            <div\n              key={i}\n              className="rounded-xl border border-dashed border-border bg-card/50 p-6"\n            >\n              <p className="font-mono text-sm text-muted-foreground">{t("certs.other")}</p>\n              <p className="mt-3 text-sm text-muted-foreground">{t("certs.otherDesc")}</p>\n            </div>\n          ))}\n        </div>\n      </section>',
           '      <section id="certificacoes" className="mx-auto max-w-6xl px-5 py-20">\n        <SectionHead label="./certifications" title={t("certs.title")} />\n        <div className="grid gap-5 md:grid-cols-3">\n          {(["c1", "c2", "c3"] as const).map((key, i) => (\n            <div key={key} className={`rounded-xl border bg-card p-6 ${i === 0 ? "glow-ring border-primary/40" : "border-border"}`}>\n              <p className={`font-mono text-sm font-semibold ${i === 0 ? "text-primary" : "text-muted-foreground"}`}>{t(`certs.${key}`)}</p>\n              <p className="mt-3 text-sm text-muted-foreground">{t(`certs.${key}d`)}</p>\n            </div>\n          ))}\n        </div>\n      </section>', "Certs — formação real")
    p(idx, '      {/* PROJECTS */}\n      <section id="projetos"',
           '      {/* ACADEMY */}\n      <section id="academia" className="mx-auto max-w-6xl px-5 py-20">\n        <SectionHead label="./academy" title={t("academic.title")} />\n        <p className="-mt-4 mb-8 text-muted-foreground">{t("academic.subtitle")}</p>\n        <div className="rounded-xl border border-dashed border-border bg-card/50 p-8 text-center">\n          <p className="font-mono text-sm text-muted-foreground">{t("academic.coming")}</p>\n        </div>\n      </section>\n\n      {/* PROJECTS */}\n      <section id="projetos"', "Seção Academy")
    p(idx, '  const contents: [string, string, string][] = [\n    ["content.a1", "content.a1d", "artigo"],\n    ["content.a2", "content.a2d", "artigo"],\n    ["content.v1", "content.v1d", "vídeo"],\n    ["content.v2", "content.v2d", "vídeo"],\n  ];',
           '  const contents: [string, string, string, string][] = [\n    ["content.yt", "content.ytd", "youtube", "content.ytLink"],\n    ["content.a1", "content.a1d", "article", ""],\n  ];', "Content array")
    p(idx, '            {contents.map(([title, desc, kind]) => (\n              <div key={title} className="card-hover rounded-xl border border-border bg-card p-6">\n                <span className="font-mono text-[11px] uppercase tracking-widest text-neon">\n                  {kind}\n                </span>\n                <h3 className="mt-2 font-semibold">{t(title)}</h3>\n                <p className="mt-2 text-sm leading-relaxed text-muted-foreground">{t(desc)}</p>\n                <span className="mt-4 inline-block font-mono text-xs text-muted-foreground">\n                  {t("content.link")}\n                </span>\n              </div>\n            ))}',
           '            {contents.map(([title, desc, kind, link]) => (\n              <div key={title} className="card-hover rounded-xl border border-border bg-card p-6">\n                <span className="font-mono text-[11px] uppercase tracking-widest text-neon">{kind}</span>\n                <h3 className="mt-2 font-semibold">{t(title)}</h3>\n                <p className="mt-2 text-sm leading-relaxed text-muted-foreground">{t(desc)}</p>\n                {link ? (\n                  <a href={t(link)} target="_blank" rel="noopener noreferrer" className="mt-4 inline-block font-mono text-xs text-primary hover:underline">{t("content.link")} →</a>\n                ) : (\n                  <span className="mt-4 inline-block font-mono text-xs text-muted-foreground">{t("content.linkSoon")}</span>\n                )}\n              </div>\n            ))}', "Content render")
    p(idx, '                <span className="text-primary">[placeholder]@exemplo.com</span>',
           '                <a href="mailto:josimaru@gmail.com" className="text-primary hover:underline">josimaru@gmail.com</a>', "Email real")
    p(idx, '                <span className="text-primary">/in/[placeholder]</span>',
           '                <a href="https://www.linkedin.com/in/josimar-caitano/" target="_blank" rel="noopener noreferrer" className="text-primary hover:underline">/in/josimar-caitano</a>', "LinkedIn real")
    p(idx, '                <span className="text-primary">/@[placeholder]</span>',
           '                <a href="https://www.youtube.com/@Josinfo" target="_blank" rel="noopener noreferrer" className="text-primary hover:underline">/@Josinfo</a>', "YouTube real")
    # Formspree
    p(idx, '  const [sent, setSent] = useState(false);',
           '  const [sent, setSent] = useState(false);\n  const [sending, setSending] = useState(false);', "State sending")
    p(idx, '  const onSubmit = (e: FormEvent) => {\n    e.preventDefault();\n    setSent(true);\n  };',
           '  const onSubmit = async (e: FormEvent) => {\n    e.preventDefault();\n    setSending(true);\n    try {\n      const form = e.target as HTMLFormElement;\n      const data = new FormData(form);\n      const res = await fetch("https://formspree.io/f/xeogrgvp", {\n        method: "POST", body: data, headers: { Accept: "application/json" },\n      });\n      if (res.ok) { setSent(true); form.reset(); }\n    } catch { /* silent */ } finally { setSending(false); }\n  };', "Formspree")
    p(idx, '              id="nome"\n              required', '              id="nome"\n              name="name"\n              required', "Input name attr")
    p(idx, '              id="email"\n              type="email"\n              required', '              id="email"\n              name="email"\n              type="email"\n              required', "Input email attr")
    p(idx, '              id="mensagem"\n              rows={4}\n              required', '              id="mensagem"\n              name="message"\n              rows={4}\n              required', "Textarea name attr")
    p(idx, '            <button\n              type="submit"\n              className="mt-5 w-full rounded-md bg-primary px-4 py-2.5 text-sm font-semibold text-primary-foreground transition-opacity hover:opacity-90"\n            >\n              {t("contact.send")}\n            </button>',
           '            <button\n              type="submit"\n              disabled={sending || sent}\n              className="mt-5 w-full rounded-md bg-primary px-4 py-2.5 text-sm font-semibold text-primary-foreground transition-opacity hover:opacity-90 disabled:opacity-60"\n            >\n              {sending ? "Sending..." : sent ? "✓ Sent" : t("contact.send")}\n            </button>', "Botão sending/sent")
    p(idx, 'text-neon">{t("contact.sent")}', 'text-primary">{t("contact.sent")}', "Cor sucesso")
    p(idx, '"radial-gradient(70% 60% at 20% 0%, color-mix(in oklab, var(--primary) 16%, transparent), transparent 70%)"',
           '"radial-gradient(70% 60% at 20% 0%, color-mix(in oklab, var(--primary) 8%, transparent), transparent 70%)"', "Hero gradient light")
    p(idx, '<span className="h-1.5 w-1.5 animate-pulse rounded-full bg-neon" />',
           '<span className="h-1.5 w-1.5 animate-pulse rounded-full bg-primary" />', "Badge neon→primary")

    # ═══════════════════════ PROJETOS.INDEX ═══════════════════════
    print(f"\n{'═'*55}\n  projetos.index.tsx\n{'═'*55}")
    p(pidx, '{ title: "Projetos de Rede | Josimar Caitano — Josinfo" }',
            '{ title: "Projects | Josimar Caitano — Principal Solutions Architect" }', "Meta title")
    p(pidx, '{ property: "og:title", content: "Projetos de Rede | Josinfo" }',
            '{ property: "og:title", content: "Projects | Josimar Caitano" }', "OG title")

    # ═══════════════════════ PROJECTS.TS ═══════════════════════
    print(f"\n{'═'*55}\n  projects.ts\n{'═'*55}")
    p(pts, '  href?: string;\n  externalLink?: boolean;\n', '', "href/ext — check se já existe")  # skip if already done by v2
    # Add href + externalLink if not present
    c = pts.read_text("utf-8")
    if "href?" not in c:
        p(pts, '  diagramNote: LocalizedText;\n};', '  diagramNote: LocalizedText;\n  href?: string;\n  externalLink?: boolean;\n};', "Type — href + externalLink")
    p(pts, '    title: { pt: "ULL Arena - HFT & Exchange Connectivity", en: "ULL Arena - HFT & Exchange Connectivity" },',
           '    title: { pt: "Mercado Financeiro — Bastidores", en: "Capital Markets — Behind the Scenes", es: "Mercados Financieros — Bastidores" },\n    href: "/ull-arena/",', "ULL Arena → título + href")
    p(pts, '      en: "Ultra-low latency (ULL) network architecture designed for High-Frequency Trading (HFT) environments. Focus on deterministic infrastructure for B3 order routing."\n    },',
           '      en: "Ultra-low latency (ULL) network architecture designed for High-Frequency Trading (HFT) environments. Focus on deterministic infrastructure for B3 order routing.",\n      es: "Arquitectura de red de ultra baja latencia (ULL) diseñada para entornos de High-Frequency Trading (HFT). Infraestructura determinística para enrutamiento de órdenes en B3."\n    },', "Summary ES")
    p(pts, '      en: "Network layer optimization to ensure microsecond execution times for critical financial market applications connected to exchanges."\n    },',
           '      en: "Network layer optimization to ensure microsecond execution times for critical financial market applications connected to exchanges.",\n      es: "Optimización de la capa de red para garantizar tiempos de ejecución en microsegundos para aplicaciones críticas del mercado financiero conectadas a exchanges."\n    },', "Context ES")
    p(pts, '      en: [\n        "Implementation of ultra-high performance cut-through switching.",\n        "Network buffer fine-tuning for microburst mitigation.",\n        "Deterministic routing and precise time synchronization via PTP."\n      ]\n    },',
           '      en: [\n        "Implementation of ultra-high performance cut-through switching.",\n        "Network buffer fine-tuning for microburst mitigation.",\n        "Deterministic routing and precise time synchronization via PTP."\n      ],\n      es: [\n        "Implementación de switching cut-through de altísimo rendimiento.",\n        "Ajuste fino de buffers de red para mitigación de microbursts.",\n        "Enrutamiento determinístico y sincronización de tiempo vía PTP."\n      ]\n    },', "Solution ES")
    p(pts, '      en: [\n        "Severe reduction of RTT (Round Trip Time) to B3.",\n        "Guaranteed stability during market volatility spikes.",\n        "Full compliance with global HFT technical requirements."\n      ]\n    },',
           '      en: [\n        "Severe reduction of RTT (Round Trip Time) to B3.",\n        "Guaranteed stability during market volatility spikes.",\n        "Full compliance with global HFT technical requirements."\n      ],\n      es: [\n        "Reducción severa del RTT (Round Trip Time) hasta B3.",\n        "Estabilidad garantizada durante picos de volatilidad del mercado.",\n        "Conformidad total con los requisitos técnicos globales de HFT."\n      ]\n    },', "Results ES")
    p(pts, '      en: "Logical topology of HFT connection and Nexus infrastructure."\n    }',
           '      en: "Logical topology of HFT connection and Nexus infrastructure.",\n      es: "Topología lógica de conexión HFT e infraestructura Nexus."\n    }', "DiagramNote ES")

    # ═══════════════════════ PROJECTCARD ═══════════════════════
    print(f"\n{'═'*55}\n  ProjectCard.tsx\n{'═'*55}")
    p(card, 'import { Link } from "@tanstack/react-router";\nimport { useI18n } from "@/lib/i18n";\nimport type { Project } from "@/data/projects";\n\nexport function ProjectCard({ project }: { project: Project }) {\n  const { lang } = useI18n();\n  return (\n    <Link\n      to={`/projetos/${project.slug}`}\n      className="card-hover group flex flex-col overflow-hidden rounded-xl border border-border bg-card"\n    >',
           'import { Link } from "@tanstack/react-router";\nimport { useI18n } from "@/lib/i18n";\nimport type { Project } from "@/data/projects";\n\nexport function ProjectCard({ project }: { project: Project }) {\n  const { lang } = useI18n();\n  if (project.href) {\n    return (\n      <a href={project.href} className="card-hover group flex flex-col overflow-hidden rounded-xl border border-border bg-card">\n        <img src={project.cover} alt={project.title[lang]} loading="lazy" width={1280} height={720} className="aspect-video w-full object-cover opacity-90 transition-opacity group-hover:opacity-100"/>\n        <div className="flex flex-1 flex-col gap-3 p-5">\n          <h3 className="text-lg font-semibold">{project.title[lang]}</h3>\n          <p className="flex-1 text-sm leading-relaxed text-muted-foreground">{project.summary[lang]}</p>\n          <div className="flex flex-wrap gap-1.5">{project.tags.map((tag) => (<span key={tag} className="rounded border border-border bg-secondary px-2 py-0.5 font-mono text-[11px] text-muted-foreground">{tag}</span>))}</div>\n        </div>\n      </a>\n    );\n  }\n  return (\n    <Link\n      to={`/projetos/${project.slug}`}\n      className="card-hover group flex flex-col overflow-hidden rounded-xl border border-border bg-card"\n    >', "Card — link direto")

    # ═══════════════════════ STYLES.CSS ═══════════════════════
    print(f"\n{'═'*55}\n  styles.css — tema light\n{'═'*55}")
    p(styles, '  --background: oklch(0.18 0.028 250);\n  --foreground: oklch(0.95 0.008 240);\n  --surface: oklch(0.22 0.03 250);\n  --card: oklch(0.235 0.03 250);\n  --card-foreground: oklch(0.95 0.008 240);\n  --popover: oklch(0.235 0.03 250);\n  --popover-foreground: oklch(0.95 0.008 240);\n  --primary: oklch(0.82 0.15 195);\n  --primary-foreground: oklch(0.18 0.028 250);\n  --neon: oklch(0.85 0.2 145);\n  --secondary: oklch(0.28 0.032 250);\n  --secondary-foreground: oklch(0.95 0.008 240);\n  --muted: oklch(0.27 0.03 250);\n  --muted-foreground: oklch(0.72 0.02 240);\n  --accent: oklch(0.3 0.05 220);\n  --accent-foreground: oklch(0.95 0.008 240);\n  --destructive: oklch(0.62 0.2 25);\n  --destructive-foreground: oklch(0.97 0 0);\n  --border: oklch(0.32 0.03 250);\n  --input: oklch(0.3 0.03 250);\n  --ring: oklch(0.82 0.15 195);\n  --grid-line: oklch(0.28 0.03 250 / 55%);\n  --glow-primary: 0 0 0 1px color-mix(in oklab, var(--primary) 35%, transparent),\n    0 12px 40px -14px color-mix(in oklab, var(--primary) 55%, transparent);',
           '  --background: #ffffff;\n  --foreground: #08213E;\n  --surface: #F4F9FD;\n  --card: #ffffff;\n  --card-foreground: #08213E;\n  --popover: #ffffff;\n  --popover-foreground: #08213E;\n  --primary: #0B5CD5;\n  --primary-foreground: #ffffff;\n  --neon: #0F8B4C;\n  --secondary: #E5F1FA;\n  --secondary-foreground: #12395F;\n  --muted: #F4F9FD;\n  --muted-foreground: #4A5E78;\n  --accent: #E5F1FA;\n  --accent-foreground: #08213E;\n  --destructive: #C93327;\n  --destructive-foreground: #ffffff;\n  --border: #DCE7F1;\n  --input: #DCE7F1;\n  --ring: #0B5CD5;\n  --grid-line: rgba(220,231,241,0.55);\n  --glow-primary: 0 1px 2px rgba(8,33,62,.05),\n    0 16px 40px -26px rgba(11,92,213,.25);', "Paleta light")
    p(styles, '  --font-sans: "Space Grotesk", ui-sans-serif, system-ui, sans-serif;\n  --font-mono: "JetBrains Mono", ui-monospace, monospace;',
           '  --font-sans: "DM Sans", ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;\n  --font-mono: "IBM Plex Mono", ui-monospace, monospace;', "Fontes")

    # ═══════════════════════ __ROOT.TSX ═══════════════════════
    print(f"\n{'═'*55}\n  __root.tsx\n{'═'*55}")
    p(root, 'href: "https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=JetBrains+Mono:wght@400;500&display=swap"',
            'href: "https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700&family=IBM+Plex+Mono:wght@400;500;600&display=swap"', "Google Fonts")

    # ═══════════════════════ ROTA PONTE ═══════════════════════
    print(f"\n{'═'*55}\n  Rota ponte → redirect\n{'═'*55}")
    if ull_rt.exists():
        ull_rt.write_text('import { createFileRoute, redirect } from "@tanstack/react-router";\nexport const Route = createFileRoute("/projetos/ull-arena")({\n  beforeLoad: () => { throw redirect({ href: "/ull-arena/" }); },\n  component: () => null,\n});\n', "utf-8")
        print("  ✓ projetos.ull-arena.tsx → redirect")

    # ═══════════════════════ ULL ARENA HTML ═══════════════════════
    if H.exists():
        print(f"\n{'═'*55}\n  ULL Arena HTML — i18n + SVG + nav + nomes\n{'═'*55}")
        # Nomes reais
        pa(H, 'Double CCIE (Enterprise + Service Provider) · CCDE · CaIT Networks',
              'Principal Solutions Architect | Enterprise Networking & Cybersecurity | Capital Markets', "Role tagline")
        pa(H, '· CaIT Networks', '', "CaIT removido")
        p(H, '<p class="cr"><b>Double CCIE</b> — Enterprise Infrastructure + Service Provider &nbsp;·&nbsp; <b>CCDE</b>',
             '<p class="cr"><b>Josimar Caitano</b> — Principal Solutions Architect | Capital Markets', "Footer CCIE/CCDE")
        p(H, 'Fundador, CaIT Networks · educador e mentor Cisco',
             'Cisco Networking Academy instructor since 2006', "ft.1 PT inline")
        p(H, '"ft.1":"Founder, CaIT Networks · Cisco educator and mentor"',
             '"ft.1":"Cisco Networking Academy instructor since 2006"', "ft.1 EN")
        p(H, '"ft.1":"Fundador, CaIT Networks · educador y mentor Cisco"',
             '"ft.1":"Instructor Cisco Networking Academy desde 2006"', "ft.1 ES")
        p(H, '<title>ULL Arena — Ultra Baixa Latência para Mercados de Capitais | Josimar Caitano</title>',
             '<title>Mercado Financeiro — Bastidores | Josimar Caitano</title>', "HTML title")
        p(H, '  ULL Arena <span class="s"></span></span>',
             '  Mercado Financeiro <span class="s">— Bastidores</span></span>', "Header branding")
        pa(H, 'ULL Arena', 'Mercado Financeiro — Bastidores', "ULL Arena restantes")
        # SVG: CE → Triton, ExaNIC → SolarFlare, ASN
        p(H, '>CE 01 / CE 02<', '>Triton 01 / 02<', "CE → Triton")
        p(H, '>Fusion L1<', '>Fusion<', "Fusion L1 → Fusion")
        pa(H, 'ExaNIC dual-port', 'SolarFlare NIC', "ExaNIC → SolarFlare")
        p(H, 'eBGP · PIM · FHRP · BFD', 'eBGP AS priv · PIM SM · BFD', "CE ASN detail")
        p(H, '>+39 ns<', '>order mux +39 ns<', "Triton mux label")
        # SVG flow: PE02 → Fusion (não CE)
        p(H, '     <line x1="1080" y1="126" x2="1080" y2="182" stroke="#B87610" stroke-width="2.5"/>',
             '     <line x1="1080" y1="126" x2="876" y2="182" stroke="#B87610" stroke-width="2.5"/>', "PE02 → Fusion")
        # Leak label
        p(H, '     <text x="900" y="200" font-size="9.5" font-weight="700" fill="#63768E" data-i18n="sr.split">planos separados</text>\n     <line x1="876" y1="213" x2="980" y2="213" stroke="#BFD5E8" stroke-width="2" stroke-dasharray="3 3"/>',
             '     <text x="900" y="200" font-size="9.5" font-weight="700" fill="#63768E" data-i18n="sr.leak">leak A15</text>\n     <line x1="876" y1="213" x2="980" y2="213" stroke="#8DA0B5" stroke-width="1.5" stroke-dasharray="4 3" marker-end="url(#rB)"/>', "leak A15")
        # i18n 37 keys
        p(H, '"s7.ft":"Final score",', '"s7.ft":"Final score",' + SR_EN + ',', "EN — 37 keys sr.*")
        p(H, '"s7.ft":"Marcador final",', '"s7.ft":"Marcador final",' + SR_ES + ',', "ES — 37 keys sr.*")
        # Nav bar
        inj(H, "</style>", NAV_CSS + "\n", "Nav CSS")
        inj(H, '\n<div class="tb">', NAV_HTML, "Nav HTML")

    # ═══════════════════════ LIMPEZA ═══════════════════════
    print(f"\n{'═'*55}\n  Limpeza\n{'═'*55}")
    for path_str, label in [
        ("src/data/types.ts","types.ts duplicado"),
        ("src/components/project/ProjectDetail.tsx","ProjectDetail.tsx órfão"),
        ("src/data/ull-arena.ts","ull-arena.ts dados ponte"),
        ("ull-network.py","ull-network.py antigo"),
        ("apply_patches.py","v1"),("apply_patches_v2.py","v2"),
        ("apply_patches_v3.py","v3"),("apply_patches_v4.py","v4"),
        ("apply_patches_v5.py","v5"),
        ("src/PATCHES-portfolio.tsx","PATCHES ref"),
        ("src/aplicarcorrecao.py","aplicarcorrecao"),
    ]:
        rm(B/path_str, label)
    d = B/"src"/"components"/"project"
    if d.exists() and not any(d.iterdir()):
        d.rmdir(); print("  🗑  project/ pasta vazia")

    # ═══════════════════════ RESULTADO ═══════════════════════
    print(f"\n{'═'*55}")
    print(f"  ✅ MASTER PATCH COMPLETO")
    print(f"{'═'*55}")
    print(f"\n  git add -A && git commit -m 'master: all fixes' && git push\n")

if __name__ == "__main__":
    main()
