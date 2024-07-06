# Task

Andrei has $n$ carrots, conveniently numbered from $1$ to $n$, and a preferred number $k$.

Two carrots $a$ and $b$ are *compatible* if $gcd(a,b)+k=lcm(a,b)$, where:
- $gcd(a,b)$ represents the greatest common divisor of the numbers $a$ and $b$;
- $lcm(a,b)$ represents the least common multiple of the numbers $a$ and $b$.

In how many ways can Andrei choose two carrots $a$ and $b$ ($1 \le a<b \le n$) such that they are *compatible*?

# Input data

Each test contains multiple test cases. The first line of the input file `morcovi.in` will contain the number of test cases $t$.

Each test case consists of two numbers $n$ and $k$ — Andrei's number of carrots and Andrei's preferred number, respectively.

# Output data

For each test case, print in the output file `morcovi.out` the number of ways in which Andrei can choose two carrots $a$ and $b$ ($1 \le a<b \le n$) such that they are *compatible*.


# Constraints and clarifications

- $1 \le t \le 100$
- $1 \le n,k \le 10^9$
- To obtain points for a specific subtask, at least one submission must pass all tests in that subtask.
|#|Points|Constraints                    |
|-|-------|------------------------------|
|0| 0     | Example                      |
|1| 25    | $n,k \le 300$                |
|2| 21    | $n,k \le 3\,000$             |
|3| 18    | $n,k \le 50\,000$            |
|4| 12    | $t=1$                        |
|5| 24    | No further constraints |

# Example

`morcovi.in`
```
5
1000000000 1
30 6
6 10
420 69
123456789 987654321
```

`morcovi.out`
```
1
4
1
8
54
```

## Explanation

- In the first test case, the only way to choose the carrots is $a=1$ and $b=2$.
- In the second test case, the 4 ways to choose the carrots are: $(1,7)$, $(2,8)$, $(3,9)$, and $(6,12)$.
- In the third test case, the only way to choose the carrots is $a=4$ and $b=6$.
- In the fourth test case, the 8 ways to choose the carrots are: $(1,70)$, $(2,35)$, $(3,72)$, $(5,14)$, $(7,10)$, $(9,24)$, $(23,92)$, and $(69,138)$.