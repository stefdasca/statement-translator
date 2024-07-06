```markdown
We are given $N$ digits. With these digits, we need to form $K$ numbers such that the sum of these $K$ numbers is minimal. The only condition we must respect when forming the $K$ numbers is that zero digits should not be at the beginning of a number.

# Task

Determine the minimum sum that can be achieved by constructing $K$ numbers that use all the $N$ digits.

# Input data

The file `cifre.in` contains on the first line two natural values $N$ and $K$ with the above-mentioned significance. The second line of the file contains $N$ digits separated by a space.

# Output data

The file `cifre.out` will contain on the first line a single number representing the sum of the $K$ numbers constructed.

# Constraints and clarifications

* $2 \leq N \leq 100\ 000$
* $1 \leq K \leq 100$
* $K \leq N$
* at least $K$ of the $N$ digits are non-zero

# Example

`cifre.in`
```
7 3
2 1 0 4 9 9 1
```

`cifre.out`
```
152
```

## Explanation

With the $7$ digits, we need to form $3$ numbers. The minimum sum we can achieve is $152$ and it can be obtained if we construct the numbers $19$, $24$ and $109$. There are also other possibilities to construct the three numbers.
```