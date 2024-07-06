**Balanced Number**: We call a natural number a _balanced number_ if the sum of the digits at even positions is equal to the sum of the digits at odd positions. For example, the number $13552$ is _balanced_ because $1+5+2=8=3+5$.

# Task

Given a natural number $N$, determine the smallest _balanced number_ strictly greater than $N$.

# Input data

The input file `ech.in` contains a single line with the natural number $N$.

# Output data

The output file `ech.out` will contain a single line, which will have the smallest _balanced number_ strictly greater than $N$.

# Constraints and clarifications

* The number $N$ has at most $23$ digits.
* For tests worth $40\ \%$ of the score, $N$ has at most $18$ digits.

# Example 1

`ech.in`
```
99
```

`ech.out`
```
110
```

# Example 2

`ech.in`
```
123133
```

`ech.out`
```
123134
```

