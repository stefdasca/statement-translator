# Task

Given an array $A$ with $N$ elements. We define $\\min(i,j)$ as the minimum value in the subarray $[i,j]$ of array $A$. Similarly, we define $\\max(i,j)$ as the maximum value in the subarray $[i,j]$ of array $A$. Additionally, there are $Q$ queries of the form $(X_i,Y_i)$ with the meaning "How many subarrays $[l,r]$ have $\\min(l,r)=X_i$ and $\\max(l,r)=Y_i$?".

# Input data

The first line contains the numbers $N$ and $Q$. The next line contains the elements $A_1,A_2, \\dots, A_N$.
Each of the following $Q$ lines contains two numbers $X_i$ and $Y_i$.

# Output data

Print $Q$ lines, where the $i$-th line contains the answer to the $i$-th query.

# Constraints and clarifications

* $1 \\leq N \\leq 10^5$
* $1 \\leq Q \\leq 100$
* $1 \\leq A_{i} \\leq N, \\forall\\ i \\in \\{1, 2, \\dots, N\\}$

| # | Points | Constraints | 
| - | ------ | ----------- |
| 1 | 41     | $1 \\leq N,Q \\leq 100$ |
| 2 | 59     | No additional constraints. |

# Example 1

`stdin`
```
7 5
3 5 3 4 2 1 5
2 5
3 5
1 2
2 4
2 4
```

`stdout`
```
2
5
1
2
2
```

# Example 2

`stdin`
```
15 10
7 9 2 13 12 13 11 13 13 13 10 5 13 7 2
5 13
7 13
11 13
5 10
7 13
2 9
7 9
2 9
11 13
11 13
```

`stdout`
```
25
1
15
1
1
2
1
2
15
15
```