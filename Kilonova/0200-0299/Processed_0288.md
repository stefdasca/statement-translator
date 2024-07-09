Given a sequence consisting of $N$ non-zero natural numbers: $a_1, a_2, \dots, a_N$. A *length $k$ 2-increasing subsequence* of the given sequence is any subsequence $a_{x_1}, a_{x_2}, \dots, a_{x_k}$, where $1 \le x_1 < x_2 < \dots < x_k \le N$, in which the following property is satisfied:
- $a_{x_i} < a_{x_{i+2}}$, for any $i$, $1 \le i \le k - 2$, meaning $a_{x_1} < a_{x_3} < a_{x_5} < \dots$ and $a_{x_2} < a_{x_4} < a_{x_6} < \dots$.

# Task
Given $T$ sequences as per the statement, determine the *maximum length* of a *2-increasing subsequence* for each of the $T$ given sequences.

# Input data
In the input file `s2c.in`, the first line contains the number $T$, representing the number of sequences, and on each of the next $2 \cdot T$ lines are the descriptions of the sequences. The $2 \cdot i$-th line contains a single natural number representing the number of elements $N_i$ in the $i$-th given sequence. The $2 \cdot i + 1$-th line contains $N_i$ natural numbers, representing the numbers in the sequence, separated by spaces.

# Output data
In the output file `s2c.out`, each of the $T$ lines contains a single natural number. The $i$-th line contains a natural number representing the maximum length of a *2-increasing subsequence* of the $i$-th sequence from the $T$ given sequences.

# Constraints and clarifications
* $1 \le T \le 10$
* $1 \le N_i \le 2\ 000$, for each $i$, $1 \le i \le T$.
* For $30\%$ of the score $1 \le N_i \le 400$, for each $i$, $1 \le i \le T$.
* For $60\%$ of the score $1 \le N_i \le 1\ 000$, for each $i$, $1 \le i \le T$.
* The elements in each sequence are non-zero natural numbers from the set $\{1, 2, 3, \dots, 30\ 000\}$.

# Example
`s2c.in`
```
2
8
1 1 3 2 5 3 4 5
5
9 6 4 2 7
```

`s2c.out`
```
6
3
```

## Explanation
We have $T = 2$ tests.

The first sequence has a length of $8$. The 2-increasing subsequences of maximum length $6$ are:
- $1, 1, 3, 2, 5, 3$
- $1, 1, 3, 2, 5, 4$
- $1, 1, 3, 2, 5, 5$
- $1, 1, 3, 2, 4, 5$
- $1, 1, 2, 3, 4, 5$

The second sequence has a length of $5$. The 2-increasing subsequences of maximum length $3$ are:
- $6, 4, 7$
- $6, 2, 7$
- $4, 2, 7$