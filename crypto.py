# WARNING: This project is for educational purposes only. Do not encrypt files without explicit permission. Always back up files before testing!

import os
from cryptography.fernet import Fernet

def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as arquivo_chave:
        arquivo_chave.write(chave)
    print("Chave gerada e salva em chave.key")
    return chave

def criptografar_arquivo(caminho_arquivo, fernet):
    with open(caminho_arquivo, "rb") as arquivo:
        dados = arquivo.read()

    dados_criptografados = fernet.encrypt(dados)

    with open(caminho_arquivo, "wb") as arquivo:
        arquivo.write(dados_criptografados)

    print(f"arquivo '{caminho_arquivo}' foi criptografado")

def criptografar_pastas_subpastas(caminho_pasta, chave):
    fernet = Fernet(chave)
    arquivos_criptografados = 0
    for root, _, files in os.walk(caminho_pasta):
        for nome_arquivo in files:
            if nome_arquivo.lower().endswith(".txt"):
                caminho_completo = os.path.join(root, nome_arquivo)
                try:
                    criptografar_arquivo(caminho_completo, fernet)
                    arquivos_criptografados += 1
                except Exception as e:
                    print(f"Erro ao criptografar '{caminho_completo}': {e}")

    if arquivos_criptografados == 0:
        print("Nenhum arquivo .txt encontrado na pasta ou subpastas.")
    else:
        print(f"\nTotal de arquivos .txt criptografados: {arquivos_criptografados}")

def main():
    caminho_pasta = input("Digite o caminho completo da pasta com arquivos .txt: ")

    if not os.path.isdir(caminho_pasta):
        print("pasta invalida")
        return
    
    chave = gerar_chave()
    criptografar_pastas_subpastas(caminho_pasta, chave)

if __name__ == "__main__":
    main()

# Reminder: Use this code only for learning in controlled environments. Respect laws, such as Brazil's LGPD!
