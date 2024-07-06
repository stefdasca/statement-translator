```markdown
# Task

Given an array of $n$ numbers, select values from the array such that no two values are chosen from consecutive positions, and their sum is maximized.

# Input data

The first line will contain $t$, the number of tests.

Each of the $t$ tests will be described as follows:

The first line will contain $n$, representing the number of numbers in the array.

The second line will contain the values of the array $v$.

# Output data

Print $t$ numbers, with one corresponding to each of the $n$ tests.

# Constraints and clarifications

* $1 \leq t \leq 10$
* $1 \leq n \leq 10^5$
* $1 \leq v_i \leq 10^6$

# Example

`stdin`
```
3
7
5 4 1 4 3 8 5
5
9 8 7 9 8
6
11 9 0 13 14 15
```

`stdout`
```
17
24
39
```
```