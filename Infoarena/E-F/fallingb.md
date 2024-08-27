# Fallingb

Gigel likes playing a fascinating version of Falling Blocks. In this version of Falling Blocks, Gigel has an infinite number of pieces of each of the following shapes: Gigel's goal is to place these pieces in a grid of size $n \times m$. He is curious in how many different ways he can fill the grid using the available types of pieces.

## Input data

The input file `fallingb.in` contains on the first line the number of test cases $T$. On each of the following $T$ lines, there are two natural numbers $n$ and $m$ representing the dimensions of the grid on which the pieces are placed.

## Output data

For each test case in the input file, print in the output file `fallingb.out` the number of ways to fill the grid with the available pieces modulo $9901$.

## Constraints and clarifications

In all tests used for evaluation,
$n = 8$

$1 \leq m \leq 120$

$1 \leq T \leq 100$

## Example

`fallingb.in`
```
1
2 2
```

`fallingb.out`
```
11
```

## Explanation

There are $11$ ways to fill a grid of size $2$ by $2$: