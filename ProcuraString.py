import os

def procurar_string_em_arquivos(pasta, string_procurada):
    # Lista para armazenar os nomes dos arquivos que contêm a string
    arquivos_com_string = []

    # Iterar sobre os arquivos na pasta
    for nome_arquivo in os.listdir(pasta):
        # Construir o caminho completo para o arquivo
        caminho_arquivo = os.path.join(pasta, nome_arquivo)

        # Verificar se o caminho é um arquivo regular
        if os.path.isfile(caminho_arquivo):
            # Abrir o arquivo e ler seu conteúdo
            with open(caminho_arquivo, 'r') as arquivo:
                # Verificar se a string procurada está no conteúdo do arquivo
                if string_procurada in arquivo.read():
                    arquivos_com_string.append(nome_arquivo)

    return arquivos_com_string

# Definir a pasta e a string a ser procurada
pasta = '/caminho/para/sua/pasta'  # Substitua pelo caminho da sua pasta
string_procurada = 'sua_string_aqui'  # Substitua pela string que você está procurando

# Chamar a função para procurar a string nos arquivos da pasta
arquivos_encontrados = procurar_string_em_arquivos(pasta, string_procurada)

# Exibir os arquivos encontrados
if arquivos_encontrados:
    print("A string foi encontrada nos seguintes arquivos:")
    for arquivo in arquivos_encontrados:
        print(arquivo)
else:
    print("A string não foi encontrada em nenhum arquivo na pasta.")
