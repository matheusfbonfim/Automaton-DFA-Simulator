class automato:
    # Método construtor
    def __init__(self):
        self.__estados = {}  # Dicionario de estados
        self.__qtd_states = 0  # Quantidade de estados
        self.__alfabeto = []  # Lista com os elementos do alfabeto
        self.__qtd_alphabet = 0  # Quantidade de elementos do alfabeto
        self.__estados_finais = [] # Lista com os estados finais
        self.__qtd_states_final = 0 # Quantidade de estados finais

    # GETTERS
    @property
    def estados(self):
        return self.__estados

    @property
    def qtd_states(self):
        return self.__qtd_states

    @property
    def alfabeto(self):
        return self.__alfabeto

    @property
    def qtd_alphabet(self):
        return self.__qtd_alphabet

    @property
    def estados_finais(self):
        return self.__estados_finais

    @property
    def qtd_states_final(self):
        return self.__qtd_states_final

    # SETTERS
    @qtd_states.setter
    def qtd_states(self, num):
        self.__qtd_states = num

    @qtd_alphabet.setter
    def qtd_alphabet(self, num):
        self.__qtd_alphabet = num

    @qtd_states_final.setter
    def qtd_states_final(self, num):
        self.__qtd_states_final = num