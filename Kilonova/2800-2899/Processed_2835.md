```markdown
Let $N$ be a natural number and $A$ an array indexed from $1$, with $N^2$ elements, constituting a permutation of the numbers $1$, $2$, $3$, . . . , $N^2$. From a position $i$, with $1 \leq i \leq N^2$, we can move to position:
* $i - 1$, if $i - 1$ is not divisible by $N$
* $i + 1$, if $i$ is not divisible by $N$
* $i - N$, if $i-N \geq 1$
* $i + N$, if $i+N \leq N^2$

An element $A_i$ is called *start* if all elements to which we can move from position $i$ have values greater than $A_i$. A *path* is a sequence of elements, $A_{i_1}, A_{i_2}, . . . , A_{i_k}$, with $k \geq 1$, such that $A_{i_1} < A_{i_2} < . . . < A_{i_k}$, with the property that the element $A_{i_1}$ is start and that we can move from position $i_1$ to $i_2$, from $i_2$ to $i_3$, ..., from $i_{k-1}$ to $i_k$.

# Task

Display an array $A$ such that the number of paths is minimal (and does not exceed $10^9$), along with the number of paths in the displayed array.

# Input data

The input file `drumuri.in` contains on the first line the natural number $N$.

# Output data

The output file `drumuri.out` will contain on the first line $N^2$ distinct natural numbers between $1$ and $N^2$, separated by a space, representing the elements of the array $A$. The second line will contain the number of paths in the array $A$ written on the first line.

# Constraints and clarifications

* $1 \leq N \leq 1\ 000$
* The number of paths in the array $A$, denoted $nrdrum$, must be less than $1\ 000\ 000\ 000$.
* If the number of paths is correctly determined for the displayed array $A$, $40 \%$ of the score will be awarded.
* Additionally, $(\frac{nrmin}{nrdrum})^4 \cdot 60 \%$ of the score is awarded, where $nrmin$ is the minimum number of paths that can be obtained for a permutation of the array $1$, $2$, $3$, . . . , $N^2$, if all possible permutations are studied.

| # | Score | Constraints |
|---|-------|-------------|
| 1 | 45    | $1 \leq N \leq 16$ |
| 2 | 36    | $17 \leq N \leq 100$ |
| 3 | 19    | No additional constraints |

# Example 1

`drumuri.in`
```
2 
```

`drumuri.out`
```
1 2 3 4
5
```

## Explanation

For the first example, the paths are $(1)$, $(1, 2)$, $(1, 2, 4)$, $(1, 3)$, $(1, 3, 4)$, and since $5$ is the minimum number of paths for all permutations of the array $1$, $2$, $3$, $4$, $100$ points will be awarded.

# Example 2

`drumuri.in`
```
2
```

`drumuri.out`
```
1 3 4 2
6
```

## Explanation

For the second example, the paths are $(1)$, $(1, 3)$, $(1, 4)$, $(2)$, $(2, 3)$, $(2, 4)$ and $40 + (\frac{5}{6})^4 \cdot 60 = 68.93$ points will be awarded.

# Example 3

`drumuri.in`
```
3
```

`drumuri.out`
```
7 6 9 1 3 5 4 8 2
15
```

## Explanation

For the third example, the paths are $(1)$, $(1, 4)$, $(1, 4, 8)$, $(1, 3)$, $(1, 3, 5)$, $(1, 3, 5, 9)$, $(1, 3, 6)$, $(1, 3, 6, 7)$, $(1, 3, 8)$, $(1, 7)$, $(1, 3, 6, 9)$, $(2)$, $(2, 5)$, $(2, 5, 9)$, $(2, 8)$ and $73.85$ points will be awarded.
```