```markdown
Consider the Fibonacci sequence: $0$, $1$, $1$, $2$, $3$, $5$, $8$, $13$, $21$, $\\dots$.

Given a natural number $n$, write this number as a sum of non-consecutive elements from the Fibonacci sequence, where each element can appear at most once, such that the number of terms in the sum is minimal.

# Input data

The input file `fibo.in` contains on the first line the natural number $n$. This number can have a maximum of $80$ digits.

# Output data

The output file `fibo.out` will contain on the first line a single integer $x$, the number of terms used. On the next line will contain the $x$ values in ascending order.

# Constraints and clarifications

* $n$ can have a maximum of $80$ digits.

# Example 1

`fibo.in`
```
20
```

`fibo.out`
```
3
2 5 13
```

# Example 2

`fibo.in`
```
8
```

`fibo.out`
```
1
8
```
```