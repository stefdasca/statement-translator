Before the tiebreaker at the National Informatics Olympiad, G., trying to intuit the subjects, writes on a piece of paper all permutations with $N$ elements. At one point, they observe that some numbers in the permutation, located between positions $2$ and $N-1$, are strictly greater than their neighboring elements (situated on adjacent positions), while others are strictly smaller. G. names the greater elements as local maxima and the smaller elements as local minima. For example, the permutation $p = (4 \ 1 \ 2 \ 8 \ 5 \ 6 \ 7 \ 3)$ has two local minima, $1$ and $5$, and two local maxima, $8$ and $7$.
G. thinks of writing all permutations with $N$ elements that have $P$ local maxima and $Q$ local minima. Since the number of permutations is very large, G. abandons the problem. The next day, at the olympiad, the exact problem that G. had thought of appears.

# Task

Determine how many permutations with $N$ elements have $P$ local maxima and $Q$ local minima.

# Input data

The first and only line of the input file `intuitie.in` contains three natural numbers, $N$, $P$, and $Q$, with the meaning from the statement.

# Output data

The first line of the output file `intuitie.out` will contain the number of permutations with $N$ elements that have $P$ local maxima and $Q$ local minima, modulo $999 \ 017$.

# Constraints and clarifications

* $3 \leq N \leq 500$
* $0 \leq P, Q \leq N-2$
* $P + Q \leq N-2$
* $50\%$ of the tests have $N \leq 50$

# Example 1

`intuitie.in`
```
4 1 0
```

`intuitie.out`
```
6
```

## Explanation

The required permutations are $(1 \ 2 \ 4 \ 3)$, $(1 \ 3 \ 4 \ 2)$, $(1 \ 4 \ 3 \ 2)$, $(2 \ 3 \ 4 \ 1)$, $(2 \ 4 \ 3 \ 1)$, $(3 \ 4 \ 2 \ 1)$. In this example, all permutations have the local maximum element equal to $4$.