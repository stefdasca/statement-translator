Mutu is studying the C++ language and has just learned about functions and the "if" statement. To test his new skills, Surdu, his professor, assigned him the task of writing a function $f$ with $N$ integer arguments $x_1, \ldots, x_N$ that returns an integer. To make the task more challenging, the assignment includes $M$ additional constraints that the function $f$ must satisfy, specified by a matrix of size $M \times (N + 1)$, denoted as $A$, with rows and columns numbered from $1$ to $M$ and from $1$ to $N + 1$, respectively. The $i$-th constraint for $1 \leq i \leq M$ is that $f(A_{i,1}, \ldots, A_{i,N}) = A_{i,N + 1}$. Since Mutu is in a hurry to qualify for the national informatics team, he is asking you to do his homework: namely, to write the function $f$ for him.

Since Mutu's knowledge is still limited, the function $f$ must fit within the material taught; otherwise, Surdu will realize the attempt at fraud. Thus, the function $f$ must follow the following format, from which Mutu can only choose the number $l$ and the triplets $(i_1, j_1, k_1)$, $(i_2, j_2, k_2)$, $\ldots$, $(i_l, j_l, k_l)$:

```cpp
int f(int x1, ..., int xN) {
    if (xi1 == j1) return k1;
    if (xi2 == j2) return k2;
    ...
    if (xil == jl) return kl;
    return -1;
}
```

# Task

Given $N$, $M$ and the matrix $A$, determine $l$ and $l$ triplets $(i_1, j_1, k_1)$, $\ldots$, $(i_l, j_l, k_l)$ such that the function $f$ defined above satisfies the $M$ constraints. If no solution exists, specify this.

# Input data

The input file `graba.in` contains:
- The first line contains $N$ and $M$.
- The next $M$ lines contain $N + 1$ integers each, where the $j$-th number on the $i$-th of these lines represents the element $A_{i,j}$ of the matrix.

# Output data

If no solution exists, the output file `graba.out` will contain a single line with `-1`. Otherwise, the output file `graba.out` will contain $l$ lines, where the $x$-th line for $1 \leq x \leq l$ will contain the numbers $i_x, j_x, k_x$ separated by spaces.

# Constraints and clarifications

* $1 \leq N \cdot M \leq 1 \ 000 \ 000$
* $0 \leq A_{i,j} \leq 1 \ 000 \ 000$ for $1 \leq i \leq M$ and $1 \leq j \leq N + 1$
* $1 \leq i_x \leq N$ for $1 \leq x \leq l$
* $0 \leq j_x, k_x \leq 1 \ 000 \ 000$ for $1 \leq x \leq l$
* $1 \leq l \leq 2 \ 000 \ 000$. It is guaranteed that if a solution exists, it can be obtained with at most $2\ 000\ 000$ triplets.

| # | Score | Constraints                    |
| - | ----- | ------------------------------ |
| 1 |   11  | $N \cdot M \leq 50$            |
| 2 |   23  | $N \cdot M \leq 200\ 000$      |
| 3 |   18  | $N \cdot M \leq 500\ 000$      |
| 4 |   48  | No additional constraints      |

**Note:** Subtask 4 contains two test groups, worth $29$ and $19$ points respectively.

# Example 1

`graba.in`
```
4 3
3 2 3 4 4
8 2 2 5 4
3 3 3 6 2
```

`graba.out`
```
4 9 0
2 2 4
1 3 2
```

## Explanation

Mutu chooses $l = 3$ triplets $(4, 9, 0)$, $(2, 2, 4)$ and $(1, 3, 2)$, leading to the following function $f$ with $N = 4$ arguments:
```cpp
int f(int x1, int x2, int x3, int x4) {
    if (x4 == 9) return 0;
    if (x2 == 2) return 4;
    if (x1 == 3) return 2;
    return -1;
}
```
This function satisfies the $M = 3$ given constraints:
- $f(3, 2, 3, 4) = 4$
- $f(8, 2, 2, 5) = 4$
- $f(3, 3, 3, 6) = 2$

# Example 2

`graba.in`
```
2 4
0 0 0
0 1 1
1 0 1
1 1 0
```

`graba.out`
```
-1
```

## Explanation

No function $f$ in the given format satisfies the $M = 4$ given constraints.