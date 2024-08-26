## Freakadebunic

Living in difficult times where the 'fear of Grandpa' is prevalent, Paula from the land of Fleschin decides to take action and dethrone the great Grandpa. The land of Freschin can be represented as a tree with bidirectional edges, consisting of $N$ nodes, with Grandpa's headquarters in node 1. Paula prepares an assault with troops positioned in $K$ different nodes. Grandpa, in turn, will counter with archers in the "early" nodes. We call a node "early" if it is the first common node in the paths to node 1 of any two troops. Determine in how many "early" nodes Grandpa needs to send archers and which these nodes are.

## Input data

The input file `freakadebunic.in` will contain 2 numbers on the first line: $N$ (the number of nodes) and $K$ (the number of nodes with troops). The second line will contain $K$ different numbers representing the nodes where Paula will send troops. On the next $N-1$ lines, there will be 2 numbers each $A$ and $B$, indicating an edge between nodes $A$ and $B$.

## Output data

The output file `freakadebunic.out` contains a single number $T$ on the first line representing the number of "early" nodes, and on the second line $T$ numbers sorted in ascending order representing the "early" nodes.

## Constraints and clarifications

$1 \leq K \leq N \leq 100\,000$

For 30 points, $1 \leq K \leq N \leq 1000$

For another 30 points, $1 \leq K \leq N \leq 3000$

## Example

`freakadebunic.in` 

```
10 4
4 5 6 8
1 2
1 4
1 3
2 5
2 6
2 7
3 8
3 9
6 10
```

`freakadebunic.out` 

```
2
2 7
```

`freakadebunic.in` 

```
4 4
5 6 7 1
2 1
3 1
4 1
3
```

`freakadebunic.out` 

```
1
3
```

## Explanation

In the first example, the path of the troops from node 5 to 1 is: $5 \rightarrow 2 \rightarrow 1$, and the path of the troops from node 6 to 1 is: $6 \rightarrow 2 \rightarrow 1$. The first common node of these paths to node 1 is node 2. If there were troops in node 10, the path to node 1 would be: $10 \rightarrow 6 \rightarrow 2 \rightarrow 1$. The first common node in the paths from nodes 5 and 10 is also node 2. In both cases, node 2 is an "early" node.