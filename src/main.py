# IMPORTS
from state import state  # Importando a class state - objeto estado
from open_file import open_file  # Importando função para abertura e leitura de arquivo
from word_input import word_input  # Importando função para inserir as palavras de entrada a serem testadas
from check_word import check_palavra # Importando função que valida a palavra de entrada no AFD

# FUNÇÃO PRINCIPAL
def main():
    """
    #####################################################
    ############### PARTE 01 ############################
    #####################################################
    """

    # Entrada com o nome do arquivo
    file_name = input("Digite o nome do arquivo de entrada (sem a extensão .txt): ")
    file_name = f"{file_name}.txt"

    # Abertura e leitura do arquivo
    lines_file = open_file(file_name)  # Lista com cada elemento sendo uma linha do .txt

    # Automato
    automato = {}  # Dicionario de estados

    """
    • Linha 1: Indica o número de estados para o conjunto Q. Assume-se os rótulos dos estados de q0
    a q(n−1), com n sendo o número de estados, já entendendo que q0 seja o estado inicial.
    Considere que 1 ≤ n ≤ 10;
    """
    # CRIACÃO DOS ESTADOS
    qtd_states = int(lines_file[0])  # Quantidade de estados

    # Valida a quantidade de estados
    if 0 <= qtd_states <= 10:
        # Cria os estados conforme a quantidade
        for indexState in range(0, qtd_states):
            # Adiciona um elemento no dicionario(map), correspondente a cada estado
            # Cada estado é um class state
            new_state = {indexState: state(indexState)}
            automato.update(new_state)
        # Estado inicial -> primeiro estado
        automato[0].is_initial = True
    else:
        print("Quantidade de estados inválido ou fora do intervalo")
        return 0

    """
    • Linha 2: Informa alfabeto de entrada. Deve ser informada a quantidade de elementos desse alfabeto
    seguida dos mesmos, separados por um espaço. Considere que o tamanho máximo para alfabeto é 10;
    """
    # CRIAÇÃO DO ALFABETO
    input_alphabet = lines_file[1]  # Ex: 2 a b
    input_alphabet = input_alphabet.split(' ')  # Separar pelo espaço (list)

    qtd_alphabet = int(input_alphabet[0])  # Quantidade de elementos do alfabeto

    # Valida se está no intervalo
    if (0 <= qtd_alphabet <= 10):
        # Lista com o alfabeto
        alphabet = []
        # Adiciona a list alfabeto os elementos da linha
        for i in range(1, qtd_alphabet + 1):
            alphabet.append(input_alphabet[i])
    else:
        print("Inválido ou fora do intervalo (Tamanho máximo para o alfabeto é 10)")
        return 0

    """
    • Linha 3: Indica os estados que são finais. Deve ser informada a quantidade de estados finais
    seguida dos mesmos separados por espaços. Pode-se considerar apenas os valores de 0 a 9 (caso
    haja 10 estados);
    """
    # INDICAÇÃO DE ESTADOS FINAIS
    line_states_final = lines_file[2]  # 1 2
    line_states_final = line_states_final.split(" ")  # List

    qtd_states_final = int(line_states_final[0])  # Quantidade de estados finais

    # Valida se está no intervalo
    if not (0 <= qtd_states_final <= 9):
        print("Fora do intervalo (Considerar apenas os estados finais de 0 a 9)")
        return 0
    elif (qtd_states_final > qtd_states):
        print("Inválido | Quantidade de estados finais excede a quantidade estados")
        return 0
    else:
        # Lista com os estados indicados como finais
        states_final = []
        # Adiciona a list com os elementos (q0 ... q10) que são considerados finais
        for i in range(1, qtd_states_final + 1):
            if (int(line_states_final[i]) >= qtd_states or int(line_states_final[i]) < 0):
                print(f"Estado final ({int(line_states_final[i])}) inválido")
                return 0
            else:
                states_final.append(int(line_states_final[i]))

        # Acessando cada class state e alterando o isEnd
        for i in range(0, qtd_states_final):
            # get retorna cada value (class state) do dicionario
            automato.get(states_final[i]).is_end = True

    """
    • Linha 4: Indica o número transições (σ) da máquina, que deve ter no máximo 50.
    """
    # TRANSIÇÕES
    num_transicoes = int(lines_file[3])  # Número transições

    """
    • Linha 5 em diante: Apresentação das transições. Em cada linha deve constar uma σ, com 
    seus elementos separados por um espaço. Ex.: "q0 a q1".

    Ex: 0 a 1

    # state_atual - Estado de partida -> 0
    # aresta - caracter de transicao  -> a
    # state_final - Estado de chegada -> 1
    """
    # ADICIONANDO AS TRANSIÇÕES AOS ESTADOS

    # Validando o número de transições
    if 0 <= num_transicoes <= 50:
        # Loop pelas linhas de transição
        for i in range(4, num_transicoes + 4):
            line_transicao = lines_file[i].split(' ')  # List da transicão

            state_atual = int(line_transicao[0])  # Elemento do vetor - estado de origem
            aresta = line_transicao[1]  # Elemento do vetor - aresta de transição
            state_final = int(line_transicao[2])  # Elemento do vetor - estado final da transição
            # print(f"Estado atual: {state_atual}, aresta: {aresta}, estado final: {state_final}")

            # Validação antes de adicionar ao automato
            # Valida se o caracter da aresta está no alfabeto
            if not (aresta in alphabet):
                print("Aresta da transicao não presente no alfabeto")
                return 0
            # Valida o estado atual e final da transicao - intervalo de dominio
            if state_atual < 0 or state_final < 0 or not (0 <= state_atual < qtd_states) or not (
                    0 <= state_final < qtd_states):
                print("Estado inicial ou final inválido")
                return 0

            # Automato - dict de estados
            # Get (dict) identifica por meio da key, o estado atual correspondente do loop
            # Adiciona a cada estado suas transicoes -> insere_transicao
            automato.get(state_atual).insere_transicao(aresta, state_final)
    else:
        print("Número de transições inválido ou excedido")
        return 0

    # ADICIONANDO O INDICATIVO VAZIO AOS ESTADOS SEM TRANSIÇÕES
    for estado in automato.values():
        # Apresenta as transicoes (a,b,c..) do estado -> estado.transicoes.keys()
        # Percorre cada letra do alfabeto (transição)
        for transicao in alphabet:
            # Verifica se a transicao está presente no estado
            # Senão, adiciona o estado vazio
            if not (transicao in estado.transicoes.keys()):
                estado.insere_transicao(transicao, '∅')

    """
    • Linhas após as transições: Informar o número de palavras a serem testadas. Considere no
    máximo 10.
    """
    # NÚMERO DE PALAVRAS A SEREM TESTADAS
    index_num_palavras = 4 + num_transicoes
    num_palavras = int(lines_file[index_num_palavras])  # Linha do arquivo

    # Validando o número de palavras
    if not (0 <= num_palavras <= 10):
        print("Número de palavras inválido ou excedido")
        return 0

    """
    • Linha(s) seguinte(s): Palavras de entrada, uma por linha. Considere o tamanho máximo das
    palavras como 15 elementos do alfabeto
    """
    # PALAVRAS DE ENTRADA
    # Lista de palavras a serem testadas
    palavras = word_input(num_palavras, index_num_palavras, lines_file, alphabet)

    """
    • Testando as palavras de entrada: 
    """
    # Lista para armazenar os resultados dos testes das palavras
    resultados = []

    for palavra in palavras:
        # Separa cada letra de uma palavra ( Ex: ['a', 'b', 'b', 'b', 'b', 'a'] )
        palavra = list(palavra)
        print(palavra)

        # Valida se a palavra é aceita ou rejeitada pelo automato
        if check_palavra(automato, palavra):
            resultados.append('Aceita.')
            print(f"Palavra {palavra} -> Aceita.\n\n")
        else:
            resultados.append('Rejeita.')
            print(f"Palavra {palavra} -> Rejeita.\n\n")

    """
    • Arquivo de saída -> Registrando os resultados 
    """
    


    """
    #####################################################
    ############### PARTE 02 ############################
    #####################################################
    """

    for i in automato.values():
        print(i.__dict__)


    print(resultados)
    return 0


# Executando a função principal
main()
