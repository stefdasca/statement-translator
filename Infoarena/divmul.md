## Task

Two numbers $x$ and $y$ are given. Find the number of ordered pairs of the form $(p, q)$ such that:
- the greatest common divisor of $p$ and $q$ is $x$
- the least common multiple of $p$ and $q$ is $y$

## Input data

The input file `divmul.in` will contain multiple tests.
The first line contains a number $T$ which represents the number of tests.
The following $T$ lines contain two numbers $x$ and $y$ as described in the statement.

## Output data

The output file `divmul.out` will contain $T$ lines.
The line $i$ contains the number of solutions for the pair on line $i+1$ of the input file.

## Constraints

$2 \leq x \leq 10\ 000$

$2 \leq y \leq 100\ 000\ 000$

$T \leq 30\ 000$

## Example

`divmul.in`
```
1
3 60
```

`divmul.out`
```
4
```

## Explanation

The 4 pairs are:
- $(3, 60)$
- $(12, 15)$
- $(15, 12)$
- $(60, 3)$