```markdown
A square matrix $A_{ij}$ of dimensions $N \times N$ with odd $N$ is called a *spiral* matrix if it respects the following properties when traversed in a spiral as per the image below:

~[img.png|width=20em]

1. For any cell $(i, j)$ in the matrix, either $A_{ij} = 0$, or $A_{ij}$ *does not* contain the digit $0$.
2. Let $(i, j)$ be any cell except the center one and $(k, l)$ the previously traversed cell in the matrix, and let $c$ be any non-zero digit, i.e., from $1$ to $9$:
   - a) If $c$ divides $i + j$, then $A_{ij}$ contains the digit $c$ if and only if $A_{kl}$ *does not* contain the digit $c$.
   - b) If $c$ *does not* divide $i + j$, then $A_{ij}$ contains the digit $c$ if and only if $A_{kl}$ contains the digit $c$.
   - c) For the number in the center cell, being the first to be traversed, there are no such restrictions.
3. An element in the matrix will be $0$ if and only if it is not allowed to contain any digit from $1$ to $9$ according to the above rules.

# Task

Given a square matrix $A$ of dimension $N$, determine the minimum number of elements in the matrix that would need to be replaced (any other natural numbers can be written in those cells) for $A$ to become a spiral matrix.

# Input data

The first line of the input file `spirala.in` contains a single natural number $N$, representing the dimensions of the matrix. The next $N$ lines contain $N$ natural numbers each, separated by a space, representing the elements of matrix $A$.

# Output data

The output file `spirala.out` will contain a single number representing the minimum number of elements that need to be replaced for $A$ to become a spiral matrix.

# Constraints and clarifications

* $1 \leq N \leq 999$, $N$ odd.
* The elements of the matrix $A$ are natural numbers less than $10^9$ containing only digits from $1$ to $9$, with the exception of elements equal to $0$.

|#| Score |        Constraints                                                             | 
|-|---------|-------------------------------------------------------------------------------|
|1|   17    | A spiral matrix can be obtained by changing at most one element in matrix $A$ |
|2|   23    | $1 \leq N \leq 45$                                                            |
|3|   21    | $1 \leq N \leq 70$                                                            |
|4|   39    | Without additional restrictions                                               |

# Example

`spirala.in`
```
5
16 36 1234 23456 145
26 1469 4569 123459 457
1236 269 13579 234579 12578
346 12569 359 135789 235789
13456 245 12457 578 45789
```

`spirala.out`
```
2
```

## Explanation

To obtain a spiral matrix, the numbers in cells $(1, 3)$ and $(5, 5)$ should be replaced. In cell $(1, 3)$, the number $12 \ 345$ could be written and in cell $(5, 5)$, the number $13 \ 789$.
```