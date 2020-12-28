"""
FUNÇÃO OUTPUT_FILE
    # Função para abertura e escrita do arquivo
    # Abertura de arquivo
        - Modo de escrita w -> write
    # Utilizado o bloco with

    # Para escrevermos dados em um arquivo, após abrir o arquivo utilizamos a função write()
    # Esta função recebe uma string como parâmetro, caso contrario dará TypeError

    # Abrindo um arquivo no modo w, se o arquivo não existir será criado, caso ele ja exista,
      o anterior será apagado e um novo será criado. Dessa forma, todo o conteúdo no arquivo
      anterior é perdido
"""


def output_file(output_file_name, resultados):
    # Escrita no arquivo de saída - Modo W - Write - Escrever

    with open(output_file_name, 'w', encoding='UTF-8') as arquivo:
        for i in range(0, len(resultados)):
            if i + 1 == len(resultados):
                arquivo.write(f"{resultados[i]}")
            else:
                arquivo.write(f"{resultados[i]}\n")
