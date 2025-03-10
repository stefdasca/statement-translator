To solve the competitive programming problem, you'll need to translate the given text from Romanian to English, while keeping the mathematical values, variable names, general syntax, structure, format, and custom image format intact. Here's how the translated statement would look:

---

For a sequence $a_1, a_2, \dots, a_N$ of integer numbers, you want to apply a sequence of operations in order to obtain a new sequence $b$, also of length $N$. Initially, the sequence $b$ is empty.

In one operation you perform one of the following:

1. Choose all even positions ($2, 4, 6, \dots$) in $a$ and add them in this order to the end of sequence $b$. After that, remove all these elements from $a$. **This operation can only be applied if the sequence $a$ still contains at least $2$ elements** (note that if the sequence $a$ has only one element, then applying this operation would not change either $a$ or $b$).
2. Choose all odd positions ($1, 3, 5, \dots$) in $a$ and add them in this order to the end of sequence $b$. Then remove all these elements from $a$. This operation can be applied regardless of the length of $a$.

Operations are repeated until the sequence $a$ becomes empty.

For example, for the sequence $[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]$, a valid sequence of operations is $1, 2, 2, 2$.

$a: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] \xrightarrow[]{1} [1, 3, 5, 7, 9] \xrightarrow[]{2} [3, 7] \xrightarrow[]{2} [7] \xrightarrow[]{2} []$.

$b: [] \xrightarrow[]{1} [2, 4, 6, 8, 10] \xrightarrow[]{2} [2, 4, 6, 8, 10, 1, 5, 9] \xrightarrow[]{2} [2, 4, 6, 8, 10, 1, 5, 9, 3] \xrightarrow[]{2} [2, 4, 6, 8, 10, 1, 5, 9, 3, 7]$.

It is noted that the last operation must be of type $2$, because sequence $a$ contained only one element ($7$).

# Task

Given $N$, the sequence $a$, and $Q$ queries in the form $L \ R$, determine for each query in how many ways we can apply the operations so that $L \leq S_b \leq R$, where $S_b$ is the maximum sum of a subarray from $b$.

# Input data

The first line of the file `parimpar.in` contains the integers $N, Q$ in this order.
The second line contains the sequence $a_1, a_2, \dots, a_N$.
For each $i$ from $1$ to $Q$, line $i + 2$ contains two numbers, $L$ and $R$, representing the $i$-th query.

# Output data

In the file `parimpar.out`, $Q$ lines will be displayed. On line $i$ there will be a single natural number representing the answer to query $i$.

# Constraints and clarifications

* $1 \leq N, Q \leq 2 \cdot 10^5$;
* $-10^9 \leq a_i \leq 10^9$;
* **Empty subarrays are counted, therefore the maximum sum of a subarray of any sequence is at least $0$.**

| # | Score | Constraints | 
| - | ------- | ---------- |
| 1 | 22 | $N \leq 15, Q \leq 100$ |
| 2 | 42 | $N, Q \leq 2 \ 000$ |
| 3 | 36 | No other restrictions |

# Example

`parimpar.in`
```
8 4
3 -4 5 8 -6 2 -11 7
0 15
17 17
2 100
17 21
```

`parimpar.out`
```
1
3
8
5
```

## Explanation

Applying the sequence of operations $2, 1, 2, 2$, we obtain $b = [3, 5, -6, -11, 8, 7, -4, 2]$. $S_b = 8 + 7 = 15$. For the first query, this is the only valid sequence of operations.

Applying the sequence of operations $1, 2, 1, 2$, we obtain $b = [-4, 8, 2, 7, 3, -6, -11, 5]$. $S_b = 8 + 2 + 7 + 3 = 20$. This contributes to the last two queries.

---