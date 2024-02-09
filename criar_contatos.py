import os
import glob
from datetime import datetime

print('''                                                       .
                    |\__/,|   (`\\                      .
                  _.|o o  |_   ) )                     .
                -(((---(((--------                     .
  ▄████  ▄▄▄     ▄▄▄█████▓ ▒█████                      .
 ██▒ ▀█▒▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒                    .
▒██░▄▄▄░▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒                    .    Autor: Gato
░▓█  ██▓░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░                    .    │
░▒▓███▀▒ ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░                    .    └──> Instagram: @gato.ads
 ░▒   ▒  ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░                     .
  ░   ░   ▒   ▒▒ ░   ░      ░ ▒ ▒░                     .
░ ░   ░   ░   ▒    ░      ░ ░ ░ ▒                      .
      ░       ░  ░            ░ ░                      .

Ferramenta para criação de pacotes vCard de contatos, prontos para importação.
''')

def criar_contato(numero, indice, nome_contato):
    contato = f"BEGIN:VCARD\nVERSION:3.0\nN:\"'{nome_contato} {indice};;;\nFN:\"'{nome_contato} {indice}\nTEL;TYPE=VOICE,CELL;VALUE=text:{numero}\"\nEND:VCARD"
    return contato

def exibir_opcoes_arquivos():
    arquivos_txt = glob.glob("*.txt")
    print("""Importe a lista de contatos nessa formatação:

+55 84 9999-1642
+55 85 8156-8582
+55 85 8523-9617
        """)
    for indice, arquivo in enumerate(arquivos_txt, start=1):
        print(f"[ {indice} ] {arquivo}")
    return arquivos_txt

def criar_diretorio_contatos():
    data_hora_atual = datetime.now().strftime("%Y_%m_%d__%H_%M_%S")
    nome_diretorio = f'contatos_{data_hora_atual}/'
    os.makedirs(nome_diretorio)
    return nome_diretorio

def dividir_contatos_grupos(numeros, tamanho_grupo):
    grupos = [numeros[i:i + tamanho_grupo] for i in range(0, len(numeros), tamanho_grupo)]
    return grupos

def main():
    arquivos_txt = exibir_opcoes_arquivos()

    escolha = int(input("\n\nNúmero do arquivo: "))

    if 1 <= escolha <= len(arquivos_txt):
        nome_arquivo = arquivos_txt[escolha - 1]
        diretorio_contatos = criar_diretorio_contatos()

        with open(nome_arquivo, 'r') as file:
            numeros = file.read().splitlines()

        tamanho_grupo = int(input("\nDigite a quantidade de contatos por pacote: "))
        nome_contato = str(input("\nDigite o nome padrão para os seus leads: "))
        grupos_contatos = dividir_contatos_grupos(numeros, tamanho_grupo)

        for indice_grupo, grupo in enumerate(grupos_contatos, start=1):
            nome_arquivo_contato = f'{diretorio_contatos}contatos_grupo_{indice_grupo}.vcf'

            with open(nome_arquivo_contato, 'w') as file:
                for indice, numero in enumerate(grupo, start=1):
                    contato = criar_contato(numero, indice + (indice_grupo - 1) * tamanho_grupo, nome_contato)
                    file.write(contato + '\n')

        print(f"Contatos criados com sucesso em {diretorio_contatos}")
    else:
        print("Escolha inválida. Por favor, digite um número válido.")

if __name__ == "__main__":
    main()
