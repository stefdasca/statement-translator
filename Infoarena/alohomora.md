# Alohomora

You are given $N$ keys and $M$ safes. Each key and each safe have 2 characteristics: rank and index. Your goal is to determine if you can open all the safes according to the following 3 rules: 
1. A key of rank $X$ can open any safe of rank $Y$ if $Y < X$.
2. A key of rank $X$ and index $A$ can open a safe of rank $X$ and index $B$ only if $A = B$. If such a pair exists, it must be used.
3. If you have $K$ keys of rank $X$, you can transform them into one key of rank $X + 1$ with any desired index.

## Input data

The input file `alohomora.in` will contain on the first line a natural number $T$ representing the number of tests. The first line of each test will contain 3 numbers $N$, $M$, and $K$. The next $N$ lines will contain two numbers each representing the rank and index of each key. The next $M$ lines will contain two numbers each representing the rank and index of each safe.

## Output data

The output file `alohomora.out` will contain $T$ lines, each line $i$ representing the answer for test $i$. The answer will be 1 if you can open all the safes, 0 otherwise.

## Constraints and clarifications

$1 \leq T \leq 10$

$1 \leq N, M, K \leq 100,000$

Ranks and indexes will be natural numbers in the range $[1, 1\ 000\ 000\ 000]$

A key can be used only once

## Example

`alohomora.in`  
```
2  
3 2 2  
2 4  
2 5  
2 5  
2 5  
3 1  
2 2  
2 2 2  
4 2 5  
2 5  
2 4  
2 6  
```

`alohomora.out`  
```
1  
0  
```

Note: The problem statement needs some modifications to be correct.