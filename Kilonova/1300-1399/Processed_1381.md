Here is the translated statement:

---

Any __stable number__ is a natural number composed of a single digit or having the sum of any two neighboring digits strictly greater than nine.
For any number that is not __stable__, one can perform operations to replace any two neighboring digits whose sum is strictly less than ten with a digit equal to their sum.

Replacement operations can be applied under the same conditions to the resulting numbers after each replacement, as many times as needed, until a __stable number__ is obtained.

For example, $291$ is a __stable number__ because $2+9>9$ and $9+1>9$, while $183$ is not stable because $1+8<10$. From the number $2453$, performing a single replacement, we can obtain $653$ or $293$ (a __stable number__) or $248$. The number $653$, not being __stable__, permits another replacement operation, thus obtaining the number $68$, which is __stable__. Similarly, from the number $248$, one can obtain the __stable number__ $68$.

# Task

Write a program to determine the largest natural __stable number__ that can be obtained from a given natural number by performing one or more of the mentioned replacement operations.

# Input data

The input file `sstabil.in` contains:
- The first line will contain a natural number $n$, representing the number of digits of the given number.
- On the second line, the digits of this number, separated by spaces.

# Output data

The output file `sstabil.out` will contain on one line the largest __stable number__ obtained.

# Constraints and clarifications

* $1 \\leq n \\leq 1 \\ 000 \\ 000$

# Example 1

`sstabil.in`
```
5
1 0 4 5 1
```

`sstabil.out`
```
191
```

## Explanation

$\\normalsize 1 \\ 0 \\ \\overgroup{\\LARGE 4 \\ 5} \\ \\normalsize 1 \\rightarrow 1 \\ \\overgroup{\\LARGE 0 \\ 9} \\ \\normalsize 1 \\rightarrow 1 \\ 9 \\ 1$

# Example 2

`sstabil.in`
```
5
5 2 8 3 2
```

`sstabil.out`
```
785
```

## Explanation

$\\overgroup{\\LARGE 5 \\ 2} \\ \\normalsize 8 \\ 3 \\ 2 \\rightarrow 7 \\ 8 \\ \\overgroup{\\LARGE 3 \\ 2} \\normalsize \\rightarrow 7 \\ 8 \\ 5$

---