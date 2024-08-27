# Rooks

Gigel has a chessboard with $N$ rows and $M$ columns. He wants to place $K$ rooks on the board such that they do not attack each other (Two rooks are said to attack each other if they are on the same row or the same column). To make things more interesting, Gigel has marked certain squares where no rook can be placed, and now he wants to know in how many ways he can place the rooks.

## Task

Help Gigel find the number of ways he can place the $K$ rooks.

## Input data

The first line of the input file `ture.in` contains three numbers: $N$, $M$, and $K$ separated by a single space. The second line contains $P$, the number of marked squares by Gigel. Then follow $P$ lines each with two numbers $x$, $y$ indicating that Gigel has marked the square on row $x$ and column $y$.

## Output data

The first line of the file `ture.out` will contain the number of ways to place the rooks on the chessboard.

## Constraints

$0 \leq N*M \leq 250$

$0 \leq K \leq 100$

$0 \leq P \leq N*M$

## Example

`ture.in`

```
3 3 3 1
2 2
```

`ture.out`

```
4
```