# Task

In ***Wonderland O(1)***, *Square* has a beautiful garden with $N$ plants arranged in a line, **numbered starting from $1$**, from left to right. To keep himself entertained, *Square* decided to assign each plant among the $N$ an integer called the *beauty coefficient*, which represents how beautiful the plant is in our character's vision. Thus, $c_i \\ (1 \\leq i \\leq N)$ represents the *beauty coefficient* of the plant numbered $i$.

On a spring day, in ***Wonderland O(1)***, comes *Triangle*, one of *Square*'s best friends. A whimsical being and an exceptional chemist, *Triangle* plans to conduct $M$ experiments on the $N$ plants in *Square*'s garden. Each experiment is characterized by a certain integer value $e_j \\ (1 \\leq j \\leq M)$, meaning that after experiment $j$ is conducted, the *beauty coefficient* of each of the $N$ plants will increase by $e_j$. More precisely, $c_1$ becomes $(c_1 + e_j)$, $c_2$ becomes $(c_2 + e_j)$, $\\dots$, $c_N$ becomes $(c_N + e_j)$.

Time flies unexpectedly fast in ***Wonderland O(1)***, so winter makes its appearance, but not alone — it comes along with *Circle*, *Square*'s grandfather. *Circle* wishes to investigate *Square*'s garden in detail, and one day he decides to give $Q$ queries. The $k$-th query out of $Q \\ (1 \\leq k \\leq Q)$ is characterized by three integers: $left_k$, $right_k$, and $t_k$. It is required to find the minimum index $pos \\ (0 \\leq pos \\leq M)$, such that after conducting the first $pos$ experiments (out of $M$), each plant $i$, with $left_k \\leq i \\leq right_k$, satisfies: $c_i \\geq t_k$. If there is no such value $pos$, you will respond with $−1$. **Attention!** $pos = 0$ (experiments) represents the initial state of the garden, before conducting any experiment.

# Input data

The input file `wonderland.in` contains on the first line the natural non-zero number $N$, representing the number of plants in *Square*'s garden. The second line of the file contains $N$ integers, separated by a space, representing the initial *beauty coefficients* of the plants. More precisely, the $i$-th number on the second line represents the initial *beauty coefficient* of the plant indexed $i$, i.e., $c_i$. The third line of the file contains the natural non-zero number $M$. The fourth line of the file contains $M$ integers, separated by a space, representing, in order, the values: $e_1, e_2, e_3, \\dots, e_M$. The fifth line of the file contains the natural non-zero number $Q$. The next $Q$ lines contain, in order, the description of the $Q$ queries given by *Circle*, on the $k$-th line of $Q$ being $left_k, right_k$, and $t_k$.

# Output data

The output file `wonderland.out` contains $Q$ lines. On the $k$-th line, you will print the answer for the $k$-th query, in the order they were given by *Circle*.

# Constraints and clarifications

- $1 \\leq N \\leq 10^5$
- $1 \\leq M \\leq 10^6$
- $−10^9 \\leq c_i \\leq 10^9$, for any $1 \\leq i \\leq N$
- $−10 \\leq e_j \\leq 100$ and $e_j \\not= 0$, for any $1 \\leq j \\leq M$
- The $M$ experiments are conducted in order: $1, 2, 3, \\dots, M$.
- The *beauty coefficients* **DO NOT** *reset* before each experiment! Changes made by one experiment are preserved for all subsequent experiments.
- $1 \\leq Q \\leq 10^5$
- $1 \\leq left_k \\leq right_k \\leq N$, for any $1 \\leq k \\leq Q$
- $−10^9 \\leq t_k \\leq 10^9$, for any $1 \\leq k \\leq Q$
- The experiments designed by *Triangle* are conducted with *Square*'s approval.

| # | Points | Constraints |
| - | ------- | ---------- |
| 1 | 11 | $N, M, Q \\leq 260$ and $e_j > 0$, for any $1 \\leq j \\leq M$ |
| 2 | 14 | $N, M, Q \\leq 10^4$ and $e_j > 0$, for any $1 \\leq j \\leq M$ |
| 3 | 16 | $N, Q \\leq 10^4$ and $e_j > 0$, for any $1 \\leq j \\leq M$ |
| 4 | 17 | $N, Q \\leq 10^4$ |
| 5 | 19 | $e_j > 0$, for any $1 \\leq j \\leq M$ |
| 6 | 23 | Without other additional constraints. |

# Example

`wonderland.in`
```
4
17 25 9 -2
3
4 -8 100
4
1 4 500
2 4 70
1 2 20
1 3 7
```

`wonderland.out`
```
-1
3
1
0
```

## Explanation

In *Square*'s garden, there are $4$ plants. Initially, before conducting any experiment, their *beauty coefficients* are: $(17, 25, 9, -2)$; plant $1$ has the *beauty coefficient* $c_1 = 17$, plant $2$ has the *beauty coefficient* $c_2 = 25$, plant $3$ has the *beauty coefficient* $c_3 = 9$, plant $4$ has the *beauty coefficient* $c_4 = −2$.

*Triangle* conducts $3$ experiments on the $4$ plants in the garden, as follows:
* After conducting the first experiment, the *beauty coefficients* will be: $(21, 29, 13, 2)$.
* After conducting the first two experiments, the *beauty coefficients* will be: $(13, 21, 5, -6)$.
* After conducting the three experiments, the *beauty coefficients* will be: $(113, 121, 105, 94)$.