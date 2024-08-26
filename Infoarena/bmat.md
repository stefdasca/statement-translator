## Task

Eudoxiu and Hurmuzachi have a binary matrix of size $N \times M$ at their disposal. The two players make alternate moves, with Eudoxiu making the first move. A move consists of choosing a submatrix of size $K \times K$, which contains the value $1$ in the top-left corner, and negating all values in that submatrix (all values of $0$ become $1$ and all values of $1$ become $0$). The submatrix does not need to be entirely inside the matrix. In this case, only the elements within the matrix will be negated. A player loses when they can no longer choose a valid submatrix. Eudoxiu and Hurmuzachi lost the initial matrix and now have a matrix that contains only $1$, $0$, and $?$. Determine the number of ways to complete the positions marked with $?$ with $1$ or $0$, so that Eudoxiu has a guaranteed winning strategy, considering that both players play optimally.

## Input Data

The input file `bmat.in` contains on the first line the numbers $N$, $M$, and $K$ with the meaning given in the statement. The next $N$ lines contain $M$ numbers, representing the elements of the matrix.

## Output Data

The output file `bmat.out` contains the number of matrices for which the first player has a guaranteed winning strategy MOD $666013$.

## Constraints and clarifications

$1 \leq N, M \leq 1000$ 

$1 \leq K \leq \text{Min}(N, M)$ 

## Example

`bmat.in`
```
2 3 2
? 0 1
1 0 0
```

`bmat.out`
```
2
```

`bmat.in`
```
2 3 2
0 0 0
0 0 1
```

`bmat.out`
```
1
```