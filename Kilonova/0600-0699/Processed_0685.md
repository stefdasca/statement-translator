# Task

You are given three natural numbers $N$, $D$, and $K$, followed by $N$ natural numbers of exactly $K$ digits. Each of the $N$ numbers is divided into $X$ groups of $D$ digits each (the last group may not always be exactly $D$ digits).

On the next line, the number $Q$ is given, and on each of the next $Q$ lines, there are $X$ digits separated by a space. Let these be $c_1, c_2, \cdots c_X$. We define the power of a number in the array as the number of groups $i$ ($1 \leq i \leq X$) for which $c_i$ appears at least once in the $i$-th group of that number. For each of the $Q$ lines, display the position of the first number in the array that has the maximum power, as well as the maximum power. If the maximum power is $0$, display $-1$.

# Input data

The first line contains three natural numbers $N$, $D$, and $K$. The next $N$ lines contain the $K$-digit numbers, one per line. The next line contains the number $Q$. The next $Q$ lines contain $X$ digits separated by a space.

# Output data

The $Q$ lines will contain at most two numbers, representing the position of the first element with the maximum power and the maximum power, separated by a space. If the maximum power is $0$, print only $-1$.

# Constraints and clarifications

* $2 \\leq N \\leq 1000$;
* $2 \\leq K \\leq 2000$;
* $1 \\leq Q \\leq 1000$;
* $1 \\leq D \\leq K$
* Numbers may also start with digit $0$.
* The array of $N$ numbers is indexed from $1$.
| # | Points | Constraints                          |
| - | ------- | ------------------------------------ |
| $1$ | $12$   | $2 \\leq N, K \\leq 20$, $1 \\leq Q \\leq 10$   |
| $2$ | $6$    | $2 \\leq N, K \\leq 200$, $1 \\leq Q \\leq 50$ |
| $3$ | $17$   | $2 \\leq N, K \\leq 600$, $1 \\leq Q \\leq 300$|
| $4$ | $18$   | $2 \\leq N, K \\leq 400$, $1 \\leq Q \\leq 1000$|
| $5$ | $8$    | No other constraints                |
| $6$ | $40$   | No other constraints                |

# Example 1

`stdin`
```
3 3 10
1234581659
2870454321
9561840782
3
4 3 9 5
5 7 3 2
2 4 9 2
```

`stdout`
```
-1
3 2
1 2
```

## Explanation

The $n$ numbers divided into groups are:

$123 \\ \\ 458 \\ \\ 165 \\ \\ 9$

$287 \\ \\ 045 \\ \\ 432 \\ \\ 1$

$956 \\ \\ 184 \\ \\ 078 \\ \\ 2$

For the first query, no number contains the digit $4$ in the first group, the digit $3$ in the second group, the digit $9$ in the third group, or the digit $5$ in the last group, so $-1$ will be displayed.

For the second query, only the third number contains the digit $5$ in the first group, no number contains the digit $7$ in the second group, only the second number contains the digit $3$ in the third group, and only the third number contains the digit $2$ in the last group, so $3 \\ 2$ will be displayed, because the maximum is $2$ and it is at the third number.

For the third query, only the first number contains the digit $2$ in the first group, all $3$ numbers contain the digit $4$ in the second group, no number contains the digit $9$ in the third group, and only the last number contains the digit $2$ in the last group, so $1 \\ 2$ will be displayed, because the maximum $2$ appears at the first and third numbers, but the first number with the maximum is displayed.