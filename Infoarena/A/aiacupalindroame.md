# Aiacupalindroame

We are given a tree with $N$ nodes numbered from $1$ to $N$ with the root at node $1$. The edges of the tree are associated with characters, which are lowercase letters of the English alphabet $(a, b, \dots, z)$. The Lowest Common Ancestor or $LCA$ of two nodes $x$ and $y$ is the node $z$ that is an ancestor of both nodes $x$ and $y$ and has the greatest depth from the root.

## Task

We are given $Q$ queries in the form of $x$ $y$ – where $x$ and $y$ are two nodes in the tree. For each query, determine if $(x, y)$ is $LCA$-palindrome or not. $(x, y)$ is considered $LCA$-palindrome if: The path from $x$ to $LCA(x, y)$ and the path from $y$ to $LCA(x, y)$ have the same length. The string of characters corresponding to the chain from $x$ to $y$, passing through $LCA(x, y)$, must be a palindrome.

## Input data

The first line of the file `aiacupalindroame.in` contains two natural numbers $N$ and $Q$, separated by a space, as described in the statement. The second line of the file contains $N-1$ numbers, separated by a space, where the $K$-th number $(1 \leq K < N)$ represents the parent of node $K+1$. The third line contains an array of exactly $N-1$ lowercase letters of the English alphabet, where the $K$-th character represents the cost of the edge between the node $K+1$ and its parent. Each of the following $Q$ lines contains a pair $x$ and $y$, separated by a space, with their meaning as described in the statement.

## Output data

The output file `aiacupalindroame.out` will contain $Q$ lines. Each line will contain $0$ if the answer to the query is false and $1$ if the answer is true.

## Constraints

$1 \leq N \leq 100\ 000$

$1 \leq Q \leq 500\ 000$

For tests worth 25 points 

$N \leq 1\ 000$ 

$Q \leq 5\ 000$

For tests worth 60 points 

$N \leq 20\ 000$ 

$Q \leq 100\ 000$

It is guaranteed that for each query the nodes are distinct.

The problem will be evaluated on tests worth 90 points.

10 points will be given automatically.

## Example

`aiacupalindroame.in` 
```
9 5
1 1 1 2 2 3 4 4
abaebaeb
2 7
2 4
1 9
5 8
5 9
```

`aiacupalindroame.out` 
```
0
1
0
1
0
```

## Explanation

For the query $(2, 7)$, $LCA (2, 7) = 1$, the distance between node $1$ and node $2$ is different from the distance between node $1$ and node $7$, so the answer is false.

For the query $(2, 4)$, $LCA = 1$, the distance from $1$ to $2$ is equal to the distance from $1$ to $4$, and the concatenation of the paths is “aa”, which is a palindrome, so the answer is true.

For the query $(1, 9)$, $LCA = 1$, the distances from $1$ to $1$ and from $1$ to $9$ differ, so the answer is false.

For $(5, 8)$, $LCA = 1$, the distances are equal, the string is “eaae” so, the answer is true.

For $(5, 9)$, $LCA = 1$, the string is “eaab”, which is not a palindrome, so the answer is false.