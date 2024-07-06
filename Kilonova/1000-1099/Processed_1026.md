Be $V$ an array of $N$ natural numbers (integers, non-negative).

# Task

Given the array $V$ and the number $M$, calculate the number of subarrays such that the geometric mean of the elements in the subarray is equal to $M$. A subarray of a given array is understood as a sequence of one or more terms from the array found in consecutive positions.

# Input data

The input file `media.in` contains on the first line, the numbers $N$ and $M$, and on the next line $N$ integers, non-negative.

# Output data

The output file `media.out` will contain a single number representing the required value.

# Constraints and clarifications

- $5 \leq N \leq 50\ 000$
- $0 \leq V [i] \leq 10^9$
- $2 \leq M \leq 10^9$
- The geometric mean of the numbers $a[1], a[2], ..., a[K] \geq 0$ is $\\sqrt[K]{a_1 a_2 \dots a_K}$.
- Scoring will be done separately, the tests being independent of each other.
- The first test meets the following constraint: $1 \leq N \leq 50$. This test is worth 15 points.
- Tests $2 − 6$ meet the following constraint: $M$ and elements of the array $V$ are powers of $2$. These tests are worth $9$ points each.
- Tests $7 − 10$ have no additional constraints. These tests are worth $10$ points each.

# Example

`media.in`
```
5 4
1 2 4 8 4
```

`media.out`
```
4
```

## Explanation

The sought subarrays are: $[4], [4], [2, 4, 8], [2, 4, 8, 4]$