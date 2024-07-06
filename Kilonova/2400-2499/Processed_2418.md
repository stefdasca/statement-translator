# Task

Two sequences are given, $a$ of size $n$ and $b$ of size $m$, both indexed from $1$. Construct the matrix $mat$ with $n$ rows and $m$ columns, where $mat_{i, j}$ = $a_i | b_j$. By the operation $x$ | $y$, for natural numbers $x$ and $y$, we refer to the bitwise OR operation. The operation is performed as follows: the numbers $x$ and $y$ are written in base $2$, and the number $x$ | $y$ has the $i$-th bit active if and only if either $x$ has the respective bit active, or $y$ has the respective bit active.

There are $q$ questions of the form: given a submatrix, calculate the sum of the values in this submatrix.

**Note**: In C++, the bitwise OR operation can be implemented as: "$x | y$".

# Input data

The first line from the input file `matmare.in` contains $n$, $m$, $q$. The second line contains the sequence $a$ of $n$ elements. The third line contains the sequence $b$ of $m$ elements.

The next $q$ lines contain four values $l$, $c$, $x$, $y$, indicating a question about the submatrix between rows $l$ and $x$ and columns $c$ and $y$.

# Output data

Print $q$ lines, on the $i$-th line being a single number: the sum of the submatrix from question $i$.

# Constraints and clarifications

* $0 \leq a_i,b_i < 2^{26}$ 
* $n,m,q \leq 200\ 000$.

| # | Points | Constraints                     |
| - | ------- | ----------                     |
| 1 | 20      | $n,m,q \leq 200$               |
| 2 | 20      | $n,m \leq 2\ 000$              |
| 3 | 40      | $a_i, b_i \leq 1$              |
| 4 | 20      | No other constraints           |

# Example

`matmare.in`
```
3 4 2
1 4 3
4 6 1 0
1 1 3 4
1 2 3 3
```

`matmare.out`
```
53
29
```

## Explanation

The resulting matrix is as follows:

```
5 7 1 1
4 6 5 4
7 7 3 3
```

For the first question, the sum of the elements in the entire matrix is $5+7+1+1+4+6+5+4+7+7+3+3 = 53$.

For the second question, the sum of the elements in the submatrix $(1,2),(3,3)$ is $7+1+6+5+7+3 = 29$.