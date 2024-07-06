Gigel participates in a mathematics and computer science contest and he loves prime numbers and sequences very much.

He has just found a sequence with $N$ natural numbers and a number $K$. Disappointed that not all elements of the sequence are prime, Gigel wants to find out which is the longest subarray in the sequence that contains at most $K$ non-prime elements.

# Task

Write a program that determines the longest subarray of elements from the sequence that contains at most $K$ non-prime numbers.

# Input data

The input file contains the numbers $N$ and $K$ on the first line, and on the next line $N$ natural numbers, separated by spaces, representing the elements of the sequence.

# Output data

The output file will contain two natural numbers $L$ and $P$, separated by a space, where $L$ is the maximum length of the determined subarray, and $P$ represents the starting index of the determined subarray.

# Constraints and clarifications

* $1 \leq N \leq 200\ 000$
* $1 \leq K \leq N$
* The elements of the sequence are less than $1\ 000\ 000$.
* If there are multiple subarrays for which the length is maximal, the one for which $P$ is minimal will be displayed.
* For tests worth $20$ points, $K = 0$.
* For other tests worth $20$ points, $N \leq 1\ 000$.
* For other tests worth $20$ points, $N \leq 200\ 000$ and $K = 1$.
* The sequence contains at least one prime number.

# Example

`secv.in`

```
8 2
10 3 7 6 11 4 9 7
```

`secv.out`

```
5 1
```

## Explanation

The resulting subarray is $(10, 3, 7, 6, 11)$. Another subarray of maximum length is $(3, 7, 6, 11, 4)$, but the starting index is larger.