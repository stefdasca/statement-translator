## Task

A subarray of a sequence $A$ is a continuous subsequence of elements from that sequence. More precisely, a subarray of a sequence represents the values of the sequence on an interval of indices $i$, $i+1$, $i+2$, $\dots$, $j$ with $1 \leq i \leq j \leq N$ (where $N$ is the number of elements in the sequence). The geometric mean of a sequence of $K$ values is the $K$th root of the product of those $K$ values. For example, the geometric mean of the values $4, 9, 6$ is $6$. Given a sequence of $N$ positive real numbers $A$, calculate the subarray of length at least $K$ and maximum geometric mean.

## Input data

The first line of the input file `geom2.in` contains the values $N$ and $K$. Each of the following $N$ lines contains the $N$ real numbers. All numbers on the same line will be separated by a space.

## Output data

The only line of the output file `geom2.out` will contain the values $i$ and $j$, separated by a space, representing the indices of the subarray with the maximum geometric mean and length at least $K$. If there are multiple solutions, you can display any of them.

## Constraints and clarifications

$1 \leq N \leq 50000$  
$1 \leq K \leq \min\{N, 5000\}$  
$0 < A[i] < 1000.0$  

For $70\%$ of the tests, $K \leq 100$

## Example

`geom2.in`  
`7 3 0.1 0.2 0.3 1.0 0.8 0.9 2.0`

`geom2.out`  
`5 7`