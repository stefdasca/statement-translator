## Task

Given an array $a$ with $N$ integers and a natural number $K$, a subarray $a[i]$, $a[i+1]$, $\dots$, $a[j]$ is called zig-zag if $a[i] > a[i+1] < a[i+2] > \dots$ or $a[i] < a[i+1] > a[i+2] < \dots$. A subarray is called almost-zig-zag of order $K$ if it contains at most $K$ errors. An error is defined as a triplet of consecutive elements in the subarray that is not zig-zag. Find all almost zig-zag subarrays of order $K$ with a length greater than or equal to 3.

## Input data

The input file `zigzag2.in` contains on the first line two integers $N$ and $K$ as described in the problem statement. The next line contains $N$ integers representing the elements of the array $a$.

## Output data

The output file `zigzag2.out` must contain an integer representing the number of almost zig-zag subarrays of order $K$ with a length greater than or equal to 3.

## Constraints and clarifications

$3 \leq N \leq 1\ 000\ 000$

$0 \leq K \leq 1\ 000\ 000$

The elements of the array are signed 32-bit integers.

For some tests worth $10$ points, it is guaranteed that $2 \leq N \leq 300$.

For other tests worth $10$ points, it is guaranteed that $2 \leq N \leq 2\ 000$.

The problem will be evaluated on tests worth $90$ points.

## Examples

Examples will represent tests worth $10$ points "from the start".

## Example

`zigzag2.in`\
`4 1 2 1 1 2`\
`zigzag2.out`\
`2`


`8 5 -2 1 7 -5 -8 9 10 3`\
`zigzag2.out`\
`18`

`9 4 6 -9 -7 -8 -1 -3 0`\
`zigzag2.out`\
`136`

## Explanation

In the first example the array has $4$ elements. We are asked for the number of almost zig-zag subarrays of order $1$ of the given array. We have $3$ subarrays with length greater than or equal to $3$:

$2 1 1 2$: the highlighted subarray has one error, as the triplet $(2,1,1)$ is not zig-zag

$2 1 1 2$: the highlighted subarray has one error, as the triplet $(1,1,2)$ is not zig-zag

$2 1 1 2$: the highlighted subarray has two errors, as the triplets $(2,1,1)$ and $(1,1,2)$ are not zig-zag