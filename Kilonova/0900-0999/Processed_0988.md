A string $x$ consisting of the letters $x_0, x_1, \ldots, x_{n-1}$ with $n > 0$ is called *k-partite of order k* if there exist $k$ and $p_1, p_2, \ldots, p_{k-1}$ with the properties:
* $0 < k \leq n$
* $0 < p_1 < p_2 < \ldots < p_{k-1} < n$
* $x_i = x_j$ for any $0 \leq i < j < p_1$
* $x_i = x_j$ for any $p_1 \leq i < j < p_2$
* $\ldots$
* $x_i = x_j$ for any $p_{k-1} \leq i < j < n$
* $x_{p_1-1} \neq x_{p_1}$, $x_{p_2-1} \neq x_{p_2}$, $\ldots$, $x_{p_k-1} \neq x_{p_k}$

For example, the length 8 strings `bbbawwww` and `daaaaddd` are k-partite of order $3$, the length 10 string `eeeeezzzzz` is k-partite of order $2$, and the length 5 string `yyyyy` is k-partite of order $1$.

# Task

Write a program which, for a string of letters $x=(x_0, x_1, \ldots, x_{n-1})$ of length $n$ and a natural number $k$, $0 < k \leq n$ determines the minimum number of letters that need to be removed from $x$ so that it becomes k-partite of order $k$. If this is not possible, it will display $-1$.

# Input data

The first line contains the numbers $n$ and $k$, separated by a space, as described above, and the second line contains the characters of the given string $x_0, x_1, \ldots, x_{n-1}$. These will not be separated by spaces.

# Output data

The first line contains a single natural number representing the determined result.

# Constraints and clarifications

* $1 \leq k \leq n \leq 5\ 000$;
* The string $x$ consists only of lowercase English letters.

|# | Points | Constraints |
| - | - | ------------|
|1|21|$n \leq 20$|
|2|36|$n \leq 100$|
|3|24|$n \leq 1\ 000$|
|4|19|No additional constraints.|

# Example 1

`stdin`
```
8 3
bbbawwww
```

`stdout`
```
0
```

## Explanation

No letter removal is necessary.

# Example 2

`stdin`
```
8 2
bbbawwww
```

`stdout`
```
1
```

## Explanation

Removing one letter *a* is enough so that the given string becomes k-partite of order $2$.

# Example 3

`stdin`
```
10 5
eeeeezzzzz
```

`stdout`
```
-1
```

## Explanation

It is not possible to achieve a k-partite string of order $5$ by removing letters from the given string.

# Example 4

`stdin`
```
10 2
bcbbxxbccc
```

`stdout`
```
3
```

## Explanation

Removing one letter *c* and the two *x* letters is enough so that the given string becomes k-partite of order $2$.