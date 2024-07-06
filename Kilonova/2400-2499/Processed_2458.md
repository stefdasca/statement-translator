# Task

Let's define $f(X) =$ the absolute difference between $X$ and the sum of its divisors strictly less than $X$. 

For example:
$f(6) = 0$, because the divisors of $6$, smaller than $6$, are $1,2,3$, and their sum is $1 + 2 + 3 = 6$. Finally, $6 - 6 = 0$.
$f(11) = 10$
$f(24) = 12$

You are given $2$ numbers $A$ and $B$. You need to calculate $\displaystyle \sum_{i=A}^{B} \ f(i)$.

# Input data

The first line of the input file `sum-div.in` contains the $2$ numbers $A$ and $B$.

# Output data

The first line of the output file `sum-div.out` will contain a single number, the sum described in the task.

# Constraints and clarifications

* $1 \leq A \leq B \leq 10 \ 000 \ 000$;

# Example 1

`sum-div.in`
```
1 9
```

`sum-div.out`
```
21
```

## Explanation

$1 + 1 + 2 + 1 + 4 + 0 + 6 + 1 + 5 = 21$

# Example 2

`sum-div.in`
```
24 24
```

`sum-div.out`
```
12
```