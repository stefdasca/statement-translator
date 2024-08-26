## Hektor

The Elf: "Hey, Cristi, why did you name this problem like this?"  
Patrick: "I named it after the author of the book 'Alone in the World.'"  
The Elf: "This BAC thing has driven you nuts... So how do I state this problem?"  
Patrick: "Well, Hektor feels alone in the world, so... he thought he could feel alone in the world on a directed acyclic graph, with costs on its $N$ nodes..."  
The Elf: "Okay, and? What do you do next?"  
Patrick: "Now he starts from node $A$ and goes to node $B$, choosing with uniform probability when he is in a node $X$ (with $X$ obviously being between node $A$ and node $B$, or even node $A$), an edge that leads to at least one path to node $B.... and the idea is that we want to see with what average cost he can reach node $B$!"
The Elf: "At least if he's alone, he should have money!"

## Input data

In the input file `hektor.in` the first line will contain 4 integers: $N$ (the number of nodes in the graph), $M$ (the number of edges in the graph), $A$ (the node where Hektor initially is), $B$ (the node where Hektor needs to reach). The next line will contain $N$ integers, with the $i$-th representing the cost of node $i$. The following $M$ lines will contain 2 numbers $x$ and $y$, indicating that there is a directed edge from node $x$ to node $y$. 

## Output data

In the output file `hektor.out` it will find a real number, representing the average cost for Hektor to reach from node $A$ to node $B$.

## Constraints

$N \leq 10^5$  
$M \leq 2 \cdot 10^5$  
The costs of the nodes are 32-bit integers.  
The answer fits within the double type, and it is considered correct if  
For Hektor to follow an edge, there must be at least one path from $A$ to $B$ passing through that edge.  
Otherwise, Hektor will ignore that edge.

## Example

`hektor.in`
```
2 1 1 2
1 1
1 2
```

`hektor.out`
```
2.00000
```

`hektor.in`
```
10 11 4 7
5 9 11 7 3 17 31 13 23 21
1 2
1 3
3 4
2 4
4 9
9 10
4 8
8 7
4 5
5 6
6 7
```

`hektor.out`
```
54.50000
```

`hektor.in`
```
13 14 1 2
1 1 1 1 1 1 1 1 1 1 1 1 1
10 12
10 11
12 13
11 13
13 1
1 3
1 4
3 5
3 8
4 6
5 9
9 7
7 2
8 7
```

`hektor.out`
```
5.50000
```

## Explanation

In the first example, no matter how uniform the probability is, we have only one option to reach from node $A=1$ to node $B=2$, namely traveling on the edge $1 \rightarrow 2$. In the second example, from $4$, Hektor can only go towards node $8$ or node $5$. He cannot go towards node $9$ because this node does not generate even one path towards node $7$.