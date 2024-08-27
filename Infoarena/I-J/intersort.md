## Task

You are given a permutation of $N$ elements and a number $S$, initially equal to $0$. Each time we swap two numbers from the permutation, $x$ and $y$, we add $\min(x,y)$ to $S$. Using this operation, sort the given permutation while minimizing the cost of $S$.

## Input data

The input file `intersort.in` will contain on the first line the natural number $N$ representing the number of elements in the permutation. The second line will contain $N$ natural numbers representing the given permutation.

## Output data

In the output file `intersort.out` you must print the minimum value of $S$ needed to sort the permutation using the described operation.

## Constraints

$1 \leq N \leq 100\ 000$

## Example

`intersort.in`
```
3
2 3 1
```

`intersort.out`
```
2
```

## Explanation

The sorting will be done in two steps. In the first step, elements $1$ and $3$ are swapped, resulting in the permutation $2 1 3$, adding to $S$ the cost $1 = \min(1,3)$. In the second step, elements $1$ and $2$ are swapped, increasing $S$ again by $1 = \min(1,2)$. Thus, the minimum value of $S$ to sort the given permutation is $2$.