
Given a natural number $n$ and a digit $k$ from the set $\{2, 3, 5, 7\}$.

# Task

Display the exponent of $k$ in the prime factorization of the product $1 \cdot 2 \cdot 3 \cdot \ldots \cdot n$.

# Input data

The input file `exponent.in` contains on the first line $n$ and $k$.

# Output data

The output file `exponent.out` will contain a single natural number, which is the exponent required by the problem.

# Constraints and clarifications

* $1 \leq n \leq 100$;
* $k \in \{2, 3, 5, 7\}$;

# Example

`exponent.in`
```
6 3
```

`exponent.out`
```
2
```

## Explanation

$1 \cdot 2 \cdot 3 \cdot \ldots \cdot 6 = 2^4 \cdot 3^2 \cdot 5$ and therefore $3$ has the exponent $2$ in the prime factorization.
