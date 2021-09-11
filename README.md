<h1 align="center">
  <img alt="automato" src=".github/automato.svg" width="25%"/>
</h1>

<h2 align="center">
  ↔️ Simulador de um AFD e geração de AF mínimo ↕️ 
</h2>
<!-- Tópicos -->

## 💻 Sobre o projeto
- Projeto desenvolvido na matéria de Teoria da Computação, durante o curso de Engenharia da Computação - **[@UTFPR](http://www.utfpr.edu.br/)**.

- Consiste na implementação de um simulador de Autômato Finito Determinístico (AFD) que aceite a especificação de um AFD, teste se o AFD pode ser minimizado e, se puder, realize o processo de minimização, apresentando-o.

- A proposta consiste em, partindo de uma lista de palavras de entrada, o simulador informe quais são aceitas e quais são rejeitadas pela linguagem reconhecida pelo autômato.

- O simulador deve seguir o formatos de entrada e saída.

## 📚 Partes do projeto

### ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) PARTE 01
 
#### ↠ Entrada - Arquivo de Texto

 - **Linha 1 :** Indica o número de estados para o conjunto Q;
- **Linha 2 :** Informa alfabeto de entrada;
- **Linha 3 :** Indica os estados que são finais. Deve ser informada a quantidade de estados finais seguida dos mesmos separados por espaços. Pode-se considerar apenas os valores de 0 a 9 (caso haja 10 estados);
- **Linha 4 :** Indica o número transições ( σ ) da máquina, que deve ter no máximo 50.
- **Linha 5 em diante :** Apresentação das transições. Em cada linha deve constar uma σ , com seus elementos separados por um espaço.
- **Linhas após as transições :** Informar o número de palavras a serem testadas. Considere no máximo 10.
- **Linha(s) seguinte(s) :** Palavras de entrada, uma por linha. Considere o tamanho máximo das palavras como 15 elementos do alfabeto.

####  ↠ Saída - Arquivo de Texto
Deve apresentar apenas a saída do processamento das palavras de entrada e exibir a mensagem "ACEITA " ou "REJEITA", com uma mensagem por linha, na respectiva ordem de entrada das palavras.


### ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+)  PARTE 02
-  ‍🔧 Em fase de construção

## 🚀 Como executar o projeto

   ```
   - Clone this repository:
   $ git clone https://github.com/matheusfbonfim/dfa-simulator
   
   - Enter in directory:
   $ cd src
   
   - Execute application:
   $ python3 main.py
   ```

## :memo: License

O projeto está sobre a licença [MIT](./LICENSE) ❤️ 

Gostou? Deixe uma estrelinha para ajudar o projeto ⭐

<!-- Mensagem final -->
<h3 align="center">
Feito com ❤️ por <a href="https://www.linkedin.com/in/matheusfbonfim/">Matheus Bonfim</a>
<br><br>
</h3>
</h3>
