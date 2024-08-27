## Task

Becuriacm

In Gigel's house there are $N$ rooms numbered from $1$ to $N$ and $M$ switches numbered from $1$ to $M$. Switch $i$ ($1 \leq i \leq M$) toggles $K_i$ bulbs: $A[i][1]$, $\dots$, $A[i][K_i]$; when the switch is toggled, each of these bulbs turns on if it is off and vice versa. Initially, in the house, there are exactly $L$ bulbs turned on: $B_1$, $\dots$, $B_L$. Gigel is leaving home and wants to find a way to turn off all the bulbs.

## Input data

The input file `becuriacm.in` contains on the first line the number $T$ of tests. The following lines contain the tests, each having the following structure: The first line of a test contains the numbers $N$, $M$, and $L$, separated by spaces. The next line contains the numbers $K_1$, $\dots$, $K_M$, separated by spaces. The next line contains the numbers $B_1$, $\dots$, $B_L$. On line $a_i$ ($1 \leq i \leq M$) of the following $M$ lines are the numbers $A[i][1]$, $\dots$, $A[i][K_i]$, separated by spaces.

## Output data

In the output file `becuriacm.out` print the answer for all tests in the order they appear. If it's possible to turn off all the bulbs, print two lines: on the first line, the number $R$ of switches that need to be toggled and $R$ numbers separated by spaces, representing the switches that need to be toggled, in ascending order. If it is not possible to turn off all the bulbs, print a single line containing $-1$.

## Constraints and clarifications

$1 \leq N \leq 500$

$1 \leq M \leq 500$

$0 \leq K_i \leq N$ for any $1 \leq i \leq M$

$0 \leq L \leq N$

In the output file, in the answer for any test, a switch appears at most once.

## Example

`becuriacm.in`
```
2 
3 5 2 
1 0 2 1 2 
1 2 
1 2 
3 1 
1 2 3 
5 3 
1 0 1 
1 
2 3 
1 2 
1 2 
1 
5 
```

`becuriacm.out`
```
1
5
-1
```

## Explanation

For the first test, it is sufficient to toggle switch $5$. In the second test, it is impossible to turn off all the bulbs.