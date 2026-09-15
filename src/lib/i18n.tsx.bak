import { createContext, useContext, useMemo, useState, type ReactNode } from "react";

export type Lang = "en" | "es" | "pt";

type Ctx = { lang: Lang; setLang: (l: Lang) => void; t: (path: string) => string };

const LangContext = createContext<Ctx | null>(null);

/* ────────────────────────────────────────────────────────
   FLAGS (use in header toggle):
     EN → 🇺🇸   ES → 🇪🇸   PT → 🇧🇷
   ──────────────────────────────────────────────────────── */

export const dict: Record<Lang, Record<string, string>> = {
  /* ═══════════════════════════════════════════════════════
     ENGLISH (DEFAULT / LEADER)
     ═══════════════════════════════════════════════════════ */
  en: {
    // ── Navigation ──
    "nav.about": "About",
    "nav.experience": "Experience",
    "nav.certs": "Certifications",
    "nav.teaching": "Teaching",
    "nav.academic": "Academy",
    "nav.projects": "Projects",
    "nav.content": "Content",
    "nav.contact": "Contact",

    // ── Hero ──
    "hero.badge": "status: online",
    "hero.name": "Josimar Caitano",
    "hero.alias": "// じょしまる",
    "hero.role": "Principal Solutions Architect | Enterprise Networking & Cybersecurity | Financial Markets | Executive Technical Advisor",
    "hero.desc":
      "Where nanoseconds decide who wins and who watches, I architect the infrastructure. Mission-critical trading systems, carrier-grade networks, zero tolerance for latency — built for the speed of capital markets.",
    "hero.cta": "Get in touch",
    "hero.cta2": "View projects",

    // ── About (F1 Manifesto Bio) ──
    "about.title": "About",
    "about.p1":
      "In Formula 1, a tenth of a second separates victory from defeat. In capital markets, that margin compresses to nanoseconds — and the infrastructure I architect is what makes the difference. At XP Investimentos, I designed and delivered the ultra-low latency trading backbone connecting Brazil's largest investment platform to B3, ICE, and Goldman Sachs. Every microsecond shaved from that path translated directly into competitive advantage worth billions in daily volume.",
    "about.p2":
      "My arena spans HFT/ULL infrastructure, active-active data center design on Cisco ACI, multi-cloud connectivity across AWS, Azure, and GCP via Equinix Fabric, and carrier-grade MPLS architectures that powered Tier-1 telecom operators. I delivered up to 80% reduction in cost and project timelines — not by cutting corners, but by engineering precision at speed, like a pit crew executing a sub-two-second tire change.",
    "about.p3":
      "For over two decades I have built teams, mentored engineers, and shaped technical talent as a Cisco Networking Academy instructor since 2006. Today at NTT DATA I lead infrastructure governance for enterprise environments where compliance and resilience are non-negotiable. My trajectory is not a career ladder — it is a racing line: every apex calculated, every straight maximized, every decision engineered for velocity.",

    // ── Experience ──
    "exp.title": "Professional Experience",
    "exp.current": "current",

    "exp.role1": "Infrastructure & Security Governance Coordinator",
    "exp.company1": "NTT DATA",
    "exp.period1": "Mar 2026 – Present",
    "exp.desc1":
      "Leading infrastructure and network governance for mission-critical enterprise environments. Embedding risk and compliance frameworks into network architecture decisions, advising engineering leadership on high-availability project execution with regulatory alignment and operational resilience.",

    "exp.role2": "IT Infrastructure Coordinator — Networking & Data Center",
    "exp.company2": "XP Investimentos",
    "exp.period2": "Oct 2020 – Oct 2024",
    "exp.desc2":
      "Owned global infrastructure strategy for one of Brazil's largest investment platforms. Architected ultra-low latency (HFT/ULL) trading infrastructure connecting XP to B3, ICE, and Goldman Sachs. Designed active-active data center on Cisco ACI (Spine-Leaf), extended global reach via Equinix Fabric and Cloud Network Edge integrating AWS, Azure, and GCP across Brazil and the United States.",

    "exp.role3": "Senior Network Engineer III — Security & Architecture",
    "exp.company3": "IBM do Brasil",
    "exp.period3": "2018 – 2020",
    "exp.desc3":
      "Co-designed a multinational MPLS backbone PoC directly with Cisco engineering. Delivered highly available interbank financial network infrastructure in Lima, Peru — mission-critical systems for the banking sector across Latin America.",

    "exp.role4": "Senior III IP Technical Leader",
    "exp.company4": "Telefónica",
    "exp.period4": "2011 – 2017",
    "exp.desc4":
      "Architected carrier-grade MPLS solutions and mobile backhaul for Tier-1 telecom clients, driving core network modernizations that delivered up to 80% reduction in cost and project timelines.",

    // ── Certifications ──
    "certs.title": "Certifications",
    "certs.c1": "MBA CTO/CIO Executive Program",
    "certs.c1d": "FIAP · 2025 – 2026 — Strategic leadership, digital transformation, and enterprise technology governance.",
    "certs.c2": "MBA Network Architecture & Cloud Computing",
    "certs.c2d": "FIAP · 2018 – 2019 — Advanced cloud design, hybrid architectures, and infrastructure automation.",
    "certs.c3": "B.S. Computer Network Engineering",
    "certs.c3d": "2008 – 2009 — Foundation in network engineering, protocols, and systems architecture.",

    // ── Teaching ──
    "teach.title": "Teaching & Mentoring",
    "teach.method": "Methodology",
    "teach.methodDesc":
      "Lab-driven classes: short theory, long practice. Every topic is validated on a real topology, with guided troubleshooting and CLI output reading until the student reasons independently. Cisco Networking Academy instructor since 2006.",
    "teach.c1": "CCNA DevNet",
    "teach.c1d": "Automation, APIs, Python for networking and Cisco developer tooling.",
    "teach.c2": "CCNP Encor",
    "teach.c2d": "Enterprise core: routing, switching, wireless, security and automation.",
    "teach.c3": "CCIE Lab — Hands-on Sessions",
    "teach.c3d": "Dedicated lab sessions: advanced OSPF, BGP design, timed troubleshooting, and real-world scenario simulation.",

    // ── Academic (NEW) ──
    "academic.title": "Academy",
    "academic.subtitle": "Exercises, labs, and study materials for my students.",
    "academic.coming": "Materials available soon",

    // ── Projects ──
    "projects.title": "Projects",
    "projects.subtitle": "Infrastructure case studies from the world of capital markets and enterprise networking.",
    "projects.all": "View all projects",
    "projects.back": "Back to Projects",
    "projects.context": "Context & Problem",
    "projects.tech": "Technologies Used",
    "projects.solution": "Solution & Architecture",
    "projects.diagram": "Diagrams",
    "projects.results": "Results & Takeaways",
    "projects.listTitle": "All Projects",

    // ── Content ──
    "content.title": "Content & Publications",
    "content.yt": "YouTube — Josinfo",
    "content.ytd": "Technical videos on network architecture, lab walkthroughs, and infrastructure deep-dives.",
    "content.ytLink": "https://www.youtube.com/@Josinfo",
    "content.a1": "HowTo: Cisco StealthWatch",
    "content.a1d": "Practical guide to deployment and flow analysis with StealthWatch for network visibility.",
    "content.link": "Watch on YouTube",
    "content.linkSoon": "Coming soon",

    // ── Contact ──
    "contact.title": "Contact",
    "contact.desc": "For consulting, mentoring, speaking engagements, or enterprise network architecture projects.",
    "contact.name": "Name",
    "contact.email": "Email",
    "contact.message": "Message",
    "contact.send": "Send message",
    "contact.sent": "Message sent successfully.",

    // ── Footer ──
    "footer.rights": "All rights reserved.",
    "lang.label": "Language",
  },

  /* ═══════════════════════════════════════════════════════
     ESPAÑOL
     ═══════════════════════════════════════════════════════ */
  es: {
    "nav.about": "Sobre mí",
    "nav.experience": "Experiencia",
    "nav.certs": "Certificaciones",
    "nav.teaching": "Enseñanza",
    "nav.academic": "Academia",
    "nav.projects": "Proyectos",
    "nav.content": "Contenido",
    "nav.contact": "Contacto",

    "hero.badge": "estado: en línea",
    "hero.name": "Josimar Caitano",
    "hero.alias": "// じょしまる",
    "hero.role": "Principal Solutions Architect | Enterprise Networking & Cybersecurity | Mercados Financieros | Executive Technical Advisor",
    "hero.desc":
      "Donde los nanosegundos deciden quién gana y quién observa, yo diseño la infraestructura. Sistemas de trading de misión crítica, redes carrier-grade, tolerancia cero a la latencia — construido para la velocidad de los mercados de capitales.",
    "hero.cta": "Contactar",
    "hero.cta2": "Ver proyectos",

    "about.title": "Sobre mí",
    "about.p1":
      "En la Fórmula 1, una décima de segundo separa la victoria de la derrota. En los mercados de capitales, ese margen se comprime a nanosegundos — y la infraestructura que yo diseño es lo que marca la diferencia. En XP Investimentos, diseñé y entregué el backbone de trading de ultra baja latencia que conectó la mayor plataforma de inversiones de Brasil con B3, ICE y Goldman Sachs. Cada microsegundo eliminado de esa ruta se tradujo directamente en ventaja competitiva de miles de millones en volumen diario.",
    "about.p2":
      "Mi arena abarca infraestructura HFT/ULL, diseño de data centers activo-activo sobre Cisco ACI, conectividad multi-nube a través de AWS, Azure y GCP vía Equinix Fabric, y arquitecturas MPLS carrier-grade que impulsaron operadores de telecomunicaciones Tier-1. Entregué hasta un 80% de reducción en costos y plazos — no recortando esquinas, sino con ingeniería de precisión a velocidad, como un equipo de pit stop ejecutando un cambio de neumáticos en menos de dos segundos.",
    "about.p3":
      "Durante más de dos décadas he construido equipos, mentoreado ingenieros y formado talento técnico como instructor de Cisco Networking Academy desde 2006. Hoy en NTT DATA lidero la gobernanza de infraestructura para entornos empresariales donde el cumplimiento y la resiliencia son innegociables. Mi trayectoria no es una escalera corporativa — es una línea de carrera: cada ápice calculado, cada recta maximizada, cada decisión diseñada para la velocidad.",

    "exp.title": "Experiencia Profesional",
    "exp.current": "actual",

    "exp.role1": "Coordinador de Gobernanza de Infraestructura y Seguridad",
    "exp.company1": "NTT DATA",
    "exp.period1": "Mar 2026 – Presente",
    "exp.desc1":
      "Liderando la gobernanza de infraestructura y redes para entornos empresariales de misión crítica. Integrando marcos de riesgo y cumplimiento en decisiones de arquitectura de red, asesorando al liderazgo de ingeniería en la ejecución de proyectos de alta disponibilidad.",

    "exp.role2": "Coordinador de Infraestructura TI — Networking y Data Center",
    "exp.company2": "XP Investimentos",
    "exp.period2": "Oct 2020 – Oct 2024",
    "exp.desc2":
      "Estrategia global de infraestructura para una de las mayores plataformas de inversión de Brasil. Arquitectura de trading de ultra baja latencia (HFT/ULL) conectando XP a B3, ICE y Goldman Sachs. Data center activo-activo sobre Cisco ACI, conectividad global vía Equinix Fabric integrando AWS, Azure y GCP.",

    "exp.role3": "Ingeniero Senior de Redes III — Seguridad y Arquitectura",
    "exp.company3": "IBM do Brasil",
    "exp.period3": "2018 – 2020",
    "exp.desc3":
      "Co-diseño de PoC de backbone MPLS multinacional directamente con ingeniería de Cisco. Entrega de infraestructura de red financiera interbancaria de alta disponibilidad en Lima, Perú.",

    "exp.role4": "Líder Técnico IP Senior III",
    "exp.company4": "Telefónica",
    "exp.period4": "2011 – 2017",
    "exp.desc4":
      "Arquitectura de soluciones MPLS carrier-grade y mobile backhaul para clientes de telecomunicaciones Tier-1, impulsando modernizaciones que entregaron hasta un 80% de reducción en costos y plazos.",

    "certs.title": "Certificaciones",
    "certs.c1": "MBA CTO/CIO Executive Program",
    "certs.c1d": "FIAP · 2025 – 2026 — Liderazgo estratégico, transformación digital y gobernanza tecnológica empresarial.",
    "certs.c2": "MBA Arquitectura de Redes y Cloud Computing",
    "certs.c2d": "FIAP · 2018 – 2019 — Diseño cloud avanzado, arquitecturas híbridas y automatización de infraestructura.",
    "certs.c3": "Ingeniería en Redes de Computadores",
    "certs.c3d": "2008 – 2009 — Fundamentos de ingeniería de redes, protocolos y arquitectura de sistemas.",

    "teach.title": "Enseñanza y Mentoría",
    "teach.method": "Metodología",
    "teach.methodDesc":
      "Clases orientadas a laboratorio: teoría breve, práctica extensa. Cada tema se valida en topología real, con troubleshooting guiado y lectura de CLI hasta que el alumno razone por sí mismo. Instructor de Cisco Networking Academy desde 2006.",
    "teach.c1": "CCNA DevNet",
    "teach.c1d": "Automatización, APIs, Python aplicado a redes y herramientas de desarrollador Cisco.",
    "teach.c2": "CCNP Encor",
    "teach.c2d": "Núcleo enterprise: routing, switching, wireless, seguridad y automatización.",
    "teach.c3": "CCIE Lab — Sesiones Prácticas",
    "teach.c3d": "Sesiones dedicadas de laboratorio: OSPF avanzado, diseño BGP, troubleshooting cronometrado y simulación de escenarios reales.",

    "academic.title": "Academia",
    "academic.subtitle": "Ejercicios, laboratorios y materiales de estudio para mis alumnos.",
    "academic.coming": "Materiales disponibles pronto",

    "projects.title": "Proyectos",
    "projects.subtitle": "Casos de estudio de infraestructura del mundo de los mercados de capitales y networking empresarial.",
    "projects.all": "Ver todos los proyectos",
    "projects.back": "Volver a Proyectos",
    "projects.context": "Contexto y Problema",
    "projects.tech": "Tecnologías Utilizadas",
    "projects.solution": "Solución y Arquitectura",
    "projects.diagram": "Diagramas",
    "projects.results": "Resultados y Aprendizajes",
    "projects.listTitle": "Todos los Proyectos",

    "content.title": "Contenido y Publicaciones",
    "content.yt": "YouTube — Josinfo",
    "content.ytd": "Videos técnicos sobre arquitectura de redes, walkthroughs de laboratorio e inmersiones en infraestructura.",
    "content.ytLink": "https://www.youtube.com/@Josinfo",
    "content.a1": "HowTo: Cisco StealthWatch",
    "content.a1d": "Guía práctica de implementación y análisis de flujos con StealthWatch para visibilidad de red.",
    "content.link": "Ver en YouTube",
    "content.linkSoon": "Próximamente",

    "contact.title": "Contacto",
    "contact.desc": "Para consultoría, mentoría, conferencias o proyectos de arquitectura de redes empresariales.",
    "contact.name": "Nombre",
    "contact.email": "Correo electrónico",
    "contact.message": "Mensaje",
    "contact.send": "Enviar mensaje",
    "contact.sent": "Mensaje enviado con éxito.",

    "footer.rights": "Todos los derechos reservados.",
    "lang.label": "Idioma",
  },

  /* ═══════════════════════════════════════════════════════
     PORTUGUÊS
     ═══════════════════════════════════════════════════════ */
  pt: {
    "nav.about": "Sobre",
    "nav.experience": "Experiência",
    "nav.certs": "Certificações",
    "nav.teaching": "Ensino",
    "nav.academic": "Academia",
    "nav.projects": "Projetos",
    "nav.content": "Conteúdo",
    "nav.contact": "Contato",

    "hero.badge": "status: online",
    "hero.name": "Josimar Caitano",
    "hero.alias": "// じょしまる",
    "hero.role": "Principal Solutions Architect | Enterprise Networking & Cybersecurity | Mercado Financeiro | Executive Technical Advisor",
    "hero.desc":
      "Onde nanosegundos decidem quem vence e quem observa, eu projeto a infraestrutura. Sistemas de trading de missão crítica, redes carrier-grade, tolerância zero à latência — construído para a velocidade dos mercados de capitais.",
    "hero.cta": "Falar comigo",
    "hero.cta2": "Ver projetos",

    "about.title": "Sobre",
    "about.p1":
      "Na Fórmula 1, um décimo de segundo separa vitória de derrota. Nos mercados de capitais, essa margem se comprime a nanosegundos — e a infraestrutura que eu projeto é o que faz a diferença. Na XP Investimentos, desenhei e entreguei o backbone de trading de ultra baixa latência conectando a maior plataforma de investimentos do Brasil à B3, ICE e Goldman Sachs. Cada microssegundo eliminado daquele caminho se traduziu diretamente em vantagem competitiva de bilhões em volume diário.",
    "about.p2":
      "Minha arena abrange infraestrutura HFT/ULL, design de data centers active-active sobre Cisco ACI, conectividade multi-cloud via AWS, Azure e GCP através do Equinix Fabric, e arquiteturas MPLS carrier-grade que sustentaram operadoras de telecomunicações Tier-1. Entreguei até 80% de redução em custos e prazos de projetos — não cortando atalhos, mas com engenharia de precisão em velocidade, como uma equipe de pit stop executando troca de pneus em menos de dois segundos.",
    "about.p3":
      "Por mais de duas décadas venho construindo equipes, mentorando engenheiros e formando talentos técnicos como instrutor da Cisco Networking Academy desde 2006. Hoje na NTT DATA lidero a governança de infraestrutura para ambientes corporativos onde compliance e resiliência são inegociáveis. Minha trajetória não é uma escada corporativa — é uma linha de corrida: cada ápice calculado, cada reta maximizada, cada decisão projetada para velocidade.",

    "exp.title": "Experiência Profissional",
    "exp.current": "atual",

    "exp.role1": "Coordenador de Governança de Infraestrutura e Segurança",
    "exp.company1": "NTT DATA",
    "exp.period1": "Mar 2026 – Presente",
    "exp.desc1":
      "Liderança de governança de infraestrutura e redes para ambientes corporativos de missão crítica. Integrando frameworks de risco e compliance em decisões de arquitetura de rede, assessorando liderança de engenharia na execução de projetos de alta disponibilidade com alinhamento regulatório e resiliência operacional.",

    "exp.role2": "Coordenador de Infraestrutura de TI — Networking & Data Center",
    "exp.company2": "XP Investimentos",
    "exp.period2": "Out 2020 – Out 2024",
    "exp.desc2":
      "Estratégia global de infraestrutura para uma das maiores plataformas de investimentos do Brasil. Arquitetura de trading de ultra baixa latência (HFT/ULL) conectando XP à B3, ICE e Goldman Sachs. Data center active-active sobre Cisco ACI (Spine-Leaf), alcance global via Equinix Fabric e Cloud Network Edge integrando AWS, Azure e GCP entre Brasil e Estados Unidos.",

    "exp.role3": "Engenheiro de Redes Senior III — Segurança & Arquitetura",
    "exp.company3": "IBM do Brasil",
    "exp.period3": "2018 – 2020",
    "exp.desc3":
      "Co-design de PoC de backbone MPLS multinacional diretamente com a engenharia da Cisco. Entrega de infraestrutura de rede financeira interbancária de alta disponibilidade em Lima, Peru — sistemas de missão crítica para o setor bancário na América Latina.",

    "exp.role4": "Líder Técnico IP Senior III",
    "exp.company4": "Telefónica",
    "exp.period4": "2011 – 2017",
    "exp.desc4":
      "Arquitetura de soluções MPLS carrier-grade e mobile backhaul para clientes de telecomunicações Tier-1, impulsionando modernizações que entregaram até 80% de redução em custos e prazos de projetos.",

    "certs.title": "Certificações",
    "certs.c1": "MBA CTO/CIO Executive Program",
    "certs.c1d": "FIAP · 2025 – 2026 — Liderança estratégica, transformação digital e governança tecnológica empresarial.",
    "certs.c2": "MBA Arquitetura de Redes e Cloud Computing",
    "certs.c2d": "FIAP · 2018 – 2019 — Design cloud avançado, arquiteturas híbridas e automação de infraestrutura.",
    "certs.c3": "Engenharia de Redes de Computadores",
    "certs.c3d": "2008 – 2009 — Fundamentos de engenharia de redes, protocolos e arquitetura de sistemas.",

    "teach.title": "Ensino & Mentoria",
    "teach.method": "Metodologia",
    "teach.methodDesc":
      "Aulas orientadas a laboratório: teoria curta, prática longa. Cada tópico é validado em topologia real, com troubleshooting guiado e leitura de saídas de CLI até o aluno raciocinar sozinho. Instrutor da Cisco Networking Academy desde 2006.",
    "teach.c1": "CCNA DevNet",
    "teach.c1d": "Automação, APIs, Python aplicado a redes e ferramentas de desenvolvedor Cisco.",
    "teach.c2": "CCNP Encor",
    "teach.c2d": "Núcleo enterprise: roteamento, switching, wireless, segurança e automação.",
    "teach.c3": "CCIE Lab — Sessões Práticas",
    "teach.c3d": "Sessões dedicadas de laboratório: OSPF avançado, design BGP, troubleshooting sob tempo e simulação de cenários reais.",

    "academic.title": "Academia",
    "academic.subtitle": "Exercícios, laboratórios e materiais de estudo para meus alunos.",
    "academic.coming": "Materiais disponíveis em breve",

    "projects.title": "Projetos",
    "projects.subtitle": "Estudos de caso de infraestrutura do mundo dos mercados de capitais e redes corporativas.",
    "projects.all": "Ver todos os projetos",
    "projects.back": "Voltar para Projetos",
    "projects.context": "Contexto & Problema",
    "projects.tech": "Tecnologias Utilizadas",
    "projects.solution": "Solução & Arquitetura",
    "projects.diagram": "Diagramas",
    "projects.results": "Resultados & Aprendizados",
    "projects.listTitle": "Todos os Projetos",

    "content.title": "Conteúdo & Publicações",
    "content.yt": "YouTube — Josinfo",
    "content.ytd": "Vídeos técnicos sobre arquitetura de redes, walkthroughs de laboratório e deep-dives em infraestrutura.",
    "content.ytLink": "https://www.youtube.com/@Josinfo",
    "content.a1": "HowTo: Cisco StealthWatch",
    "content.a1d": "Guia prático de implantação e análise de fluxos com StealthWatch para visibilidade de rede.",
    "content.link": "Assistir no YouTube",
    "content.linkSoon": "Em breve",

    "contact.title": "Contato",
    "contact.desc": "Para consultoria, mentoria, palestras ou projetos de arquitetura de redes corporativas.",
    "contact.name": "Nome",
    "contact.email": "E-mail",
    "contact.message": "Mensagem",
    "contact.send": "Enviar mensagem",
    "contact.sent": "Mensagem enviada com sucesso.",

    "footer.rights": "Todos os direitos reservados.",
    "lang.label": "Idioma",
  },
};

export function LanguageProvider({ children }: { children: ReactNode }) {
  const [lang, setLang] = useState<Lang>("en");
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
