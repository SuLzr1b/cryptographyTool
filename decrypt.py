# WARNING: This project is for educational purposes only. Do not encrypt files without explicit permission. Always back up files before testing!

import os
from cryptography.fernet import Fernet

def carregar_chave():
    if not os.path.exists("chave.key"):
        print("Não existe chave.key")
        return None
    
    with open("chave.key", "rb") as arquivo_chave:
        return arquivo_chave.read()

def descriptografar_arquivo(caminho_arquivo, fernet):
    with open(caminho_arquivo, "rb") as arquivo:
        dados_criptografados = arquivo.read()

    dados_descriptografados = fernet.decrypt(dados_criptografados)

    with open(caminho_arquivo, "wb") as arquivo:
        arquivo.write(dados_descriptografados)

    print(f"arquivo '{caminho_arquivo}' foi descriptografado")

def descriptografar_pastas_subpastas(caminho_pasta, chave):
    fernet = Fernet(chave)
    arquivos_descriptografados = 0
    for root, _, files in os.walk(caminho_pasta):
        for nome_arquivo in files:
            if nome_arquivo.lower().endswith(".txt"):
                caminho_completo = os.path.join(root, nome_arquivo)
                try:
                    descriptografar_arquivo(caminho_completo, fernet)
                    arquivos_descriptografados += 1
                except Exception as e:
                    print(f"Erro ao descriptografar '{caminho_completo}': {e}")

    if arquivos_descriptografados == 0:
        print("Nenhum arquivo .txt encontrado na pasta ou subpastas.")
    else:
        print(f"\nTotal de arquivos .txt criptografados: {arquivos_descriptografados}")

def main():
    caminho_pasta = input("Digite o caminho completo da pasta com arquivos .txt criptografados: ")

    if not os.path.isdir(caminho_pasta):
        print("pasta invalida")
        return
    
    chave = carregar_chave()
    if chave is None:
        return

    descriptografar_pastas_subpastas(caminho_pasta, chave)

if __name__ == "__main__":
    main()


# Reminder: Use this code only for learning in controlled environments. Respect laws, such as Brazil's LGPD!
