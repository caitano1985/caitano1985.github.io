#!/usr/bin/env python3
"""
FIX TRADUÇÃO — Módulo 3.1 apenas
Injeta 37 keys sr.* nos dicionários EN e ES
do arquivo public/ull-arena/index.html

Não mexe em NENHUM outro arquivo.
Zero risco de quebrar o build.

Executa: python3 fix_traducao.py
Na RAIZ do projeto.
"""
from pathlib import Path
import sys

def main():
    f = Path("public/ull-arena/index.html")
    if not f.exists():
        print("ERRO: public/ull-arena/index.html não encontrado.")
        sys.exit(1)

    c = f.read_text("utf-8")

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
        '"sr.mdl1":"market data direct on L1"',
        '"sr.ordtx":"TCP orders"',
        '"sr.cap":"Trading Rack requirements and how the elite architecture meets them without paying latency"',
        '"sr.c1":"B3 requirement"',
        '"sr.c2":"Common implementation"',
        '"sr.c3":"Elite implementation"',
        '"sr.r1a":"Routed Layer 3 access"',
        '"sr.r1b":"CE in the feed and order path"',
        '"sr.r1c":"CE only in control plane; data via L1"',
        '"sr.r2a":"Dual connections"',
        '"sr.r2b":"FHRP with convergence in seconds"',
        '"sr.r2c":"FHRP + BFD 100 ms × 3 · sub-second"',
        '"sr.r3a":"Optimized eBGP routing"',
        '"sr.r3b":"Default timers, no BFD"',
        '"sr.r3c":"Timers 7/21 + BFD + prefix filters"',
        '"sr.r4a":"UMDF multicast via PIM sparse"',
        '"sr.r4b":"Join on CE, software replication"',
        '"sr.r4c":"Join on CE, electrical replication on L1"',
        '"sr.r5a":"Redundant feeds A and B"',
        '"sr.r5b":"Feed arbitrage in application"',
        '"sr.r5c":"A/B arbitrage in FPGA on the NIC"',
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
        '"sr.mdl1":"market data directo en L1"',
        '"sr.ordtx":"órdenes TCP"',
        '"sr.cap":"Exigencias del Rack Negociación y cómo la arquitectura de élite las cumple sin pagar latencia"',
        '"sr.c1":"Exigencia de B3"',
        '"sr.c2":"Implementación común"',
        '"sr.c3":"Implementación de élite"',
        '"sr.r1a":"Acceso en Capa 3 ruteado"',
        '"sr.r1b":"CE en el camino del feed y de las órdenes"',
        '"sr.r1c":"CE solo en plano de control; datos vía L1"',
        '"sr.r2a":"Conexiones dualizadas"',
        '"sr.r2b":"FHRP con convergencia en segundos"',
        '"sr.r2c":"FHRP + BFD 100 ms × 3 · sub-segundo"',
        '"sr.r3a":"Ruteo eBGP optimizado"',
        '"sr.r3b":"Timers por defecto, sin BFD"',
        '"sr.r3c":"Timers 7/21 + BFD + filtros de prefijo"',
        '"sr.r4a":"Multicast UMDF vía PIM sparse"',
        '"sr.r4b":"Join en CE, replicación en software"',
        '"sr.r4c":"Join en CE, replicación eléctrica en L1"',
        '"sr.r5a":"Feeds A y B redundantes"',
        '"sr.r5b":"Arbitraje de feed en aplicación"',
        '"sr.r5c":"Arbitraje A/B en FPGA en la NIC"',
        '"sr.eng":"La lectura errónea del manual de B3 es concluir que, porque la modalidad exige Capa 3, el router debe estar en el camino del market data. No es así. El CE existe para establecer la sesión eBGP, anunciar el bloque del Rack Negociación, mantener la adyacencia PIM y hacer el join de los grupos UMDF. Una vez formado el árbol multicast, el tráfico puede entregarse al Fusion y replicarse eléctricamente a los servidores sin volver a atravesar procesamiento de ruteo. El CE queda en el plano de control; el dato corre en Capa 1. Esta separación es la diferencia entre 156 µs y 294 ns."',
        '"sr.board":"Dos instituciones pueden estar igualmente conformes al mismo manual de la bolsa y operar en regímenes de latencia separados por tres órdenes de magnitud. Conformidad regulatoria y ventaja competitiva son ejes independientes — cumplir el requisito es el piso, no la estrategia. Lo que separa a las dos es una decisión de arquitectura que no cuesta más licencia ni más contrato: cuesta saber dónde colocar cada caja."',
    ])

    ok = True

    # EN
    if "sr.k" in c and '"sr.k":"Module' in c:
        print("  ✓ EN — já injetado (pulando)")
    elif '"s7.ft":"Final score",' in c:
        c = c.replace('"s7.ft":"Final score",', '"s7.ft":"Final score",' + SR_EN + ',', 1)
        print("  ✓ EN — 37 keys sr.* injetadas")
    else:
        print("  ✗ EN — marker não encontrado")
        ok = False

    # ES
    if "sr.k" in c and '"sr.k":"Módulo 3.1' in c:
        print("  ✓ ES — já injetado (pulando)")
    elif '"s7.ft":"Marcador final",' in c:
        c = c.replace('"s7.ft":"Marcador final",', '"s7.ft":"Marcador final",' + SR_ES + ',', 1)
        print("  ✓ ES — 37 keys sr.* injetadas")
    else:
        print("  ✗ ES — marker não encontrado")
        ok = False

    f.write_text(c, "utf-8")

    if ok:
        print(f"\n  ✅ TRADUÇÃO CORRIGIDA")
        print(f"  → Módulo 3.1 agora traduz em 🇺🇸 e 🇪🇸")
        print(f"  → Modo engenharia + modo board — ambos traduzidos")
        print(f"\n  git add public/ull-arena/index.html")
        print(f"  git commit -m 'fix: i18n module 3.1 EN+ES'")
        print(f"  git push\n")
    else:
        print(f"\n  ⚠ Verifique o arquivo manualmente\n")

if __name__ == "__main__":
    main()
