Two natural numbers $M$ and $N$ are read.

# Task

Eliminate a sequence of digits from the number $N$ to obtain a number divisible by $M$ with the maximum value.

# Input data

The input file `div.in` contains in the first line the non-zero natural number $M$ and in the second line the natural number $N$.

# Output data

The output file `div.out` will contain two integers $i_1$ and $i_2$ separated by a space, representing the indices of the first and the last digit to be removed.

The digits of $N$ are indexed from $1$, from left to right. If there are multiple solutions, the one with the smallest first index should be written. If no digit needs to be removed, it will write two $0$s.

# Constraints and clarifications

* $2 \leq M \leq 30\ 000$
* $N$ has at most $5\ 000$ digits
* the first digit of $N$ is non-zero
* a sequence consists of digits located at consecutive positions in the number $N$

# Example 1

`div.in`
```
2
3333333333
```

`div.out`
```
1 10
```

# Example 2

`div.in`
```
7
33332222
```

`div.out`
```
0 0
```

# Example 3

`div.in`
```
7
3333322222
```

`div.out`
```
5 6
```

Please double check the statement and fix potential grammar and/or syntax errors according to the rules of the English language.