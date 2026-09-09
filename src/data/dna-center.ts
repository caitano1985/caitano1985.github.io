import dnaCover from "@/assets/project-dna.jpg";
import type { Project } from "./types";

export const dnaCenter: Project = {
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
};