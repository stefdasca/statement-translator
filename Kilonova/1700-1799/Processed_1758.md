```markdown
Consider a sequence $A$ with $N$ non-zero integer elements. We call a sequence of $A$ any succession of elements found in consecutive positions in the sequence: $A_i, A_{i+1}, \dots, A_j$ with $1 \leq i < j \leq N$.

The length of the sequence is understood to be the number of elements that compose it. For any sequence $A_i, A_{i+1}, \dots, A_j$, we call a *split-point* an index $k$, $i \leq k < j$, which divides the sequence into two non-empty subarrays: $A_i, A_{i+1}, \dots, A_k$ and $A_{k+1}, A_{k+2}, \dots, A_j$.

Let $D_{max}$ be the maximum absolute value of the difference between the sums of the elements of the two subarrays separated by a *split-point*, considering all possible sequences $A_i, A_{i+1}, \dots, A_j$, and let $L_{max}$ be the maximum length of a sequence characterized by the value $D_{max}$.

# Task

Given $N$ and the values of the elements of sequence $A$, determine $D_{max}$ and $L_{max}$.

# Input data

The input file `ksplit.in` contains a natural number $N$ that represents the number of elements of the sequence $A$ on the first line, and on the second line, it contains $N$ non-zero integers separated by a space.

# Output data

The output file `ksplit.out` will contain two lines. The first line contains the natural number $D_{max}$ and the next line contains the natural number $L_{max}$.

# Constraints and clarifications

* $2 \leq N \leq 100\ 000$
* The elements of the sequence $A$ are non-zero integers from the interval $[-1\ 000\ 000, 1\ 000\ 000]$.

# Example

`ksplit.in`
```
4
2 3 -1 5
```

`ksplit.out`
```
6
3
```

## Explanation

Among all the possible sequences, we choose the sequence $2\ 3\ -1$, which is formed from the first $3$ elements of the sequence.
The value of $D_{max}$ is $6$, meaning: $s_1 = 2 + 3 = 5$, $s_2 = -1$, $D_{max} = |5 - (-1)| = 6$, $L_{max} = 3$.
It is also observed that there is the sequence $-1\ 5$ for which: $s_1 = -1$, $s_2 = 5$, $D_{max} = |-1 - 5| = 6$ but this sequence has a length of $2$.
```