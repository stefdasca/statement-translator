>Martin.

Martin chooses two natural numbers $a$ and $b$. He also chooses a number $k$ and calculates the numbers $x$ and $y$, which represent the remainders of $a$ and $b$ when divided by $k$.

# Task

Knowing the numbers $k$, $x$, $y$ and the sum $s = a+b$, determine if we can choose two numbers $a$ and $b$ that meet Martin's conditions.

# Input data

The first line contains 4 numbers $k$, $x$, $y$ and $s$ with the meanings stated in the problem.

# Output data

If it is possible to choose two numbers that meet the conditions, print `YES`, otherwise print `NO`.

# Constraints and clarifications

* $1 \leq k \leq 1 \ 000 \ 000 \ 000$;
* $0 \leq x, y < k$;
* $1 \leq s \leq 2 \ 000 \ 000 \ 000$;

# Example 1

`stdin`
```
5 2 4 11
```

`stdout`
```
YES
```

## Explanation

The solution $a=7$ and $b=4$ meets the conditions.

# Example 2

`stdin`
```
7 2 5 9
```

`stdout`
```
NO
```