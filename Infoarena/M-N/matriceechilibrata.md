## BalancedMatrix

Komi received a gift from Tadano: a binary matrix with $N$ rows and $M$ columns, where each row has a sum of $X$ and each column has a sum of $Y$. Unfortunately, she lost the gift :(. But you can help her! Find any binary matrix with $N$ rows and $M$ columns, where each row has a sum of $X$ and each column has a sum of $Y$, if it is possible.

## Task

Find any binary matrix with $N$ rows and $M$ columns, where each row has a sum of $X$ and each column has a sum of $Y$, if it is possible.

## Input data

The input file `matriceechilibrata.in` contains the numbers $N$, $M$, $X$, $Y$.

## Output data

In the output file `matriceechilibrata.out` you must print $N$ rows, each containing $M$ binary digits not separated by spaces. They will represent the matrix found. If the required matrix does not exist, print $-1$.

## Constraints

$1 \leq N \\
1 \leq M \\
1 \leq X \\
1 \leq Y \ \leq 1000$

$X \leq M$

$Y \leq N$ 

For $20$ points $NM \leq 20$

For another $20$ points, $X$ and $Y$ are coprime.

## Example

`matriceechilibrata.in`
```
2 4 2 1
```
`matriceechilibrata.out`
```
1100
0011
```

`matriceechilibrata.in`
```
10 10 1 2
```
`matriceechilibrata.out`
```
-1
```

## Explanation

For the first example, $1 + 1 + 0 + 0 = 0 + 0 + 1 + 1 = 2$, $1 + 0 = 1 + 0 = 0 + 1 = 0 + 1 = 1$.

For the second example, there is no matrix with $N$ rows and $M$ columns where the sum of each row is $1$, and the sum of each column is $2$.