```markdown
Let $n$ and $p$ be two natural numbers.
We denote by $A(n, p)$ the set of all natural numbers with the following properties:
* They are greater than or equal to $2$ and less than or equal to $n$;
* Their prime factorization contains only exponents less than or equal to $p$.

Examples:
$A(15, 1) = \{2, 3, 5, 6, 7, 10, 11, 13, 14, 15\}$
$A(27, 2) = \{2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 25, 26\}$

# Task

Write a program that reads two natural numbers $n$ and $p$ and determines the cardinality of the set $A(n, p)$.

# Input data

The input file `cardinal.in` contains on the first line two natural numbers $n$ and $p$ separated by a space.

# Output data

The output file `cardinal.out` will contain on the first line the cardinality of the set $A(n, p)$.

# Constraints and clarifications
* $2 \leq n \leq 10 ^ 9$
* $1 \leq p \leq 10$

# Example 1

`cardinal.in`
```
15 1
```

`cardinal.out`
```
10
```

## Explanation

There are $10$ natural numbers less than or equal to $15$ that contain in their prime factorization exponents less than or equal to $1$.

# Example 2

`cardinal.in`
```
27 2
```

`cardinal.out`
```
22
```

## Explanation

There are $22$ natural numbers less than or equal to $27$ that contain in their prime factorization exponents less than or equal to $2$.
```