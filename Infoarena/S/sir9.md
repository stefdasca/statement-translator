# Sir9

Let's consider an array $c_1 c_2 \dots c_n$ consisting of $n$ characters from the set $\{A, B\}$. We concatenate the array with itself and obtain an array of length $2n$. For an index $k \ (1 \leq k \leq 2n)$, we consider the subarrays of length at most $n$ that end at position $k$. Among these, let $s(k)$ be the lexicographically smallest subarray. Determine the index $k$ for which $s(k)$ has the greatest length.

## Input data

The input file `sir9.in` contains:
- On the first line, the natural number $n$, representing the length of the array.
- On the next $n$ lines, the characters of the array in order (one character per line).

## Output data

The output file `sir9.out` must contain:
- On the first line, the natural number $k$. If there are multiple values for $k$, choose the smallest.

## Constraints and clarifications

$1 \leq n \leq 30\ 000$

## Example

`sir9.in`
```
8
A
B
B
A
B
A
A
B
```

`sir9.out`
```
13
```