---
Given a sequence with $N$ natural numbers $a_1, a_2, \dots, a_N$. On an element $a_i$ from the sequence, you can perform increment operations (addition with $1: a_i = a_i + 1$) or decrement operations (subtraction with $1: a_i = a_i - 1$). Each element in the sequence can be incremented or decremented any number of times.

# Task

Given the sequence of the $N$ natural numbers, determine:
1. the total minimum number of operations needed to transform all numbers in the sequence into prime numbers;
2. the minimum number of operations (increments and decrements) that must be performed on the elements of the sequence so that there exists a subarray of length $K$ consisting only of prime numbers.

# Input data

The input file `secvp.in` contains in the first line the natural numbers $N$ and $K$, and in the next line $N$ natural numbers. The numbers written on the same line are separated by spaces.

# Output data

The output file `secvp.out` contains in the first line a natural number $T$, representing the total minimum number of operations needed to transform all the numbers in the sequence into prime numbers. The second line will contain two natural numbers separated by space $minK nrsK$, where $minK$ represents the minimum number of operations that must be performed on the elements of the sequence so that there exists a subarray of length $K$ consisting only of prime numbers, and $nrsK$ represents the number of subarrays of length $K$ which can be obtained with the same number $minK$ of increments/decrements.

# Constraints and clarifications

* $2 \leq K \leq N \leq 100\ 000$
* $0 \leq a_i \leq 1\ 000\ 000$, for $1 \leq i \leq N$
* A subarray in the sequence is formed of elements that are located in consecutive positions in the given sequence.
* $1$ is not a prime number.
* Correct determination of the value $T$ awards $30\%$ of the test score. Correct determination of the values $T$ and $minK$ awards $70\%$ of the test score. Full marks are awarded for the correct determination of all $3$ values.

# Example 1

`secvp.in`
```
7 3
15 3 8 26 22 10 14
```

`secvp.out`
```
9
3 2
```

## Explanation

To transform $15$ into a prime number, $2$ increments are needed.
To transform $3$ into a prime number, $0$ operations are needed.
To transform $8$ into a prime number, $1$ decrement is needed.
To transform $26$ into a prime number, $3$ decrements are needed.
To transform $22$ into a prime number, $1$ increment is needed.
To transform $10$ into a prime number, $1$ increment is needed.
To transform $14$ into a prime number, $1$ decrement is needed.
The total number of operations needed is $9$.
The minimum number of operations needed to obtain a subarray of length $K$ is $3$. The two subarrays of length $K$ that require $3$ operations are $a_1, a_2, a_3$ and $a_5, a_6, a_7$.

