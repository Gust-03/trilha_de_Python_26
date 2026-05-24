
Funcionamento do programa
O simulador_tcg tem como objetivo simular um jogo de cartas de combate estilo Trading Card Game.
O programa irá receber do usuário o nome de uma criatura com valores de vida e de ataque simulando as caracteristicas de um jogo TCG além do nome e pontos de vida de uma criatura adversária 
após terem os valores recebidos o programa realizara uma batalha de turnos entre as criaturas onde a cada turno a primeira criatura ataca a segunda e depois é atacada pela mesma,
a cada turno é anunciado o dano causado durante o ataque do turno e a vida remanescente de cada criatura. 
Quando a vida de uma criatura chega a 0 pontos ela é declarada derrotada junto da vitória da criatura sobressalente.

Rodando o programa
Após o início do programa, será pedido ao usúario quele ele digite o nome da criatura o qual pode ser qualquer tipo de linha de texto,
após isso será peço ao usuário que digite o valor de pontos de vida da criatura e logo em seguida os pontos de ataque, esses valores devem ser digitados somente como números inteiros maiores que 0.
Feito isso o mesmo processo se repete mas desta vez perguntando o nome e pontos de vida e ataque da segunda criatura, o usuário deve inserir um outro nome para a segunda criatura além de outros pontos de vida e ataque.
inserido os valores o programa irá rodar o simulador de combate onde automaticamente os turnos serão rodados até que aja uma criatura vencedora.

Perguntas teóricas
1. Qual é a principal diferença prática entre usar um laço for e um laço while em Python? Por que o while foi a melhor escolha para este duelo?
R.  Um laço for baseia se que o loop irá acontecer um número determinado de vezes, enquanto que um laço while determina que um loop vai acontecer enquanto a condição do laço estiver atendida. 
    O laço while é a melhor escolha pois ele casa com a proposta de que os turnos continuam a rodarem enquanto(while) os pontos de vida form maiores que 0 o que é um fator variável

2. Para que serve a palavra-chave return dentro de uma função? O que acontece se uma função fizer um cálculo matemático mas não possuiro return?
R.  A palavra chave return tem como finalidade retornar o resultado da função, se a função fizer um cálculo mas não tiver return ela não entregará o resultado do cálculo para o programa       

3. O que é um "Loop Infinito" e como podemos evitá-lo ao construir uma estrutura while?
R.  Um loop infinito acontece quando não há condições de parada em um loop então ele devolve resultados sem parar,
    Ele pode se evitado em uma estrutura while ao adicionar uma condição break dentro do loop 
