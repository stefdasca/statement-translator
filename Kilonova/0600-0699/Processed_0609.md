The owner of a famous computer science club in Slatina wants to introduce some bracelets made of multiple colors (which he considers to be integers) that he will make from a multicolored rubber strip. Since he consumed too much milk following the last event organized at Manuel Shaorma, he asks for your help in making the bracelets.

We consider an array $\textit{a}$ with $\textit{N}$ elements, indexed from 1. We will call a $\textit{band}$ a maximal subarray $[l, r]$ with all elements equal, that is $a_l = a_{l+1} = \ldots = a_r$.

Two operations will be performed on this array:
* $\text{1} \ L \ R$ - You need to find the number of bands and the maximum length of a band considering only the elements in the interval $[L, R]$. **The considered subarray will be viewed as circular, meaning $a_l$ and $a_r$ will be considered neighbors**.
* $\text{2} \ L \ R \ M \ B_1 \ B_2 \ldots B_M$ - The elements of the array from $L$ to $R$ will take values according to the pattern $\textit{B}$ of length $\textit{M}$. When the subarray that needs to be filled is longer than the pattern, **the pattern will repeat** (the last repetition might not be complete). For example, $2 \ 3 \ 10 \ 3 \ 1 \ 2 \ 2$ means that the values of the array from $3$ to $10$ will be: $1, 2, 2, 1, 2, 2, 1, 2$.

In total, $\textit{Q}$ such operations will be performed on $\textit{a}$.

# Task

First, you need to find the number of bands and the maximum length of a band for the initial array. Then, find the answer for each type 1 operation. At the end of all operations, you need to display all elements of the array.

# Input data

The first line contains the numbers $\textit{N}$ and $\textit{Q}$ with the meaning from the statement.
Then, the second line contains the initial values of the array.
The next $\textit{Q}$ lines contain the operations that follow the format above.

# Output data

The first line will contain the answer for the initial array, two numbers representing the number of bands and the maximum length of a band. Then, the number of bands and the maximum length of a band will be printed for each type 1 operation.
On the last line, the elements of the array will be printed after all the operations.

# Constraints and clarifications
* $1 \leq N \leq 250 \ 000$
* $1 \leq Q \leq 200 \ 000$
* For each operation, we will have $1 \le L \le R \le N$ and $1 \le M \le N$
* $0 \leq \text{Sum of \textit{M}-values for all operations} \leq 250 \ 000$
* $1 \leq a_i, B_i \leq 10^9$

## Subtask 1 (7 points)
* $N, Q \leq 5 \ 000$ for all operations
## Subtask 2 (9 points)
* The operations are only of type 1
## Subtask 3 (5 points)
* The sum of values $R - L$ for all type 2 operations $ \le 200 \ 000$
## Subtask 4 (10 points)
* $M = 1$ for all operations
## Subtask 5 (11 points)
* $\text{Sum of \textit{M}-values for all operations} \leq 5 \ 000$
## Subtask 6 (27 points)
* $N, Q \le 75 \ 000 \text{ and sum of \textit{M}-values for all operations} \leq 50 \ 000$
## Subtask 7 (31 points)
* No other restrictions

# Example
`stdin`
```
12 9	
1 1 2 3 2 1 2 2 2 3 1 1
1 1 11				
1 3 9
2 6 6 1 2
1 3 9
1 1 11
2 4 10 4 2 2 1 1
1 1 12
1 3 9
1 1 11
```
`stdout`
```
7 4 
7 3
4 4
2 6
5 5
4 5
2 5
4 4
1 1 2 2 2 1 1 2 2 1 1 1
```
Explanations
---
Initially, we have 7 bands: $11..11$, $2$, $3$, $2$, $1$, $222$, $3$, with the maximum length 4.
For the first operation, we still have 7 bands as above, but the first will be $11..1$ instead of $11..11$, so the maximum length is 3.
For the second operation, we have 4 bands: $22..22$, $3$, $2$, $1$, with the maximum length 4.
After the third operation, the array will become $1, 1, 2, 3, 2, 2, 2, 2, 2, 3, 1, 1$.
For the fourth operation, we have 2 bands: $2..22222$ and $3$, with the maximum length 6.
For the fifth operation, we have 5 bands: $11..11$, $2$, $3$, $22222$, $3$, with the maximum length 5.