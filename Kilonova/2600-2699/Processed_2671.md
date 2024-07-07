
# Task

For a given natural number $n$, what is the smallest natural number $x$ whose reverse is strictly greater than $n$?

The reverse of a natural number is obtained by reading the number from right to left. For example:

- The reverse of $0$ is $0$.
- The reverse of $1234$ is $4321$.
- The reverse of $8430982$ is $2890348$.
- The reverse of $1200$ is $0021 (=21)$.

# Input data

The input file `oglinditus.in` will contain the number $n$.

# Output data

The output file `oglinditus.out` will contain the smallest natural number $x$ whose reverse is strictly greater than $n$.

# Constraints and clarifications
- $1 \le n \le 10^{18}$
|#|Points|Constraints                            |
|-|-------|--------------------------------------|
|1| 10    | $n \le 10$                           |
|2| 10    | $n$ is a power of $10$               |
|3| 30    | $n \le 10^6$                         |
|4| 20    | $n \le 10^9$                         |
|5| 30    | No additional constraints            |

# Example 1

`oglinditus.in`

```
9
```

`oglinditus.out`
```
11
```

## Explanation

The reverse of $11$ is $11 > 9$.

# Example 2

`oglinditus.in`

```
800
```

`oglinditus.out`
```
108
```

## Explanation

The reverse of $108$ is $801 > 800$.

# Example 3

`oglinditus.in`

```
97
```

`oglinditus.out`
```
89
```

## Explanation

The reverse of $89$ is $98 > 97$.
```
