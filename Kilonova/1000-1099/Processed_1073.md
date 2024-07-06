```markdown
A number is called **putere4** if it can be written in the form $X^4$ + $Y^4$ (with $X$ and $Y$ being non-zero natural numbers).

Given a sequence of $N$ natural numbers $T_1$, $T_2$, $\dots$, $T_N$. The sum of a subarray of $K$ terms of the sequence $T_i^4$ + $T_{i+1}^4$ + $\dots$ + $T_{i+K-1}^4$ is called **sum4** if its last digit is $4$.

# Task

Write a program that reads the non-zero natural numbers $N$ and $K$ and a sequence of $N$ non-zero natural numbers and determines:

* the number of terms in the given sequence that are **putere4**;
* the number of subarrays of length $K$ of the given sequence which represent a **sum4**.

# Input data

The first line of the file `patru.in` contains two natural numbers $N$ and $K$, separated by a space. The second line contains $N$ natural numbers, separated by a space, representing the terms of the given sequence.

# Output data

The output file `patru.out` contains on the first line the number of terms of the sequence that are **putere4**. The second line will contain the number of subarrays of the requested type.

# Constraints and clarifications

* $2 \leq K \leq N \leq 20\ 000$
* the terms of the sequence are natural numbers less than or equal to $10^9$;
* by subarray, we mean a succession of elements in the sequence located at consecutive positions;
* 60\% of the score is awarded for correctly displaying only the first value.

# Example

`patru.in`
```
7 5
1 2 17 15 23 19 17
```

`patru.out`
```
3
2
```

## Explanation

There are three **putere4** elements, namely $2$, $17$, and $17$. There are $2$ **sum4** subarrays of length $5$ with the given property (the one that starts at position $1$ and the one that starts at position $2$).
```