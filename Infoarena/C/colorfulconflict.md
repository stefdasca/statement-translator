## Task 

We are given a matrix of $N$ rows and $N$ columns. Each cell $(i, j)$ contains the color $A_{i,j}$. The bounding box of a color $x$ is defined as the rectangle of minimum area with sides parallel to those of the matrix that includes all cells where the color $x$ is found. Two colors $x$ and $y$ are considered to be in conflict if and only if their bounding boxes overlap (have a non-zero intersection area). Find 3 colors for which, any pair chosen, they do not conflict.

## Input data 

The input file `colorfulconflict.in` contains the number $N$ on the first line. The next $N$ lines contain $N$ numbers each, representing the colors $A_{i,j}$.

## Output data

The output file `colorfulconflict.out` contains, in the case where there are no 3 colors with the required property, the number $-1$. Otherwise, it will print the 3 numbers identifying the 3 colors found.

## Constraints 

$1 \leq N \leq 1000$ 

$1 \leq A_{i,j} \leq 1000000$

For 33% of the score, $A_{i,j} \leq 100$

For 7% of the score, $N \leq 5$

For 11% of the score, $N \leq 10$

For 16% of the score, $N \leq 20$

For 24% of the score, $N \leq 50$

For 49% of the score, $N \leq 200$

## Example 

`colorfulconflict.in`
```
3 
1 4 2 
5 1 4 
2 5 6
```
`colorfulconflict.out`
```
-1
```

`colorfulconflict.in`
```
6 
1 2 3 4 5 1 
2 1 5 4 3 2 
1 7 8 4 1 2 
8 7 1 4 3 9 
1 1 1 2 2 2 
6 6 6 6 6 6 
```
`colorfulconflict.out`
```
5 6 9
```

## Explanation 

In the first example, there are no 3 colors such that any pair of colors chosen among the 3 do not conflict.

In the second example, possible solutions are:
```
3 6 9 
4 6 9 
5 7 9 
5 6 7 
5 8 9 
5 6 8 
5 6 9 
3 7 9 
3 6 7 
4 7 9 
4 6 7 
6 7 9 
4 8 9 
4 6 8 
6 8 9
```
Also, all permutations of each solution are correct because the order in which we print the numbers in the output file is not relevant.