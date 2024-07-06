```markdown
Agent caterpillar Smith is tired of always destroying trees and now he develops his artistic sense – he much prefers coloring them. Every time he wants to create a new tree painting, he takes with him the $K$ colored pencils, chooses a tree from the garden, and starts working. The tree chosen by Smith is made up of $N$ nodes, has node $R$ as the root, and its structure is suitable for painting:
- each node has at most two branches that lead to two other nodes: one to the left and/or one to the right;
- between any two nodes there is a unique path made up of distinct branches, on which the caterpillar can walk to get from one node to another;
- the nodes in the left subtree of a node are all placed to the left of it, and those in the right subtree are all more to the right, therefore the nodes have been labeled from $1$ to $N$ from the leftmost to the rightmost.

The caterpillar noticed that his paintings are beautiful only if they respect some basic rules he read in a book:
- any node must be colored with exactly one of the $K$ colors;
- a node must be colored differently from its parent from the root (i.e., different from the node that precedes it when the caterpillar walks on the path from the root to the node);
- viewed from the outside, the tree must be colored differently from left to right: any node has a different color from the nearest node to its left and from the nearest node to its right (in other words, the color of the node labeled with $i$ must be different from the color of the nodes labeled with $i-1$, $i+1$).

# Task

Write a program that determines for a given tree in how many beautiful paintings (paintings that respect the criteria of the statement) it can be transformed. Since the required number can be very large, it is sufficient to find the remainder of the division by $10\ 007$.

# Input data

The input file `acolor.in` will contain on the first line the integers $N$, $R$, $K$ separated by a space. The next $N$ lines describe the structure of the tree. More precisely, on line $i+1$ there will be two numbers $st_i$, $dr_i$ separated by a space, representing the left child node and the right child node of node $i$, respectively. If a node has no left and/or right child then the corresponding number will be $0$.

# Output data

The output file `acolor.out` will contain a single line that contains the number of beautiful paintings that can be obtained for the given tree.

# Constraints and clarifications

* $0 < N \leq 100\ 000$;
* $1 \leq R \leq N$;
* $1 \leq K \leq 100$;
* $40$ points are awarded for tests with $N \leq 100$ and $K \leq 10$. 
* $60$ points are awarded for tests with $N \leq 400$ and $K \leq 15$.

# Example 1

`acolor.in`
```
9 5 4
0 0
1 3
0 4
0 0
2 6
0 7
0 9
0 0
8 0
```

`acolor.out`
```
3601
```

## Explanation

~[acolor.png]

# Example 2

`acolor.in`
```
3 1 2
0 3
0 0
2 0
```

`acolor.out`
```
0
```
```