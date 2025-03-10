
# Task

Consider the following sequence $1$, $1$, $2$, $1$, $2$, $3$, $1$, $2$, $3$, $4$, $1$, $2$, $3$, $4$, $5$, $\\dots$. Given two positions $p$, $q$ in this sequence, determine:
1. The number of distinct values in the sequence located between the two positions, inclusively;
2. The distinct values in the sequence delimited by the two positions $p$ and $q$, in increasing order, each value followed by its number of occurrences.

# Input data

The first line of the input file `sir.in` contains three natural numbers $c$, $p$, and $q$ separated by a space representing: $c$ task, and $p$, $q$ the two positions in the sequence. For $c=1$, task $1$ is solved, and for $c=2$, task $2$.

# Output data

The output file `sir.out` contains:
- if $c=1$ - the first line contains a natural number representing the number of distinct values in the sequence located between the two positions $p$ and $q$, inclusively;
- if $c=2$ - successive lines contain two numbers separated by a space, representing a distinct value from the sequence followed by its number of occurrences.

# Constraints and clarifications

* $1 \leq p \leq q \leq 1 \ 000 \ 000 \ 000$;
* for tests worth $37$ points, $c=1$

# Example 1

`sir.in`
```
1
3 12
```

`sir.out`
```
4
```

# Example 2

`sir.in`
```
2
3 12
```

`sir.out`
```
1 3
2 4
3 2
4 1
```

## Explanation

In this example, task $2$ is solved. The distinct numbers in the sequence located between positions $3$ and $12$ (inclusive) are $1$, $2$, $3$, $4$, and their number of occurrences is $3$, $4$, $2$, $1$.
