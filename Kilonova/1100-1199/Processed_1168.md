
Notate with $c$ and $r$ the quotient and the remainder of the division of a number $nr$ by $2^k$, where $k$ is a non-zero natural number. On the number, we can successively perform the following operations:

$O_1(nr, k)$ represents the transformation of the number $nr$ into the number $2^k \cdot (2 \cdot c + 1) + r$ for any remainder $r$

$O_2(nr, k)$ represents the transformation of the number $nr$ into the number $2^{k-1} \cdot c + r$ only if $r < 2^{k-1}$

# Task

Given $m$ and $n$, two non-zero natural numbers.

Perform successive operations $O_1$ or $O_2$ on the numbers $m$ and $n$ for chosen values of $k$, such that after a finite number of operations the two numbers become equal and the resulting value is minimal.

# Input data

The input file `operatii.out` contains a single line: $m \ n$, two non-zero natural numbers, separated by a space, representing the two given numbers.

# Output data

The output file `operatii.out` contains the following on the $i+j+3$ lines:

* the first line, the non-zero natural number $nmin$, representing the minimum value obtained from $m$ and $n$ by applying a sequence of $O_1$ or $O_2$ operations;
* the second line, the number of operations performed on the first number $m$;
* the next $i$ lines:
   * pairs of numbers representing the operation ($1$ or $2$) and the respective value of $k$ for that operation, separated by a space;
* the number of operations performed on the second number $n$, on line $i+2$.
* the next $j$ lines:
   * pairs of numbers representing the operation ($1$ or $2$) and the respective value of $k$ for that operation, separated by a space.

# Constraints and clarifications

* $1 < m,n \leq 2 \ 000 \ 000 \ 000$

# Example

`operatii.in`
```
11 45
```

`operatii.out`
```
15
2
2 3
1 2
2
2 2
2 4
```
