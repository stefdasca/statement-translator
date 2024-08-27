## Task

Mioara has a tree with $N$ nodes, where the root is node $1$, and where each node $i$ has a value $v[i]$ between $1$ and $N$. All values are distinct. A subset $A$ of nodes is called good if and only if: 
1. Any two nodes $i$, $j \in A$, where $i$ is an ancestor of $j$, satisfy $v[i] < v[j]$;
2. For any two nodes $i$, $j \in A$, if $l$ is the deepest common ancestor of $i$ and $j$, then $l \in A$.

Mioara is curious: what is the sum of the values $|A|$ (i.e., the size of $A$) for all good sets $A$?

## Input data

The input file `arbset.in` contains on the first line the number $N$. The second line contains the values $v[1]$, $\dots$, $v[N]$. 

The next $N - 1$ lines each contain two values $x$, $y$, indicating the existence of an edge from $x$ to $y$.

## Output data

The output file `arbset.out` contains the required answer, modulo $10^9 + 7$.

## Constraints and clarifications
Subtasks:
- Subtask 1 (10 points) $N \leq 20$
- Subtask 2 (20 points) $N \leq 2000$
- Subtask 3 (10 points) $N \leq 300000$ Any node has at most 2 incident edges.
- Subtask 4 (10 points) $N \leq 300000$ At most one node has more than 1 incident edge.
- Subtask 5 (30 points) $N \leq 300000$ Any node has at most 3 incident edges.
- Subtask 6 (20 points) $N \leq 300000$

## Example

`arbset.in`
```
4 
2 1 3 4 
1 2 
1 3 
1 4 
```

`arbset.out`
```
11 
```

## Explanation

The good sets are $\emptyset$ (with size $0$), $\{1\}$, $\{2\}$, $\{3\}$, $\{4\}$ (with size $1$), $\{1, 4\}$ (with size $2$) and $\{1, 3, 4\}$ (with size $3$). Thus, the result is $11$.