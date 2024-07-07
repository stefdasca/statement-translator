Given an infinite tree with $N$ nodes, numbered from $1$ to $N$.

The tree will be transformed as follows: at any stage, each node of degree $1$ different from the root in the current tree is replaced with a tree identical to the initially given one, and at the next stage, the process will be repeated for the obtained tree, thus forming an infinite tree. The following $3$ images present an example of the initially given tree, the tree obtained after the first stage of leaf extension, and the tree obtained after $2$ stages of leaf extension.

~[tairos.jpg]

# Task
Determine how many nodes are at distance $D$ from the root of the infinite tree.

# Input data
The input file `tairos.in` contains:
- The first line contains a natural number $N$, representing the number of nodes in the initially given tree.
- The second line contains an integer $D$, as described above.
- Each of the following $N-1$ lines contains $2$ integers $x$ and $y$ indicating that in the initially given tree there exists an edge $[x,y]$.

# Output data
The output file `tairos.out` will contain a single number, namely the remainder of the division of the requested number of nodes by $1 \ 000 \ 000 \ 007$.

# Constraints and clarifications
* $2 \leq N \leq 100$;
* $1 \leq D \leq 10 \ 000$;
* An *tree* is an undirected, connected graph without cycles.
* The *distance between two nodes $x$ and $y$* of a tree is equal to the *number of edges* of a chain with endpoints in nodes $x$ and $y$, a chain formed from distinct nodes.
* The *root* will be considered as node $1$;
* For $17$ points, we have $N = 3$;
* For another $22$ points, the answer is $\leq 10 \ 000$;
* In the contest, $10$ points were awarded by default, here the last $6$ tests are worth $10$ points extra.

# Example 1

`tairos.in`
```
4
3
1 2
3 1
3 4
```

`tairos.out`
```
5
```

## Explanation

The tree given in the input file has $4$ nodes. The number of nodes at distance $3$ from the root is required.
Following the images in the above examples, at distance $3$, we have the following $5$ nodes: $222$, $223$, $241$, $421$ and $43$.

# Example 2

`tairos.in`
```
5
3
1 2
3 1
3 5
4 3
```

`tairos.out`
```
8
```

`tairos.in`
```
5
25
2 1
2 3
1 4
5 2
```

`tairos.out`
```
33554432
