```markdown
Andrei lives on Dacia Boulevard and wants to find a new friend from the same street. Being interested in strong personalities, he studied each of his neighbors over the past week and assigned each a score, a natural number.
We say that an individual with a score of $A$ has a stronger personality than an individual with a score of $B$ if the highest exponent that appears in the prime factorization of $A$ is greater than the highest exponent that appears in the prime factorization of $B$. If these values are equal, then the maximum prime factor with the maximum exponent in $A$ must be greater than the maximum prime factor with the maximum exponent in $B$ for the first individual to have a stronger personality than the second. If this criterion does not decide, then the individual with the higher score is considered to have a stronger personality.

# Task

Given $N$, the number of Andrei's neighbors, and their associated scores, determine the score of the neighbor with the strongest personality.

# Input data

The first line contains a natural number, $N$ (the meaning given by the statement). The second line will contain $N$ natural numbers, the $i$-th of these representing the score of neighbor $i$.

# Output data

The first line will contain a single natural number, representing the score of the person with whom Andrei wishes to be friends.

# Constraints and clarifications

* $1 \leq N \leq 10 \ 000$;
* $2 \leq $ the score of any neighbor of Andrei $ \leq 100 \ 000$.

# Example 1

`stdin`
```
6
864 540 972 432 27000 4802
```

`stdout`
```
972
```

## Explanation

$864 = 2^5 \cdot 3^3$ 
$540 = 2^2 \cdot 3^3 \cdot 5$
$972 = 2^2 \cdot 3^5$
$432 = 2^4 \cdot 3^3$
$27000 = 2^3 \cdot 3^3 \cdot 5^3$
$4802 = 2 \cdot 7^4$

The highest exponents are for the numbers $864$ and $972$. Among these two numbers, $972$ is the score of the neighbor with the strongest personality, according to the second criterion.

# Example 2

`stdin`
```
4
45 81 27 50
```

`stdout`
```
81
```

## Explanation

$45 = 3^2 \cdot 5$
$81 = 3^4$
$27 = 3^3$
$50 = 2 \cdot 5^2$

The strongest personality is the neighbor with the score $81$, because the exponent $4$ is greater than the other exponents when comparing personalities.

# Example 3

`stdin`
```
3
75 50 75
```

`stdout`
```
75
```

## Explanation

$75 = 3 \cdot 5^2$
$50 = 2 \cdot 5^2$

According to the third criterion, the neighbor with the score $75$ has the strongest personality.
```