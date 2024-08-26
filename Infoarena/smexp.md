## Task

Let $M$ be a square matrix with $N$ rows and $N$ columns, containing non-negative integer elements. $Sum(M)$ is defined as the sum of all elements in matrix $M$. Given a matrix $A$ with $N$ rows and $N$ columns, containing non-negative integer elements, calculate the value $X = (Sum(A_1) + \dots + Sum(A_K))$ modulo $1000000007$.

## Input data

The first line of the input file `smexp.in` contains the natural numbers $N$ and $K$. 

Then follow $N$ lines, each containing $N$ non-negative integer numbers. The $j$-th element of the $i$-th of these lines represents the value $A(i,j)$.

## Output data

The output file `smexp.out` will contain the number $X$ defined above.

## Constraints and clarifications

$1 \leq N \leq 10$ 

$1 \leq K \leq 1000000000$ 

$0 \leq A(i,j) \leq 10000$

## Example

`smexp.in`
```
2 3
1 2
3 4
```

`smexp.out`
```
354
```