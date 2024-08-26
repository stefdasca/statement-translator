# Cifre4

As Christmas is approaching quickly, Petrica wants to be kinder. He likes problems with large time limits, so he wants to find the smallest number formed only with the digits $2$, $3$, $5$, and $7$ that gives the remainder $N$ when divided by $P$.

## Input data

The input file `cifre4.in` contains on the first line a natural number $T$ which signifies the number of tests. The next $T$ lines contain two natural numbers $N$ and $P$, with the meaning described in the statement.

## Output data

The output file `cifre4.out` will contain $T$ lines, on the $i$-th line it will contain the answer for the $i$-th test, or $-1$ if there is no solution.

## Constraints

$T = 5$  
$1 \leq P \leq 5 \cdot 10^6$  
$1 \leq N \leq P - 1$  

## Example

`cifre4.in`  
```
3  
52 100  
11 100  
51 1123  
```

`cifre4.out`  
```
52  
-1  
322352  
```

## Explanation

The smallest number which gives the remainder $52$ when divided by $100$ is $52$.  
There is no number with the required property that gives the remainder $11$ when divided by $100$.