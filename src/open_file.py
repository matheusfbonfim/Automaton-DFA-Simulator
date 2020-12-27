"""
FUNÇÃO OPEN_FILE
    # Função para abertura e leitura do arquivo
    # Abertura de arquivo
        - Modo de leitura padrão r -> read
    # Leitura do arquivo - Retorno de uma string
        - Utilizado o bloco with
    # readlines()
        - Faz um lista com os elementos sendo cada linha do texto presente no arquivo
"""

def open_file(file_name):
    # O bloco with - Forma flexível de manipular arquivos (abertura e fechamento automático)
    with open(file_name) as file:
        lines_file = file.readlines()  # Lista com as linhas do arquivo
        # Removendo o \n de cada elemento do array
        for index in range(len(lines_file)):
            lines_file[index] = lines_file[index].rstrip('\n')

    return lines_file