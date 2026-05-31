Descrição:
O programa tem como o intuito devolver ao usúario determinados dados de uma lista de reagentes químicos separados por nome do reagente, identidade do lote e porcentagem de pureza.

Funcionamento:
No momento em que o programa é iniciado pelo usuário ele asseça três diferentes listas, a lista de nomes de reagentes, a lista de lotes dos reagentes e a lista de pureza dos reagentes.
Asseçando a lista de nomes dos reagentes o programa delvolve ao usuário a quantidade de tipos únicos de reagetnes disponíveis.
Em seguida o programa une as três listas e devolve ao usuário um relátorio de cada reagente disponível junto de seu lote de identidade e sua porcentagem de pureza.
E por fim o programa devole um usuário outro relatório contendo apenas os reagentes cuja pureza seja maior ou igual a 98%

Perguntas
1.  Levando em consideração a estrutura do nosso inventário, por que seria incorreto usar a função dict() para transformar o resultado do nosso zip() em um dicionário, utilizando o nome do reagente como "Chave" e o lote como "Valor"?
  Em nosso zip() temos reagentes que se repetem com lotes e purezas diferentes, então os reagentes não funcionariam como chaves na a função dict() pois dicionarios não aceitam duplicatas.

2.  O que a função zip() gera na memória do Python antes de usarmos a função list() para forçar a visualização dos dados?
  A função zip() gera um objeto zip, que é uma iterção entre 2 ou mais tuplas as unindo em apenas uma só.

3.  Observando o seu código final, de que forma o List Comprehension substitui a necessidade de criar uma lista vazia e usar a estrutura de repetição for tradicional acompanhada do método .append()?
  Subistitui no sentido que permite criar uma "versão alterada" da lista original em vez de criar uma noa lista vazia e ir montando ela com dados extraidos da primeira lista do 0 no método .append() .
