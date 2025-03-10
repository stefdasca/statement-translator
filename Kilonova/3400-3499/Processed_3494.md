
# Task

You are given $n$ integer numbers $a_1,a_2,\dots,a_n$. You must construct an **arithmetic progression** composed of integer numbers $b_1,b_2,\dots,b_n$ such that $|b_i-a_i|\le 1$ for each $1\le i\le n$.

# Input data

The first line contains the number $n$ (the length of the array $a$). The second line contains $n$ integer numbers $a_1,a_2,\dots,a_n$ (the elements of the array $a$).

# Output data

If there is no solution, print $-1$. Otherwise, the first line contains $n$ numbers $b_1,b_2,\dots,b_n$ (the elements of the arithmetic progression $b$, in order).

# Constraints and clarifications

For all test cases, $3 \le n \le 10^5$ and $1\le a_i\le 10^{12}$.

|#| Points | Constraints                                                  |
|-|---------|-------------------------------------------------------------|
|1|    9    | It is guaranteed that if a solution exists, then a possible solution is the array $b=a$. |
|2|   10    | $n=3$                                                       |
|3|    4    | $n=4$                                                       |
|4|   24    | $n\le 12$                                                   |
|5|   22    | $1\le a_i\le 10$ for any $1\le i\le n$                     |
|6|   31    |   No additional constraints                                 |

# Example 1

`stdin`
```
7
2 4 6 10 12 16 18
```

`stdout`
```
1 4 7 10 13 16 19
```

## Explanation

The only solution in this case is an arithmetic progression with a difference of $3$ and the first element $1$. The differences $b_i-a_i$ are as follows: $-1,0,+1,0,+1,0,+1$.

# Example 2

`stdin`
```
4
2 2 3 2
```

`stdout`
```
2 2 2 2
```

## Explanation

The difference can also be $0$.

# Example 3

`stdin`
```
4
4 3 2 1
```

`stdout`
```
4 3 2 1
```

## Explanation

The difference can also be negative, in this case $-1$.

# Example 4

`stdin`
```
3
1 8 9
```

`stdout`
```
-1
```
