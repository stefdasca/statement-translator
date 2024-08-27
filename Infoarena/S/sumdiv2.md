SumDiv2

It is known that every number strictly greater than $1$ has at least $2$ divisors: $1$ and the number itself.

## Task

Consider $N$ intervals of natural numbers specified by two natural numbers $A_i$ and $B_i$ $(i=1, 2, \dots, N)$. For each interval $i$, display the sum of the divisors of all numbers in the interval $[A_i, B_i]$. 

## Input data

The input file `sumdiv2.in` contains on the first line the natural number $N$. Subsequent $N$ lines contain the heads of the $N$ intervals. On line $i+1$ there are two natural numbers, representing the bounds of interval $i$: $A_i$ and $B_i$ (separated by a space). 

## Output data

The output file `sumdiv2.out` contains $N$ lines. On line $i$ there will be a single natural number, representing the sum corresponding to the $i$-th interval. 

## Constraints and clarifications

$1 \leq N \leq 100\,000$ 

$2 \leq A < B \leq 1\,000\,000$ 

The interval $[A,B]$ is closed, so the values $A$ and $B$ will also be considered. 

For $20\%$ of the tests $N \leq 10$ and $B \leq 500$ 

For another $30\%$ of the tests $B \leq 100\,000$ 

The result will be less than $2^{64}$ 

## Example

`sumdiv2.in`
```
2
2 3
3 7
```

`sumdiv2.out`
```
7
37
``` 

## Explanation

In the first interval, the divisors of $2$ are $1$ and $2$, and the divisors of $3$ are $1$ and $3$. Their sum is $1+2+1+3=7$.