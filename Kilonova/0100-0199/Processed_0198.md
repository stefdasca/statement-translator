It is considered a graph that initially consists of $P$ isolated nodes, labeled from $1$ to $P$. Additionally, there are $N$ entries, where an entry can mean:

* command – a command is in the form `I+J`, meaning that the edge connecting nodes $I$ and $J$ is added to the graph (if $I$ and $J$ were already connected at that moment, no action is taken);
* query – a query is in the form `I?J`, meaning it is asked whether $I$ and $J$ are in the same connected component at that moment.

# Task
Starting from an initial graph of isolated nodes, which gradually "merge," you are also asked whether certain pairs of nodes are in the same connected component.

# Input data
From the file `entries.in`, the first line will contain the number $N$ of entries. The following $N$ lines contain the entries, one per line. An entry is encoded by three numbers separated by a space. The first two numbers represent the nodes $I$ and $J$ (integer numbers between $1$ and $P$), and the third is $1$ if the entry is a command and $2$ if the entry is a query.

# Output data
For each query, print on a separate line in the file `entries.out` the number $1$ if the nodes in question are in the same connected component at that moment, and the number $0$ otherwise.

# Constraints and clarifications
* For $40$ points: $1 \leq N \leq 5 \ 000$, $1 \leq P \leq 10 \ 000 \ 000$
* For another $60$ points: $1 \leq N \leq 100 \ 000$, $1 \leq P \leq 500 \ 000 \ 000$
* The problem has been modified

# Example

`entries.in`
```
9
1 2 2
1 2 1
3 7 2
2 3 1
1 3 2
2 4 2
1 4 1
3 4 2
1 7 2
```

`entries.out`
```
0
0
1
0
1
0
```