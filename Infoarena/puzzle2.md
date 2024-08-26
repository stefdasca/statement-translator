# Puzzle2

Ionita and Costi bought a rectangular puzzle of Amsterdam city, consisting of $N$ pieces of the same size. Unfortunately, no matter how hard they tried, they were not able to solve it, so they asked Alberto for help. Not wanting to spoil the fun of solving a puzzle for them, he decided to write a number from $1$ to $N$ on the back of each piece and provide a list of $M$ pairs $(a_i, b_i)$ with the meaning that pieces numbered $a_i$ and $b_i$ would be neighbors (would have a common side) if the puzzle were correctly solved. However, the two still couldn't solve the puzzle, so they are asking you to do it for them. They provide you with the $M$ pairs and ask you to reconstruct the puzzle.

## Input data

The input file `puzzle2.in` will contain on the first line $N$ and $M$, representing the number of puzzle pieces and pairs, respectively. The following $M$ lines will contain 2 numbers separated by a space: $a_i, b_i$.

## Output data

The output file `puzzle2.out` must contain on the first line 2 numbers $R$ and $C$, representing the number of rows and columns in the puzzle, respectively. The following $R$ lines must contain $C$ numbers each, between $1$ and $N$.

## Constraints and clarifications

$1 \leq N \leq 100\ 000$

$1 \leq M \leq 400\ 000$

$1 \leq a_i, b_i \leq N$

$a_i \ne b_i$

The $M$ pairs represent all possible pairs in the puzzle.

If the puzzle has $R$ rows and $C$ columns, then $M = (R - 1) \cdot C + (C - 1) \cdot R$

The existence of a solution is guaranteed. Any correct solution is accepted.

## Example

`puzzle2.in`
```
9 12
1 9
5 4
8 9
7 3
1 7
3 5
6 5
8 2
9 3
7 4
3 2
6 2
```
`puzzle2.out`
```
3 3
4 5 6
7 3 2
1 9 8
```