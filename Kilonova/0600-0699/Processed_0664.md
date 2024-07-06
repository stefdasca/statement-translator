Here is the translated text:

## Given Information

A matrix with $n$ rows and $m$ columns is filled with three types of values:

1. Empty squares, marked with .
2. Walls, marked with #
3. Characters, marked with $R$

## Task

The task is a simple one: find the maximum value of $k$ such that if we expand the walls by $k$ squares in all directions, all characters marked with $R$ can still reach each other. It is guaranteed that the characters can reach each other from the beginning.

A character can move on the matrix in the $4$ directions (up, down, left, right).

An expansion by $k$ consists of the following operation: For each square in the initial matrix marked with #, we will mark all squares within a distance of at most $k$ from it with #. In other words, all squares within a distance of at most $k$ from a wall in the initial matrix also become walls.

If a character is blocked by a wall due to the expansion by $x$, then we cannot expand the wall by $x$.

It is guaranteed that there is at least one wall in each test and at least two characters.

## Input data

The first line of the input file `expansion.in` contains two integers, $n$ and $m$.

The following $n$ rows will contain the description of the matrix, which has $n$ rows and $m$ columns and contains the characters mentioned above, $a_{i, j}$ representing the square on row $i$ and column $j$.

## Output data

The first line of the output file `expansion.out` will contain a single integer, the value of $k$, according to the description in the statement.

## Constraints and clarifications

* $1 \leq n, m \leq 2 \cdot 10^3$;

|#|Points|Constraints|
|-|-|--------|
|1|12|$a_{i, j}$ = # for any $2 \leq i \leq n-1$ and $2 \leq j \leq m-1$|
|2|45|$1 \leq n, m \leq 100$|
|3|43|No other constraints|

## Example 1

`expansion.in`
```
5 5
R...R
.....
..#..
.....
R...R
```

`expansion.out`
```
1
```

## Explanation

~[gol.png]

With red we marked the initial walls and with orange, the walls obtained as a result of the expansions.

For the first example, all $R$'s can reach each other if we expand the walls by $1$, but this will be impossible if we expand the walls by $2$.

## Example 2

`expansion.in`
```
2 6
R#.#.R
......
```

`expansion.out`
```
0
```

## Explanation

For the second example, if we expand the walls by $1$ square, the $R$ at ($1, 1$) would be trapped between the walls. 

