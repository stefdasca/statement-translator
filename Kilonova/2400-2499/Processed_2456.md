
We define the following two operations that can be performed on a stack:

* $push(x)$ — the number $x$ is added to the top of the stack
* $pop$ — the number at the top of the stack is removed from the stack

A sequence of operations is considered _correct_ if, when the operations are performed in order on an initially empty stack, the following two conditions are met:

1. No $pop$ operation is performed on an empty stack.
2. After the last operation, the stack is empty.

For example, $(push(1), \ pop)$ is a correct sequence, whereas $(push(1), \ push(2))$ or $(pop, \ push(1))$ are not correct sequences.

We consider a list $L_1, \dots , L_N$ of operations, numbered from $1$ to $N$. By $s(i, j)$, where $i \leq j$, we define the sequence of operations $L_i, L_{i+1}, \dots , L_j$.

We define the value $maxstack(i, j)$ as follows. If $s(i, j)$ is not a correct sequence, then by definition $maxstack(i, j) = 0$. Otherwise, we perform the operations $L_i, L_{i+1}, \dots , L_j$ in order on an initially empty stack. After each operation, we compute the maximum value in the stack. Let $m_k$ be the maximum value after operation $k$, or zero if the stack is empty. Then, $maxstack(i, j) = m_i + m_{i+1} + \dots + m_j$.

# Task

Given $N$, the list $L$ of operations, a number $Q$ and $Q$ queries of the form $(l, r)$, where $1 \leq l \leq r \leq N$. Additionally, a number $C$ is given. Based on the value of $C$, calculate the following values for each query:

1. If $C = 1$, calculate $maxstack(l, r)$ modulo $10^9 + 7$. **It is guaranteed that $s(l, r)$ is correct for all queries.**
2. If $C = 2$, calculate the sum of $maxstack(i, j)$ values for all $l \leq i \leq j \leq r$ modulo $10^9 + 7$. **It is guaranteed that for each query, if the operations in $s(l, r)$ are performed in order, no $pop$ operation is performed on an empty stack.**

# Input data

The first line of the input contains the value $C$. The second line contains the integers $N$ and $Q$. The third line contains the non-negative integers $X_1, X_2, \dots , X_N$, which encode $L_1, \dots , L_N$ as follows:

* If $X_i > 0$, then $L_i = push(X_i)$
* If $X_i = 0$, then $L_i = pop$

# Output data

Each of the $Q$ lines of output will contain the answers to the queries, in order. All answers must be given modulo $10^9 + 7$.

# Constraints and clarifications

* $1 \leq N, Q \leq 300 \ 000$
* $0 \leq X_i \leq 10^9$, for any $1 \leq i \leq N$
* It is guaranteed that $L_1, \dots , L_N$ is a correct sequence of operations
* We say that a sequence of operations is _finally empty_ if when performing these operations on an initially empty stack, the stack is empty only before the first operation and after the last operation. For example, $(push(1), \ pop)$ is _finally empty_, but $(push(1), \ pop, \ push(1), \ pop)$ is not.

| # | Points | Constraints          |
| - | ------- | ------------------- |
| 1 | 7      | $C = 1, N, Q \leq 100$ |
| 2 | 14      | $C = 1, N, Q \leq 100$      |
| 3 | 15      | $C = 1, X_i \leq 30$ and $s(l, r)$ is finally empty for all queries $(l, r)$     |
| 4 | 13      | $C = 1$      |
| 5 | 14      | $C = 2, s(l, r)$ is correct and finally empty for all queries $(l, r)$      |
| 6 | 11      | $C = 2, s(l, r)$ is correct for all queries $(l, r)$      |
| 7 | 10      | $C = 2, N \leq 70 \ 000, Q \leq 50$      |
| 8 | 11      | $C = 2, N, Q \leq 70 \ 000$      |
| 9 | 5      | $C = 2$      |

# Example 1

`stdin`
```
1
6 2
5 4 0 0 23 0
1 4
5 6
```

`stdout`
```
15
23
```

## Explanation

For the first query, we will perform the operations from $1$ to $4$ in order. After the first operation, the stack looks like this: $(5)$. $m_1 = 5$. After the second operation, the stack looks like this: $(5, 4)$. $m_2 = 5$. After the third operation, the stack looks like this: $(5)$. $m_3 = 5$. After the last operation, the stack is empty. $m_4 = 0. \ m_1 + m_2 + m_3 + m_4 = 5 + 5 + 5 + 0 = 15$.

# Example 2

`stdin`
```
1
10 4
22 0 26 0 72 447 0 497 0 0
1 10
3 10
8 9
1 4
```

`stdout`
```
1208
1186
497
48
```

## Explanation

For the first query, $m_1 + \dots + m_{10} = 22 + 0 + 26 + 0 + 72 + 447 + 72 + 497 + 72 + 0 = 1208.$

For the second query, $m_3 + \dots + m_{10} = 26 + 0 + 72 + 447 + 72 + 497 + 72 + 0 = 1186.$

For the third query, $m_8 + m_9 = 497 + 0 = 497.$

For the last query, $m_1 + m_2 + m_3 + m_4 = 22 + 0 + 26 + 0 = 48.$

# Example 3

`stdin`
```
2
10 5
22 0 26 0 72 447 0 497 0 0
1 10
3 10
8 9
1 4
1 9
```

`stdout`
```
5538
4260
497
96
1984
```

## Explanation

The $maxstack$ values for all subarrays $(i, j)$ are written in the table below. Cells where $i > j$ (for which the operation is not defined) are left empty.

|$_{j} \diagdown ^{i}$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ | $10$ |
| - | - | - | - | - | - | - | - | - | - | - |
| $1$ | $0$ |  |  |  |  |  |  |  |  |  |
| $2$ | $22$ | $0$ |  |  |  |  |  |  |  |  |
| $3$ | $0$ | $0$ | $0$ |  |  |  |  |  |  |  |
| $4$ | $48$ | $0$ | $26$ | $0$ |  |  |  |  |  |  |
| $5$ | $0$ | $0$ | $0$ | $0$ | $0$ |  |  |  |  |  |
| $6$ | $0$ | $0$ | $0$ | $0$ | $0$ | $0$ |  |  |  |  |
| $7$ | $0$ | $0$ | $0$ | $0$ | $0$ | $447$ | $0$ |  |  |  |
| $8$ | $0$ | $0$ | $0$ | $0$ | $0$ | $0$ | $0$ | $0$ |  |  |
| $9$ | $0$ | $0$ | $0$ | $0$ | $0$ | $944$ | $0$ | $497$ | $0$ |  |
| $10$ | $1208$ | $0$ | $1186$ | $0$ | $1160$ | $0$ | $0$ | $0$ | $0$ | $0$ |
