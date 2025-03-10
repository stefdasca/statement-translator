~[OIG2.jpeg|align=right|width=30%]`

Bobi has $N$ toys that can be colored in various colors. For each color, the interval $[L_i, R_i]$ is known, meaning that any toy in the interval $[L_i, R_i]$ can be colored in color $i$. A subset of toys is considered *compatible* if there is at least one common color in which all of them can be colored.

# Task

Count how many *compatible* subsets of toys exist, modulo ${10}^{9}+7$.

# Input data

The first line contains the numbers $N$ and $K$, representing the number of toys and the number of colors, respectively. The following $K$ lines contain two integers $L_i$ and $R_i$, representing the interval of toys that can be colored in color $i$.

# Output data

Print a single number, representing the number of compatible subsets of toys, modulo ${10}^{9}+7$.

# Constraints and clarifications

* $1 \leq N \leq 1 \ 000 \ 000 \ 000$
* $1 \leq K \leq 20$
* $1 \leq L_i \leq R_i \leq N$
* For tests worth $5$ points, $N \leq 20$
* For other tests worth $25$ points, $N \leq 10.000, K \leq 10$

# Example 1

`stdin`
```
5 3
1 4
2 3
4 5
```

`stdout`
```
18
```

## Explanation

The compatible subsets are: $\\empty$, $\\{1\\}$, $\\{2\\}$, $\\{3\\}$, $\\{4\\}$, $\\{5\\}$, $\\{1, 2\\}$, $\\{1, 3\\}$, $\\{1, 4\\}$, $\\{2, 3\\}$, $\\{2, 4\\}$, $\\{3, 4\\}$, $\\{4, 5\\}$, $\\{1, 2, 3\\}$, $\\{1, 2, 4\\}$, $\\{1, 3, 4\\}$, $\\{2, 3, 4\\}$, $\\{1, 2, 3, 4\\}$. For example, the subset $\\{1, 5\\}$ would not be compatible because toys $1$ and $5$ do not have any common color.

# Example 2

`stdin`
```
5 1
1 5
```

`stdout`
```
32
```

## Explanation

All subsets are compatible.