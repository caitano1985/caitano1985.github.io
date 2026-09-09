import multicastCover from "@/assets/project-multicast.jpg";
import type { Project } from "./types";

export const multicast: Project = {
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
};