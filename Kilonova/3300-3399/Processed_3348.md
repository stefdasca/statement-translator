# Task

We have a square matrix of size $n$.

All elements equidistant from the matrix edge are said to be on the same "concentric square". For example, the elements on the contour (row $1$, column $1$, row $n$, column $n$) are on the first concentric square. The elements on row $2$, column $2$, row $n-1$, column $n-1$, are on the second concentric square, and so on. The matrices in the following figure have $4$ concentric squares.

It is known that each concentric square has natural, distinct, consecutive numbers, starting with $1$.

Each such square can be rotated to the left or to the right. The rotation cost is given by the distance that the elements are moved (for example, a rotation by two positions has the cost of $2$, whether it is done to the left or to the right).

We want to bring all elements with value $1$ on the same half-diagonal (as in one of the four examples of matrices below). We also want to achieve this while minimizing the value $C =$ the sum of all concentric squares' rotation costs.

~[rotate.png|align=center|width=40%]

# Input data

The file `rotate.in` contains on the first line the value $n$. On each of the next $n$ lines, there are $n$ natural numbers, separated by spaces, representing the given matrix.

# Output data

The file `rotate.out` contains on the first line the value $C$. On each of the next $n$ lines, there are $n$ natural numbers, separated by spaces, representing the configuration of the final matrix to obtain the cost $C$. If there are multiple ways to obtain the cost $C$, the matrix will be displayed with the half-diagonal completed with the minimum code (in the figure, the codes of the half-diagonals are marked in red frames, from $1$ to $4$).

# Constraints and clarifications

* $1 \leq n \leq 1\ 000$;
* The elements on the same concentric square form a permutation.

# Example

`rotate.in`
```
4
8 1 6 2
9 3 4 7
5 1 2 3
4 10 11 12
```

`rotate.out`
```
2
1 6 2 7
8 1 3 3
9 2 4 12
5 4 10 11
```

## Explanation

By rotating with one position to the left both square $1$ and with one position to the right square $2$, we obtain the cost $C = 2$ and the matrix presented in `rotate.out`.