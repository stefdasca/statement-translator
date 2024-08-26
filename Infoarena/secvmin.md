Secvmin

Two sequences of natural numbers, $A$ and $B$, of lengths $N$ and $M$ respectively, are given. $B$ has all distinct elements. Determine the minimum size of a subarray from $A$ in which $B$ can be found as a subsequence. If such a subarray does not exist, display $-1$.

## Task

## Input data

The input file `secvmin.in` will contain on the first line the numbers $N$ and $M$. The second line contains the $N$ natural numbers in array $A$, and the third line will contain the $M$ values in array $B$.

## Output data

The output file `secvmin.out` will contain a single value, the minimum size of a subarray that meets the property described.

## Constraints and clarifications

$1 \leq N$
$M \leq 100\ 000$ 
$1 \leq A_i$
$B_i \leq 1\ 000\ 000$

## Example

`secvmin.in`
```
8 3
4 7 8 2 4 5 9 1
7 8 4
```

`secvmin.out`
```
4
```

## Explanation

The solution is given by the subarray between positions $2$ and $5$ in array $A$.