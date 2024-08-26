## Task

An array of numbers is said to be of type $W$ if: It consists of four segments in decreasing order, increasing order, decreasing order, increasing order. The order is not strict, so the increasing and decreasing segments can include consecutive equal elements. Any two consecutive segments share one common end. Any segment contains at least two distinct values. For example, the array $(3\ 1\ 2\ 1\ 1\ 4)$ is of type $W$, because it consists of the segments $(3\ 1)$, $(1\ 2)$, $(2\ 1\ 1)$, $(1\ 4)$. The array $(3\ 1\ 2\ 2\ 2\ 4)$ is not of type $W$. This can be split into the segments $(3\ 1)$, $(1\ 2)$, $(2\ 2\ 2)$, $(2\ 4)$, but the segment $(2\ 2\ 2)$ does not contain at least two distinct values. Given an array of $N$ integers, how many distinct permutations of it are of type $W$? Two permutations $(p_1\ p_2\ \dots\ p_N)$ and $(q_1\ q_2\ \dots\ q_N)$ are considered distinct if there exists a position $1 \leq i \leq N$ such that $p_i ≠ q_i$. In the above example, $(3\ 1\ 2\ 1\ 1\ 4)$ should be counted only once, because permuting the $3$ ones does not create distinct permutations.

## Input data

In the input file `w.in`, the first line contains $N$. The second line contains the $N$ values of the array, separated by spaces.

## Output data

In the output file `w.out`, print the number of distinct permutations of type $W$, modulo $1\ 000\ 000\ 007$.

## Constraints and clarifications

$5 \leq N \leq 300\ 000$

Values of the elements in the array are natural numbers between $1$ and $1\ 000\ 000$ inclusive.

For $20\%$ of the tests, the array contains only two distinct values.

For another $30\%$ of the tests, all $N$ elements are distinct.

## Example

`w.in`
```
5
3 1 4 2 3
```

`w.out`
```
6
```

`w.in`
```
7
1 2 2 2 3 4 4
```

`w.out`
```
72
```

## Explanation

For the first example, the $6$ permutations of type $W$ are:
```
3 1 3 2 4
3 1 4 2 3
3 2 3 1 4
3 2 4 1 3
3 4 1 3 2
3 4 2 3 1
```