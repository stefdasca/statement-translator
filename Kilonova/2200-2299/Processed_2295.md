Mirunel, Miruna's brother, has developed a true passion for mathematics. While playing with sequences of natural numbers, he encountered a problem for which his mathematical skills are not sufficient. He discovered a sequence $S$ consisting of $N$ natural numbers ranging between $1$ and $N$ and needs to determine the maximum length of a subarray that contains a majority element. In a subarray of length $L$, an element is majority if it appears at least $\\lfloor \\frac{L+1}{2} \\rfloor$ times (the integer part of $\\frac{L+1}{2}$).

# Task

Determine the maximum length of a subarray that contains a majority element.

# Input data

The input file `mate.in` will contain on the first line a single natural number, $N$, with the meaning given in the statement. On the next line, there are $N$ natural numbers separated by a single space, representing the number sequence.

# Output data

The output file `mate.out` will contain a single natural number, representing the maximum length of a subarray that contains a majority element.

# Constraints and clarifications

* $1 \\leq N \\leq 500 \ 000$
* $1 \\leq S_i \\leq N$

# Example 1

`mate.in`
```
5
4 1 1 2 3
```

`mate.out`
```
4
```

## Explanation

The subarray $1 \ 1 \ 2 \ 3$ of length $4$ contains $1$, which is a majority element because it appears $\\lfloor \\frac{4+1}{2} \\rfloor = 2$ times.