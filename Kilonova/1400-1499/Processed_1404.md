
Consider the sequence of distinct positive integers $a_1, a_2, \dots, a_N$. We denote by $L_i$ the maximum length of a subsequence of consecutive values that can be obtained by sorting in ascending order the first $i$ elements of the given sequence. For example, for the sequence $7, 2, 3, 8, 20, 4, 10, 9$, we have:
$L_1 = 1$, $L_2 = 1$, $L_3 = 2$, $L_4 = 2$, $L_5 = 2$, $L_6 = 3$, $L_7 = 3$, $L_8 = 4$.

# Task

Determine $L_1, L_2, \ldots, L_N$.

# Input data

The file `secvente.in` contains on the first line the natural number $N$. Each of the following $N$ lines contains a natural number; thus, on line $i+1$ will be the element $a_i$, for $i = 1,2, \dots, N$.

# Output data

The file `secvente.out` contains exactly $N$ lines. On line $i = 1,2, \dots, N$, the value $L_i$ will be printed.

# Constraints and clarifications

* $3 \leq N \leq 200 \ 000$
* $1 \leq a_i \leq 1 \ 000 \ 000$, for any $i = 1,2, \dots, N$
* For $35\%$ of tests it is guaranteed that $N \leq 1 \ 000$

# Example

`secvente.in`
```
8
7
3
2
8
20
4
10
9
```

`secvente.out`
```
1
1
2
2
2
3
3
4
```

## Explanation

- $L_1$: The sequence is $7$. The maximum length is $1$.
- $L_2$: The sequence is $7, 3$. The maximum length is $1$.
- $L_3$: The sequence is $7, 3, 2$. The sorted sequence is $\textcolor{red}{2, 3}, 7$. The maximum length is $2$ (given by the subsequence $2, 3$).
- $L_4$: The sequence is $7, 3, 2, 8$. The maximum length is $2$ (given by the subsequence $2, 3$).
- $L_5$: The sequence is $7, 3, 2, 8, 20$. The maximum length is $2$ (given by the subsequence $2, 3$).
- $L_6$: The sequence is $7, 3, 2, 8, 20, 4$. The sorted sequence is $\textcolor{red}{2, 3, 4}, 7, 8, 20$. The maximum length is $3$ (given by the subsequence $2, 3, 4$).
- $L_7$: The sequence is $7, 3, 2, 8, 20, 4, 10$. The maximum length is $3$ (given by the subsequence $2, 3, 4$).
- $L_8$: The sequence is $7, 3, 2, 8, 20, 4, 10, 9$. The sorted sequence is $2, 3, 4, \textcolor{red}{7, 8, 9, 10}, 20$. The maximum length is $4$ (given by the subsequence $7, 8, 9, 10$).
