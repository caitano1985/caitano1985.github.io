import dnaCover from "@/assets/project-dna.jpg";
import multicastCover from "@/assets/project-multicast.jpg";
import type { Lang } from "@/lib/i18n";

export type LocalizedText = Record<Lang, string>;
export type LocalizedList = Record<Lang, string[]>;

export type Project = {
  slug: string;
  cover: string;
  tags: string[];
  title: LocalizedText;
  summary: LocalizedText;
  context: LocalizedText;
  solution: LocalizedList;
  results: LocalizedList;
  diagramNote: LocalizedText;
};

export const projects: Project[] = [
  {
    slug: "dna-center",
    cover: dnaCover,
    tags: ["Cisco DNA Center", "SD-Access", "Automação", "ISE", "Assurance"],
    title: { pt: "Cisco DNA Center", en: "Cisco DNA Center" },
    summary: {
      pt: "Automação e gerenciamento de rede campus com Cisco DNA Center: SD-Access, políticas baseadas em grupo e monitoramento centralizado.",
      en: "Campus network automation and management with Cisco DNA Center: SD-Access, group-based policy and centralized monitoring.",
    },
    context: {
      pt: "[placeholder] Ambiente campus multi-site com provisionamento manual, inventário desatualizado e políticas de acesso inconsistentes entre prédios. O tempo médio para provisionar um novo switch de acesso era alto e a visibilidade de falhas dependia de checagens manuais no NOC.",
      en: "[placeholder] Multi-site campus environment with manual provisioning, outdated inventory and inconsistent access policies across buildings. Average time to provision a new access switch was high and fault visibility depended on manual NOC checks.",
    },
    solution: {
      pt: [
        "[placeholder] Desenho do fabric SD-Access com Control Plane (LISP), Border e Edge Nodes distribuídos por site.",
        "[placeholder] Integração com Cisco ISE para segmentação por SGT e políticas baseadas em identidade.",
        "[placeholder] Templates de provisionamento (LAN Automation e Plug and Play) para padronizar switches de acesso.",
        "[placeholder] Uso do DNA Assurance para baseline de saúde de clientes, wireless e dispositivos de rede.",
        "[placeholder] Automação complementar via APIs REST do DNA Center para relatórios e conformidade.",
      ],
      en: [
        "[placeholder] SD-Access fabric design with Control Plane (LISP), Border and Edge Nodes distributed per site.",
        "[placeholder] Cisco ISE integration for SGT-based segmentation and identity-driven policy.",
        "[placeholder] Provisioning templates (LAN Automation and Plug and Play) to standardize access switches.",
        "[placeholder] DNA Assurance used to baseline client, wireless and network device health.",
        "[placeholder] Additional automation through DNA Center REST APIs for reporting and compliance.",
      ],
    },
    results: {
      pt: [
        "[placeholder] Redução significativa do tempo de provisionamento de novos switches.",
        "[placeholder] Política de segmentação uniforme entre sites.",
        "[placeholder] Detecção proativa de problemas de conectividade via Assurance.",
      ],
      en: [
        "[placeholder] Significant reduction in provisioning time for new switches.",
        "[placeholder] Uniform segmentation policy across sites.",
        "[placeholder] Proactive detection of connectivity issues through Assurance.",
      ],
    },
    diagramNote: {
      pt: "[placeholder] Diagrama de topologia do fabric SD-Access — substituir pela imagem real do projeto.",
      en: "[placeholder] SD-Access fabric topology diagram — replace with the real project image.",
    },
  },
  {
    slug: "multicast",
    cover: multicastCover,
    tags: ["Multicast", "PIM", "IGMP", "RP", "Troubleshooting"],
    title: { pt: "Multicast Receiver e Sender", en: "Multicast Receiver and Sender" },
    summary: {
      pt: "Implementação e validação de multicast fim a fim: PIM Sparse-Mode, IGMP nos receivers e testes com sender em laboratório.",
      en: "End-to-end multicast implementation and validation: PIM Sparse-Mode, IGMP on receivers and lab sender testing.",
    },
    context: {
      pt: "[placeholder] Necessidade de distribuir fluxos de dados de mercado (market data) para múltiplos receivers sem replicar tráfego unicast, mantendo previsibilidade de latência e controle de quem pode receber cada grupo.",
      en: "[placeholder] Need to distribute market data streams to multiple receivers without replicating unicast traffic, keeping latency predictable and controlling which hosts may join each group.",
    },
    solution: {
      pt: [
        "[placeholder] PIM Sparse-Mode habilitado no core, com RP estático/Anycast-RP para redundância.",
        "[placeholder] IGMPv2/v3 nos segmentos de acesso, com IGMP snooping nos switches.",
        "[placeholder] Configuração do sender (origem do fluxo) e dos receivers em laboratório para validação.",
        "[placeholder] Filtros de grupo e boundaries para limitar o escopo do multicast por domínio.",
        "[placeholder] Verificação com show ip mroute, show ip pim neighbor e show ip igmp groups.",
      ],
      en: [
        "[placeholder] PIM Sparse-Mode enabled in the core, with static/Anycast RP for redundancy.",
        "[placeholder] IGMPv2/v3 on access segments, with IGMP snooping on switches.",
        "[placeholder] Sender (stream source) and receiver configuration in the lab for validation.",
        "[placeholder] Group filters and boundaries to scope multicast per domain.",
        "[placeholder] Verification with show ip mroute, show ip pim neighbor and show ip igmp groups.",
      ],
    },
    results: {
      pt: [
        "[placeholder] Entrega estável dos fluxos aos receivers com árvore de distribuição otimizada.",
        "[placeholder] Redução de tráfego duplicado no core.",
        "[placeholder] Roteiro de troubleshooting reaproveitado nas sessões de laboratório CCIE.",
      ],
      en: [
        "[placeholder] Stable stream delivery to receivers with an optimized distribution tree.",
        "[placeholder] Reduction of duplicated traffic in the core.",
        "[placeholder] Troubleshooting playbook reused in CCIE lab sessions.",
      ],
    },
    diagramNote: {
      pt: "[placeholder] Topologia sender/receiver e configurações — substituir pelo material real.",
      en: "[placeholder] Sender/receiver topology and configs — replace with the real material.",
    },
  },
];

export const getProject = (slug: string) => projects.find((p) => p.slug === slug);
