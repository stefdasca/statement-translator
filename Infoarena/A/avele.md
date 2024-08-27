## Avele

A rooted tree $T$ is called an AVELE tree if, for every non-zero node $v$, $v$ has exactly two children (not necessarily non-zero), $left\_son(v)$ and $right\_son(v)$, and the heights of the subtrees rooted at these two children differ by at most $1$. (formally, $|height(left\_son(v)) - height(right\_son(v))| \leq 1$, where $|x|$ denotes the absolute value of the integer $x$). The height of the subtree rooted at node $v$ is equal to $0$ if and only if the subtree is empty (in other words, $height(0) = 0$), otherwise it is defined by the formula $height(v) = 1 + max(height(left\_son(v)), height(right\_son(v)))$. 

## Task

A binary tree rooted at node $1$ is given. Determine the minimum cost to transform it into an AVELE tree. The possible operations are: Deleting a leaf from anywhere in the tree (with cost $cost\_rem$); Adding a leaf anywhere in the tree (with cost $cost\_add$).

## Input data

The input file `avele.in` contains on the first line the natural numbers $N$, $cost\_add$, $cost\_rem$ separated by a space, and on the next $N$ lines, two natural numbers each, representing $left\_son(i)$ and $right\_son(i)$, for each node $i$ in the tree.

## Output data

The output file `avele.out` must contain a single natural number, representing the minimum cost to transform the tree into an AVELE tree.

## Constraints and clarifications

$1 \leq N \leq 100\ 000$  
$0 \leq left\_son(i), right\_son(i) \leq N$  
$1 \leq cost\_add, cost\_rem \leq 1\ 000\ 000\ 000$  
It is guaranteed that the input data is valid for a binary tree rooted at node $1$.

## Example

`avele.in`
```
3 10 5
2 0
3 0
0 0
```

`avele.out`
```
5
```

`avele.in`
```
3 2 8
0 2
3 0
0 0
```

`avele.out`
```
2
```

`avele.in`
```
3 1 1
2 3
0 0
0 0
```

`avele.out`
```
0
```