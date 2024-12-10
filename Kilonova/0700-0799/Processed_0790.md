
We define a power of $3$ as a number of the form $3^k$, ($k$ is a strictly positive natural number), a power of $5$ as a number of the form $5^k$ ($k$ is a strictly positive natural number), and a power of $2$ as a number of the form $2^k$ ($k$ is a strictly positive natural number).
We are given a sequence of $n$ natural numbers. Starting from this sequence, we form a new sequence by eliminating all numbers that are not powers of $3$ and not powers of $5$. The relative order among the numbers that are not eliminated is preserved.

# Task

- Determine how many numbers the newly formed sequence contains.
- Also determine the number of subarrays of length equal to a power of $2$ in the newly formed sequence where the number of powers of $3$ is equal to the number of powers of $5$. A subarray is formed from elements found at consecutive positions in this newly formed sequence, and the length of a subarray is equal to the number of elements it contains.

# Input data

The first line of the file `235.in` contains a natural number $n$. Each of the following $n$ lines contains a natural number greater than $1$ representing the numbers of the initial sequence.

# Output data

The first line of the file `235.out` will contain a natural value $m$ representing the number of elements remaining in the sequence after elimination. The second line will contain a natural value $S$ representing the number of subarrays in the newly formed sequence that have the required properties.

# Constraints and clarifications

* $2 \leq n \leq 500\ \\ 000$;
* The numbers in the initial sequence are natural numbers in the interval [$2, 2 \cdot 10^9$].
* It is guaranteed that $m \leq 40\ \\ 000$ for each input data set.
* 30% of the points are awarded for the correct determination of the value of $m$, and 100% of the points are awarded for the correct determination of both values ($m$ and $s$).

# Example

`235.in`
```
8
625
125
5
9
15
81
100
125
```

`235.out`
```
6
4
```

## Explanation

The remaining sequence after eliminating numbers that are not powers of $5$ or $3$ has $6$ elements: $625, 125, 5, 9, 81, 125$.

In this sequence there are:
- two subarrays of two values containing an equal number of powers of $3$ and powers of $5$: $5, 9$ and $81, 125$;
- two subarrays of four numbers containing an equal number of powers of $3$ and powers of $5$: $125, 5, 9, 81$ and $5, 9, 81, 125$