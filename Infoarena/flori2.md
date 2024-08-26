# Flowers2

In a field, there are $N$ flowers, represented as points in a plane. Determine the maximum number of flowers lying on the same straight line.

## Input data

The first line of the input file flori2.in contains the number of test cases $T$. The following lines describe the $T$ tests. The first line of each test case contains the number of flowers $N$. The next $N$ lines contain 2 integers each: the coordinates $X$ and $Y$ of each flower. There will not be two flowers located at the same point.

## Output data

For each test case, print to the output file flori2.out a line containing the maximum number of flowers lying on the same line.

## Constraints and clarifications

$1 \leq T \leq 11$  
$1 \leq N \leq 1000$  
$-10\,000\,000 \leq$ coordinates $X$ and $Y$ of a flower $\leq 10\,000\,000$

## Example

`flori2.in`  
```
2
4
0 0
1 1
2 2
0 1
2
0 0
1 1
3 2
```

`flori2.out`  
```
3
2
```