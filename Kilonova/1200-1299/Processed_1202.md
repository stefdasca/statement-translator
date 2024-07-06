```
Let $n$ be a non-zero natural number, $n \leq 100$.

# Task

Write a program that determines $n$ disjoint subsets, each containing $n$ distinct elements from the set $\{1, 2, \dots, n^2\}$, and where the sum of the elements in each subset is the same.

# Input data

The input file `sume.in` contains on the first line the non-zero natural number $n$.

# Output data

The output file `sume.out` contains $n$ lines, one for each determined subset. Line $i$ contains the $n$ elements of subset $i$, separated by a space.

# Constraints and clarifications

* $1 \leq n \leq 100$
* Two subsets are disjoint if they have no common elements
* The solution is not unique; you can display any solution that meets the conditions of the problem statement
* The order of the subsets or the elements of the subsets **DOES NOT** matter

# Example

`sume.in`
```
4
```

`sume.out`
```
11 6 1 16
15 10 5 4
3 8 9 14
13 2 7 12
```
```