
The SEPI safe, where the prizes of the computer science olympiads are stored, is secured with a cipher in the form of a square matrix $A$ with $N$ rows and $N$ columns, where $N$ is an even natural number. The rows and columns are numbered starting from $1$.

The _cipher-matrix_ $A$ consists of $\frac{N}{2}$ layers. The $i$-th layer ($1 \leq i \leq \frac{N}{2}$) will contain the elements located on the edge of matrix $A$, after excluding the first $i - 1$ layers. The order of the elements of this layer is obtained starting from position $(i, i)$, traversing the top edge from left to right, the right edge from top to bottom, the bottom edge from right to left, and then the left edge from bottom to top.

~[seif.png|align=right]

For example, for $N = 4$ and the cipher-matrix in the adjacent figure, the elements of the first layer are, in traversal order, $7, 4, 5, 6, 8, 7, 9, 5, 4, 3, 1, 5$ (colored light gray). The elements of the second layer are located on the edge of matrix $A$, after excluding the first layer. The elements of the second layer, in their traversal order, are $7, 9, 4, 2$ (colored dark gray).

Each layer acts as a rotor of the cipher and its elements can be circularly permuted to the left or to the right by a certain number of positions. 
A sequence of $T$ circular permutation operations on the elements of a given layer is applied to the cipher-matrix, either to the left or to the right.

A circular permutation operation has the following structure: _layer positions direction_, where $layer$ represents the order number of the layer on which the permutation is applied, $positions$ represents the number of positions with which it is permuted, and $direction$ is a character: `S` for left or `D` for right.

# Task

Given the natural number $N$, the $N \cdot N$ elements of the cipher-matrix as well as the sequence of $T$ circular permutation operations of some layers, determine the final configuration of the matrix, which will allow the safe to be opened!

# Input data

The input file `seif.in` contains:

* The first line contains the natural number $N$
* Each of the following $N$ lines contains $N$ natural numbers representing the initial cipher-matrix
* The $(N + 2)$-th line contains the natural number $T$ representing the number of permutation operations
* The following $T$ lines contain the $T$ circular permutation operations, one operation per line, in the format described in the statement: _layer positions direction_.

# Output data

The output file `seif.out` will contain the first $N$ lines each with $N$ numbers representing the elements of the matrix after applying the $T$ circular permutation operations.

# Constraints and clarifications

* $2 \leq N \leq 500$
* $N$ is an even number
* $1 \leq T \leq 10^5$
* The number of positions for a permutation is non-zero and $\leq 10^6$.
* The elements of the cipher-matrix are natural numbers $\leq 2 \cdot 10^9$.
* Multiple circular permutation operations can be performed on the same layer.
* The elements written on the same line in the input file, respectively in the output file are separated by a single space.

# Example 1

`seif.in`
```
2
1 2
4 3
3
1 1 D
1 3 S
1 3 D
```

`seif.out`
```
4 1 
3 2
```

## Explanation

$N = 2$ and $T = 3$. The matrix changes as follows:

initial:
```
1 2
4 3
```

after operation $1 \ 1 \ D$:
```
4 1
3 2
```

after operation $1 \ 3 \ S$:
```
3 4
2 1
```

after operation $1 \ 3 \ D$:
```
4 1
3 2
```

# Example 2

`seif.in`
```
4
5 6 1 2
4 3 2 9
2 4 6 8
1 3 5 7
2
1 1 D
2 5 S
```

`seif.out`
```
4 5 6 1 
2 2 6 2 
1 3 4 9 
3 5 7 8
```

## Explanation

$N = 4$ and $T = 2$. The matrix changes as follows:

initial

```
5 6 1 2
4 3 2 9
2 4 6 8
1 3 5 7
```
after operation $1 \ 1 \ D$:

```
4 5 6 1
2 3 2 2
1 4 6 9
3 5 7 8
```

after operation $2 \ 5 \ S$:

```
4 5 6 1
2 2 6 2
1 3 4 9
3 5 7 8
```
```
