## Task

Hipiotu' has found a new way to have fun. He looks out of the window of the dormitory in Grozavesti and imagines the beautiful landscape outside as a grid with $N$ rows and $N$ columns. He notices that in each cell of the grid there is a natural number between $1$ and $1\ 000\ 000$. He wants to swap some rows or columns of the grid such that, in the end, the elements on the main diagonal are in increasing order. The elements on the main diagonal are the elements for which the column they are located in is equal to the row they are located in. More precisely, if we denote the grid with $A$, after the swaps, we want $A_{1,1} \leq A_{2,2} \leq \dots \leq A_{N,N}$. For Hipiotu', spiritual things are more important, so he does not necessarily want to make a minimum number of swaps, but he only wants this number to be at most $2 \times N$. Evidently, a row or column cannot be swapped with itself, and the order in which the swaps are performed matters.

## Input data

The first line of the file `grozavesti.in` contains a natural number $N$ with the significance mentioned in the statement. The next $N$ lines contain $N$ numbers each, separated by a single space, representing the values of the grid imagined by Hipiotu'.

## Output data

The first line of the file `grozavesti.out` contains a natural number $M$ representing the number of swaps performed by your solution. Each of the next $M$ lines describes the swaps performed in order and has the format $c \; x \; y$, where $c$ is a character that can have the value $C$ if two columns are swapped, respectively $L$ if two rows are swapped. $x$ and $y$ represent the two rows or columns that are swapped.

## Constraints and clarifications

$1 \leq N \leq 300$

## Example

`grozavesti.in`
```
3
1 3 2
2 1 3
2 2 1
```

`grozavesti.out`
```
2
C 2 3
L 1 2
```

## Explanation

Of course, a solution in which the number of swaps is $0$ would have been possible, but $2 \leq 3 \times 2$ so this one is also correct.