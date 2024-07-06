```markdown
Two non-zero natural numbers $N$ and $K$ are considered. We define a $K$-sequence as a sequence of natural numbers with $K$ terms.

# Task

Determine the number formed by the last $4$ digits of the number of distinct $K$-sequences with the property that each of them has the least common multiple of the terms equal to $N$.

# Input data

The input file `multiplu.in` contains on the first line the two numbers $N$ and $K$ separated by a single space.

# Output data

The output file `multiplu.out` contains a single natural number representing the required result.

# Constraints and clarifications

* $1 \leq N, K \leq 10^9$;

# Example

`multiplu.in`
```
5 2
```

`multiplu.out`
```
3
```

## Explanation

The $3 \ 2$-sequences with the least common multiple of the terms equal to $5$ are: $(1, 5)$, $(5, 1)$ and $(5, 5)$.
```