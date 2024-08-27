## Task

A tgraph is an undirected graph having one of the following properties: 
- It has a single vertex 
- It contains an isolated vertex (which is not adjacent to any other vertex), and the graph obtained by removing this vertex is a tgraph 
- It contains a vertex that is adjacent to all others, and the graph obtained by removing this vertex and its adjacent edges is a tgraph

An equivalent definition of a tgraph is the following: to each node $K$ a non-negative value $a[K]$ can be assigned, such that there exists a strictly positive integer $T$ with the property that any subset of vertices in the graph is independent if and only if the sum of the values associated with the vertices in the subset is strictly less than $T$. A subset is called independent if either of the following statements is true: 
- It consists of a single vertex 
- Between any two vertices that are part of the subset there is no edge

Given a tgraph, assign a non-negative value $a[K]$ to each node $K$ and determine the number $T$, such that the aforementioned definition is respected.

## Input data

The first line of the input file `tgraf.in` contains an integer $P$, representing the number of tgraphs that will be described hereafter.
A tgraph is described on multiple lines as follows:
- the first line contains the integers $N$ and $M$, separated by a space, representing the number of vertices and the number of edges in the tgraph
- the next $M$ lines contain two distinct integers $a$ and $b$, from the set $\{1, 2, \dots, N\}$, indicating that there is an edge between the vertex numbered $a$ and the one numbered $b$

Descriptions of two consecutive tgraphs are separated by an empty line.

## Output data

For each of the $P$ tgraphs in the input file, you must print two lines to the output file `tgraf.out`:
- the first line will contain the number $T$
- the second will contain $N$ non-negative integers, representing the values associated with the vertices, in order, from 1 to $N$.

## Constraints and clarifications

$1 \leq P \leq 20$

$1 \leq N \leq 25$

$0 \leq M \leq N*(N-1)/2$

The determined number $T$ and the values associated with the vertices must be less than or equal to $10^9$

In general, the solution is not unique.

## Example

`tgraf.in`

```
4 
1 0 
2 0 
3 3 
1 2 
1 3 
2 3 
4 2 
1 4 
3 4 
```

`tgraf.out`

```
1 
0 
1000 
10 20 2 1 
1 
1 1 8 2 
```