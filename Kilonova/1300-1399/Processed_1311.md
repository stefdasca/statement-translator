
# Task

Given two natural numbers $n$ and $p$, the task is to find a natural number $m \leq 350\ 000$ with the property that it can be written both as the sum of $p$ nonzero perfect squares and as the sum of $p+1$ nonzero perfect squares, ..., and as the sum of $n$ nonzero perfect squares.

# Input data

The first line of the input file `patrate.in` contains two natural numbers $n$ and $p$ separated by a space, having the above meaning.

# Output data

The first line of the output file `patrate.out` will contain the sought natural number $m$. 
It is followed by $n-p+1$ lines. Line $i$ of the file, for $i=2, 3, \ldots, n-p+2$, will contain $p+i-2$ natural numbers separated by a space, with the property that the sum of their squares is $m$.

# Constraints and clarifications

* $2 \leq p \leq n \leq 1\ 000$
* The solution is not unique, any correct solution will be accepted.

# Example

`patrate.in`
```
4 3
```

`patrate.out`
```
18
1 1 4
2 1 2 3 
```

## Explanation

$18 = 1^2 + 1^2 + 4^2$
$18 = 2^2 + 1^2 + 2^2 + 3^2$
