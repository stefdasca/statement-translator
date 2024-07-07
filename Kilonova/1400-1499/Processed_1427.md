
# Task

Determine a strictly increasing sequence of length $N$ consisting of positive natural numbers, $1 \leq a_1 < a_2 < a_3 < \dots < a_N \leq \lfloor 2 \cdot N \cdot \sqrt{N} \rfloor$, with the property that any three distinct terms of the sequence do not form an arithmetic progression, i.e., for any natural numbers $i$, $j$, and $k$ with $1 \leq i < j < k \leq N$, the condition $a_i + a_k \neq 2 \cdot a_j$ is met. Here, $\\lfloor x \\rfloor$ denotes the floor function of $x$.

For example, for $N = 5$, the largest term of the sequence must be less than or equal to $\lfloor2 \cdot 5 \cdot \sqrt{5} \rfloor$, that is, $a_N \leq 22$, so a solution is: $1, 2, 4, 5, 10$.

# Input data

The input file `progresie.in` contains on the first line the natural number $N$ as described above.

# Output data

The output file `progresie.out` will contain on the first line, separated by a space, the $N$ elements of the sequence $a_i$, $1 \leq i \leq N$.

# Constraints and clarifications

* $3 \leq N \leq 20\ 000$
* If the solution is not unique, any correct solution will be accepted.

# Example 1

`progresie.in`
```
5
```

`progresie.out`
```
1 2 4 5 10
```

# Example 2

`progresie.in`
```
7
```

`progresie.out`
```
3 5 6 11 12 14 15
```
