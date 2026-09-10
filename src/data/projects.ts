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
    slug: "ull-arena",
    cover: multicastCover, 
    tags: ["ULL", "HFT", "B3 Exchange", "Nexus", "Ultra-Low Latency"],
    title: { pt: "ULL Arena - HFT & Exchange Connectivity", en: "ULL Arena - HFT & Exchange Connectivity" },
    summary: {
      pt: "Arquitetura de rede de ultra-baixa latência (ULL) desenhada para ambientes de High-Frequency Trading (HFT). Foco em infraestrutura determinística para roteamento de ordens.",
      en: "Ultra-low latency (ULL) network architecture designed for High-Frequency Trading (HFT) environments. Focus on deterministic infrastructure for order routing."
    },
    context: {
      pt: "Otimização da camada de rede para garantir tempos de execução na casa dos microssegundos para aplicações críticas do mercado financeiro conectadas às exchanges.",
      en: "Network layer optimization to ensure microsecond execution times for critical financial market applications connected to exchanges."
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
      ]
    },
    results: {
      pt: [
        "Redução severa do RTT (Round Trip Time).",
        "Estabilidade garantida durante picos de volatilidade do mercado.",
        "Conformidade total com os requisitos técnicos globais de HFT."
      ],
      en: [
        "Severe reduction of RTT (Round Trip Time).",
        "Guaranteed stability during market volatility spikes.",
        "Full compliance with global HFT technical requirements."
      ]
    },
    diagramNote: {
      pt: "Topologia lógica de conexão HFT e infraestrutura Nexus.",
      en: "Logical topology of HFT connection and Nexus infrastructure."
    }
  }
];

export const getProject = (slug: string) => projects.find((p) => p.slug === slug);
