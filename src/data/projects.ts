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
  href?: string;
  externalLink?: boolean;
};

export const projects: Project[] = [
  {
    slug: "ull-arena",
    cover: "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=800&q=80", 
    tags: ["ULL", "HFT", "B3 Exchange", "Nexus", "Ultra-Low Latency"],
    title: { pt: "Mercado Financeiro — Bastidores", en: "Capital Markets — Behind the Scenes", es: "Mercados Financieros — Bastidores" },
    href: "/ull-arena/",
    summary: {
      pt: "Arquitetura de rede de ultra-baixa latência (ULL) desenhada para ambientes de High-Frequency Trading (HFT). Foco em infraestrutura determinística para roteamento de ordens na B3.",
      en: "Ultra-low latency (ULL) network architecture designed for High-Frequency Trading (HFT) environments. Focus on deterministic infrastructure for B3 order routing.",
      es: "Arquitectura de red de ultra baja latencia (ULL) diseñada para entornos de High-Frequency Trading (HFT). Infraestructura determinística para enrutamiento de órdenes en B3."
    },
    context: {
      pt: "Otimização da camada de rede para garantir tempos de execução na casa dos microssegundos para aplicações críticas do mercado financeiro conectadas às exchanges.",
      en: "Network layer optimization to ensure microsecond execution times for critical financial market applications connected to exchanges.",
      es: "Optimización de la capa de red para garantizar tiempos de ejecución en microsegundos para aplicaciones críticas del mercado financiero conectadas a exchanges."
    },
    solution: {
      pt: [
        "Implementação de switching cut-through de altíssima performance.",
        "Ajuste fino de buffers de rede para mitigação de microbursts.",
        "Roteamento determinístico e sincronização de tempo via PTP."
      ],
      en: [
        "Implementation of ultra-high performance cut-through switching.",
        "Network buffer fine-tuning for microburst mitigation.",
        "Deterministic routing and precise time synchronization via PTP."
      ],
      es: [
        "Implementación de switching cut-through de altísimo rendimiento.",
        "Ajuste fino de buffers de red para mitigación de microbursts.",
        "Enrutamiento determinístico y sincronización de tiempo vía PTP."
      ]
    },
    results: {
      pt: [
        "Redução severa do RTT (Round Trip Time) até a B3.",
        "Estabilidade garantida durante picos de volatilidade do mercado.",
        "Conformidade total com os requisitos técnicos globais de HFT."
      ],
      en: [
        "Severe reduction of RTT (Round Trip Time) to B3.",
        "Guaranteed stability during market volatility spikes.",
        "Full compliance with global HFT technical requirements."
      ],
      es: [
        "Reducción severa del RTT (Round Trip Time) hasta B3.",
        "Estabilidad garantizada durante picos de volatilidad del mercado.",
        "Conformidad total con los requisitos técnicos globales de HFT."
      ]
    },
    diagramNote: {
      pt: "Topologia lógica de conexão HFT e infraestrutura Nexus.",
      en: "Logical topology of HFT connection and Nexus infrastructure.",
      es: "Topología lógica de conexión HFT e infraestructura Nexus."
    }
  }
];

export const getProject = (slug: string) => projects.find((p) => p.slug === slug);