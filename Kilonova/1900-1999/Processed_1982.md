# Task

You are given $q$ queries. For each of the $q$ queries, two values $n$ and $k$ will be given. Calculate $C_n^k \text{ mod } (10^9+7)$, where $C_n^k$ represents the combinations of $n$ taken $k$ at a time.

# Input data

The first line of the file `combination.in` will contain $q$, the number of queries. Each of the following $q$ lines will contain two natural numbers, $n$ and $k$.

# Output data

For each of the $q$ queries, print the required answer in the `combination.out` file. Because these values can be very large, you are required to print only the remainder when divided by $10^9+7$.

# Constraints and clarifications

* $10^9 + 7$ is a prime number.
* $0 \leq q \leq 10^5$
* $0 \leq k \leq n \leq 10^5$

|#|Score|Constraints|
|-|-|-|
|0|0|Example|
|1|20|$0 \leq n, q \leq 5 \cdot 10^3$|
|2|40|$0 \leq n, q \leq 10^4$|
|3|40|No additional constraints|

# Example

`combination.in`
```
11
7 5
35 20
85 40
67 40
44 7
76 69
60 35
44 43
28 20
44 13
93 17
```

`combination.out`
```
21
247943139
221670461
845448992
38320568
186189386
610920233
44
3108105
915526075
419070982
```

## Explanation

$C_7^5 \text{ mod } (10^9+7) = 21$.