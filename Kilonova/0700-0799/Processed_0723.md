The problem statement is given below, translated into English while preserving the formats and custom elements:

---

A sequence of $n$ positive natural numbers $x_1, x_2, \dots, x_n$ and a natural number $m$ are given.

# Task
Check if the value of the expression $\sqrt[m]{x_1 x_2 x_3 \dots x_n}$ is a natural number. If affirmative, display this number decomposed into prime factors.

# Input data
In the file `expresie.in`, the first line contains $m$, the second line contains $n$, and the third line contains the numbers $x_1$, $x_2$, $\dots$, $x_n$, separated by a space.

# Output data
In the file `expresie.out`, the first line will contain the digit $0$, if the value of the expression is not a natural number, respectively $1$ if it is a natural number. 
If the value of the expression is a natural number, the following lines will contain pairs in the form "$p\ e$" ($p$ is a prime factor that appears in the decomposition with power $e \geq 1$). These pairs will be written in ascending order by the first number (i.e., $p$).

# Constraints
- $n$ is a positive natural number less than $5000$.
- $x_i$ is a positive natural number less than $30\,000$, $i \in \{1, 2, \dots, n\}$.
- **$m$ can be one of the digits $2$, $3$ or $4$.**

# Example 1
`expresie.in`
```
2
4
32 81 100 19
```
`expresie.out`
```
0
```
## Explanation
$\sqrt[2]{32 \cdot 81 \cdot 100 \cdot 19}$ is not a natural number.

# Example 2
`expresie.in`
```
2
4
32 81 100 18
```
`expresie.out`
```
1
2 4
3 3
5 1
```
## Explanation
$\sqrt[2]{32 \cdot 81 \cdot 100 \cdot 18} = 2^4 \cdot 3^3 \cdot 5^1$

