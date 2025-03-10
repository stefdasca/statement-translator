
# Task

Two integers $a$ and $b$ are given. Calculate the sum of all odd numbers greater than or equal to $a$ and less than or equal to $b$.

# Input data

The first line of the input file `sume-impare.in` contains two integers, $a$ and $b$.

# Output data

The first line of the output file `sume-impare.out` will contain a single integer $s$, the required sum.

# Constraints and clarifications

| # | Points |               Constraints                |
| - |  --   | ---------------------------------------- |
| 1 |   7   |               Examples                    |
| 2 |  45   | $a$, $b$, and $s$  $ \leq 10^9$           |
| 3 |  48   | $a$, $b$, and $s$  $ \leq 10^{18}$        |

# Example 1

`sume-impare.in`
```
4 15
```

`sume-impare.out`
```
60
```

## Explanation

We take odd numbers greater than $4$ and less than $15$, $5 + 7 + 9 + 11 + 13 + 15 = 60$.

# Example 2

`sume-impare.in`
```
15 26
```

`sume-impare.out`
```
120
```

## Explanation

$15 + 17 + 19 + 21 + 23 + 25 = 120$.
