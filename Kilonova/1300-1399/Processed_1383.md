The problem collection has $P$ pages, numbered from $1$ to $P$. The problems in the collection are numbered $1$, $2$, $3$, $\dots$, etc., in the order they appear in the collection. On the first page of the collection, only one problem (number $1$) is written. On the second page, exactly two problems (numbers $2$ and $3$) are written in that order. On the third page, exactly three problems (numbers $4$, $5$, and $6$) are written in that order, $\dots$, on the $P$-th page, exactly $P$ problems are written.

# Task

Write a program that reads the natural numbers $P$ and $N$ and determines the values:

1. $T$, the total number of digits used in numbering all the problems in the collection;
2. $M$, the minimum number of pages needed for the collection to contain the problem numbered $N$.

# Input data

The file `culegere.in` contains on the first line the two natural numbers $P$ and $N$ separated by a space, as described in the statement.

# Output data

The file `culegere.out` contains:

* the first line containing the natural number $T$, as described in the statement;
* the second line containing the natural number $M$, as described in the statement.

# Constraints and clarifications

* $1 \leq P \leq 16\ 000$;
* $1 \leq N \leq 2\ 112\ 600\ 000$;
* solving task $1$ correctly grants $50\%$ of the points;
* solving task $2$ correctly grants $50\%$ of the points.

# Example

`culegere.in`
```
5 9
```

`culegere.out`
```
21
4
```

## Explanation

The problems are numbered as follows:
* $1$ (page $1$)
* $2$, $3$ (page $2$)
* $4$, $5$, $6$ (page $3$)
* $7$, $8$, $9$, $10$ (page $4$)
* $11$, $12$, $13$, $14$, $15$ (page $5$)

Writing these numbers used $21$ digits $\rightarrow\ T = 21$.

To contain the problem numbered $9$, the collection needs to have at least $4$ pages $\rightarrow\ M = 4$.