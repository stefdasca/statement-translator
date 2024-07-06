```
Smith the Caterpillar has started coloring again. This time he decided to try with undirected graphs with $N$ nodes labeled from $1$ to $N$ and $M$ edges numbered from $1$ to $M$.

On a walk, Smith starts from the node labeled $1$, walks along the edges of the graph, and then returns to the starting node.

Thus, the path that Smith takes starts and ends with node $1$, it may pass multiple times through the same node, and it can also pass multiple times through the same edge.

The edges of the graph are initially colored white, and each time the caterpillar passes over an edge it changes its color: from white to red and from red to white.

Each path corresponds to a final coloring of the edges, which we will name a possible configuration and represent it as a string of $M$ elements representing the final colors of the edges ($A$ for white and $R$ for red).

Smith has observed that not all possible configurations are beautiful. There are some 'special' edges that only look good if they have a certain color.

Smith wants to make a big impact in the art graph market, so he generates all possible beautiful configurations in lexicographic order for a given graph. He will launch the $K$-th generated configuration, with configurations being numbered starting from $1$.

# Task

Write a program that determines the $K$-th possible beautiful configuration, in lexicographic order.

# Input data

The first line of the input file `bcolor.in` contains the natural numbers $N, M, K$ separated by a space. The next $M$ lines contain the descriptions of the edges of the graph.
Line $i+1$ contains the description of edge $i$, consisting of $3$ natural numbers $x, y, z$ separated by a space.
The numbers $x$ and $y$ represent the nodes which are the endpoints of the edge, and $z$ is a number that can take the values with the following meanings:
* $z=0$ the edge is not special
* $z=1$ the edge is special, it must be colored white
* $z=2$ the edge is special, it must be colored red

# Output data

The output file `bcolor.out` will contain a single line consisting of $M$ characters from the set $\{ A, R \}$ representing in order the colors of the edges from the $K$-th possible beautiful configuration for the graph in the input file.

# Constraints and clarifications
* $1 \leq N, M \leq 200$
* $1 \leq K \leq 10^{8}$
* There are at least $K$ possible beautiful configurations for the given graph.
* The edges in the input file are distinct.

# Example

`bcolor.in`
```
10 9 2
1 2 0
3 5 1
2 3 0
3 4 0
4 5 0
5 2 0
2 4 0
6 7 0
7 8 0
8 6 0
```

`bcolor.out`
```
AAAARRRAAA
```

## Explanation

The possible beautiful configurations in lexicographic order are:
1: AAAAAAAAAA
2: AAAARRRAAA
3: AARRAARAAA
4: AARRRRAAAA
```

