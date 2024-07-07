
A square matrix of size $N$ containing natural numbers is considered. We define a **cross of width $K$** as the union of the set of all elements located on $K$ consecutive rows of the matrix and the set of all elements located on $K$ consecutive columns of the matrix. Two elements of the matrix are considered distinct if they are situated on distinct positions in the matrix. The degenerate form of a cross, in the shape of `T` or `L`, is also allowed when one of the rows or columns that form the cross are at the edge of the matrix. We define the **value** of a cross as the sum of the elements from which it is formed.

# Task

Write a program that, for a given value $K$, determines a cross of width $K$ whose value is maximal and its position in the matrix. This position will be expressed by the pair of indices representing the first row among the $K$ consecutive rows and the first column among the $K$ consecutive columns from which the cross is formed.

# Input data

The file `cruce.in` contains on the first line the numbers $N$ and $K$, and on the following $N$ lines $N$ integers each, representing in order, by rows, the elements of the matrix. The numbers on the same line are separated by a space.

# Output data

The file `cruce.out` will contain three numbers $Vmax \\ L \\ C$, separated by a space, representing the maximum value determined for a cross of width $K$, respectively the row and column that express its position in the matrix.

# Constraints and clarifications

* $1 \leq K < N \leq 500$;
* The numbers in the matrix are in the interval $[-5\ 000, 5\ 000]$
* Rows and columns are indexed starting from 1.
* If there are multiple crosses of width $K$ with the maximum value, the position with the smaller row index will be considered, and in the case of equal rows, the position with the smaller column index will be considered.

# Example 1

`cruce.in`
```
5 2
1 -2 3 -1 4
-3 2 2 -2 -1
1 2 3 4 5
1 0 -7 1 1
3 2 1 2 3
```

`cruce.out`
```
23 2 4
```

## Explanation

The elements forming the cross with maximum value are:

~[cruce.png]

# Example 2

`cruce.in`
```
5 2
0 0 1 1 1
2 2 2 2 2
2 2 2 2 2
2 2 2 2 2
0 0 1 1 1
```

`cruce.out`
```
28 2 3
```

## Explanation

The maximum value of a cross of width $2$ is $28$. In the example, there are other crosses with a value of $28$, but with higher starting row or column indices.
For example, the cross starting from row $3$ and column $3$.
