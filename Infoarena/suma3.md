# Suma3

On a grid sheet, we have a rectangle delineated. Inside the delineated rectangle, there is a natural number written on each square. Exactly half of the numbers are equal to $0$, and the remaining numbers are distinct. We aim to create a path on the grid inside the rectangle by traversing all the numbers different from $0$ such that each number appears exactly once on the path. The traversal is done by moving from one number to one of the numbers adjacent in the grid on the line, column, or diagonal. We define the sum of the path as being equal to the sum of products of the form $k * a_{i,j}$, where $k$ is the ordinal number of the number in the order of traversal, and $a_{i,j}$ is the current number on the path.

## Task

Determine the path with the minimum sum, as well as this sum.

## Input data

The input file `suma3.in` contains on the first line two natural numbers, $M$ and $N$, representing the dimensions of the rectangle (it will have $M$ rows and $N$ columns). The following $M$ lines contain $N$ natural numbers, separated by at least one space. 

## Output data

The output file `suma3.out` will contain a natural number on the first line, representing the sum of the minimum path. The second line will describe the minimum path, i.e., all the numbers different from $0$ in the grid, in the order in which they were included in the sum. The numbers will be separated by at least one space.

## Constraints and clarifications

$1 \leq M, N \leq 8$

$M * N$ will always be an even number

$0 \leq nr_{i,j} \leq 100$, for any $i$ between $1$ and $M$, $j$ between $1$ and $N$

It will always be possible to traverse all the numbers

## Example

`suma3.in`

```
3 4
1 0 10 0
4 3 0 8
0 0 2 0
```

`suma3.out`

```
70
10 8 2 3 4 1
```

## Explanation

$1 * 10 + 2 * 8 + 3 * 2 + 4 * 3 + 5 * 4 + 6 * 1 = 10 + 16 + 6 + 12 + 20 + 6 = 70$.