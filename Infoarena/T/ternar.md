## Ternary

Mescheriakov escaped from distant Siberia and returned to his homeland. On the long journey home, he met a scholar who challenged him with the following problem: "Given a matrix of $0$, $1$, and $2$, determine the rectangle of maximum area that has $1$ on the boundary and only $2$ inside." Mescheriakov managed to solve this problem, but he is curious if you can do the same.

## Input data

The input file `ternar.in` contains on the first line two natural numbers $N$ and $M$ representing the dimensions of the matrix. The next $N$ lines contain $M$ numbers from the set $\{0,1,2\}$ representing the scholar's matrix.

## Output data

The output file `ternar.out` will contain a single number, representing the maximum area of the required rectangle.

## Constraints

$1 \leq N$,

$M \leq 1234$

## Example

`ternar.in`
```
3 6 
1 1 1 1 1 1 
1 0 1 1 2 1 
1 1 1 1 1 1 
```

`ternar.out`
```
9
```