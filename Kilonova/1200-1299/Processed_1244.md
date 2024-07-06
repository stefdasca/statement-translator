Some natural numbers have the property that they can be written as the sum of consecutive natural numbers (for example $7 = 3 + 4$, $10 = 1 + 2 + 3 + 4$, $18 = 3 + 4 + 5 + 6$). Moreover, some natural numbers can be written in multiple ways as the sum of consecutive natural numbers (for example $15 = 1 + 2 + 3 + 4 + 5 = 4 + 5 + 6 = 7 + 8$). We define the length of such a writing as the number of terms in the respective sum (for example, the writing $15 = 4 + 5 + 6$ has a length of $3$). If a natural number does not have this property (for example the number $4$), then the length of its writing is considered to be $1$. For a natural number, we define the value $\text{lmax}$ as the maximum length of all its writings as the sum of consecutive natural numbers (for example, for the number $15$ the value of $\text{lmax}$ is $5$, because all possible writings of the number $15$ are: $1 + 2 + 3 + 4 + 5$, $4 + 5 + 6$ and $7 + 8$ and the sum $1 + 2 + 3 + 4 + 5$ has the largest number of terms, namely $5$).

# Task

Given two non-zero natural numbers $a$ and $b$, $(a \leq b)$, calculate:
1. the number $\text{nr}$ representing the count of natural numbers greater than or equal to $a$ and less than or equal to $b$ that have such writings with a length of at least $2$
2. the number $\text{max}$ representing the maximum value of $\text{lmax}$ corresponding to such writings of all natural numbers greater than or equal to $a$ and less than or equal to $b$
3. the number $\text{nrmax}$ representing the count of natural numbers greater than or equal to $a$ and less than or equal to $b$ that have writings of length equal to $\text{max}$.

# Input data

The input file `suma.in` will contain the two non-zero natural numbers $a$ and $b$, separated by a space.

# Output data

The output file `suma.out` will contain
* the first line containing the value of the number $\text{nr}$
* the second line containing the value of the number $\text{max}$
* the third line containing the value of the number $\text{nrmax}$

# Constraints and clarifications
* $1 \leq a \leq b \leq 65\ 000$
* $0 \leq b - a \leq 100$
* For each test, partial scores will be awarded as follows:
    * for the correct calculation of the number $\text{nr}$, $40\%$ of the test score will be awarded
    * for the correct calculation of the number $\text{max}$, $30\%$ of the test score will be awarded
    * for the correct calculation of the number $\text{nrmax}$, $30\%$ of the test score will be awarded

# Example

`suma.in`
```
10 20
```

`suma.out`
```
10
5
2
```

## Explanation

Between $10$ and $20$ there are $11$ natural numbers, and the only number that does not have such a writing is $16$. The maximum length of a writing is $5$ and is obtained for $2$ numbers: $15 = 1 + 2 + 3 + 4 + 5$ and $20 = 2 + 3 + 4 + 5 + 6$.

