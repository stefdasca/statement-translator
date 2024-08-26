## Task

Ojilă is intensively preparing for OJI with his great-grandmother, who participated in the first edition of the International Mathematical Olympiad. His great-grandmother gives him the following problem. A sequence $a_1, a_2, \dots, a_N$ of non-zero natural numbers is given. For a non-empty subarray $a_i, a_{i+1}, \dots, a_j$, its cost is $h \cdot (j - i + 1)$, where $h$ is the minimum value in the subarray. Determine the maximum cost of a subarray.

## Input data

The input file `strabunica.in` contains on the first line the number $N$. The next line contains $n$ non-zero natural numbers separated by spaces, representing the elements of the sequence.

## Output data

The output file `strabunica.out` will contain a single natural number representing the maximum cost of a subarray.

## Constraints and clarifications

$1 \leq N \leq 200\,000$

The elements of the sequence are non-zero natural numbers less than or equal to $1\,000\,000\,000$.

## Example

`strabunica.in`
```
5
1 9 7 8 1
```

`strabunica.out`
```
21
```

## Explanation

The subarray with the maximum cost is $9, 7, 8$, so $h = 7$.