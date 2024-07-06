In a matrix $N$ x $N$ we have all the numbers from $1$ to $N^2$. The following procedure is considered to extract elements from the matrix row by row and arrange them into a permutation: a sniper hits one of the $4$ corners of the matrix. The diagonal/semi-diagonal of the matrix starting from that corner is traversed. The elements are added to the end of the permutation in the order of traversal. The traversed elements are removed from the matrix, and the remaining elements shift vertically or horizontally, reforming a new matrix that has "lost" a row or a column. A shift can be done horizontally or vertically at choice. **After the sniper shot and horizontal or vertical shift, the remaining elements must still form a matrix!**

# Task

Determine the $P$-th permutation of size $N^2$ in lexicographic order that can be obtained using the process described above.

## Note!

Due to the large size of the matrix, the data will be generated according to the [program](stub.cpp) given to the contestants in the workspace, with an example of input/output found in the `main` function.

# Input data

The first line contains the numbers $N$, $P$, and $Seed$. If $Seed = 0$, each of the following $N$ lines contains $N$ natural numbers, otherwise, the numbers will be generated according to the algorithm in the appendix, and can be accessed using the `ReadPerm(N)` function.

# Output data

If $seed = 0$, then the $N^2$ numbers representing the $P$-th permutation in lexicographic order that can be obtained will be printed on a single line, otherwise, a single value calculated according to the code below will be printed. We recommend using the `WritePerm(value)` function for all $N^2$ numbers in order.

$N^2$ numbers will be printed, representing the $P$-th permutation in lexicographic order that can be obtained. Again, for simplicity in testing, we recommend using the `WritePerm(value)` function for all $N^2$ numbers in order, and if $Seed = 0$, then all numbers will be printed at the output, otherwise the new resultant $Seed$ value will be printed.

# Constraints and clarifications
* $1 \leq N \leq 2\ 500$
* $1 \leq P \leq 10^{18}$
* $1 \leq A_{i,j} \leq N^2$
* The values in the matrix $A$ are distinct.
* It is guaranteed that there are at least $P$ permutations that can be obtained using the process described in the task.
* The semi-diagonal of a matrix is considered to be the diagonal starting from the bottom-left corner and traversing the elements towards the top-right or vice versa, while the diagonal of a matrix is considered to be the diagonal starting from the top-left corner and traversing the elements towards the bottom-right.
* Correction: the numbers do not necessarily form a permutation, but are distinct and do not exceed one million.

## Subtask 1 (9 points)
* $N \leq 3$
## Subtask 2 (21 points)
* $P = 1$
## Subtask 3 (43 points)
* $1 \leq N \leq 500$
## Subtask 4 (27 points)
* Without additional restrictions

# Example
`stdin`
```
3 5 0
6 4 3 
1 5 9 
2 8 7
```
`stdout`
```
2 5 3 1 4 8 9 6 7
```

`stdin`
```text
6 9 1729
```
`stdout`
```
5976389439715066411
```

Explanations
---

For the first example, the bottom-left corner is chosen, so the numbers 2 5 3 are added to the permutation. The matrix then becomes:

$
\begin{matrix}
6 & 4 &  \\
1 &   & 9\\
  & 8 & 7
\end{matrix}
$

Then a vertical shift is chosen and the matrix becomes:

$
\begin{matrix}
6 & 4 & 9\\
1 & 8 & 7
\end{matrix}
$

We choose the bottom-left corner (thus adding 1 4 to the permutation), and the matrix becomes:

$
\begin{matrix}
    6 &   & 9\\
      & 8 & 7
\end{matrix}
$

and after a horizontal shift, the matrix becomes:

$
\begin{matrix}
    6 & 9\\
    8 & 7
\end{matrix}
$

We choose the bottom-left corner again (thus adding 8 9 to the permutation), and the matrix becomes

$
\begin{matrix}
    6 & 7
\end{matrix}
$

We select 6, then 7 and finally obtain the permutation 2 5 3 1 4 8 9 6 7.