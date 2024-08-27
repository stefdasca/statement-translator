## Task

Bob loves chocolate very much and he can never get enough of it. Imagine his joy when his parents told him they would buy many rectangular pieces of chocolate for his birthday. A piece of chocolate is a rectangle $1 \times 2$ or $2 \times 1$. Bob’s parents also bought him a cake, which can be represented as a matrix with $M$ rows and $N$ columns. Some positions on the cake are occupied by candles, while others are empty. Bob’s parents asked him to put as many pieces of chocolate on the cake as possible, in such a way that any 2 pieces do not overlap. However, Bob wants to keep as many pieces as possible for himself. Therefore, he wants to place a minimum number of pieces on the cake, keeping the rest for himself. To make sure his parents do not get suspicious, Bob wants to place the pieces of chocolate in such a way that no additional piece can be placed on the cake (i.e., there should not be 2 adjacent free squares either horizontally or vertically). Determine the minimum number of pieces of chocolate that need to be placed on the cake, so that they do not overlap and no additional pieces can be placed.

## Input data

The first line of the input file `choco.in` contains 2 integers, separated by a space: $M$ and $N$. The next $M$ lines each contain $N$ characters, describing the cake. The $j$-th character on the $i$-th of these $M$ lines can be either '*' (ASCII code 42), representing a candle, or '.' (ASCII code 46), representing a free position.

## Output data

In the output file `choco.out` print the minimum number of pieces of chocolate that Bob will place on the cake.

## Constraints and clarifications

$1 \leq M \leq 70$

$1 \leq N \leq 7$

## Example

`choco.in` `choco.out`
```
5 5
.*..*
*....
..**.
**.*.
.**..
4
```