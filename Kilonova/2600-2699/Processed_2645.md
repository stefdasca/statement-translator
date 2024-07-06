# Control Digit of a Natural Number $x$

The control digit of a natural number $x$ is obtained as follows:

* if the number $x$ has a single digit, then the control digit of $x$ is equal to $x$;
* if the number $x$ has at least two digits, then the sum of the digits of $x$ is calculated (let's denote it by $s$); the control digit of $x$ will be equal to the control digit of $s$.

For example, the control digit of the number $175$ is equal to the control digit of the number $13 (1 + 7 + 5)$, which is equal to $4 (1 + 3)$. Let $x_1, x_2, \dots, x_N$ be a sequence of $N$ natural numbers. Two positions $i$ and $j$, with $1 \leq i \leq j \leq N$, define the subarray $[i, j]$ which will contain the numbers $x_i, x_{i+1}, \dots, x_j$. A subarray $[i, j]$ with the property that the sum of all elements in the subarray has a control digit equal to $9$ will be called secv9.

# Task

Write a program that, given $N$, the number of elements in the sequence, and $x_1, x_2, \dots, x_N$, the elements of the sequence, solves the following two tasks:
1. display the maximum length of a secv9 subarray;
2. display the number of secv9 subarrays in the sequence.

# Input Data

The input file `secv9.in` contains on the first line two natural numbers $C$ and $N$, representing the task that needs to be solved ($1$ or $2$), and the length of the sequence. The next line contains $N$ natural numbers $x_1, x_2, \dots, x_N$, separated by spaces, representing the elements of the sequence.

# Output Data

The output file `secv9.out` will contain on the first line a single natural number, representing the answer to the task $C$ from the input file.

# Constraints and Clarifications

* $1 \leq N \leq 1 \ 000 \ 000$
* $0 \leq x_i \leq 1 \ 000$, for any $1 \leq i \leq N$.
* It is guaranteed for all test data that there exists at least one secv9 subarray.

|#|Score|Constraints|
|-|-|--------|
|1|8|$C = 1$ and $1 \leq N \leq 1 \ 000$|
|2|10|$C = 1$ and $1 \ 001 \leq N \leq 5 \ 000$|
|3|21|$C = 1$ and $5 \ 001 \leq N \leq 1 \ 000 \ 000$|
|4|11|$C = 2$ and $1 \leq N \leq 1 \ 000$|
|5|15|$C = 2$ and $1 \ 001 \leq N \leq 5 \ 000$|
|6|35|$C = 2$ and $5 \ 001 \leq N \leq 1 \ 000 \ 000$|

# Example 1

`secv9.in`
```
1 7
1 7 6 1 11 5 9
```

`secv9.out`
```
3
```

## Explanation

There are two secv9 subarrays in the given sequence:

* The subarray $[3,5]$, consisting of the numbers $6, 1$, and $11$, has the sum of terms $18=6+1+11$, so the control digit is $9$;
* The subarray $[7,7]$, consisting of the number $9$, has the sum of terms $9$, so the control digit is $9$.

The maximum length of a secv9 subarray is 3.

# Example 2

`secv9.in`
```
2 7
1 7 6 1 11 5 9
```

`secv9.out`
```
2
```

## Explanation

There are two secv9 subarrays in the sequence: $[3,5]$ and $[7,7]$.