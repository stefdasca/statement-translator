## Fibsum

You are given $T$ queries $(left, right)$ and you are required to compute the sum $(fib\ left + fib\ left+1 + \dots + fib\ right)\ \mod\ 1\ 000\ 000\ 007$ for each of the $T$ queries, where $fib\ i$ represents the $i$-th term in the Fibonacci sequence.

## Input data

The input file `fibsum.in` will contain $T$ lines, each with 2 natural numbers $left$ and $right$, representing the query ranges.

## Output data

The output file `fibsum.out` will contain $T$ lines, with the $i$-th line containing the answer for the $i$-th query.

## Constraints

$1 \leq T \leq 10^4$  
$0 \leq left \leq right \leq 10^9$  
$fib\ 0 = fib\ 1 = 1$

## Example

`fibsum.in` 
```
2
3 5
1 4
```

`fibsum.out` 
```
16
11
```

## Explanation

The first terms of the Fibonacci sequence are:
$fib\ 0 = 1$  
$fib\ 1 = 1$  
$fib\ 2 = 2$  
$fib\ 3 = 3$  
$fib\ 4 = 5$  
$fib\ 5 = 8$

The first query is over the interval $[3, 5]$, with the sum $3 + 5 + 8 = 16$.

The second query is over the interval $[1, 4]$, with the sum $1 + 2 + 3 + 5 = 11$.