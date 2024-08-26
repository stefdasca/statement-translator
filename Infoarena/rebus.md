## Task

You are given a horizontal crossword represented as an infinite grid, a list of $N$ words placed in the grid, each letter occupying one cell of the grid, and a pattern $P$. The $i$-th word initially occupies the positions $(i, 0) \rightarrow (i, |c_{i}|-1)$, where $|c_{i}|$ is the length of the $i$-th word. Two operations can be performed on the words:
1. A word is selected and shifted one position to the left or right, which has a cost of $1$
2. Two words are selected, and the lines containing them are swapped, maintaining their original offsets, which has a cost of $0$

Find the minimum cost of a set of moves such that the pattern $P$ is found in at least one column of the grid.

## Input data

The input file `rebus.in` contains on the first line a natural number $T$, representing the number of tests. The following lines contain these $T$ tests in the following format: the first line contains a natural number $N$, representing the number of words in the grid. The next $N$ lines contain the $N$ words, one per line. On the $(N+2)$-th line is the pattern $P$.

## Output data

The output file `rebus.out` will contain $T$ lines, with the $i$-th number representing the answer for the $i$-th test, or $-1$ if there is no solution.

## Constraints and clarifications

$1 \leq T \leq 10$

$1 \leq N \leq 25$

$1 \leq |c_{i}| \leq 25$

$|P| = N$

The $N$ words contain letters from the set $\{a, b, c, d, e, f\}$

## Example

`rebus.in`
```
1 
3 
aae 
bcbb 
edd 
eec
```

`rebus.out`
```
2
```

## Explanation

On the left, we have the initial position of the words in the grid. The first operation we will perform is to swap $bcbb$ with $edd$, the second operation is to shift $aae$ one position to the left, and the third operation is to shift $edd$ one position to the right. In the end, the cost of these $3$ operations is $0 + 1 + 1 = 2$, with the final configuration represented by the image on the right.

$ \dots $