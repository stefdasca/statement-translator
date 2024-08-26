Indep

Given an array of natural numbers $A_1, A_2, \dots, A_n$ find the number of its independent subsequences. A subsequence is called independent if the largest natural number that divides all of its elements is $1$.

##  Task

Write a program that finds the required number.

##  Input data

The first line of the input file contains an integer $N$ representing the number of elements in the array. The next $N$ lines contain one element of the array each.

##  Output data

The output file will contain on the first line a single integer representing the required number.

##  Constraints and clarifications

$1 \leq N \leq 500$

The elements of the array are natural numbers from the interval $[1, 1000]$

A subsequence is understood as a subset of elements of the array that are not necessarily in consecutive positions.

##  Example

`indep.in`:
```
4
3
4
2
6
```

`indep.out`:
```
6
```

##  Explanation

The independent subsequences are:
$\{3, 2\}$
$\{3, 4\}$
$\{3, 4, 2\}$
$\{3, 2, 6\}$
$\{3, 4, 6\}$
$\{3, 4, 2, 6\}$