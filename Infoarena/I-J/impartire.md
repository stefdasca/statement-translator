# Division

Two natural numbers $M$ and $N$ are given.

## Task

Print the number $M/N$ in complete decimal form (with repeating period if applicable).

## Input data

The input file `impartire.in` contains on a single line the numbers $M$ and $N$ separated by a space.

## Output data

The result will be printed to the file `impartire.out` on a single line in the form $0.non\_repeating\_part$ or $0.non\_repeating\_part(repeating\_part)$ depending on the case.

## Constraints

$$
0 < M < N \\
N \leq 100000
$$

## Examples

`impartire.in` `impartire.out` 
```
13 25
0.52
```
`impartire.in` `impartire.out` 
```
73 505
0.1(4455)
```