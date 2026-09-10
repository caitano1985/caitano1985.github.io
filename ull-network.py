from pathlib import Path
import re
import shutil
from datetime import datetime

ROOT = Path(__file__).resolve().parent

IGNORE_DIRS = {
    ".git",
    "node_modules",
    "dist",
    ".output",
    ".tanstack",
    ".nitro",
    "coverage",
}

TEXT_EXTENSIONS = {
    ".ts",
    ".tsx",
    ".js",
    ".jsx",
    ".json",
    ".html",
    ".css",
    ".md",
    ".yaml",
    ".yml",
    ".toml",
    ".txt",
}

OLD_PATH = "/ull-arena/index.html"

GITHUB_PATH = (
    "https://github.com/caitano1985/"
    "caitano1985.github.io/blob/main/public/ull-arena/index.html"
)


def ignored(path):
    return any(part in IGNORE_DIRS for part in path.parts)


print("=" * 80)
print("🔥 ULL ARENA — LOCALIZAR E CORRIGIR REFERÊNCIA FANTASMA")
print("=" * 80)

matches = []

# ----------------------------------------------------------------------
# 1. Procurar TODAS as referências a ULL Arena
# ----------------------------------------------------------------------

print("\n[1/3] 🔎 Procurando referências a 'ull-arena'...\n")

for path in ROOT.rglob("*"):

    if not path.is_file():
        continue

    if ignored(path):
        continue

    if path.suffix.lower() not in TEXT_EXTENSIONS:
        continue

    try:
        text = path.read_text(
            encoding="utf-8",
            errors="ignore"
        )
    except Exception:
        continue

    for line_number, line in enumerate(text.splitlines(), start=1):

        if "ull-arena" in line.lower():

            matches.append(
                (
                    path,
                    line_number,
                    line
                )
            )


if not matches:

    print("⚠️ Nenhuma referência 'ull-arena' encontrada.")
else:

    for path, line_number, line in matches:

        print("-" * 80)
        print(f"ARQUIVO : {path.relative_to(ROOT)}")
        print(f"LINHA   : {line_number}")
        print(f"CONTEÚDO: {line.strip()}")


# ----------------------------------------------------------------------
# 2. Procurar especificamente o caminho que causa o erro
# ----------------------------------------------------------------------

print("\n")
print("=" * 80)
print("[2/3] 🎯 Procurando '/ull-arena/index.html'")
print("=" * 80)

found_bad_reference = False
changed_files = []

for path in ROOT.rglob("*"):

    if not path.is_file():
        continue

    if ignored(path):
        continue

    if path.suffix.lower() not in TEXT_EXTENSIONS:
        continue

    try:
        original = path.read_text(
            encoding="utf-8",
            errors="ignore"
        )
    except Exception:
        continue

    if OLD_PATH not in original:
        continue

    found_bad_reference = True

    print(f"\n🚨 REFERÊNCIA ENCONTRADA:")
    print(path.relative_to(ROOT))

    # Backup
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    backup = path.with_name(
        f"{path.stem}.backup_{timestamp}{path.suffix}"
    )

    shutil.copy2(path, backup)

    print(f"🛡️ Backup: {backup.name}")

    # --------------------------------------------------------------
    # Caso 1:
    # href="/ull-arena/index.html"
    # --------------------------------------------------------------

    new_text = original.replace(
        '"'+OLD_PATH+'"',
        '"'+GITHUB_PATH+'"'
    )

    new_text = new_text.replace(
        "'"+OLD_PATH+"'",
        "'"+GITHUB_PATH+"'"
    )

    # --------------------------------------------------------------
    # Caso 2:
    # href: "/ull-arena/index.html"
    # --------------------------------------------------------------

    new_text = new_text.replace(
        f'href: "{OLD_PATH}"',
        f'href: "{GITHUB_PATH}"'
    )

    new_text = new_text.replace(
        f"href: '{OLD_PATH}'",
        f"href: '{GITHUB_PATH}'"
    )

    # --------------------------------------------------------------
    # Caso 3:
    # qualquer string contendo o caminho
    # --------------------------------------------------------------

    new_text = re.sub(
        re.escape(OLD_PATH),
        GITHUB_PATH,
        new_text
    )

    if new_text != original:

        path.write_text(
            new_text,
            encoding="utf-8"
        )

        changed_files.append(path)

        print("✅ REFERÊNCIA CORRIGIDA")

    else:

        print(
            "⚠️ A referência foi encontrada, "
            "mas não foi possível alterar automaticamente."
        )


# ----------------------------------------------------------------------
# 3. Resultado
# ----------------------------------------------------------------------

print("\n")
print("=" * 80)
print("[3/3] 📊 RESULTADO")
print("=" * 80)

if changed_files:

    print("\n🔥 ARQUIVOS ALTERADOS:")

    for path in changed_files:
        print(
            "   ✅",
            path.relative_to(ROOT)
        )

    print("\nA referência problemática agora aponta para:")

    print(GITHUB_PATH)

    print("\n")
    print("=" * 80)
    print("🛑 NÃO FOI FEITO COMMIT")
    print("🛑 NÃO FOI FEITO PUSH")
    print("🛑 vite.config.ts NÃO FOI ALTERADO")
    print("=" * 80)

elif found_bad_reference:

    print("\n⚠️ Encontramos a referência, mas nenhuma alteração foi aplicada.")

else:

    print("""
✅ A referência '/ull-arena/index.html' NÃO EXISTE MAIS.

Isso significa que o problema específico já foi removido do código-fonte.

Agora precisamos verificar o build/prerender.
""")

print("\n")
print("Próximo comando:")
print("    npm run build")
print()
