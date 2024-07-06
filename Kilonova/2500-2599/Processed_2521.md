### Task

A ***Red Black Tree*** is defined as a binary tree with the following properties:
- Each node is either colored black or red;
- Each node has either $2$ children or $0$ children (it is a leaf);
- Each leaf is colored black;
- The root is colored black;
- Two nodes connected by an edge cannot both be red;
- $\\forall u$, a node in the tree, then, $\\forall v, w$, leaves in the subtree of $u$, the number of black-colored nodes on the path from $u$ to $v$ is equal to the number of black-colored nodes on the path from $u$ to $w$.

A ***Red Splay BTreap*** is defined as a binary tree with the following properties:

- Each node is either colored black or red;
- Each node has either $2$ children or $0$ children (it is a leaf);
- Each leaf is colored black;
- The root is colored black;
- Two nodes connected by an edge cannot both be red;
- $\\forall u$, a node in the tree, then, $\\forall v, w$, leaves in the subtree of $u$, the absolute difference between the number of black-colored nodes on the path from $u$ to $v$ and the number of black-colored nodes on the path from $u$ to $w$ is at most 1.

### Task

Given a tree with $N$ nodes numbered from $1$ to $N$ (**which is known to admit a Red Black Tree coloring**). Find how many of its colorings (with red and black) form a ***Red Splay BTreap***, but not a ***Red Black Tree***, modulo $998\ 244\ 353$.

### Input data

The first line will contain $N$, the number of nodes in the tree. The next $N-1$ lines contain the edges of the graph, each containing a pair of nodes $(u, v)$, meaning there is an edge between nodes $u$ and $v$ in the tree.

### Output data

Print a single number, representing the number of ways to color the tree such that it forms a ***Red Splay BTreap***, but not a ***Red Black Tree***, modulo $998\ 244\ 353$.

### Constraints and clarifications

- $1 \leq N \leq 99\ 615$;
- $1 \leq u, v \leq N$;
- The tree has the root in node $1$;
- For tests worth $15$ points, $1 \leq N \leq 11$;
- For tests worth another $16$ points, $1 \leq N \leq 31$;
- For the remaining $69$ points, there are no additional constraints.

### Example 1

`stdin`
```
5
1 3
3 2
1 4
3 5
```

`stdout`
```
1
```

#### Explanation

The only way to color the nodes is `BBBBB`.

### Example 2

`stdin`
```
13
1 3
3 2
2 8
3 5
5 4
5 7
7 6
1 10
10 9
10 11
2 12
7 13
```

`stdout`
```
6
```

#### Explanation

The $6$ ways to color the tree are: `BBRBBBBBBBBBB`, `BBBBRBBBBBBBB`, `BRBBRBBBBBBBB`, `BBBBBBRBBBBBB`, `BRBBBBRBBBBBB`, `BBRBBBRBBRBBB`.

### Example 3

`stdin`
```
15
1 2
2 5
2 3
3 4
1 9
9 7
7 6
7 8
9 11
11 10
11 13
13 12
3 14
13 15
```

`stdout`
```
12
```

#### Explanation

The $12$ ways to color the tree are: `BBBBBBBBRBBBBBB`, `BBRBBBBBRBBBBBB`, `BBBBBBBBBBRBBBB`, `BBRBBBBBBBRBBBB`, `BBBBBBRBBBRBBBB`, `BBRBBBRBBBRBBBB`, `BBBBBBBBBBBBRBB`, `BBRBBBBBBBBBRBB`, `BBBBBBRBBBBBRBB`, `BBRBBBRBBBBBRBB`, `BBBBBBBBRBBBRBB`, `BRBBBBBBRBBBRBB`.