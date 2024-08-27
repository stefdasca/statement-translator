## Task

Let $n$ be a non-zero natural number and a sequence of $n$ natural numbers denoted $d_1$, $d_2$, $\dots$, $d_n$. Write a program that determines a connected graph with the degree sequence of its vertices $d_1$, $d_2$, $\dots$, $d_n$.

## Input data

The input file `grade.in` contains on the first line a natural number $n$, and on the second line $n$ natural values separated by spaces, representing the numbers $d_1$, $d_2$, $\dots$, $d_n$.

## Output data

The output file will contain on each line two natural numbers (ranging between $1$ and $n$), separated by a space $x \ y$, meaning « in the obtained connected graph there exists an edge between vertex $x$ and vertex $y$ ».

## Constraints and clarifications

$1 \leq n \leq 5000$

The vertices of the graph will be numbered from $1$ to $n$.

It is not necessary for vertex $1$ to have degree $d_1$, vertex $2$ to have degree $d_2$, etc.

Two degree sequences are considered equal if they match after sorting.

## Example

`grade.in`
```
5
2 1 1 2 4
```

`grade.out`
```
5 1
4 1
3 2
3 1
2 1
```