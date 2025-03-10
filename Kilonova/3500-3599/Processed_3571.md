
# Task
A **"antenna tree"** with $n$ nodes is defined by the following structure:
- $n$ nodes are aligned in a line and between any two adjacent nodes, there is an edge. These nodes are numbered from $1$ to $n$.
- Each of the $n$ nodes can have $0$, $1$, or $2$ lateral neighbors.
- Lateral neighbors are labeled with values greater than $n$.
- An **"antenna tree"** has at least $n$ and at most $3 \cdot n$ nodes.

In the figure below, we have an antenna tree with $10$ nodes, for $n = 5$. Nodes $1$ and $4$ have two lateral neighbors, nodes $2$ and $5$ have no lateral neighbors, and node $3$ has one lateral neighbor.

~[fig1.png|align=center]

Given an **antenna tree** with $n$ nodes, determine the number of **connected subtrees** in the given tree. The result should be calculated modulo $10^9 + 7$.

# Input data

The first line of the input file `antena.in` contains the natural number $n$.  
Each of the following $n$ lines describes the lateral neighbors of each node from $1$ to $n$ as follows:  
- The first number on each line is $nv$ representing the **number of lateral neighbors** ($0$, $1$, or $2$).
- The next $nv$ values on the line represent the **identifiers of the lateral neighbors**, distinct and greater than $n$.

# Output data

The first line of the output file `antena.out` will contain a single integer representing the **number of connected subtrees** modulo $10^9 + 7$.

# Constraints and clarifications

- $1 \leq n \leq 100 \ 000$;
- $0 \leq nv \leq 2$;
- The numbers that identify the lateral neighbors are natural, distinct, and greater than $n$.  
- It is guaranteed that the nodes of the tree are labeled with consecutive numbers from $1$ to the total number of nodes in the tree (at least $n$ and at most $3 \cdot n$ nodes).
- Subtasks:

|#| Points |        Constraints                             | 
|-|---------|-----------------------------------------------|
|1|   17    |$1 \leq n \leq 10$,  $1 \leq nv \leq 2$                       |
|2|   20    |$1 \leq n \leq 100 \ 000$,  $nv = 0$ (no lateral neighbors)  |
|3|   38    | $1 \leq n \leq 2 \ 000$,  $1 \leq nv \leq 2$   |
|4|   25    | $1 \leq n \leq 100 \ 000$,  $1 \leq nv \leq 2$    |

# Example 1

`antena.in`
```
2
2 3 4
1 5
```

`antena.out`
```
17
```

## Explanation

In the figure below, you can see the tree from the example:

~[fig2.png|align=center]

The counted connected subtrees are:
1. **Individual nodes**: $(1)$, $(2)$, $(3)$, $(4)$, $(5)$;
2. **Groups of connected nodes**: $(1,3)$, $(1,4)$, $(1,3,4)$, $(2,5)$, $(1,2)$, $(1,2,3)$, $(1,2,4)$, $(1,2,5)$, $(1,2,3,4)$, $(1,2,3,5)$, $(1,2,4,5)$, $(1,2,3,4,5)$.

For each group of nodes in parentheses, **all the edges present in the tree between those nodes** are considered.
The total number of connected subtrees is $17$.

# Example 2

`antena.in`
```
5
2 9 7
0
1 8
2 6 10
0
```

`antena.out`
```
131
```

## Explanation

This example corresponds to the tree in the problem statement:

~[fig1.png|align=center]
