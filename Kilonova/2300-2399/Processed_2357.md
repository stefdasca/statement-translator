Given a **natural number** $n$ and $n$ natural numbers.

# Task

Find a code $c$, which is the smallest number among the read numbers that contains the largest digit from their writing.

# Input data

The first line of the file `cod.in` contains $n$, a natural number representing the number of numbers from which the code will be determined. The next line contains $n$ natural numbers separated by a space.

# Output data

The file `cod.out` will contain, on the first line, the number $c$ which represents the code.

# Constraints and clarifications

- $1 \leq n \leq 1\ 000$;
- numbers have at least one digit and at most $9$ digits.

# Example 1

`cod.in`
```
10
23 12 64 12 72 345 67 23 71 634
```

`cod.out`
```
67
```

## Explanation

$n=10$  
The largest digit in the writing of the numbers is $7$ and is found in the writing of the numbers $72$, $67$, $71$. The smallest number is $67$.