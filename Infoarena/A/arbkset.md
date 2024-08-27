Arbkset

## Task

You are given a tree with $N$ nodes numbered from $1$ to $N$, having the root at node $1$. Each node $i$ $(1 \leq i \leq N)$ has an associated value $v(i)$. We want to select a set of exactly $K$ nodes such that:
- any two nodes in the set are not adjacent in the tree (i.e., for any two nodes $i$ and $j$ in the set, neither $i$ is the parent of $j$, nor $j$ is the parent of $i$)
- the sum of the values associated with the $K$ nodes in the set is maximal.

## Input data

The input file `arbkset.in` contains the number $T$ on the first line, representing the number of tests in the file. Then follow the $T$ tests. Each test is described on 3 lines in the file. The first line contains the numbers $N$ and $K$. The second line contains $N-1$ numbers, representing, in order, the parents of the nodes $2, \dots, N$. The third line contains $N$ integers, representing, in order, the values $v(1), \dots, v(N)$. 

## Output data

In the output file `arbkset.out` you will print $T$ lines. On the $i$-th line, print the maximum sum of the values associated with a set that satisfies the conditions from the statement. If such a set does not exist, print $-1$. 

## Constraints and clarifications

$1 \leq T \leq 15$  
$2 \leq N \leq 15000$  
$1 \leq K \leq \min(N, 1000)$  
$1 \leq v(i) \leq 10000$  
The parent of a node $i$ is always one of the nodes $1, \dots, i-1$.  

## Example

`arbkset.in`  
`3`  
`2 1`  
`1`  
`10 20`  
`2 2`  
`1`  
`10 20`  
`5 4`  
`1 2 2 2 1`  
`10 1 1 1 20`  

`arbkset.out`  
`20`  
`-1`  
`32` 

## Explanation

In the first test, the set consists of only node $2$. In the second test, it is not possible to select a set with $2$ nodes having the properties required in the statement. In the third test, the set consists of nodes $1$, $3$, $4$, and $5$.