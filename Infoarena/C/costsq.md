## Task

Given a sequence with $N$ elements: $w(1)$, $\dots$, $w(N)$. We want to divide this sequence into $K$ disjoint subarrays (a subarray consists of consecutive elements of the given sequence), in such a way that each element of the sequence belongs to exactly one subarray. We denote by $S[i:j]$ the subarray that starts at position $i$ and ends at position $j$. The cost of $S[i:j]$ is $(w(i)+w(i+1)+\dots+w(j))^2$. The cost of dividing into $K$ subarrays is equal to the sum of the costs of the $K$ subarrays. Determine a division of the given sequence into $K$ disjoint subarrays such that the cost of the division is minimal. Additionally, there are some additional constraints. If the subarray $S[i:j]$ is part of the division, then $i$ must satisfy the following constraints: $l(j) \leq i \leq u(j)$ (more precisely, if we choose a subarray to end at position $j$, then the starting position of the subarray must be between $l(j)$ and $u(j)$). The values $l(j)$ and $u(j)$ have the following properties:

$l(j) \leq l(j+1)$ (for $1 \leq j \leq N-1$)

$u(j) \leq u(j+1)$ (for $1 \leq j \leq N-1$)

## Input data

The first line of the input file `costsq.in` contains the integers $N$ and $K$. The next $N$ lines describe the given sequence. The $i$-th of these lines contains the values $w(i)$, $l(i)$, and $u(i)$ (in this order). All numbers on the same line are separated by a space.

## Output data

In the output file `costsq.out` you will print the minimum total cost of dividing the given sequence into $K$ subarrays that respect the given constraints. It is guaranteed that there will be at least one valid division.

## Constraints and clarifications

$1 \leq N \leq 100\ 000$

$1 \leq K \leq \min{100,N}$

$1 \leq w(i) \leq 1\ 000$

## Example

`costsq.in`
```
13 3
8 1 1
6 1 1
4 1 2
6 1 3
3 2 4
7 2 5
8 2 7
2 3 8
5 4 8
3 4 8
4 4 8
5 4 8
9 7 10
```

`costsq.out`
```
1642
```