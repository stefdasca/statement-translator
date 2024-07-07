
# Task

You are given $t$ pairs of positive natural numbers. For each pair, find the greatest common divisor (*gcd*) and the least common multiple (*lcm*).

We define the greatest common divisor (*gcd*) of a pair of numbers $(a, b)$ as the largest number that is a divisor of both $a$ and $b$. We denote $x = (a, b)$.

We define the least common multiple (*lcm*) of a pair of numbers $[a, b]$ as the smallest number that is a multiple of both $a$ and $b$. We denote $x = [a, b]$.

# Input data

The first line contains $t$, the number of tests. The following $t$ lines contain the two numbers from each pair, $a$ and $b$.

# Output data

Each of the $t$ lines will contain in order two numbers, representing the *gcd* and *lcm* of the two numbers.

# Constraints and clarifications

* $1 \leq t \leq 10^5$
* $1 \leq a, b \leq 10^9$
* For tests worth $40$ points, $1 \leq a, b \leq 10^5$.

# Example

`stdin`
```
5
14 8
55 33
63 94
39 27
24 54
```

`stdout`
```
2 56
11 165
1 5922
3 351
6 216
```

## Explanation

$(14, 8) = 2$, $[14, 8] = 56$, etc.
