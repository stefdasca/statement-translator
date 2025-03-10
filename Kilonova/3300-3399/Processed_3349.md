
# Task

Given a sequence of $n$ natural numbers, determine two positions $i$ and $j$ such that the sum of the elements from position $1$ to $i$ (inclusive) multiplied by the sum of the elements from position $i+1$ to $j$ (inclusive) and multiplied by the sum of the elements from position $j+1$ to $n$ (inclusive) is maximized.

# Input data

The file `splitmax3.in` contains on the first line the number $n$. The second line contains $n$ natural numbers separated by spaces.

# Output data

The file `splitmax.out` contains on the first line three numbers, separated by spaces: $M$, $i$, $j$ representing respectively the maximum value obtained and the positions $i$ and $j$ according to the task. If there are multiple solutions with the maximum $M$, choose the one with the smallest $i$.

# Constraints and clarifications

* $3 \leq n \leq 100 \ 000$;
* $1 \leq i < j \leq n$;
* The values of the sequence are non-zero natural numbers of one digit.
* The requested value has at most $18$ digits.

# Example

`splitmax3.in`
```
5
1 3 1 4 7
```

`splitmax3.out`
```
140 2 4
```
