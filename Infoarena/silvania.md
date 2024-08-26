# Silvania

Silvania, in Latin, means "wooded area." This problem is about forests. Bogdi from Silvania, the lumberjack, has turned to ecology. He decided to surround the forest with a fence so that other lumberjacks do not attack it anymore. However, not knowing how to do anything other than cutting wood, the fence will be constructed from the forest's wood. The forest in Silvania consists of a number of trees, each with a certain amount of wood, placed in a line at various positions. Bogdi can cut down any subset of trees, and from this act, he collects an amount of wood equal to the sum of the wood quantities of the cut trees. Bogdi definitely wants, after this cut, to have enough wood to surround the remaining trees with a single fence -- that is, to have an amount of wood greater than or equal to the distance between the first and the last remaining uncut tree. Help him find the minimum number of trees he needs to cut.

## Input data

The input file `silvania.in` will contain, on the first line, the number $N$ of tests. The next line will contain $N$ numbers, the wood quantities of the trees. The next line will contain $N$ numbers, the positions of the trees. 

## Output data

In the output file `silvania.out`, a single natural number will be printed, the minimum number of trees that need to be cut. 

## Constraints

$1 \leq N \leq 5000$

$1 \leq$ the wood quantity of a tree $\leq 1000000000$

$1 \leq$ the position of a tree $\leq 1000000000$

The positions of the trees are distinct

For tests worth 10 points $1 \leq N \leq 100$

For tests worth another 30 points $1 \leq N \leq 1000$

Each of these sub-tasks (the two mentioned above, and the one worth 60 points with $1 \leq N \leq 5000$) is divided into 2 smaller sub-tasks. The first half of the sub-task score is for tests where each tree is unique. More precisely, there are no two different trees with the exact same amount of wood. The second half of the sub-task score is for tests that have no additional restrictions.

## Example

`silvania.in`
```
5
2 3 2 1 2
4 5 1 3 10 2
```

`silvania.out`
```
2
```

## Explanation

There are several ways to cut the trees and build the fence. One of them: Cut the second tree (to get 3 wood) and the last tree (for another 2 wood). Build a fence from position $1$ to position $3 \dots 4$.