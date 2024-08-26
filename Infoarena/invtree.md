## Task

After learning in computer science about trees and the fact that they grow from top to bottom, you discover that you have been lied to, and now you have in front of you a tree that grows inversely, with the root at the bottom and the tree branching upwards. Each edge in the tree has a certain length, and a node is at a height equal to the sum of the lengths of the edges on the path from it to the root. Let's denote the height of node $i$ as $h_i$. You have a ladder of length $H$ and you wonder which nodes you can reach using it. But because the ladder might not be tall enough for your interests, you have thought of a strategy to extend it. More specifically, you can cut an edge of the tree, and thus the entire subtree will fall to the ground, allowing you to gather the branches to extend your ladder by the sum of the lengths of the fallen edges. You can even use the cut branch to extend your ladder. Because you are very independent, you have decided to ignore the laws of physics and disregard your parents' education: to cut a certain edge, you will climb to the upper node of that edge (the one with the greater height), let's call it $i$, and you will literally cut the branch beneath your feet. Of course, you can only do this if the current ladder is tall enough to get you to node $i$, meaning $H_{current} \geq h_i$. You are interested in which of the $N$ nodes of the tree you can reach, knowing that you can apply the described strategy as many times as you want, without considering the repeated falls you will suffer. It is considered that you can reach a node $i$ if you can bring your ladder to a height greater than or equal to $h_i$ and the node has not previously fallen due to the cutting of an edge.

## Input data

The first line of the input file will contain two numbers, $N$ the number of nodes and $H$ the initial height of the ladder. The next $N - 1$ lines will contain three numbers, $x$, $y$, $l$, signifying that there is an edge of length $l$ which connects nodes $x$ and $y$.

## Output data

The output file will contain a single line, which will print a string consisting of digits $0$ and $1$, the $i$-th digit being $1$ if it is possible to reach node $i$ and $0$ otherwise.

## Constraints and clarifications

$1 \leq N \leq 100000$

$1 \leq H \leq 1000000000$ 

$1 \leq l \leq 1000000000$ for all edges

For tests worth 12 points, $N \leq 250$

For tests worth 36 points, $N \leq 1000$

The root of the tree is node $1$

## Example

`invtree.in`

`invtree.out`

`5 1 1 2 1 2 3 10 1 4 9 4 5 1`

`11011`
 
## Explanation

Node $2$ can be reached without cutting any edge. To reach nodes $4$ and $5$, it is necessary to cut the edge $1-2$ and thus increase your ladder by $11$ units, obtaining a ladder of length $12$. If you wanted to reach node $3$, you could not cut the edges $1-2$ and $1-3$ because then the node would fall to the ground, nor the edges $1-4$ and $4-5$, so you will not be able to gather wood to extend your ladder.