Int

Given $N$ open intervals (the endpoints are not included in the interval), situated on the OX axis. Determine a subset of intervals with the maximum number of elements such that the intersection of any two intervals in the subset is empty. 

## Input data

The first line of the input file `int.in` contains the number $N$ of intervals. The next $N$ lines contain two integers each, $A$ and $B$, representing the left endpoint and the right endpoint of an interval, respectively. 

## Output data

In the output file `int.out`, print the number of elements in the determined subset. 

## Constraints and clarifications

$1 \leq N \leq 50\ 000$

For each interval, we have $-2\ 000\ 000\ 000 \leq A < B \leq 2\ 000\ 000\ 000$

40$\%$ of the test files will have $N \leq 2000$

## Example

`int.in`
`
5
-3 10
-11 -7
1 6
0 1
0 30
`

`int.out`
`
3
`

## Explanation

The subset could contain the intervals $(-11,-7)$, $(0,1)$, and $(1,6)$