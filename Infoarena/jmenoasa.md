## Task

Tired of complicated story problems, Miruna proposes the following problem: You are given a matrix with $N$ rows and $M$ columns, containing natural numbers. You need to find a submatrix of maximum area where the elements in each row and in each column are in strictly increasing order.

## Input data

The input file `jmenoasa.in` will contain on the first line 2 natural numbers $N$ and $M$ representing the dimensions of the matrix. The next $N$ lines will contain $M$ natural numbers each - the elements of the matrix.

## Output data

In the output file `jmenoasa.out` you will print a single natural number representing the maximum area of a submatrix that satisfies the conditions in the task statement.

## Constraints and clarifications

$1 \leq N, M \leq 1000$

Elements of the matrix will be in the interval $[0, 10^9]$

A submatrix represents the two-dimensional extension of a subarray

Attention: It is recommended to read using ifstream objects (standard C reading or stdin redirection - to use cin - does not fit in time). Alternatively, you can parse to get the maximum score.

## Example

`jmenoasa.in`
```
3 4
1 7 5 3
6 3 4 1
6 5 6 2
```

`jmenoasa.out`
```
4
```

## Explanation

```
1 7 5 3 
6 3 4 1 
6 5 6 2 
```