## Task

You just got the coolest mobile game, GrEA: Gravity by EA. Fortunately, you purchased the entire season pass and gained access to this problem statement. In this game, there is a grid of size $2 \times N$, consisting of characters $0$ and $1$. Gravity Guy, the game's protagonist, starts from the first cell on the first row and wants to reach the last column, on either row, with a minimum number of steps, moving only through cells with the value $0$. In one step, he can move to adjacent cells on the current row or change gravity, moving to the other row on any column, provided the absolute value difference does not exceed $K$. More formally, from cell $c$, he can move to cells $c-1$ and $c+1$ on the current row or cells $t$ with $|t-c| \leq K$ on the other row, if they exist and have the value $0$. Print the minimum number of steps to reach the last column.

## Input data

The input file `grea.in` contains on the first line two integers, $N$ and $K$. Each of the next $2$ lines contains $N$ binary characters.

## Output data

The output file `grea.out` will contain the answer on the first line.

## Constraints and clarifications

$1 \leq K \leq N \leq 250\ 000$

It is guaranteed that a solution exists.

## Example

`grea.in`

```
4 2
0110
0100
```

`grea.out`

```
2
```