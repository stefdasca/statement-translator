# Task

King Beetle Theodore is the owner of an ant farm, where ant $i$ is assigned the natural number $a_i$, and the king is assigned the number $x$. He, being a perfectionist owner, wishes the product of the ants' numbers to be a power of the number he holds. Knowing that a new ant will join the farm tomorrow, and King Theodore can choose its number, find the minimum number the new ant should be given.

# Input data

The first line of input contains two integers $N$ and $x$, where $N$ represents the number of ants already in the farm, and $x$ represents the number assigned to the king.

The next line contains $N$ natural numbers, where $a_i$ represents the number of ant $i$.

# Output data

Print a single number which will represent the answer to the king's question. Since the number can be too large, King Theodore requests only the remainder of this number modulo $10^9 + 7$.
If there is no solution, print $-1$.

# Constraints and clarifications

* $ 1 \leq N \leq 2 \cdot 10^5$
* $ 1 \leq X, a_i \leq 10^{12}$

|#| Points |        Constraints                                    | 
|-|---------|------------------------------------------------------|
|0|   0     | Examples                                              |
|1|   35    | $N, X, a_i \leq 10$                                  |
|2|   20    | $X, a_i \leq 10^6$                                   |
|3|   45    | no additional constraints                             |

# Example

`stdin`
```
4 6
8 6 4 6
```

`stdout`
```
243
```

## Explanation

The product of the existing ants is $1152$, and $6^{7}$ is $279\ 936$.