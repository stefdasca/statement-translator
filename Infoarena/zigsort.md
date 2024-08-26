## Task

Given an array of natural numbers $A[]$ that contains $N$ elements with distinct values. A zig-zag sort of order $k$ is defined as a rearrangement of the elements such that: $a_1 > a_2 > \dots > a_k > a_{k+1}$ $a_{k+1} < a_{k+2} < \dots < a_{2k+1}$ $a_{2k+1} > a_{2k+2} > \dots > a_{3k+1}$ and so on, meaning: the first $k+1$ elements must be in descending order the elements from positions $k+1$ to $2k+1$ must be in ascending order the elements from positions $2k+1$ to $3k+1$ must be in descending order In general, the elements from positions $pk+1$ to $(p+1)k+1$ must be in descending order if $p$ is even and ascending order if $p$ is odd. To solve the problem, you need to implement such a sorting but using only swaps between elements on consecutive positions (swap $A[i]$ and $A[i+1]$).

## Input data

The input file `zigsort.in` contains on the first line a natural number $T$ representing the number of tests, followed by the descriptions of each test: The first line contains the numbers $N$ and $K$ separated by a space. The next line contains $N$ natural numbers, the initial values of the array $A[]$.

## Output data

In the output file `zigsort.out` print for each test, on a separate line, the swaps as described that sort the array $A[]$ transforming it into a zig-zag sorted array of order $K$: The first number $M$ represents the number of swaps needed, and the next $M$ numbers represent indices $i$ for which $swap(A[i], A[i+1])$ is called, in this order, so that in the end, we have the desired result.

## Constraints and clarifications

$1 \leq N \leq 100000$

$1 \leq K \leq 4$

$4 \leq N$

$1 \leq A[i] \leq 100000$ for any $i$

If $K > 1$ then $N \mod K = 1$ (all monotone sequences have length $K$).

The program will be scored only if for any test $M \leq 375000$ and the swaps are valid (positions $i$ are in the interval $[1, N-1]$, and applied in the order they are printed to sort the array according to the constraints). There will be a maximum of 20 tests in the input file.

## Example

zigsort.in

```
2
4 1
5 6 3 1
7 3
6 7 5 3 2 1 9
```

zigsort.out

```
2
1
2
4
1
4
5
4
```

## Explanation

For the first test, the swaps are:

`1 2 3 4`\
`5 6 3 1` -> initial $A[]$, finally $A[1] > A[2] < A[3] > A[4]$\
apply $swap(1,2) \Rightarrow 6 5 3 1$\
apply $swap(2,3) \Rightarrow 6 3 5 1$ which satisfies $6 > 3 < 5 > 1$.

Two swaps were needed, position 1 with 2 and then 2 with 3.