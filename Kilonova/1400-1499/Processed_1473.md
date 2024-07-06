```markdown
Consider a sequence of positive natural numbers $a[1], a[2], \dots , a[n]$ and a natural number $k$.

# Task

Determine a group of $k$ numbers from the sequence that have the property that their greatest common divisor is maximum. If there are multiple such groups, determine the group for which the sum of the elements is maximum.

# Input data

The input file `cmmdc.in` contains on the first line the natural numbers $n$ and $k$ separated by a space. The second line contains the natural numbers $a[1], a[2], \dots , a[n]$ separated by a space.

# Output data

The output file `cmmdc.out` contains on the first line a natural number representing the greatest common divisor of exactly $k$ numbers from the sequence, as maximum as possible. On the second line, separated by a space and **sorted in descending order**, are the $k$ numbers from the sequence that give the maximum greatest common divisor.

# Constraints and clarifications

* $1 \leq n \leq 1 \\ 000 \\ 000$
* $1 \leq k \leq 100 \\ 000$
* $k \leq n$
* $1 \leq a[i] \leq 1 \\ 000 \\ 000$, for $1 \leq i \leq n$
* The values in the sequence can repeat.

# Example

`cmmdc.in`
```
6 3
6 9 8 10 15 3
```

`cmmdc.out`
```
3
15 9 6
```

## Explanation

The greatest common divisor that can be obtained from a group of 3 numbers is 3, and the three numbers that give the maximum sum, sorted in descending order, are $15, 9$ and $6$.
```