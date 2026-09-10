import subprocess
import sys

def executar(comando):
    print(f"\n[RODANDO] {comando}")
    # Captura a saída do comando para vermos o erro real
    processo = subprocess.run(comando, shell=True, capture_output=True, text=True)
    
    if processo.stdout:
        print(process.stdout)
    if processo.stderr:
        print(">>> LOG DE ERRO/AVISO:")
        print(process.stderr)
        
    return processo.returncode

def main():
    print("Iniciando diagnóstico da vitrine...")
    
    # Executa o build local para forçar o erro a aparecer na tela
    codigo_build = executar("bun run build")
    
    if codigo_build != 0:
        print("\n❌ FALHA NO BUILD: O script parou porque encontrou o erro que está travando o GitHub.")
        print("Copie todos os logs acima e mande no chat.")
        sys.exit(1)
        
    print("\n✅ BUILD COM SUCESSO! Não há erros no código.")
    print("Iniciando deploy automático...")
    executar("git add -A")
    executar('git commit -m "fix: correcoes finais para ULL Arena"')
    executar("git push")

if __name__ == "__main__":
    main()
