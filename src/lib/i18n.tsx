import { createContext, useContext, useMemo, useState, type ReactNode } from "react";

export type Lang = "pt" | "en";

type Ctx = { lang: Lang; setLang: (l: Lang) => void; t: (path: string) => string };

const LangContext = createContext<Ctx | null>(null);

export const dict: Record<Lang, Record<string, string>> = {
  pt: {
    "nav.about": "Sobre",
    "nav.experience": "Experiência",
    "nav.certs": "Certificações",
    "nav.teaching": "Ensino",
    "nav.projects": "Projetos",
    "nav.content": "Conteúdo",
    "nav.contact": "Contato",
    "hero.badge": "status: online",
    "hero.role": "CCIE x2 | Principal IP Solutions Architect | Instrutor de Redes",
    "hero.desc":
      "Especialista sênior em redes e engenheiro de infraestrutura de TI, com foco em roteamento avançado, segurança e operações de rede para o setor financeiro.",
    "hero.cta": "Falar comigo",
    "hero.cta2": "Ver projetos",
    "hero.photoNote": "[placeholder] foto profissional",
    "about.title": "Sobre",
    "about.p1":
      "Josimar Caitano, conhecido como Josinfo, é engenheiro de infraestrutura com dupla certificação CCIE. Atua hoje como Principal IP Solutions Architect for Financial Services, desenhando arquiteturas IP críticas para instituições financeiras.",
    "about.p2":
      "Sua especialidade combina roteamento avançado (OSPF, BGP e afins), segurança de rede, operação de NOC e visibilidade com Cisco StealthWatch. Reconhecido pela comunidade — como a Academia Brasileira de Redes (ABRedes) — como referência em roteamento e mentoria técnica.",
    "about.p3":
      "Além da prática de campo, dedica boa parte do tempo a ensinar: aulas de CCNA DevNet e CCNP Encor, laboratórios de preparação para o CCIE e produção de artigos e vídeos técnicos.",
    "exp.title": "Experiência Profissional",
    "exp.current": "atual",
    "exp.role1": "Principal IP Solutions Architect for Financial Services",
    "exp.company1": "Setor Financeiro",
    "exp.period1": "Atual",
    "exp.desc1":
      "Arquitetura de soluções IP para ambientes financeiros de missão crítica: roteamento avançado, segmentação, segurança e visibilidade de rede.",
    "exp.role2": "Cargo — [placeholder]",
    "exp.company2": "Empresa X",
    "exp.period2": "Período — [placeholder]",
    "exp.desc2":
      "[placeholder] Descrição da experiência anterior: escopo, tecnologias e principais entregas.",
    "exp.role3": "Cargo — [placeholder]",
    "exp.company3": "Empresa Y",
    "exp.period3": "Período — [placeholder]",
    "exp.desc3":
      "[placeholder] Descrição da experiência anterior: escopo, tecnologias e principais entregas.",
    "certs.title": "Certificações",
    "certs.ccie": "CCIE x2",
    "certs.ccieDesc": "Cisco Certified Internetwork Expert — dupla certificação.",
    "certs.other": "Certificação Cisco — [placeholder]",
    "certs.otherDesc": "[placeholder] Adicionar trilha, número e data de emissão.",
    "teach.title": "Ensino & Mentoria",
    "teach.method": "Metodologia",
    "teach.methodDesc":
      "Aulas orientadas a laboratório: teoria curta, prática longa. Cada tópico é validado em topologia real, com troubleshooting guiado e leitura de saídas de CLI até o aluno raciocinar sozinho.",
    "teach.c1": "CCNA DevNet",
    "teach.c1d": "Automação, APIs, Python aplicado a redes e ferramentas de desenvolvedor Cisco.",
    "teach.c2": "CCNP Encor",
    "teach.c2d": "Núcleo de enterprise: roteamento, switching, wireless, segurança e automação.",
    "teach.c3": "CCIE Lab — sessões práticas",
    "teach.c3d": "Sessões dedicadas de laboratório, como OSPF avançado e troubleshooting sob tempo.",
    "projects.title": "Projetos",
    "projects.subtitle": "Estudos de caso de arquitetura e implementação de rede.",
    "projects.all": "Ver todos os projetos",
    "projects.back": "Voltar para Projetos",
    "projects.context": "Contexto & Problema",
    "projects.tech": "Tecnologias Utilizadas",
    "projects.solution": "Solução & Arquitetura",
    "projects.diagram": "Diagramas",
    "projects.results": "Resultados & Aprendizados",
    "projects.listTitle": "Todos os Projetos",
    "content.title": "Conteúdo & Publicações",
    "content.a1": "HowTo: Cisco StealthWatch",
    "content.a1d": "[placeholder] Guia prático de implantação e análise de fluxos com StealthWatch.",
    "content.a2": "Artigo técnico — [placeholder]",
    "content.a2d": "[placeholder] Resumo do artigo e link para o blog.",
    "content.v1": "Vídeo — OSPF na prática",
    "content.v1d": "[placeholder] Link do YouTube a ser adicionado.",
    "content.v2": "Vídeo — [placeholder]",
    "content.v2d": "[placeholder] Link do YouTube a ser adicionado.",
    "content.link": "Link em breve",
    "contact.title": "Contato",
    "contact.desc": "Para mentorias, palestras, aulas ou projetos de arquitetura de rede.",
    "contact.name": "Nome",
    "contact.email": "E-mail",
    "contact.message": "Mensagem",
    "contact.send": "Enviar mensagem",
    "contact.sent": "Mensagem registrada. Em breve o envio real será conectado.",
    "footer.rights": "Todos os direitos reservados.",
    "lang.label": "Idioma",
  },
  en: {
    "nav.about": "About",
    "nav.experience": "Experience",
    "nav.certs": "Certifications",
    "nav.teaching": "Teaching",
    "nav.projects": "Projects",
    "nav.content": "Content",
    "nav.contact": "Contact",
    "hero.badge": "status: online",
    "hero.role": "CCIE x2 | Principal IP Solutions Architect | Network Instructor",
    "hero.desc":
      "Senior network specialist and IT infrastructure engineer focused on advanced routing, network security and operations for the financial services sector.",
    "hero.cta": "Get in touch",
    "hero.cta2": "View projects",
    "hero.photoNote": "[placeholder] professional photo",
    "about.title": "About",
    "about.p1":
      "Josimar Caitano, known as Josinfo, is an infrastructure engineer holding a double CCIE certification. He currently works as Principal IP Solutions Architect for Financial Services, designing mission-critical IP architectures for financial institutions.",
    "about.p2":
      "His expertise combines advanced routing (OSPF, BGP and beyond), network security, NOC operations and visibility with Cisco StealthWatch. He is recognized by the community — such as the Brazilian Network Academy (ABRedes) — as a reference in routing and technical mentoring.",
    "about.p3":
      "Beyond field work, he devotes much of his time to teaching: CCNA DevNet and CCNP Encor classes, CCIE lab preparation sessions, and technical articles and videos.",
    "exp.title": "Professional Experience",
    "exp.current": "current",
    "exp.role1": "Principal IP Solutions Architect for Financial Services",
    "exp.company1": "Financial Services",
    "exp.period1": "Current",
    "exp.desc1":
      "IP solution architecture for mission-critical financial environments: advanced routing, segmentation, security and network visibility.",
    "exp.role2": "Role — [placeholder]",
    "exp.company2": "Company X",
    "exp.period2": "Period — [placeholder]",
    "exp.desc2": "[placeholder] Previous role description: scope, technologies and key deliveries.",
    "exp.role3": "Role — [placeholder]",
    "exp.company3": "Company Y",
    "exp.period3": "Period — [placeholder]",
    "exp.desc3": "[placeholder] Previous role description: scope, technologies and key deliveries.",
    "certs.title": "Certifications",
    "certs.ccie": "CCIE x2",
    "certs.ccieDesc": "Cisco Certified Internetwork Expert — double certification.",
    "certs.other": "Cisco certification — [placeholder]",
    "certs.otherDesc": "[placeholder] Add track, number and issue date.",
    "teach.title": "Teaching & Mentoring",
    "teach.method": "Methodology",
    "teach.methodDesc":
      "Lab-driven classes: short theory, long practice. Every topic is validated on a real topology, with guided troubleshooting and CLI output reading until the student reasons independently.",
    "teach.c1": "CCNA DevNet",
    "teach.c1d": "Automation, APIs, Python for networking and Cisco developer tooling.",
    "teach.c2": "CCNP Encor",
    "teach.c2d": "Enterprise core: routing, switching, wireless, security and automation.",
    "teach.c3": "CCIE Lab — hands-on sessions",
    "teach.c3d": "Dedicated lab sessions such as advanced OSPF and timed troubleshooting.",
    "projects.title": "Projects",
    "projects.subtitle": "Network architecture and implementation case studies.",
    "projects.all": "View all projects",
    "projects.back": "Back to Projects",
    "projects.context": "Context & Problem",
    "projects.tech": "Technologies Used",
    "projects.solution": "Solution & Architecture",
    "projects.diagram": "Diagrams",
    "projects.results": "Results & Takeaways",
    "projects.listTitle": "All Projects",
    "content.title": "Content & Publications",
    "content.a1": "HowTo: Cisco StealthWatch",
    "content.a1d": "[placeholder] Practical guide to deployment and flow analysis with StealthWatch.",
    "content.a2": "Technical article — [placeholder]",
    "content.a2d": "[placeholder] Article summary and blog link.",
    "content.v1": "Video — OSPF in practice",
    "content.v1d": "[placeholder] YouTube link to be added.",
    "content.v2": "Video — [placeholder]",
    "content.v2d": "[placeholder] YouTube link to be added.",
    "content.link": "Link coming soon",
    "contact.title": "Contact",
    "contact.desc": "For mentoring, talks, classes or network architecture projects.",
    "contact.name": "Name",
    "contact.email": "Email",
    "contact.message": "Message",
    "contact.send": "Send message",
    "contact.sent": "Message captured. Real delivery will be wired up soon.",
    "footer.rights": "All rights reserved.",
    "lang.label": "Language",
  },
};

export function LanguageProvider({ children }: { children: ReactNode }) {
  const [lang, setLang] = useState<Lang>("pt");
  const value = useMemo<Ctx>(
    () => ({ lang, setLang, t: (path: string) => dict[lang][path] ?? path }),
    [lang],
  );
  return <LangContext.Provider value={value}>{children}</LangContext.Provider>;
}

export function useI18n() {
  const ctx = useContext(LangContext);
  if (!ctx) throw new Error("useI18n must be used within LanguageProvider");
  return ctx;
}
