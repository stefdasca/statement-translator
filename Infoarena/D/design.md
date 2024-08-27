## Task

While taking a shower, Bossanip was asked by his roommate (Rostogol): 
Rostogol: Do you want to destroy the world? 
Bossanip: What? 
Rostogol: Do you want to destroy the world? 
Bossanip: Whaaaaaat? I can't hear you. 
Rostogol: Do you want to destroy the world? 
Bossanip: Yes, yes, yes$\dots$ 
Set on destroying the world, the two adventurers engaged in art and fashion design. Unfortunately, art is like a Joker: it looks good but does nothing. Bored by the lack of originality of people dressing in clothes, Rostogol decided to be more rebellious. Thus, he decided to dress as a tree with $N$ nodes (why not?). Obsessed with expressing his chromatic feelings about the existence of the universe, Bossanip wanted to color the tree Rostogol is wearing using colors from $1$ to $K$. It's never good in life to be decisive, which is why instead of deciding what color to paint each node, they are more interested in what colors the tree nodes are surrounded by. Thus, for each node $X$ from $1$ to $N$, you know the list of neighbor colors of node $X$, but you do not know the color of that node. Find the lexicographically smallest solution with which you can color the tree.

## Input data

The input file `design.in` will contain on the first line $2$ natural numbers $N$ and $K$. The next $3 \times N$ lines describe the tree and its colors. For each node $i$ we have: 
- A natural number $X$ representing the number of neighbors in the tree of node $i$
- $X$ natural numbers with values from $1$ to $K$ representing the colors of the neighbors of node $i$ (in random order)
- $X$ natural numbers with values from $1$ to $N$ representing the indices of the neighboring nodes of node $i$ in the tree (in random order) 

## Output data

The output file `design.out` will contain $N$ numbers representing the colors of the $N$ nodes. The displayed solution must be lexicographically smallest.

## Constraints and clarifications

$2 \leq K \leq 6$  
$K \leq N$  
$K \times N \leq 500$  

This problem would have been better if it was named Christmas, but wait$\dots$

## Example

`design.in`  
```
6 2
3 2 1 2 4 2 5
3 2 1 1 1 6
3 1 2 2 1 1
1 1 1 1 1 1 
2 2 1 2 1 1
2 2 15 4 2 1 1 2
9 4 1 2 3 4
1 3 5 11 2 1
1 2 4 2 1 2
3 6 2 1 1 2
7 1 1 4 2 1
2 5 8 1 1 7
4 1 2 3 4 1 
10 14 15 1 1
9 2 1 1 2
12 2 3 4 11
13 1 1 12 
1 1 9
1 1 
1 9
3 1 1 1 2
2 2 1 1 1
4 1 3 2 4
```