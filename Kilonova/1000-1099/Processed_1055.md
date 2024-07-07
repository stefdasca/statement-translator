
# Task

You are given two natural numbers $n$ and $k$. Determine the largest value that can be obtained by removing exactly $k$ digits from the number $n$, with all removed digits being in consecutive positions (one after another).

# Input data

The input file `cifrevecine.in` will contain on the first line the number $n$ and the second line the number $k$.

# Output data

The output file `cifrevecine.out` will contain the required value on the first line.

# Constraints and clarifications

* $n$ is a number between $10$ and $10^{17}$ inclusive.
* $1 \leq k$ and $k$ is strictly smaller than the number of digits in $n$.
* For $50$ points, $k = 1$.

# Example 1

`cifrevecine.in`
```
10002
3
```

`cifrevecine.out`
```
12
```

# Example 2

`cifrevecine.in`
```
1938
2
```

`cifrevecine.out`
```
38
```
