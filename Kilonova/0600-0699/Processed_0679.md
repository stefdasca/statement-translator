```markdown
Two integers $N, M$ are given along with two sequences of non-negative integers $P$, of $N$ elements, and $Q$, of $M$ elements. Then, the matrix $A$ with $N$ rows and $M$ columns is defined, where the element $A_{i,j}$ at row $i$ and column $j$ is defined by the relation

$$ A_{i,j} = (P_i \cdot Q_j) \text{ xor } P_i \text{ xor } Q_j $$

The **xor** operator represents the bitwise exclusive OR, written as `^` in C++.

We define the value $S(a, b, c, d)$, for $1 \le a \le b \le N$, $1 \le c \le d \le M$, as:

$$ S(a, b, c, d) = \sum_{i=a}^{b} \sum_{j=c}^d A_{i,j} $$

Akane is a curious person and wants to find the following value:

$$ \sum_{1 \le a \le b \le N} \sum_{1 \le c \le d \le M} {S(a, b, c, d)}^2 $$

Can you help her calculate this value, modulo $10^9 + 7$?

# Input data
The first line contains the numbers $N, M$, with the meaning as described above. The second line contains $N$ numbers, the elements of the sequence $P$. The third line contains $M$ numbers, the elements of the sequence $Q$.

# Output data
The first line will print an integer representing the requested value, modulo $10^9 + 7$.

# Constraints and clarifications
* $1 \le N, M \le 2\ 000$
* $0 \le P_i, Q_j \le 10^4$, for $1 \le i \le N; 1 \le j \le M$

## Subtask 1 (30 points)
* $1 \le N, M \le 30$

## Subtask 2 (40 points)
* $1 \le N, M \le 300$

## Subtask 3 (30 points)
* No additional constraints

# Examples
`stdin`
```
3 1
1 1 1
0
```
`stdout`
```
20
```
`stdin`
```
3 1
1 2 3
0
```
`stdout`
```
84
```
`stdin`
```
3 2
1 2 3
1 2
```
`stdout`
```
912
```
Explanations
---
For the first example, we have $ A = \begin{bmatrix}
1 \\
1 \\
1 \\
\end{bmatrix} $. 
There will be $3$ submatrices formed from a single element, each having the value $S$ equal to $1$, $2$ submatrices formed from $2$ elements each having the value $S$ equal to $2^2 = 4$, and finally, the entire matrix having the value $3^2 = 9$. Summing these values, we get $1 \cdot 3 + 2 \cdot 4 + 1 \cdot 9 = 20$. $20 \text{ modulo } 10^9 + 7$ is just $20$.
For the last example, $ A = \begin{bmatrix}
1 & 1 \\
1 & 4 \\
1 & 7 \\
\end{bmatrix}$.
```
