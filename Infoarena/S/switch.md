# Switch

Marian strikes again! This time, our hero has two binary matrices (each element of the matrix is either $0$ or $1$), with dimensions $2×2$ (two rows and two columns) and wants to transform the first matrix into the second one. To do this, he performs a series of operations only on the first matrix. An operation consists of: Marian chooses a row, a column, or one of the two diagonals of the matrix and negates the corresponding elements (from $0$ they become $1$, and from $1$ they become $0$). Determine if Marian can transform the first matrix into the second matrix by intelligently performing the allowed operations.

## Input data

The input file `switch.in` contains the first line which contains $T$, the number of tests. Each of the following $T$ tests will contain $4$ lines, with exactly $2$ numbers on each line (the numbers will be $0$ or $1$), separated by a space. The first $2$ lines describe the first matrix, and the next $2$ lines describe the second matrix.

## Output data

The output file `switch.out` will contain $T$ lines, each containing the text "DA" or "NU", the answer for the respective test.

## Constraints

The operations can be performed in any order and any number of times. 
$T \leq 500$

## Example

`switch.in`
```
3
0 1
1 0
0 0
0 0
1 0
1 1
0 1
1 0
1 0
0 1
1 1
0 0
```

`switch.out`
```
DA
DA
NU
```

## Explanation

In the case of the first test, Marian chooses the secondary diagonal and negates its elements, thus obtaining the second matrix. In the second test, Marian negates the first column, then the second one. For the 3rd test, there is no set of operations that transforms the first matrix into the second one.