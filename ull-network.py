import subprocess
import sys

def executar_comando(comando):
    """Executa um comando no terminal e lida com possíveis falhas."""
    print(f"\n⚡ Executando: {comando}")
    try:
        resultado = subprocess.run(comando, shell=True, check=True, text=True, capture_output=True)
        print(resultado.stdout)
    except subprocess.CalledProcessError as erro:
        print(f"❌ Falha crítica ao executar: {comando}")
        print(erro.stderr)
        sys.exit(1)

def iniciar_deploy():
    """Gerencia o ciclo de vida do versionamento."""
    print("🔥 Iniciando protocolo de deploy para a ULL Arena...\n")
    
    # 1. Verifica o status atual
    executar_comando("git status")
    
    # 2. Adiciona todos os arquivos modificados
    executar_comando("git add .")
    
    # 3. Solicita a mensagem de commit
    mensagem = input("💬 Digite a mensagem do commit (ex: feat: adiciona card): ")
    if not mensagem.strip():
        print("⚠️ Nenhuma mensagem fornecida. Operação abortada para manter a governança do código.")
        sys.exit(1)
        
    executar_comando(f'git commit -m "{mensagem}"')
    
    # 4. Envia para o GitHub
    executar_comando("git push")
    
    print("\n✅ Deploy concluído com sucesso! A infraestrutura está na nuvem.")

if __name__ == "__main__":
    iniciar_deploy()
