import csv

def cria_csv():

    # Dados a serem escritos no arquivo CSV
    dados = [
        ['id', 'nome', 'idade', 'email', 'cpf']
    ]

    # Nome do arquivo CSV
    nome_arquivo = 'banco_dados.csv'

    # Abrir o arquivo CSV em modo de escrita
    with open(nome_arquivo, 'w', newline='') as arquivo_csv:
        # Criar um objeto escritor CSV
        escritor_csv = csv.writer(arquivo_csv)

        # Escrever os dados no arquivo CSV
        for linha in dados:
            escritor_csv.writerow(linha)
