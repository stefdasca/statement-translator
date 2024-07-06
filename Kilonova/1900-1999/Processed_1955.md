# Problem Statement

Bossanip and Henry have a tree $A$ with $N$ nodes. They are wondering, for each value $k$ between $1$ and $N-1$, what is the number of subtrees of $A$ for which the maximum degree of a node in the subtree is equal to $k$. A subtree is defined as a **connected** subset of nodes and edges from tree $A$. The degree of a node in a subtree is defined as the number of neighbors that node has in the subtree (**NOT** in tree $A$).

# Input Data

The input file `grarbore.in` will contain on the first line a natural number $T$, indicating the number of trees in the input file. On the following lines, the descriptions of those $T$ trees will be found. The description of the $i$-th tree will contain on the first line the natural number $N_i$, indicating the size of the $i$-th tree. On the next $N_i-1$ lines, there will be $N_i-1$ pairs of numbers $a$ and $b$, indicating that the $i$-th tree contains the edge $(a, b)$.

# Output Data

In the output file `grarbore.out` you will print $T$ lines. On the $i$-th of these lines, you will print $N_i-1$ values, the $k$-th of these being equal to the number of subtrees of the $i$-th tree for which the maximum degree of a node in the subtree is exactly $k$.

# Constraints and Clarifications

* $T = 5$;
* $1 \leq N_i \leq 500$;
* Nodes are numbered from $0$;
* For $60\%$ of the tests $n \leq 250$;
* For $10\%$ of the tests $n \leq 10$.

# Example

`grarbore.in`
```
1
5
0 1
0 2
1 3
1 4
```

`grarbore.out`
```
4 6 2 0
```

## Explanation

There are $4$ trees for which the maximum degree of a node is $1$, formed from the subsets of nodes $(0, 1)$, $(0, 2)$, $(1, 3)$, $(1, 4)$. There are $6$ trees for which the maximum degree of a node is $2$, formed from the subsets of nodes $(0, 1, 2)$, $(0, 1, 3)$, $(0, 1, 4)$, $(1, 3, 4)$, $(0, 1, 2, 3)$, $(0, 1, 2, 4)$. There are $2$ trees for which the maximum degree of a node is $3$, formed from the subsets of nodes $(0, 1, 3, 4)$, $(0, 1, 2, 3, 4)$. There are no trees for which the maximum degree of a node is $4$.