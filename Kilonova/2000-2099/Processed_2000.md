```markdown
A sequence consisting of $N$ natural numbers indexed from $1$ to $N$ is considered. Initially, the sequence contains only zero values and will be filled with natural numbers as follows. The sequence is traversed multiple times from position $1$ to position $N$ and whenever a zero value is encountered, it is replaced with the smallest non-zero value $X$ that does not exist in the sequence. At the same time, all non-zero values strictly less than $X$ are replaced with zero. The traversal stops when the sequence contains only non-zero values.

# Task

Given $N$, determine the sequence in its final form.

# Input data

The input file `towerx.in` contains on the first line a non-zero natural number $N$ – the length of the sequence.

# Output data

The output file `towerx.out` will contain on the first line $N$ natural numbers separated by spaces, representing the elements of the sequence in the final form.

# Constraints and clarifications

* $1 \leq N \leq 10\ 000$

# Example 1

`towerx.in`
```
3
```

`towerx.out`
```
3 1 2
```

## Explanation

The sequence goes through the following forms.
$0 \ 0 \ 0$
$1 \ 0 \ 0$
$0 \ 2 \ 0$
$0 \ 2 \ 1$
$3 \ 0 \ 0$
$3 \ 1 \ 0$
$3 \ 0 \ 2$
$3 \ 1 \ 2$
```