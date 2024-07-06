```markdown
Let $n$ be a non-zero natural number.
Construct the set $M$ of all numbers formed by exactly $n$ digits, numbers formed only with the digits $1$ and $2$.

# Task

Write a program that reads the natural number $n$ and then determines the smallest natural number $x$ from the set $M$ with the property that $x$ is divisible by $2^n$.

# Input data

The file `doilan.in` contains on the first line the natural number $n$.

# Output data

The output file `doilan.out` will contain on the first line a natural number formed by $n$ digits, only digits $1$ and $2$, representing the smallest number $x$ from the set $M$, divisible by $2^n$.

# Constraints and clarifications

* $1 \leq n \leq 100$
* For $30\%$ of the score, $n \leq 18$

# Example 1

`doilan.in`
```
3
```

`doilan.out`
```
112
```

## Explanation

The smallest number of three digits, formed only with the digits $1$ and $2$, divisible by $2^3$, is $x = 112$. Thus, this number will be written on the first line of the output file `doilan.out`.
```