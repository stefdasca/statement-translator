## Task

Given a square matrix with $N$ rows and $N$ columns containing non-zero natural numbers, the matrix must be divided into nine regions as follows: two rows $l_{1}$ and $l_{2}$ and two columns $c_{1}$ and $c_{2}$ are chosen, $1 \leq l_{1} < l_{2} < N$ , $1 \leq c_{1} < c_{2} < N$, and the matrix is cut along these rows and columns, as shown in the figure below: It can be observed that zones $1, 4$, and $7$ consist of all elements from the first $c_{1}$ columns, zones $2, 5$, and $8$ are between columns $c_{1} +1$ and $c_{2}$ , and zones $3, 6, 9$ are between columns $c_{2} +1$ and $N$. Similarly, zones $1, 2$, and $3$ are between rows $1$ and $l_{1}$ , $4, 5$, and $6$ between $l_{1} +1$ and $l_{2}$ , and zones $7, 8$, and $9$ between rows $l_{2} +1$ and $N$. The sums of the elements for each of the nine regions thus formed are noted in any order. Determine the rows $l_{1}$ and $l_{2}$ and the columns $c_{1}$ and $c_{2}$ such that the given nine sums are formed.

## Input data

The input file `zone.in` contains on the first line the natural number $N$, the size of the matrix. The second line contains nine natural numbers, the sums of the given regions in any order. Each of the following $N$ lines contains $N$ non-zero natural numbers, the elements of the matrix. It is recommended to use $scanf$ for reading instead of $cin$.

## Output data

The output file `zone.out` will contain a single line which will contain four natural numbers, $l_{1}$, $l_{2}$, $c_{1}$ and $c_{2}$, separated by exactly one space, representing the solution to the problem. If there are multiple possible solutions, the one where $l_{1}$ is as small as possible will be displayed. If even in this case there are multiple possible solutions, the one where $c_{1}$ is as small as possible will be displayed. If even in this case there are multiple solutions, the one where $l_{2}$ is as small as possible will be displayed. If even in this case there are multiple solutions, the one where the sum of the four numbers is as small as possible will be displayed.

## Constraints

$3 \leq N \leq 512$ 

Each element in the matrix does not exceed $10$ million 

The nine sums are not necessarily pairwise distinct 

The existence of at least one solution is guaranteed 

## Example

`zone.in` 

```
5 
28 3 5 2 20 7 5 11 15 
1 2 5 6 1 
5 6 1 3 3 
9 8 1 4 5 
8 5 2 1 6 
1 6 3 2 2 
```

`zone.out` 

```
1 3 2 3 
```

## Explanation

The matrix will be cut as follows: