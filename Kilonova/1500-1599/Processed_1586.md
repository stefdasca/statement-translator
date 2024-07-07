
Given $N$ triplets of natural numbers ($a_i$, $b_i$, $c_i$), where $c_i \neq 0$ and $1 \leq i \leq N$, each representing a rational number $q_i$ equal to $\\frac{(-1)^{a_i} \cdot b_i}{c_i}$.

# Task
Find a non-empty subsequence of the sequence $q_1$, $q_2$, ..., $q_N$ whose product of values is as large as possible.

# Input data

The input file `colibri.in` contains on the first line the number $N$. The next $N$ lines describe the $N$ triplets: line $i$ contains the natural numbers $a_i$, $b_i$, $c_i$, separated by spaces.

# Output data

The first line of the output file `colibri.out` contains a sequence of $N$ digits. Digit $i$, where $1 \leq i \leq N$, is `1` if and only if $q_i$ is selected in the solution subsequence, otherwise it is `0`. The digits of the sequence should not be separated by spaces.

# Constraints and clarifications

* $1 \leq N \leq 50\ 000$;
* $0 \leq a_i, b_i \leq 1\ 000\ 000$, for any $1 \leq i \leq N$;
* $1 \leq c_i \leq 1\ 000\ 000$, for any $1 \leq i \leq N$;
* If there are multiple solutions, any correct solution is accepted;
* We say that a sequence $x$ is a subsequence of a sequence $y$ if and only if $x$ can be obtained from $y$ by eliminating some elements from $y$ (including none) without changing the relative order of the remaining elements.

| # | Score   | Constraints          |
| - | ------- | -------------------  |
| 1 | 30      | $N \leq 19$ and $a_i, b_i, c_i \leq 9$ |
| 2 | 20      | $N \leq 19$           |
| 3 | 20      | $a_i, b_i, c_i \leq 9$      |
| 4 | 30      | No additional constraints.      |

# Example 1

`colibri.in`
```
5
0 0 1
2 4 2
4 7 7
1 2 3
0 3 2
```

`colibri.out`
```
01001
```

## Explanation

In the example $N = 5$, $q_1 = \\frac{0}{1}$, $q_2 = \\frac{4}{2}$, $q_3 = \\frac{7}{7}$, $q_4 = -\\frac{2}{3}$ and $q_5 = \\frac{3}{2}$.

The maximum possible product is equal to $3$. This can be obtained either by taking the subsequence consisting of the numbers $q_2$ and $q_5$, or by taking the subsequence formed by the numbers $q_2$, $q_3$ and $q_5$. In other words, the answer `01101` is also correct.
```
