"""
FUNÇÃO CHECK PALAVRA
    - A função tem por finalidade testar se a palavra de entrada é aceita ou rejeitada
      pelo automato definido (AFD)
    - Parâmetros da função
        - automato ->  {indexState: class state} -> Dicionario de estados
        - palavra -> Lista com os elementos sendo cada letra da palavra de entrada
    - Métodos
        - get -> Retorna o elemento do dicionario, conforme o parametro key -> ex: automato.get(indexState) = class state
        - Acessando a class, retorna o dicionario com as transições do estado -> ex: automato.get(0).transicoes
    - Validação
        - Para palavra ser aceita, ao final das transições o ultimo estado deve ser indicado como estado final
        - Acessar a class state -> automato[proximo_estado]
        - Usar o método is_end -> automato[proximo_estado].is_end == True
    - Observações
        - Cada elemento da palavra (letra) representa uma transição, esta que será utilizada
          nas passagens de estados
"""


def check_palavra(automato, palavra):
    qtd_transicoes_palavra = len(palavra)  # Quantidade de transições - letras da palavra

    # !! DUVIDA - Se não tiver transição, palavra é rejeitada
    if qtd_transicoes_palavra == 0:
        return False

    # Estado inicial q0
    estado_atual = automato.get(0).transicoes  # Retorna dicionario de transições do estado
    print(estado_atual)

    # Dado a primeira transição (palavra[0]) -> Armazena na variavel o proximo estado
    # estado_atual -> ex: {'a': 1, 'b': 2} -> estado_atual[palavra[0]] = 1
    proximo_estado = estado_atual[palavra[0]]
    print(proximo_estado)

    # Validação - Caso tenha somente uma transição
    if automato[proximo_estado].is_end and qtd_transicoes_palavra == 1:
        return True

    for i in range(1, qtd_transicoes_palavra):
        estado_atual = automato.get(proximo_estado).transicoes
        print(estado_atual)

        proximo_estado = estado_atual[palavra[i]]
        print(proximo_estado)

        # automato -> {indexState: class state}
        # proximo_estado -> inteiro que indica o estado
        print(f"Automato é final: {(automato[proximo_estado].is_end)}")
        print(f"i: {i} / qtd_transicoes: {qtd_transicoes_palavra}")

        # Validação - estado final e ultima transição
        if (automato[proximo_estado].is_end) and (i + 1 == qtd_transicoes_palavra):
            return True
        # Valida se o próximo estado é vazio
        if proximo_estado == '∅':
            return False

    return False


# DESENVOLVENDO O ALGORITMO
"""

def movimento(automato, palavra):
    print(palavra)
    print()

    # Estado inicial q0 - transicao a
    estado_atual = automato.get(0).transicoes  # Estado inicial q0
    print(estado_atual)
    proximo_estado = estado_atual[palavra[0]]
    print(proximo_estado)

    print()

    # Estado q1 - transicao b
    estado_atual = automato.get(proximo_estado).transicoes  # q1
    print(estado_atual)
    proximo_estado = estado_atual[palavra[1]]
    print(proximo_estado)

    print()

    # Estado q2 - transicao b
    estado_atual = automato.get(proximo_estado).transicoes  # q1
    print(estado_atual)
    proximo_estado = estado_atual[palavra[2]]
    print(proximo_estado)

    print()

    # Estado q2 - transicao b
    estado_atual = automato.get(proximo_estado).transicoes  # q1
    print(estado_atual)
    proximo_estado = estado_atual[palavra[3]]
    print(proximo_estado)

    print()

    # Estado q2 - transicao b
    estado_atual = automato.get(proximo_estado).transicoes  # q1
    print(estado_atual)
    proximo_estado = estado_atual[palavra[4]]
    print(proximo_estado)

    print()

    # Estado q2 - transicao a
    estado_atual = automato.get(proximo_estado).transicoes  # q1
    print(estado_atual)
    proximo_estado = estado_atual[palavra[5]]
    print(proximo_estado)
    
"""
