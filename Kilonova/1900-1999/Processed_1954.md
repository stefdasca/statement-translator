AxonT wants to see if you have the flooow. Given a flow network, with costs on edges, composed of the following components:
* Nodes \(S\) and \(T\), each placed on a separate row.
* The set \(V\) of nodes arranged on \(N\) rows, each row consisting of \(L[i]+1\) nodes \(( 1 \leq i \leq N)\).
* Node \(D\) placed on the last row.
* From node \(S\) to node \(T\) there is an edge with capacity \(K\) and cost \(0\).
* From node \(T\) to each node on the first row of the set \(V\), there are edges with capacity \(K\) and cost \(0\).
* From each node on row \(i\) to each node on row \(i+1\) (in the set \(V\)), there is a directed edge with capacity \(K\) and cost \(0\).
* From each node on the last row (row \(N\)) to node \(D\) there are edges with capacity \(K\) and cost \(0\).
* From the \(j\)-th node on line \(i\) to the \(j+1\)-th node on line \(i, 1 \leq i \leq N\) and \(1 \leq j \leq L[i]\), there is an edge with capacity \(1\) and cost \(A[i][j]\).

# Task

Knowing that \(S\) is the source of the flow and \(D\) is the destination, and given the numbers \(N\), \(K\), as well as the matrix \(A\), determine the maximum flow of maximum cost on the described network.

~[img1.jpg|align=center|width=auto]

# Input data

The file `flooow.in` contains on the first line 2 numbers \(N\) and \(K\) with the meaning from the statement/drawing. The next \(N\) lines describe the matrix \(A\). Each of the \(N\) lines begins with a number \(L\), the number of edges among the nodes on this line (there will be \(L+1\) nodes). Also on this line will follow \(L\) natural numbers, the costs of the \(L\) edges.

# Output data

The file `flooow.out` will contain on the first line two natural numbers separated by a space: the maximum amount of flow that can be transported from \(S\) to \(D\) and the maximum cost to transport this amount of flow.

# Constraints and clarifications

* \( 1 \leq N \leq 200 \ 000 \);
* \( 1 \leq\) the number of nodes on a row \(\leq 200 \ 001\);
* \( 1 \leq\) the number of elements in matrix \(A \leq 200 \ 000\);
* \( -10 \ 000 \leq\) any value in matrix \(A \leq 10 \ 000\);
* \( 1 \leq K \leq 5 \ 000\).

# Example

`flooow.in`
```
3 2
5 1 2 -1 2 1
5 3 -2 3 -2 3
2 -1 -2
```

`flooow.out`
```
2 13
```

