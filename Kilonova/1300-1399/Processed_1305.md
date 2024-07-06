Miruna has just learned about geometric progressions in her mathematics class. A sequence of positive natural numbers is called a geometric progression if one of the following two conditions is met:

* The sequence consists of a single element.
* If the sequence consists of $N (N > 1)$ elements $v_1, v_2, \dots, v_N$, then there exists an integer $K$ strictly greater than $1$ such that the ratio of any two consecutive elements in the sequence is equal to $K$. In other words, for any index $i, 1 \leq i < N, v_{i+1} / v_i = K$.

Miruna has a vivid imagination, so she invents a new notion never encountered before - that of a geometric subsequence: given a sequence of positive natural numbers, a subsequence that is a geometric progression is called a geometric subsequence.

# Task

Write a program that, for a sequence of $N$ elements, displays the length of its longest geometric subsequence.

# Input data

The input file `subgeom.in` will contain on the first line the natural number $T$ representing the number of data sets in the file. Each of the next $T$ lines contains a data set in the form:

$N \ v_1 \ v_2 \ \dots \ v_N$

The first value is a natural number $N$, representing the number of elements in the sequence, followed by the $N$ positive natural numbers that make up the sequence, separated by a space.

# Output data

The output file `subgeom.out` will contain $T$ lines, one line for each data set. Line $i$ will contain a natural number representing the maximum length of a geometric subsequence of the sequence described on line $i + 1$ in the input file.

# Constraints and clarifications

* $1 \leq T \leq 10$
* $1 \leq N \leq 5\ 000$
* For $40\%$ of the tests $1 \leq N \leq 128$
* The elements of the sequence are natural numbers in the range $[1, 10^5]$
* A subsequence of a sequence $v_1, v_2, \dots , v_N$ consists of elements of the sequence considered in the order they appear in the sequence: $v_{i1}, v_{i2}, \dots, v_{ik} (1 \leq i1 < i2 < \dots < ik \leq N)$.

# Example

`subgeom.in`
```
6
3 5 3 7
3 8 4 2
3 4 4 4
3 5 1 10
4 1 2 3 9
5 6 2 8 6 18
```

`subgeom.out`
```
1
1
1
2
3
3
```

## Explanation

In the first three tests, all geometric subsequences have length $1$.

In the fourth test, the solution is formed by the subsequence $5, 10$.

In the fifth test, the solution is formed by the subsequence $1, 3, 9$.

In the last test, the solution is formed by the subsequence $2, 6, 18$.