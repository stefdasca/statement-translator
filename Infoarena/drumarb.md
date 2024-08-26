# Drumarb

An arbore (tree) with $N$ nodes, numbered from $1$ to $N$, is given. Additionally, $M$ questions are provided, to which you must respond. A question is specified by 4 nodes in the tree, $x$, $y$, $z$, and $t$, and asks for determining the number of nodes that lie on both the path from $x$ to $y$ and the path from $z$ to $t$ (in other words, you need to determine how many nodes are part of the intersection of the paths $x$-$y$ and $z$-$t$ in the tree).

## Input data

The first line of the input file `drumarb.in` contains 2 integers, $N$ and $M$, separated by a space. The next $N-1$ lines contain pairs of numbers $u$ and $v$, separated by a space, indicating that there is an edge between node $u$ and node $v$ in the tree. The following $M$ lines contain 4 integers each, separated by spaces, $x$, $y$, $z$, and $t$, specifying one question.

## Output data

In the output file `drumarb.out`, you will print the answer to each of the $M$ questions, in the order they are given in the input file. Each answer will be printed on a separate line.

## Constraints and clarifications

$1 \leq N \leq 100\ 000$

$1 \leq M \leq 100\ 000$

$1 \leq u, v, x, y, z, t \leq N$

## Example

`drumarb.in`

```
11 5
1 2
2 4
4 5
4 6
6 7
2 8
1 3
3 9
10 9
11 9
5 11 6 10
3 10 8 4
9 2 5 7
9 4 5 7
5 11 8 7
```

`drumarb.out`

```
5
0
0
1
2
```

