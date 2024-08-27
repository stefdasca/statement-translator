## Task

Given $N$ linear functions of the form $A * T + B$, determine the minimum value function for $M$ queries at a given time $T$. The queries are provided in increasing order of $T$.

## Input data

The input file `vmin.in` will contain on the first line two natural numbers $N$ and $M$. The following $N$ lines will contain $N$ pairs of integers, representing the values $A$ and $B$ for each function. On the line $N+2$, there will be $M$ elements representing the moments of time for which we need to determine the minimum value function.

## Output data

The output file `vmin.out` will contain on a single line $M$ values, representing the answers to the $M$ queries. The answer to a query is represented by the index of the minimum value function at that moment.

## Constraints and clarifications

$1 \leq N \leq 100\ 000$

$1 \leq M \leq 1\ 000\ 000$

$-10^9 \leq A,B \leq 10^9$

$0 \leq T \leq 10^9$

For tests worth $40p$, $N \leq 1\ 000$, $M \leq 3\ 000$

## Example

`vmin.in`
```
4 3
4 5
2 9
8 7
11 3
0 5 7
```

`vmin.out`
```
4 2 2
```

## Explanation

For time $T=0$, the minimum function is $11 * 0 + 3 = 3$, which is the function with index $4$.

For time $T=5$, the minimum function is $2 * 5 + 9 = 19$, which is the function with index $2$.

For time $T=7$, the minimum function is again $2 * 7 + 9 = 23$, which is the function with index $2$.