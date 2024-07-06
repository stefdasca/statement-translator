Tassadar, the mayor of the city Araoșimit, has planted Japanese cherry trees along the boulevards. Over time, they have grown large and beautiful, but now they are too big, and their branches hinder traffic. For this reason, the mayor decided it would be necessary to cut some branches while preserving the beauty of the trees.

# Task 

Given $T$ pairs of trees $(A, B)$ with fixed roots, determine the minimum number of operations required on tree $A$ so that it becomes isomorphic to tree $B$, or state if this is not possible. An operation consists of removing a leaf from tree $A$.

# Input data

The input file `sakura.in` contains on the first line a single natural number $T$, representing the number of pairs of trees. The next $T$ pairs will be described. The first line of the description for each pair contains the number $N$, representing the number of nodes in the first tree (which will be operated upon). On the next $N - 1$ lines, there will be two numbers $x$ and $y$, indicating that there is an edge between the nodes with indices $x$ and $y$. On the following line, there is a number $M$, representing the number of nodes in the second tree. On the next $M - 1$ lines, there will be two numbers $x$ and $y$, indicating that there is an edge between the nodes with indices $x$ and $y$.

# Output data

In the output file `sakura.out`, $T$ lines will be displayed. On each line, you will print a single natural number, representing the answer for each pair of trees, in the order given in the input file. If, for a pair, it is possible to obtain the second tree from the first, you will display the minimum number of operations. Otherwise, you will display `-1`.

# Constraints and clarifications

* $ 1 \leq T \leq 10$;
* $ 1 \leq N, M \leq 500$;
* For $20\%$ of the tests $N, M \leq 13$;
* For $60\%$ of the tests $N, M \leq 100$;
* The nodes of the trees are numbered from $0$;
* All trees have the root node with index $0$;
* After removing a leaf, it is possible for the respective leaf's parent to also become a leaf and thus be removable;
* Two trees are considered isomorphic if they have the same root and there is a possibility to re-label the nodes of the first tree so that the two trees are identical.

# Example

`sakura.in`
```
2
4
0 1
0 2
3 1
2
0 1
1
2
0 1
```

`sakura.out`
```
2
-1
```

## Explanation

For the first pair, we can delete, in this order, nodes $3$ and $1$. The remaining trees are isomorphic because they have the same root $(0)$, and we can re-label node $2$ from the first tree to $1$. Thus, they will become identical. For the second pair, there is no solution.