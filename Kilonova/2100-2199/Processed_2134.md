```markdown
Consider an array $v_1, v_2, \dots, v_N$ of integers. The *magic operation* consists of executing the following steps:

* Select a position $i$, $1 < i < N$.
* $v_i$ modifies its value to $v_{i-1} + v_{i+1} - v_i$.

You have the option to perform the *magic operation* as many times as you want.

# Task

Your goal is to transform the initial array into an array with the sum of elements as small as possible. Let $S$ be this sum, and $K$ the minimum number of applications of the *magic operation* to achieve an array with sum $S$.

# Input data

The first line contains the number $P$ ($1$ or $2$) which indicates the task that needs to be solved. The second line contains the natural number $N$ representing the length of the array. The third line contains $N$ integers separated by a space, the initial values of the array $v$.

# Output data

The output file will contain exactly one integer. If $P = 1$, this number must be $S$ (the minimum sum that can be obtained), and if $P = 2$, it should print $K$ (the minimum number of *magic operations* to obtain the sum $S$).

# Constraints and clarifications

* $1 \leq N \leq 500\ 000$
* $-10^{12} \leq v_i \leq 10^{12}$
* It is guaranteed that $S$ and $K$ can be represented as 64-bit signed integers.

|#|Score|Constraints|
|-|-|-|
|1|2|$P=1$, $N \leq 25$, $K \leq 5$|
|2|3|$P=2$, $N \leq 25$, $K \leq 5$|
|3|4|$P=1$, $N \leq 500$|
|4|6|$P=2$, $N \leq 500$|
|5|6|$P=1$, $N \leq 1\ 000$|
|6|9|$P=2$, $N \leq 1\ 000$|
|7|4|$P=1$, $K \leq 500\ 000$|
|8|6|$P=2$, $K \leq 500\ 000$|
|9|24|$P=1$|
|10|36|$P=2$|

# Example 1
`minimizesum.in`
```
1
5
0 6 14 9 9
```

`minimizesum.out`
```
0
```

# Example 2
`minimizesum.in`
```
2
5
0 6 14 9 9
```

`minimizesum.out`
```
4
```

## Explanation
In the first 2 examples, the *magic operation* can be successively applied at positions $3$, $2$, $4$, $3$:
$[0, 6, 14, 9, 9] \rightarrow [0, 6, 1, 9, 9]$  $\rightarrow [0, -5, 1, 9, 9] \rightarrow$   $[0, -5, 1, 1, 9] \rightarrow [0, -5, -5, 1, 9]$

Thus, we obtain in $4$ *magic operations* an array with sum $0 + (-5) + (-5) + 1 + 9 = 0$. A smaller sum cannot be obtained regardless of the number of *magic operation* applications.

# Example 3
`minimizesum.in`
```
1
15
21 19 14 9 8 5 5 4 3 3 7 13 19 28 37
```

`minimizesum.out`
```
184
```

# Example 4
`minimizesum.in`
```
2
15
21 19 14 9 8 5 5 4 3 3 7 13 19 28 37
```

`minimizesum.out`
```
6
```

## Explanation
In examples 3 and 4, the *magic operation* can be successively applied at positions $7$, $8$, $5$, $2$, $3$, $4$. The final array with sum $184$ will be:
$[21, 16, 11, 8, 6, 5, 4, 3, 3, 3, 7, 13, 19, 28, 37]$

# Example 5
`minimizesum.in`
```
1
25
139 101 61 17 -18 -54 -88 -119 -152 -182 -211 -238 -264 -276 -278 -276 -267 -245 -214 -178 -140 -95 -48 0 50
```

`minimizesum.out`
```
-2990
```

# Example 6
`minimizesum.in`
```
2
25
139 101 61 17 -18 -54 -88 -119 -152 -182 -211 -238 -264 -276 -278 -276 -267 -245 -214 -178 -140 -95 -48 0 50
```

`minimizesum.out`
```
5
```

## Explanation
In the last 2 examples, the *magic operation* can be successively applied at positions $3$, $2$, $3$, $8$, $5$.
```