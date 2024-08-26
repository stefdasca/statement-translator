## Task

Given a matrix with $N$ rows and $M$ columns. We have $P$ laboratory mice, each of them being willing to traverse the matrix one or more times according to the following rules:
1) A path starts in the cell $(1, 1)$ and ends in the cell $(N, M)$. 
2) If at some moment the mouse is in cell $(X, Y)$, then it can move to the cell $(X + 1, Y)$ or to the cell $(X, Y + 1)$. Obviously, if one of these cells is outside the matrix, the mouse cannot move to that respective cell. We want to use the mice to traverse every possible path exactly once. Moreover, we want each of the $P$ mice to traverse the same number of paths. Otherwise, some mice will feel unfairly treated and will complain to the laboratory mice's union. Since the union has caused us problems in the past, we want to find out if a fair distribution of paths is possible for multiple triplets $N$ $M$ $P$.

## Input data

The input file `far.in` contains on its first line a number $T$. The next $T$ lines will each contain a triplet $N$ $M$ $P$, with the meaning described in the problem statement.

## Output data

The output file `far.out` will contain exactly $T$ lines. Line $i$ will contain the number 1 if a fair distribution is possible for case $i$ or the number 0 otherwise.

## Constraints and clarifications

$1 \leq N, M \leq 10^9$ 

$1 \leq P \leq 2000000000$ 

(You don't want to know how much cheese we need...)

For tests worth 40 points: 

$1 \leq N, M \leq 400$. 

For tests worth 60 points: 

$1 \leq N, M \leq 10^6$. 

Note! Notice that the name of the problem and the names of the input/output files do not match.

## Example

`far.in`
```
2 
2 2 3
2 3 3
```

`far.out`
```
0
1
```

## Explanation

In the first case, there are 2 paths: $(1, 1) \rightarrow (1, 2) \rightarrow (2, 2)$, and $(1, 1) \rightarrow (2, 1) \rightarrow (2, 2)$. We have more mice than possible paths, so the answer is negative.

In the second case, there are 3 paths: $(1, 1) \rightarrow (2, 1) \rightarrow (2, 2) \rightarrow (2, 3)$, $(1, 1) \rightarrow (1, 2) \rightarrow (2, 2) \rightarrow (2, 3)$, and $(1, 1) \rightarrow (1, 2) \rightarrow (1, 3) \rightarrow (2, 3)$. Since we have 3 mice, we can give each one a path.