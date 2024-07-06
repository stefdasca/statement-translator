A hypersymmetric matrix is a square matrix defined recursively as follows:
1. Matrices of dimension `1×1` are hypersymmetric.
2. A matrix of dimension `N×N (N>1)` is hypersymmetric if it simultaneously meets the following two conditions:
* It is symmetric vertically, horizontally, with respect to the main diagonal, and with respect to the secondary diagonal.
* The submatrices of dimensions `N/2×N/2` (with `N/2` rounded down) located in the four corners of the matrix are themselves hypersymmetric.

A binary matrix is a matrix whose elements are `0` or `1`. The value of a hypersymmetric binary matrix is the number in base `2` with $N^2$ bits obtained by concatenating the elements of the matrix read line-wise from left to right, top to bottom.

# Task
Given `N` and `K`, calculate the `K`-th value in ascending order among all values of hypersymmetric binary matrices of dimension `N×N`.

# Input data
The input file `hipersimetrie.in` contains on the first line the number `N`. The second line contains a string of characters `0` or `1` representing the value of `K` in base `2` (it is guaranteed that the first character of the string is `1`).

# Output data
In the output file `hipersimetrie.out` print the `K`-th value in ascending order among all values of hypersymmetric binary matrices of dimension `N×N`. Since this value can be very large, it is required to print only the remainder modulo `1.000.000.007` of this value.

# Constraints and clarifications
* `1 \leq N \leq 1\ 000\ 000\ 000`;
* $1 \leq K \leq 2^{1\ 000\ 000}$;
* It is guaranteed that for the given value of `N` there are at least `K` hypersymmetric binary matrices;
* For tests worth `27` points, it is guaranteed that `N \leq 1\ 500`
* For other tests worth `62` points, it is guaranteed that `N \leq 1\ 000\ 000`
* For other tests worth `11` points, `N \leq 1\ 000\ 000\ 000`

# Example

`hipersimetrie.in`

```
3
100
```

`hipersimetrie.out`

```
186
```

Explanations
---

$K=100_2=4$.  
The `4`-th matrix in ascending order of value is  
`0 1 0`  
`1 1 1`  
`0 1 0`  

Its value is `010111010` in base `2`, which is `186` in base `10`.