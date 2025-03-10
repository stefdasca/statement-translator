Gigel has a matrix with $N$ rows and $M$ columns in which each cell contains a digit. He writes on each row $i$ of the matrix (from left to right) the $i$-th Fibonacci number. If the number has more than $M$ digits, then he writes only the last $M$ digits.

For example, for $N = 13$ and $M = 2$, he will obtain the matrix:

| 0 | 1 |
|---|---|
| 0 | 1 |
| 0 | 2 |
| 0 | 3 |
| 0 | 5 |
| 0 | 8 |
| 1 | 3 |
| 2 | 1 |
| 3 | 4 |
| 5 | 5 |
| 8 | 9 |
| 4 | 4 |
| 3 | 3 |

# Task

Gigel gives you $Q$ questions of the form $C, L, R$: how many times does the digit $C$ appear between lines $L$ and $R$ (including lines $L$ and $R$).

# Input data

The first line contains $N$, $M$, and $Q$.

The next $Q$ lines contain the queries, in the form $(C, L, R)$.

# Output data

The output file will contain $Q$ lines, each line containing the answer corresponding to a query.

# Constraints and clarifications

* $1 \leq N \leq 10^{17}$
* $1 \leq M \leq 6$
* $1 \leq Q \leq 10^5$
* $0 \leq C \leq 9$
* $1 \leq L \leq R \leq N$
* Gigel reminds you that the Fibonacci sequence starts with $1, 1$ and each element is equal to the sum of the last two.

| #    | Score | Constraints                  |
| ---- | ------ | ---------------------------- |
| 1    | 10     | $1 \leq N \leq 10^6$         |
| 2    | 30     | $M = 1$                      |
| 3    | 60     | No additional constraints    |

# Example

`stdin`
```
13 2 3
1 1 7
4 8 12
0 1 13
```

`stdout`
```
3
3
6
```

## Explanation

Between lines 1 and 7 there are 3 digits of 1, between lines 8 and 12 there are 3 digits of 4, and between lines 1 and 13 there are 6 digits of 0.