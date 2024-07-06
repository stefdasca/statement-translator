Here is the translated problem statement in English:

---

An tree with $n$ nodes numbered from $1$ to $n$ is given. The root is the node numbered $1$, and each node has an associated non-zero natural number.

# Task
Select a **connected subgraph** from the initial tree for which the sum of the values associated with the nodes equals a given natural number $k$. A subgraph is the graph from which nodes are removed together with their corresponding edges.

# Input data
The input file `arbore.in` has the following structure:
- The first line contains the numbers $n$ and $k$;
- The second line contains the value associated with node $1$ (the root of the tree);
- The third line contains two numbers: the first represents the parent node of node $2$, and the second represents the value associated with node $2$;
- The fourth line contains two numbers: the first represents the parent node of node $3$, and the second represents the value associated with node $3$;
- ...
- The line $n+1$ contains two numbers: the first represents the parent node of node $n$, and the second represents the value associated with node $n$.

# Output data
The output will be written to the file `arbore.out`:
- if **no solution exists**, it will only display the number $-1$ on the first line;
- if **a solution exists**, it will display the nodes that form a connected subgraph which meets the task requirements (one node per line).

# Constraints and clarifications
- $1 \le n \le 100$
- $1 \le k \le 1\ 000$
- The value associated with a node is a number from the interval $[1, 1\ 000]$.

# Example
`arbore.in`
```
10 29
30
1 7
1 22
2 5
2 10
4 1
4 2
5 25
5 2
5 4
```
`arbore.out`
```
2
4
5
6
9
10
```

## Explanation
~[img.png|width=45em]

---

I have translated the provided text while keeping the format and syntax structures. Please let me know if there are further adjustments or if you need assistance with anything else.