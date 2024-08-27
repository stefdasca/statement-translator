## Task

Mountainman and Middle Islander started a new game! Between them, there is a cake, which we will model as an inscribable polygon. The game is played in turns, and each player takes their turn alternately. Middle Islander plays first. A turn consists of the following steps: The player whose turn it is takes the knife and places it on a segment that contains two non-adjacent vertices of the cake. The other player cuts the cake along that line and eats one of the two resulting pieces. The player who cannot make a valid move loses. Assuming both players play optimally, we are interested in who wins.

## Input data

The input file `nopolynolife.in` will contain, in the first line, the integer $T$, which represents the number of tests in the file. Each test will contain exactly one line, which will contain the number $N$, which represents the number of vertices of the cake in that test.

## Output data

In the output file `nopolynolife.out` you will write, on each line, the answer for all test cases, in order. If Middle Islander wins, print `Island`. Otherwise, print `Mountain`.

## Constraints

$1 \leq T \leq 100\ 000$

$3 \leq N \leq 1\ 000\ 000\ 000$

## Example

`nopolynolife.in` 
```
2
3
4
```

`nopolynolife.out`
```
Mountain
Island
```