DreptPal

Given a matrix with $N$ rows and $M$ columns containing natural numbers. We define a palindromic rectangle as a submatrix of the given matrix that has an odd number of columns and respects the property that each row of the submatrix forms a palindromic sequence.

## Task

Determine the palindromic rectangle of maximum area of a given matrix.

## Input data

The input file `dreptpal.in` contains on the first line two natural numbers $N$ and $M$ with the meanings given in the statement. The next $N$ lines contain $M$ natural numbers each, representing the given matrix.

## Output data

The output file `dreptpal.out` will contain a single number representing the required maximum area.

## Constraints

$1 \leq N$, $M \leq 1000$

The values of the matrix are natural numbers in the interval $\[0, 10^9\]$

## Example

`dreptpal.in`
```
4 5
5 3 4 3 2
6 2 6 2 6
1 3 1 3 4
7 8 3 9 2
```

`dreptpal.out`
```
9
```

## Explanation

The sought submatrix is the bolded one.