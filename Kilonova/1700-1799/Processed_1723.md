Irina likes natural numbers. She knows that any natural number with non-zero digits can be represented as a sequence of digits from the set $A = \{1, 2, \dots, 9 \}$. Irina chooses a digit $k$ and aims to find out how many natural numbers have the sum of the digits equal to a given number $S$ and at the same time are represented using only digits from the set $\{1, 2, \dots, k \}$.

# Task

Given $S$ and $k$, determine the **last digit** of the number of natural numbers that are represented only with digits from the set $\{1, \dots, k \}$ and have the sum of their digits equal to $S$.

# Input data

In the `numere.in` file, the first line contains the natural numbers $T$ and $k$, separated by a space, where $T$ represents the number of tests, and $k$ has the meaning from the statement. The second line contains $T$ natural numbers, separated by spaces. The $i$-th number on the second line represents the sum $S$ corresponding to the $i$-th test.

# Output data

In the `numere.out` file, print on the first line, separated by spaces, $T$ digits calculated according to the requirements, in the order given in the input file.

# Constraints and clarifications

* $1 \leq T \leq 10$
* $2 \leq k \leq 5$
* $1 \leq S \leq 2^{30}$

# Example

`numere.in`
```
2 3
3 5 
```

`numere.out`
```
4 3
```

## Explanation

With the digits $\{1, 2, 3\}$ and the sum of the digits equal to $3$, we can write the numbers $111$, $12$, $21$, $3$, thus $4$ numbers.

With the digits $\{1, 2, 3\}$ and the sum of the digits equal to $5$, we can write the numbers $11111$, $1112$, $1121$, $1211$, $2111$, $122$, $212$, $221$, $113$, $131$, $311$, $23$, $32$, thus $13$ numbers.