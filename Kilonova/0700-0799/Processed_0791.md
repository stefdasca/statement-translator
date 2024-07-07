
We consider the matrix $A$ whose elements can only have the values $0$ or $1$ and in which the numbering of rows and columns starts from $1$. For any element of the matrix, we define the notion of a neighbor as those elements in the matrix located immediately adjacent to it in one of the horizontal, vertical, or two diagonal directions (see the figure below where the neighbors of the element marked with $o$ are marked with $x$).

~[vecini.png]

# Task

Given the matrix $A$, determine the maximum number of good neighbors that one of the matrix elements has, as well as the number of elements that have this maximum number of good neighbors.

# Input data

The input file `vecini.in` contains on the first line three natural values $m \ n \ k$ representing the number of rows, the number of columns, and respectively the number of values equal to $1$ in the matrix $A$. Each of the following $k$ lines contains two values $i$ and $j$ meaning that $A_{ij}$ is equal to $1$. These values are given in the order of traversing the matrix from row $1$ to row $m$.

# Output data

The output file `vecini.out` will contain on the first line two natural numbers $x$ and $y$ separated by a single space: $x$ will represent the maximum number of good neighbors that one of the elements of the given matrix has, and $y$ will represent the number of elements in the given matrix that have this maximum number of good neighbors.

# Constraints and clarifications

* $2 \leq m,n \leq 1 \ 000$;
* $0 \leq k \leq n \cdot m / 2+1$;
* For $30$% of the tests $2 \leq m,n \leq 200$;

# Example

`vecini.in`
```
3 4 7
1 3
2 1
2 4
3 1
3 4
3 3
3 2
```

`vecini.out`
```
3 6
```

## Explanation

The matrix $A$ is as follows:
```
0 0 1 0
1 0 0 1
1 1 1 1
```
The maximum number of good neighbors encountered for the matrix elements is $3$. There are $6$ elements that have this maximum number of good neighbors, those located at positions: $1,2; 2,2; 2,3; 2,4; 3,2; 3,3$ (the ones that are underlined in the representation of the matrix above).
