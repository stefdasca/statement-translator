## Task

An $N \times M$ matrix $A$ is given. Each cell has either the value $0$ (indicating that this cell is free) or an integer color between $1$ and $K$. Colored cells are inaccessible, while free cells are accessible. Travel between two accessible cells is only possible if they share a side. We call a color $C$ an unlocker if it is possible to travel from any free cell to any other free cell in the matrix when we also allow access to cells of color $C$. How many of the $K$ colors are unlockers?

## Input data

The input file `unlock.in` will contain on its first line the number of tests $T$. The structure of a test is as follows: the first line contains the values $N$ $M$ $K$ with the meaning given in the statement. The next $N$ lines will contain $M$ values each, between $0$ and $K$.

## Output data

The output file `unlock.out` will contain $T$ lines that contain integer values, representing the number of colors that are unlockers for each test.

## Constraints and clarifications

$1 \leq T \leq 30$ 

$1 \leq N, M \leq 250$ 

$1 \leq K \leq N \times M - 1$ 

There is always at least one free cell.

It is possible that some of the $K$ colors do not appear in any cell.

## Example

`unlock.in` 

```
1
3 3 2
0 0 0
1 2 1
0 0 0
```

`unlock.out` 

```
2
```