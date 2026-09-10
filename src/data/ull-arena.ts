// src/data/ull-arena.ts
// Conteúdo da página de apresentação da ULL Arena.
// O artefato interativo em si vive em /public/ull-arena/index.html
// e é servido estaticamente em https://caitano1985.github.io/ull-arena/

export type Modulo = {
  n: string;
  titulo: string;
  tipo: "lab" | "game" | "topologia" | "modelo";
  descricao: string;
};

export type Trilha = {
  nivel: string;
  rotulo: string;
};

export const ullArena = {
  slug: "ull-arena",
  titulo: "ULL Arena",
  subtitulo: "Infraestrutura de ultra baixa latência para mercados de capitais",
  chamada:
    "Sete laboratórios jogáveis sobre a rede que conecta uma mesa de operações ao matching engine de uma bolsa. Duas lentes — engenharia e board — sobre o mesmo sistema.",
  href: "/ull-arena/",
  trilha: "Ultra baixa latência",
  nivel: "400 · Elite",
  idiomas: ["EN", "PT-BR", "ES"],
  atualizadoEm: "2026-09",

  resumo: [
    "A B3 exige, na modalidade Rack Negociação, acesso em Camada 3 roteado com eBGP e PIM Sparse. Quase todo mundo lê esse requisito como 'coloque o roteador no caminho do market data'. Não é isso que o manual diz.",
    "O CE existe para estabelecer a sessão BGP, anunciar o bloco e fazer o join dos grupos UMDF. Depois que a árvore multicast está formada, o feed pode ser entregue em Camada 1 e replicado eletricamente para os servidores — sem voltar a atravessar processamento de roteamento.",
    "A diferença entre as duas leituras do mesmo manual é de três ordens de grandeza. Esta página existe para tornar isso visível, jogável e defensável diante de um comitê.",
  ],

  paraQuem: [
    "Engenheiros de infraestrutura em corretoras, bolsas e mesas proprietárias",
    "Arquitetos que precisam justificar investimento em latência para um comitê",
    "Profissionais de rede migrando para o mercado financeiro",
    "Executivos que aprovam orçamento sem vocabulário técnico para avaliá-lo",
  ],

  modulos: [
    { n: "1", titulo: "A escala", tipo: "lab",
      descricao: "Converte nanossegundos em tempo perceptível. Se 1 ns virasse 1 s, uma ordem saindo do escritório custaria doze dias." },
    { n: "2", titulo: "A topologia", tipo: "topologia",
      descricao: "Malha completa bolsa ↔ cross-connect ↔ gaiola, com aula guiada em sete passos e disparo de pacote com contador ao vivo." },
    { n: "3", titulo: "Pista de obstáculos", tipo: "game",
      descricao: "Remova firewall, switch convencional e NIC comum do caminho crítico. Sua bola corre contra a configuração de elite." },
    { n: "3.1", titulo: "Rack Negociação B3", tipo: "topologia",
      descricao: "Conformidade × elite lado a lado. Mesmo eBGP, mesmo PIM, mesma dualização — 156 µs contra 294 ns." },
    { n: "4", titulo: "A prova do firewall", tipo: "game",
      descricao: "Duelo stateful × filtro FPGA. O argumento numérico para a conversa com segurança da informação." },
    { n: "5", titulo: "A cauda que mata", tipo: "lab",
      descricao: "Distribuição de latência, p50 / p99 / p99,9 e índice de jitter. Ninguém é pago pela média." },
    { n: "6", titulo: "Rotas globais", tipo: "game",
      descricao: "Distância geodésica, fibra e micro-ondas entre B3, CME, NY4, LD4, FR2, JPX, SSE, HKEX, SGX e ASX." },
    { n: "7", titulo: "Arbitragem BR ↔ US", tipo: "game",
      descricao: "Você contra o seu algoritmo, mesma infraestrutura, dez rodadas simultâneas. O humano perde sempre — e esse é o ponto." },
    { n: "8", titulo: "Monte a mesa", tipo: "modelo",
      descricao: "Configurador com veredito em nanossegundos e em capital, mais tese econômica com payback e sensibilidade." },
    { n: "9", titulo: "O juiz do tempo", tipo: "lab",
      descricao: "PTP, GNSS, holdover e o esquema em faixas do MiFID II / RTS 25 — por que relógio livre reprova em auditoria." },
    { n: "10", titulo: "Perguntas do board", tipo: "modelo",
      descricao: "As cinco perguntas de comitê, cada uma com resposta de engenharia e resposta de board." },
  ] satisfies Modulo[],

  stack: [
    "HTML e SVG autorais, sem dependência externa",
    "Motor de internacionalização próprio (EN / PT-BR / ES)",
    "Simulação estatística de distribuição de latência",
    "Cálculo geodésico de rota entre praças de colocation",
    "Modelo logístico de probabilidade de captura",
  ],

  aviso:
    "Material didático original. Latências, custos e parâmetros econômicos são ordens de grandeza públicas e premissas ilustrativas, destinadas ao ensino do raciocínio de arquitetura. Não constituem recomendação de investimento nem especificação de projeto.",
} as const;
