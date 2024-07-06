```
Let $N$ be a natural number. Consider all triplets of the form $(a, b, c)$, with $1 \leq a, b, c \leq N$, $a \neq b \neq c \neq a$, with the property that $c$ is the greatest common divisor of the numbers $a$ and $b$ ($c = \text{gcd}(a, b)$).

# Task

Given $N$, determine the value of the expression $a_1 \cdot b_1 \cdot c_1 + a_2 \cdot b_2 \cdot c_2 + \dots + a_k \cdot b_k \cdot c_k$, where $(a_1, b_1, c_1)$, $(a_2, b_2, c_2)$, ..., $(a_k, b_k, c_k)$ are all the triplets that meet the above conditions. Since the result can be very large, display the remainder of the expression when divided by the number $1\ 000\ 000\ 007$.

# Input data
The number $N$ is read from the keyboard.

# Output data
The screen will contain a single natural number $R$ representing the remainder of the division of the result of the above-described expression by the number $1\ 000\ 000\ 007$.

# Constraints and clarifications

* $3 \leq N \leq 10^6$

# Example

`stdin`
```
4
```

`stdout`
```
36
```

## Explanation

The valid triplets are: $(2, 3, 1)$, $(3, 4, 1)$, $(3, 2, 1)$, $(4, 3, 1)$.
$2 \cdot 3 \cdot 1 + 3 \cdot 4 \cdot 1 + 3 \cdot 2 \cdot 1 + 4 \cdot 3 \cdot 1 = 36$
The remainder of the number $36$ when divided by $1\ 000\ 000\ 007$ is $36$.
```