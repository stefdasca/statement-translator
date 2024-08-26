# Resturi2

Given a natural number $K$ and the natural numbers $p_1 , p_2 , \dots, p_K , r_1 , r_2 , \dots, r_K$, where $p_1 , \dots, p_K$ are pairwise distinct prime numbers, and $0 \leq r_i < p_i$, for any $i$ from $1$ to $K$. We say that a number $X$ is free of remainders if the remainder of dividing $X$ by $p_i$ is different from $r_i$, for any $i$ from $1$ to $K$. Consider the sorted sequence of natural numbers that are free of remainders. Determine the $N$-th element of the sequence.

## Input data

The file `resturi.in` contains on the first line the numbers $K$ and $N$, separated by a space. The following $K$ lines contain pairs of numbers $p_i , r_i$, separated by a space.

## Output data

The file `resturi.out` contains on the first line a single number $M$, representing the $N$-th number in the considered sequence.

## Constraints

$0 \leq K \leq 10$

$1 \leq N \leq 2\ 000\ 000\ 000$

The considered sequence is indexed starting from $1$.

It is guaranteed that the result will be less than $10\ 000\ 000\ 000$ (ten billion).

## Example

`resturi2.in` 
```
3 6
2 1
3 2
5 2
```

`resturi2.out`
```
18
```
In this case, the considered sequence is: $3, 4, 6, 7, 10, 12, 13, 16, 18, 19, 21, 24, 25, 27, 28, 30, 31, \dots$

`resturi2.in` 
```
4 16
3 2
17 9
7 1
23 0
```

`resturi2.out`
```
30
```
In this case, the considered sequence is: $3, 4, 6, 7, 10, 12, 13, 16, 18, 19, 21, 24, 25, 27, 28, 30, 31, \dots$