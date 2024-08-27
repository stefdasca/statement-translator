## Task

In algebra, Tassadar has a "magic" problem to solve. Given $T$ square matrices, he needs to identify the "magic" ones. A matrix $A$ of size $N \times N$ is magic if for any permutation $P$ of length $N$ chosen, the sum $A[1][P_1] + A[2][P_2] + \dots + A[N][P_N]$ is constant. Tassadar has solved the problem, but he is curious if you can solve it as well.

## Input data

The input file `magicmatrix.in` contains on the first line an integer $T$, signifying the number of matrices. Next, each matrix is described as follows: one line contains the integer $N$ representing the size of the matrix, and the following $N$ lines will contain $N$ integers $A_{ij}$, representing its content.

## Output data

In the output file `magicmatrix.out` you will print $T$ lines with the answer `YES` if the corresponding matrix from the input file is magic, or `NO` otherwise.

## Constraints and clarifications

$1 \leq T \leq 10$  
$1 \leq N \leq 500$  
$-1\ 000\ 000\ 000 \leq A_{ij} \leq 1\ 000\ 000\ 000$

## Example

`magicmatrix.in`
```
2 
3 
3 -2 -1 
2 -3 -2 
-1 -6 -5 
4 
-2 -5 8 0 
4 7 -9 -4 
5 -1 0 5 
-7 -4 3 -8
```

`magicmatrix.out`
```
YES
NO
```

## Explanation

For the first matrix, any permutation chosen, the associated sum is equal to $-5$. For the second matrix, the sums corresponding to permutations $P = \{1, 2, 3, 4\}$ and $Q = \{2, 1, 3, 4\}$ are different.