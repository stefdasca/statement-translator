
# Task

Given is a tree with $N$ nodes and the root in $1$, each node has an associated value.

For each node, specify how many values in the subtree rooted at that node are less than or equal to the value associated with the node.

# Input data

The first line contains $N$. The second line contains the parent array. The third line contains the values associated with the nodes.

# Output data

Print the answer for each node from $1$ to $N$, in this order.

# Constraints and clarifications

- $1 \le N \le 10^5$;
- $1 \le \text{Node values} \le 10^9$.

# Example

`stdin`
```
5
1 2 2 1
3 4 2 5 1
```

`stdout`
```
3 2 1 1 1
```

## Explanation

The tree looks like this:  
~[graph.png]
