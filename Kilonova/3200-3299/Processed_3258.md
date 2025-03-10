
# Task

Marcel received a bag of balls from his grandmother with natural numbers inscribed on them. His grandmother, Bogdana, told him that some balls are friendly, and some are less friendly, and she taught him how to determine which is which. A number is called friendly if, in its prime factorization, all exponents are equal. A ball is called friendly if it has a friendly number inscribed on it. For example:
* The ball with the number $27000 = 2^3 \cdot 3^3 \cdot 5^3$ is friendly.
* The ball with the number $30184 = 2^3 \cdot 3^3 \cdot 11$ is not friendly.

Marcel wonders what is the percentage that, by extracting a single ball from the received bag, it will be a friendly ball.

# Input data

The first line contains a natural number $N$, representing the number of balls in the received bag, and the next line contains $N$ natural numbers which are the numbers inscribed on the balls.

# Output data

The first line will contain a natural number representing the percentage that the extracted ball is friendly. Provide the integer part of this percentage. $ \lfloor 57.64\% \rfloor = 57\% $

# Constraints and clarifications

* $1 \leq N \leq 100 \ 000$;
* $1 \leq x_i \leq 100 \ 000$.

# Example 1

`stdin`
```
11
1 2 3 4 5 6 7 8 9 10 11
```

`stdout`
```
100
```

## Explanation

All numbers are friendly.
* $2, 3, 5, 7, 11$ are prime numbers, so they are friendly.
* $1$ is also friendly.
* $4 = 2^2$ has a single exponent, so it is friendly.
* $6 = 2^1 \cdot 3^1$ has coefficients equal to $1$.
* $9 = 3^2$ has a single exponent, so it is friendly.
* $10 = 2^1 \cdot 5^1$ has coefficients equal to $1$.

# Example 2

`stdin`
```
9
12 18 20 24 28 40 44 45 48
```

`stdout`
```
0
```

## Explanation

None of the numbers are friendly.

# Example 3

`stdin`
```
7
1 12 9 48 7 7 12
```

`stdout`
```
57
```
