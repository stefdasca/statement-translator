## Deforestation

Our main character, Alex, got lost in a forest and decided that the only way to get out of the forest is to completely deforest it. The forest is represented by a set of trees of different heights, connected by roads of different lengths such that by traveling along the roads, one can reach any tree from any other tree. Alex can felled any tree he wants, and this action will cost him one energy point. Once a tree is felled, it must fall on one of the roads to which it is connected. If the height of the tree is strictly greater than the length of the road and the tree at the other end of the road has not yet fallen, it will also be felled at no additional cost. This tree will fall and can in turn fell another tree to which it is connected, and so on. Additionally, Alex can fell multiple trees simultaneously regardless of their positions and can choose the direction in which any tree will fall. Since he wants to consume as little energy as possible, Alex asks you to find the minimum possible number of energy points needed to fell all the trees.

## Input data

The first line will contain the number of trees $n$. The second line will contain $n$ values, the $i$-th number representing the height of tree $i$. The next $n-1$ lines will contain a triplet $(a, b, l)$ meaning there is a road of length $l$ between trees $a$ and $b$. 

## Output data

The output file will contain a single line that contains the required answer. 

## Constraints

$n \leq 1\ 000$ 

$1 \leq \text{the height of each tree} \leq 1\ 000$

It is guaranteed that the forest has a tree structure.

### $10$ points subtask:

$n \leq 10$ and the tree has the form of a line (there are exactly $2$ nodes with degree $1$ and $n-2$ with degree $2$) 

### $20$ points subtask:
$n \leq 100$ and the tree is formed from a central node to which all other nodes are connected 

### $30$ points subtask:
$n \leq 1\ 000$ and the tree is binary (each node has at most two children) 

### $40$ points subtask:
$n \leq 1\ 000$

## Example

`defrisare.in`
```
6
10 5 7 4 1 1
1 2 2
2 3 6
2 4 3
4 5 9
4 6 5
```

`defrisare.out`
```
4 
```

## Explanation

The number next to each node represents the height of the corresponding tree.

There are two ways to achieve a minimum number of operations:
1. Tree $1$ ($10$) falls on tree $2$ ($5$) which falls on tree $3$ ($7$) while the rest are felled individually. $(4)$
2. Tree $1$ ($10$) falls on tree $2$ ($5$) which falls on tree $4$ ($4$) while the rest are felled individually. $(4)$