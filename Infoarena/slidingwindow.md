## Task

Given an array of $N$ integers and a positive natural number $D$, determine the smallest number $K$ such that there exist at least two positions in the array, $i$ and $j$, $j > i$ which simultaneously satisfy the conditions:
$| A_i - A_j | \leq K$
$j - i \leq D$

## Input data

The input file `slidingwindow.in` will contain on the first line two natural numbers $N$ and $D$. The next line will contain $N$ numbers representing the given array.

## Output data

The output file `slidingwindow.out` will contain a single natural number $K$.

## Constraints and clarifications

$2 \leq D$  
$D \leq N$  
$N \leq 1\ 000\ 000$  
$|A_i| \leq 1\ 000\ 000\ 000$  

## Example

`slidingwindow.in`  
```
5 2  
5 7 1 4 8  
```

`slidingwindow.out`  
```
2  
```