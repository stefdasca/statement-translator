Ksecv

## Task
A sequence $S$ containing $N$ positive integers is given. The positions of these numbers are numbered from $1$ to $N$. A subarray $S[i:j]$ $(1 \leq i \leq j \leq N)$ of a sequence $S$ is a sequence consisting of the elements at positions $i$, $i+1$, $\dots$, $j$ within the sequence $S$. We will say that a position $x$ belongs to a subarray $S[i:j]$, if $i \leq x \leq j$. The cost of a subarray $S[i:j]$ is equal to the maximum element within it. A $K$-partition of a sequence $S$ is a set of $K$ disjoint subarrays (in terms of positions in $S$) of $S$, which together cover the entire sequence $S$ (i.e., every position in $S$ belongs to exactly one subarray). The cost of a $K$-partition is equal to the sum of the costs of the $K$ subarrays. Determine a $K$-partition of minimum cost for a given sequence $S$.

## Input data
The input file `ksecv.in` contains two integers, separated by a space: $N$ and $K$. The second line contains $N$ integers, representing, in order, the elements of the given sequence $S$. Two consecutive numbers in the sequence will be separated by a space.

## Output data
In the output file `ksecv.out` you will print the minimum cost of a $K$-partition of the given sequence $S$ in the input file.

## Constraints and clarifications
$1 \leq N \leq 100\ 000$

$1 \leq K \leq min(N, 100)$

Any element of the sequence is an integer from the interval $[0, 10\ 000\ 000]$

## Example
`ksecv.in`

```
7 3 
3 2 1 5 6 3 2
```

`ksecv.out`

```
10
```