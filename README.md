# TDD Engenharia de Software

Co-autores: [Luisfelipeqt](github.com/Luisfelipeqt) e Laryssa Melonio

Esse repositório é a resposta para a tarefa da disciplina de Engenharia de Software da UNDB.

O objetivo é desenvolver o código e testes unitários abordando a metodolodia Test Driven Development, ou Desenvolvimento Guiado por Testes, para resolver um conjunto de problemas:

#### Soma de um Array
#### Diferença Diagonal
#### Palíndromo

Este trio optou por utilizar a linguagem de programação Python 3.X e a framework Pytest para desenvolvimento dos códigos e testes.

### Sobre os problemas:
Fonte: [cavalcantigor/eng-software-tdd](https://github.com/cavalcantigor/eng-software-tdd/blob/main/README.md#tarefas)

> #### Soma de um Array

> Dado um array de inteiros, encontre a soma de seus elementos.
>> Exemplo: para o array [1, 2, 3] o resultado de sua soma é 6, uma vez que 1 + 2 + 3 = 6.

> Para essa tarefa, considere um array de tamanho n, onde 0 < n <= 1000.

> #### Diferença Diagonal
>Dada uma matriz quadrada de tamanho **n**, calcule a diferença absoluta da soma de suas diagonais.

> Exemplo: 
> ```
> 1 2 3
> 4 5 6
> 9 8 9
> ```
> A diferença diagonal absoluta para essa matriz é:
> - 1 + 5 + 9 = 15 (diagonal da esquerda para a direita)
> - 3 + 5 + 9 = 17 (diagonal da direita para a esquerda)
> - Diferença absoluta: |15 - 17| = 2 (diferença em módulo)

> Para esse problema, considere 2 <= n <= 1000 e cada elemento da matriz como um inteiro -100 < `m[i][j]` <= 100.
> #### Palíndromo
> Dada uma string de tamanho variável **n**, determine se essa string é um palíndromo.

> Exemplos:
> - "ABBA" é um palíndromo.
> - "SOCORRAM ME SUBI NO ONIBUS EM MARROCOS" é um palíndromo (perceba que para essa verificação os espaços em branco não são levados em consideração).
> - "ABCDCBA" é um palíndromo.
> - "ABAB" **não** é um palíndromo.


> Para essa tarefa considere 0 < n <= 1000.
