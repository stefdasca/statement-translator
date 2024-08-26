# Arbore2

I have two trees, represented by two binary trees with $M$ and $N$ nodes, respectively. In each node of such a tree, flowers grow (at least $0$, at most $10$). The order of the children matters (we distinguish between the left child and the right child). Two binary trees with flowers in the nodes are similar if (recursive definition): they both have $0$ nodes OR they both have at least one node, the same number of flowers in the root, the left subtrees are similar, and the right subtrees are similar. I want to transform the given two trees into $2$ similar trees (according to the definition above) with exactly $K$ $(0 \leq K \leq 100)$ flowers each, having the same roots as the initial trees. To achieve my goal, I can perform $2$ types of operations: cut a branch (remove a subtree from one of the two trees) or pluck a flower (decrease the number of flowers in one of the nodes of one of the trees by $1$). Since I want to work as little as possible to achieve my goal, I want to cut as few branches as possible and if there are several ways to cut as few branches as possible, I will choose one where I pluck as few flowers as possible. 

## Task

Write a program to help me!

## Input data

The file `arbore2.in` contains the desired number $K$ of flowers on the first line. The two trees follow, one after the other. A tree is given by the number of nodes $NR$ $(1 \leq NR \leq 100)$. Next, $NR$ lines follow, each containing information for a node: the number of flowers $F$ $(0 \leq F \leq 10)$, the number of the left child (or $0$ if it does not exist), and the number of the right child (or $0$ if it does not exist). The trees are valid (they contain numbers from $1$ to $NR$, do not have cycles $\dots$) and both have the root in node $1$. 

## Output data

In the file `arbore2.out` you will print on the first line the number $T$ of branch cuts and the number $R$ of flower plucks in the optimal solution. On the next $T$ lines, you will print the branch cuts. A branch cut is given by two numbers $ARB$ and $NOD$; this means that I cut the branch from tree $ARB$ ($1$ or $2$), which connected the node $NOD$ to its father. On the next $R$ lines, you will print the flower plucks. A flower pluck is given by two numbers $ARB$ and $NOD$; this means that I plucked a flower from node $NOD$ of tree $ARB$. The numbers on each line will be separated by a space. If there are multiple optimal solutions, print any one of them. All given tests will have at least one solution. 

## Example

`arbore2.in` 
```
7 
3 
5 2 3 
2 0 0 
1 0 0 
3 
6 2 0 
6 0 3 
5 0 0 
2 
5 1 3 
3 
2 1 2 
7 
```
`arbore2.out`
```
2 2 
1 2 
2 2 
2 2 
1 1 
1 3 
```