"""
FUNÇÃO WORD_IN_ALPHABET
    - Utilizando a biblioteca Counter
    - Counter retorna um dicionario com as keys sendo cada letra da palavra
      e os values sendo a quantidade que essa letra aparece
    - A função tem por finalidade analisar se todas as letras da palavra testada
      estão presente no alfabeto
    - Counter retorna uma <class 'collections.Counter'>
"""

from collections import Counter


def word_in_alphabet(alphabet, line_palavra):
    total_caracteres = 0
    counter = Counter(line_palavra)

    for caracter in alphabet:
        if caracter in counter.keys():
            total_caracteres += counter.get(caracter)

    # print(f"Tamanho da palavra: {len(line_palavra)} / Total caracteres: {total_caracteres}")

    if total_caracteres == len(line_palavra):
        return True
    else:
        return False


"""
FUNÇÃO WORD_INPUT
    - A função tem por finalidade retornar uma lista das palavras de entrada 
      que são usadas para testar o AFD
    - num_palavras: Numero de palavras a serem testadas
    - index_num_palavras: A partir de qual linha do arquivo as palavras são registradas
    - lines_file: lista contendo as linhas do arquivo de entrada
    - alphabet: lista contendo os elementos do alfabeto
"""


def word_input(num_palavras, index_num_palavras, lines_file, alphabet):
    # PALAVRAS DE ENTRADA
    palavras = []  # List de palavras a serem testadas

    for i in range(1, num_palavras + 1):
        # Cada palavra a ser testada presente no arquivo
        line_palavra = lines_file[index_num_palavras + i]

        # Validando o tamanho da palavra - 15 elementos do alfabeto
        if 0 <= len(line_palavra) <= 15:
            # Verificando se todas as letras da palavra pertence ao alfabeto
            if not (word_in_alphabet(alphabet, line_palavra)):
                print(f"Algum(ns) elemento(s) da palavra {line_palavra} não pertence ao alfabeto")
                return 0
            else:
                # Adicionando na lista de palavras
                palavras.append(line_palavra)
        else:
            print(f"Tamanho máximo da palavra ({line_palavra}) excedido")
            return 0

    return palavras