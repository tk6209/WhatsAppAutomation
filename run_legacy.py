import os
import sys
import subprocess

LEGACY_FOLDER = "legacy"

def listar_scripts():
    arquivos = [f for f in os.listdir(LEGACY_FOLDER) if f.endswith(".py")]
    return arquivos

def exibir_opcoes(scripts):
    print("\n📜 Scripts disponíveis em /legacy:")
    for i, script in enumerate(scripts, 1):
        print(f"{i}. {script}")

def escolher_script(scripts):
    try:
        escolha = int(input("\nDigite o número do script que deseja executar: "))
        if 1 <= escolha <= len(scripts):
            return scripts[escolha - 1]
        else:
            print("❌ Escolha inválida.")
            return None
    except ValueError:
        print("❌ Entrada inválida.")
        return None

def executar_script(script):
    caminho = os.path.join(LEGACY_FOLDER, script)
    print(f"\n▶️ Executando: {script}\n{'-'*40}")
    subprocess.run(["python", caminho])

def main():
    if not os.path.exists(LEGACY_FOLDER):
        print("❌ Pasta 'legacy' não encontrada.")
        return

    scripts = listar_scripts()
    if not scripts:
        print("❌ Nenhum script .py encontrado na pasta legacy.")
        return

    exibir_opcoes(scripts)
    script_escolhido = escolher_script(scripts)

    if script_escolhido:
        executar_script(script_escolhido)

if __name__ == "__main__":
    main()
