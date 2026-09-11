import { useI18n } from "@/lib/i18n";

export function SiteFooter() {
  const { t } = useI18n();
  return (
    <footer className="border-t border-border bg-surface/40">
      <div className="mx-auto flex max-w-6xl flex-col gap-2 px-5 py-8 text-sm text-muted-foreground sm:flex-row sm:items-center sm:justify-between">
        <span className="font-mono text-xs">
          Josimar Caitano // じょしまる
        </span>
        <span className="text-xs">
          © {new Date().getFullYear()} Josimar Caitano. {t("footer.rights")}
        </span>
      </div>
    </footer>
  );
}
