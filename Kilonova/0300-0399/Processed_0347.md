An interval $[a, b]$ is a giga-xor interval if and only if the *xor* sum of the natural numbers inside the interval $[a, b]$ is equal to $0$, where $a$ and $b$ are natural numbers.

Strictly speaking, an interval $[a, b]$ is giga-xor if and only if $a \oplus (a + 1) \oplus (a + 2) \oplus \ldots \oplus b = 0$.

You are given $T$ pairs of numbers $(a, b)$. For each pair, you need to find the length of the shortest interval $[x, y]$ such that $1 \le x \le a \le b \le y$ and $[x, y]$ is a giga-xor interval.

# Task

# Input data

The first line contains $T$ ($1 \leq T \leq 5 \cdot 10^5$), the number of pairs.

The following $T$ lines contain $2$ integers $a$, $b$ ($1 \leq a \leq b \leq 10^{18}$).

For tests worth $10$ points, $b \leq 100$

For tests worth $30$ more points, $b \leq 10^6$

# Output data

Print on $T$ lines, the answer for each pair.

# Example

`stdin`

```
5
4 5
2 3
1 7
8 8
1 10
```

`stdout`

```
4
3
7
4
11
```

