# Academia de Hanói

**Número da Lista**: 4<br>
**Conteúdo da Disciplina**: D&C<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 18/0113585 |  Hugo Ricardo Souza Bezerra |
| 18/0125770  |  Lucas Gabriel Bezerra |

## Sobre 
Academia de Hanói é um jogo baseado no puzzle Torre de Hanói. Na academia Hanói os discos são organizados de maneira que todos os clientes possam pegar os discos desejados sem dificuldades (ordenados de maneira decrescente, dessa forma um cliente que deseja usar um disco de 10 Kg não precisa levantar um disco de 15 Kg). Sempre que precisa mover os discos o Sr.Hanói, dono da acadêmia e um senhor de idade, sente dificuldade de reorganiza-los empilhados em ordem decrescente. O objetivo do jogo é ajudar o Sr.Hanói a mover os discos de A para C. Porém, isso pode não ser uma tarefa simples, por isso você pode ter que recorrer a uma máquina que o Sr.Hanói comprou. A máquina faz o trabalho de organização por você utilizando um algoritmo dividir e conquistar, o problema é que ela gasta muita energia elétrica e o Sr.Hanói não vai gostar nadinha de ver a conta depois.

## Screenshots
![](https://i.imgur.com/5swxOcB.gif)
![](https://i.imgur.com/51PRHOL.png)
![](https://i.imgur.com/K85ELmJ.png)
![](https://i.imgur.com/31T6PmF.png)

## Vídeo
> https://youtu.be/yLr2FS7FQMs

## Instalação 
**Linguagem**: Python<br>
**Framework**: --- <br>

**Pré-requisitos** para rodar o Academia de Hanói:
* Instale o [Python](https://www.python.org/downloads/) (versão 3.8.5)
* Instale o [Pyxel](https://github.com/kitao/pyxel/blob/master/README.pt.md) (versão 1.4.3)

Instalar e Executar (Sistema baseado em Debian)

    $ pip3 install pyxel 
    $ git clone https://github.com/projeto-de-algoritmos/DC_Academia-de-Hanoi.git
    $ cd DC_Academia-de-Hanoi/src
    $ python3 app.py


## Uso 
Para usar a aplicação Academia de Hanoi siga os seguintes passos:
* Execute a aplicação como mostrado acima
* Opcional: Clique nos botões de "+" ou "-" para modificar a quantidade de discos no jogo
* Clique no botão "Start" para iniciar o jogo
* Clique e arraste para mover os discos no topo de uma torre e transferi-los para outra torre 
* Tente passar todos os discos da parra a torre C
* Caso queira ver a resposta para a solução no mínimo de movimentos possíveis clique no botão "Solve"
