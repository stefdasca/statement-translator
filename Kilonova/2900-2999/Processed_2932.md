For a matrix with $n$ rows and $n$ columns, we group the $n^2$ elements into $2 \cdot n - 1$ diagonals parallel to the secondary diagonal (numbered starting from $1$). For example, for $n = 5$, noting for each position in the matrix the diagonal to which it belongs, we get:

~[diagsecundare.png|align=center|width=30%]

# Task

Given $n$ and a matrix $a$ with $n$ rows and $n$ columns. For each $d$ from $2$ to $2 \cdot n - 2$, notice that if we eliminate diagonal $d$, the matrix will be divided into two parts. Display for each $d$, the sum of the left part, and the sum of the right part.

# Input data

The first line of the input file ```taietura.in``` contains the number $n$. The next $n$ lines contain $n$ elements each, representing the matrix $a$.
    
# Output data

The output file ```taietura.out``` should contain $2 \cdot n - 3$ lines. On the $d$-th line, print two numbers, the sum of the values on the left, followed by the sum of the values on the right.
 
# Constraints and clarifications
* $2 \leq n \leq 2 \ 000$
* $0 \leq a_{i, j} \leq 10^9$

|#|Points|Constraints|
|-|-|--------|
|1|40|$n \leq 200$|
|2|60|No additional constraints|

# Example
`taietura.in`
```
4
3 6 4 5
1 2 7 1
3 11 5 8
9 2 2 4
```
`taietura.out`
```
3 63
10 54
19 22
51 14
59 4
```

## Explanation

In the example, the values on the $5$-th diagonal are $1$, $5$, $2$.

~[poza2.png|align=center|width=30%]

If we eliminate the $3$-rd diagonal, on the left part we have the sum $3 + 6 + 1 = 10$, and on the right part we have the sum $5 + 7 + 1 + 11 + 5 + 8 + 9 + 2 + 2 + 4 = 54$.