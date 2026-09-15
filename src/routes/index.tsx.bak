import { createFileRoute, Link } from "@tanstack/react-router";
import { useState, type FormEvent } from "react";
import portrait from "@/assets/portrait.jpg";
import { ProjectCard } from "@/components/ProjectCard";
import { projects } from "@/data/projects";
import { useI18n } from "@/lib/i18n";





export const Route = createFileRoute("/")({
  head: () => ({
    meta: [
      { title: "Josimar Caitano — Principal Solutions Architect | Capital Markets & Enterprise Infrastructure" },
      {
        name: "description",
        content:
          "Mission-critical network architect specializing in ultra-low latency (ULL/HFT) trading infrastructure, multi-cloud connectivity, and enterprise security governance for capital markets.",
      },
      { property: "og:title", content: "Josimar Caitano — Principal Solutions Architect | Capital Markets" },
      {
        property: "og:description",
        content:
          "Architecting ultra-low latency infrastructure for the world's fastest financial markets. Enterprise networking, cybersecurity, and technical leadership.",
      },
      { property: "og:type", content: "profile" },
      { name: "twitter:card", content: "summary_large_image" },
    ],
  }),
  component: Home,
});

function SectionHead({ label, title }: { label: string; title: string }) {
  return (
    <div className="mb-8">
      <p className="mono-label">{label}</p>
      <h2 className="mt-2 text-2xl font-bold sm:text-3xl">{title}</h2>
    </div>
  );
}

function Home() {
  const { t, lang } = useI18n();
  const [sent, setSent] = useState(false);
  const [sending, setSending] = useState(false);

  const experiences = [
    { role: "exp.role1", company: "exp.company1", period: "exp.period1", desc: "exp.desc1", current: true },
    { role: "exp.role2", company: "exp.company2", period: "exp.period2", desc: "exp.desc2", current: false },
    { role: "exp.role3", company: "exp.company3", period: "exp.period3", desc: "exp.desc3", current: false },
    { role: "exp.role4", company: "exp.company4", period: "exp.period4", desc: "exp.desc4", current: false },
  ];

  const courses: [string, string][] = [
    ["teach.c1", "teach.c1d"],
    ["teach.c2", "teach.c2d"],
    ["teach.c3", "teach.c3d"],
  ];

  const contents: [string, string, string, string][] = [
    ["content.yt", "content.ytd", "youtube", "content.ytLink"],
    ["content.a1", "content.a1d", "article", ""],
  ];

  const onSubmit = async (e: FormEvent) => {
    e.preventDefault();
    setSending(true);
    try {
      const form = e.target as HTMLFormElement;
      const data = new FormData(form);
      const res = await fetch("https://formspree.io/f/xeogrgvp", {
        method: "POST", body: data, headers: { Accept: "application/json" },
      });
      if (res.ok) { setSent(true); form.reset(); }
    } catch { /* silent */ } finally { setSending(false); }
  };

  return (
    <main>
      {/* HERO */}
      <section className="relative overflow-hidden border-b border-border">
        <div className="grid-bg absolute inset-0 opacity-40" aria-hidden />
        <div
          className="absolute inset-0"
          aria-hidden
          style={{
            background:
              "radial-gradient(70% 60% at 20% 0%, color-mix(in oklab, var(--primary) 8%, transparent), transparent 70%)",
          }}
        />
        <div className="relative mx-auto grid max-w-6xl items-center gap-10 px-5 py-20 md:grid-cols-[1.3fr_1fr] md:py-28">
          <div>
            <span className="inline-flex items-center gap-2 rounded-full border border-border bg-surface px-3 py-1 font-mono text-[11px] text-muted-foreground">
              <span className="h-1.5 w-1.5 animate-pulse rounded-full bg-primary" />
              {t("hero.badge")}
            </span>
            <h1 className="mt-5 text-4xl font-bold leading-tight sm:text-5xl">
              {t("hero.name")}
              <span className="block font-mono text-xl text-primary sm:text-2xl">{t("hero.alias")}</span>
            </h1>
            <p className="mt-4 max-w-xl font-mono text-sm text-primary sm:text-base">
              {t("hero.role")}
            </p>
            <p className="mt-4 max-w-xl leading-relaxed text-muted-foreground">{t("hero.desc")}</p>
            <div className="mt-8 flex flex-wrap gap-3">
              <a
                href="#contato"
                className="glow-ring rounded-md bg-primary px-5 py-2.5 text-sm font-semibold text-primary-foreground transition-transform hover:-translate-y-0.5"
              >
                {t("hero.cta")}
              </a>
              <a
                href="#projetos"
                className="rounded-md border border-border px-5 py-2.5 text-sm font-semibold transition-colors hover:border-primary hover:text-primary"
              >
                {t("hero.cta2")}
              </a>
            </div>
            <div className="mt-6 flex gap-4 font-mono text-xs text-muted-foreground">
              <a href="https://www.linkedin.com/in/josimar-caitano/" target="_blank" rel="noopener noreferrer" className="hover:text-primary">
                linkedin/josimar-caitano
              </a>
              <a href="https://www.youtube.com/@Josinfo" target="_blank" rel="noopener noreferrer" className="hover:text-primary">
                youtube/@Josinfo
              </a>
            </div>
          </div>

          <figure className="relative mx-auto w-full max-w-xs">
            <img
              src={portrait}
              alt="Josimar Caitano"
              width={1024}
              height={1024}
              className="w-full rounded-2xl border border-border object-cover"
            />
            {/* photo caption removed */}
          </figure>
        </div>
      </section>

      {/* ABOUT */}
      <section id="about" className="mx-auto max-w-6xl px-5 py-20">
        <SectionHead label="./about" title={t("about.title")} />
        <div className="grid gap-5 text-muted-foreground md:grid-cols-3">
          <p className="leading-relaxed">{t("about.p1")}</p>
          <p className="leading-relaxed">{t("about.p2")}</p>
          <p className="leading-relaxed">{t("about.p3")}</p>
        </div>
      </section>

      {/* EXPERIENCE */}
      <section id="experiencia" className="border-y border-border bg-surface/40">
        <div className="mx-auto max-w-6xl px-5 py-20">
          <SectionHead label="./experience" title={t("exp.title")} />
          <ol className="relative space-y-6 border-l border-border pl-6">
            {experiences.map((exp) => (
              <li key={exp.role} className="relative">
                <span
                  className={`absolute -left-[1.7rem] top-2 h-2.5 w-2.5 rounded-full ${
                    exp.current ? "bg-neon" : "bg-border"
                  }`}
                />
                <div className="rounded-xl border border-border bg-card p-5">
                  <div className="flex flex-wrap items-center gap-2">
                    <h3 className="font-semibold">{t(exp.role)}</h3>
                    {exp.current && (
                      <span className="rounded border border-neon/50 px-2 py-0.5 font-mono text-[10px] uppercase text-neon">
                        {t("exp.current")}
                      </span>
                    )}
                  </div>
                  <p className="mt-1 font-mono text-xs text-primary">
                    {t(exp.company)} · {t(exp.period)}
                  </p>
                  <p className="mt-3 text-sm leading-relaxed text-muted-foreground">{t(exp.desc)}</p>
                </div>
              </li>
            ))}
          </ol>
        </div>
      </section>

      {/* CERTIFICATIONS */}
      <section id="certificacoes" className="mx-auto max-w-6xl px-5 py-20">
        <SectionHead label="./certifications" title={t("certs.title")} />
        <div className="grid gap-5 md:grid-cols-3">
          {(["c1", "c2", "c3"] as const).map((key, i) => (
            <div key={key} className={`rounded-xl border bg-card p-6 ${i === 0 ? "glow-ring border-primary/40" : "border-border"}`}>
              <p className={`font-mono text-sm font-semibold ${i === 0 ? "text-primary" : "text-muted-foreground"}`}>{t(`certs.${key}`)}</p>
              <p className="mt-3 text-sm text-muted-foreground">{t(`certs.${key}d`)}</p>
            </div>
          ))}
        </div>
      </section>

      {/* TEACHING */}
      <section id="ensino" className="border-y border-border bg-surface/40">
        <div className="mx-auto max-w-6xl px-5 py-20">
          <SectionHead label="./teaching" title={t("teach.title")} />
          <div className="grid gap-5 md:grid-cols-3">
            {courses.map(([title, desc]) => (
              <div key={title} className="card-hover rounded-xl border border-border bg-card p-6">
                <h3 className="font-semibold text-primary">{t(title)}</h3>
                <p className="mt-3 text-sm leading-relaxed text-muted-foreground">{t(desc)}</p>
              </div>
            ))}
          </div>
          <div className="mt-6 rounded-xl border border-border bg-card p-6">
            <p className="mono-label">{t("teach.method")}</p>
            <p className="mt-3 leading-relaxed text-muted-foreground">{t("teach.methodDesc")}</p>
          </div>
        </div>
      </section>

      {/* ACADEMY */}
      <section id="academia" className="mx-auto max-w-6xl px-5 py-20">
        <SectionHead label="./academy" title={t("academic.title")} />
        <p className="-mt-4 mb-8 text-muted-foreground">{t("academic.subtitle")}</p>
        <div className="rounded-xl border border-dashed border-border bg-card/50 p-8 text-center">
          <p className="font-mono text-sm text-muted-foreground">{t("academic.coming")}</p>
        </div>
      </section>

      {/* PROJECTS */}
      <section id="projetos" className="mx-auto max-w-6xl px-5 py-20">
        <SectionHead label="./projects" title={t("projects.title")} />
        <p className="-mt-4 mb-8 text-muted-foreground">{t("projects.subtitle")}</p>
        <div className="grid gap-6 sm:grid-cols-2">
          {projects.map((p) => (
            <ProjectCard key={p.slug} project={p} />
          ))}
        </div>
        <Link
          to="/projetos"
          className="mt-8 inline-block font-mono text-sm text-primary hover:underline"
        >
          {t("projects.all")} →
        </Link>
      </section>

      {/* CONTENT */}
      <section id="conteudo" className="border-y border-border bg-surface/40">
        <div className="mx-auto max-w-6xl px-5 py-20">
          <SectionHead label="./content" title={t("content.title")} />
          <div className="grid gap-5 sm:grid-cols-2">
            {contents.map(([title, desc, kind, link]) => (
              <div key={title} className="card-hover rounded-xl border border-border bg-card p-6">
                <span className="font-mono text-[11px] uppercase tracking-widest text-neon">{kind}</span>
                <h3 className="mt-2 font-semibold">{t(title)}</h3>
                <p className="mt-2 text-sm leading-relaxed text-muted-foreground">{t(desc)}</p>
                {link ? (
                  <a href={t(link)} target="_blank" rel="noopener noreferrer" className="mt-4 inline-block font-mono text-xs text-primary hover:underline">{t("content.link")} →</a>
                ) : (
                  <span className="mt-4 inline-block font-mono text-xs text-muted-foreground">{t("content.linkSoon")}</span>
                )}
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CONTACT */}
      <section id="contato" className="mx-auto max-w-6xl px-5 py-20">
        <SectionHead label="./contact" title={t("contact.title")} />
        <div className="grid gap-10 md:grid-cols-2">
          <div>
            <p className="leading-relaxed text-muted-foreground">{t("contact.desc")}</p>
            <ul className="mt-6 space-y-3 font-mono text-sm">
              <li>
                <span className="text-muted-foreground">email:</span>{" "}
                <a href="mailto:josimaru@gmail.com" className="text-primary hover:underline">josimaru@gmail.com</a>
              </li>
              <li>
                <span className="text-muted-foreground">linkedin:</span>{" "}
                <a href="https://www.linkedin.com/in/josimar-caitano/" target="_blank" rel="noopener noreferrer" className="text-primary hover:underline">/in/josimar-caitano</a>
              </li>
              <li>
                <span className="text-muted-foreground">youtube:</span>{" "}
                <a href="https://www.youtube.com/@Josinfo" target="_blank" rel="noopener noreferrer" className="text-primary hover:underline">/@Josinfo</a>
              </li>
            </ul>
          </div>

          <form onSubmit={onSubmit} className="rounded-xl border border-border bg-card p-6">
            <label className="block font-mono text-xs text-muted-foreground" htmlFor="nome">
              {t("contact.name")}
            </label>
            <input
              id="nome"
              name="name"
              required
              className="mt-1 w-full rounded-md border border-input bg-background px-3 py-2 text-sm outline-none focus:border-primary"
            />
            <label
              className="mt-4 block font-mono text-xs text-muted-foreground"
              htmlFor="email"
            >
              {t("contact.email")}
            </label>
            <input
              id="email"
              name="email"
              type="email"
              required
              className="mt-1 w-full rounded-md border border-input bg-background px-3 py-2 text-sm outline-none focus:border-primary"
            />
            <label
              className="mt-4 block font-mono text-xs text-muted-foreground"
              htmlFor="mensagem"
            >
              {t("contact.message")}
            </label>
            <textarea
              id="mensagem"
              name="message"
              rows={4}
              required
              className="mt-1 w-full rounded-md border border-input bg-background px-3 py-2 text-sm outline-none focus:border-primary"
            />
            <button
              type="submit"
              disabled={sending || sent}
              className="mt-5 w-full rounded-md bg-primary px-4 py-2.5 text-sm font-semibold text-primary-foreground transition-opacity hover:opacity-90 disabled:opacity-60"
            >
              {sending ? "Sending..." : sent ? "✓ Sent" : t("contact.send")}
            </button>
            {sent && (
              <p className="mt-3 font-mono text-xs text-primary">{t("contact.sent")}</p>
            )}
          </form>
        </div>
        <p className="sr-only">{lang}</p>
      </section>
    </main>
  );
}
