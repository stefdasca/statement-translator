# Dominoes

On a board there are $N$ dominoes. These are arranged in the form of a tree. If some domino pieces are hit with enough force, they will fall onto another piece (except for piece $1$ which does not fall onto other pieces). For each domino piece on the board, it is known how many other pieces need to fall onto it in order for it to fall, as well as which pieces can fall onto it. Mitruț has just discovered the board with the dominoes and is wondering what is the minimum number of pieces he needs to knock over in order for piece $1$ to fall. Since Mitruț has strict rules regarding trees, he only allows himself to knock over the pieces that have no other pieces falling onto them (the leaves in the tree).

## Task

Answer Mitruț's question.

## Input data

The input file `dominouri.in` contains on the first line the number $N$. The following $N$ lines each contain a number $C_i$ $(1 \leq i \leq N)$, representing how many pieces can fall onto piece $i$, followed by $C_i$ numbers - the indices of the pieces which if hit fall onto piece $i$. The last line of the file contains $N$ natural numbers $F_i$ $(1 \leq i \leq N)$. $F_i$ represents the number of pieces that need to fall on domino $i$ for it to also fall. The leaves in the tree have this number equal to zero.

## Output data

The output file `dominouri.out` contains on the first line a single natural number representing the answer to Mitruț's question.

## Constraints and clarifications

$1 \leq N \leq 100\ 000$ 

$F_i$ is always less than or equal to the number of children of node (piece) $i$.
  
For all terminal nodes in the tree $F_i = 0$.

## Example

`dominouri.in` 
```
10 
3 2 3 4 
2 5 6 
1 7 
3 8 9 10 
0 
0 
0 
0 
0 
0 
2 1 1 2 0 0 0 0 0 0 
```

`dominouri.out` 
```
2
```

## Explanation

Two pieces are enough to knock over domino $1$. These are either $5$ and $7$ or $6$ and $7$. Domino $7$ is used to knock over $3$, while piece $5$ is used to knock over $2$. The pieces that make $1$ fall are $2$ and $3$.