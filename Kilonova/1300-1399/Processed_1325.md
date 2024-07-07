Let's consider a sequence of $n$ chemical substances $s = s_1, s_2, \ldots, s_n$. The substances are distinctly numbered from $1$ to $n$, and each substance appears exactly once in the sequence $s$.

Let's consider a subarray $s_{i, j} = (s_i, s_{i + 1}, \ldots, s_j)$ and denote $\\text{min}_{i, j}$ and $\\text{max}_{i, j}$ as the smallest and largest numbers in the subarray, respectively. The respective subarray constitutes an interval if it contains all natural numbers between $\\text{min}_{i, j}$ and $\\text{max}_{i, j}$.

Different experiments will be conducted with the substances in sequence $s$. During an experiment, two _adjacent_ substances $s_i$ and $s_{i + 1}$ can react only if their order numbers are consecutive. Following the reaction, a new substance, formed from the reacting substances, denoted as $(s_i, s_{i + 1})$ is obtained. Furthermore, the obtained substances can react if they are adjacent, and by merging the subarrays of the substances that compose them, an interval is obtained. The experiment is declared successful if, in the end, following the above rules, a single substance formed from all $n$ substances in sequence $s$ is obtained, and this is declared **stable**.

For example, for $n = 6$ substances and sequence $s = 6, 3, 2, 1, 4, 5$, we can proceed as follows:

| Step | Action | Configuration |
| ----- | ------- | ------------ |
| $1$ | Initial sequence | $6 \\ 3 \\ 2 \\ 1 \\ 4 \\ 5$ |
| $2$ | React substance $2$ with $1$ and obtain substance $(2, 1)$ | $6 \\ 3 \\ (2, 1) \\ 4 \\ 5$ |
| $3$ | React substance $4$ with substance $5$ and obtain substance $(4, 5)$ | $6 \\ 3 \\ (2, 1) \\ (4, 5)$ |
| $4$ | React substance $3$ and $(2, 1)$ resulting in $(3, 2, 1)$ | $6 \\ (3, 2, 1) \\ (4, 5)$ |
| $5$ | React substances $(3, 2, 1)$ and $(4, 5)$ resulting in substance $(3, 2, 1, 4, 5)$ | $6 \\ (3, 2, 1, 4, 5)$ |
| $6$ | React substance $6$ with $(3, 2, 1, 4, 5)$ resulting in stable substance $(6, 3, 2, 1, 4, 5)$ | $(6, 3, 2, 1, 4, 5)$ |

It is not always possible to obtain a stable final substance from any sequence of substances following the reactions.

# Task

Determine for a given sequence of substances, if following the reactions that can occur according to the rules in the statement, a stable substance will result.

# Input data

The input file `reactii.in` contains on the first line the natural number $n$, the number of substances. The second line contains a natural number $m$, representing the number of sequences of $n$ substances in the input file. Each of the next $m$ lines contains $n$ distinct natural numbers, separated by a space, representing a sequence of $n$ substances.

# Output data

The output file `reactii.out` contains, for each sequence of substances in the input file, one line, which contains the value 1 if a stable substance can be obtained for the respective sequence or the value 0 otherwise.

# Constraints and clarifications

* $2 \leq n \leq 15\ 000$
* $1 \leq m \leq 20$
* At one moment, only two substances can react.

# Example

`reactii.in`
```
6
4
6 3 2 1 5 4
3 4 1 6 5 2
2 3 1 5 4 6
6 2 3 1 4 5
```

`reactii.out`
```
1
0
1
1
