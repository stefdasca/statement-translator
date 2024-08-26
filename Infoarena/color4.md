## Task

Color 4

Vacation is coming and Gigel has decided to spend less time in front of the computer and to start painting. However, he likes computer science so much that he wants his paintings to be related to trees rooted at node $1$. Thus, all his paintings will take the form of a tree with $N$ nodes. Initially, all nodes will have color $1$. But Gigel is not satisfied and tries to make his paintings more interesting. Therefore, he can color a subtree with a color of his choice. From time to time, he is curious about which is the dominant color in a subtree and how many nodes have that color. However, the trees he paints can be impressive in size, so he will ask you to help him.

## Input data

The first line of the input file contains $3$ numbers, $N$, $M$, $C$ separated by a space. $N$ - the number of nodes of the tree, $M$ - the number of operations, $C$ - the maximum number of colors that Gigel has at his disposal. The next $N-1$ lines describe the tree, each containing $2$ numbers $x$ and $y$ indicating that there is an edge between $x$ and $y$. The next $M$ lines describe the operations as follows:
- $0 \ x \ c$ - the subtree of $x$ is colored with color $c$
- $1 \ x$ - the dominant color in the subtree rooted at $x$ and the number of nodes that have that color.

## Output data

The output file color4.out will contain a number of lines equal to the number of operations of type $1$ in the input file. On each line, there will be $2$ numbers $C$ $A$ with the significance: $C$ - the dominant color and $A$ - the number of nodes colored in color $C$.

## Constraints and clarifications

$1 \leq N \leq 50000$

$1 \leq M \leq 10000$

$1 \leq C \leq 75$

A color is dominant in a subtree if it has the most nodes colored in that color. If there are multiple colors that are dominant in a subtree, the color with the smallest index will be displayed.

## Example

`color4.in`

$11 \ 7 \ 3$ 

$10 \ 11$

$6 \ 7$

$11 \ 7$

$11 \ 9$

$4 \ 8$

$8 \ 2$

$10 \ 3$

$10 \ 4$

$4 \ 1$

$5 \ 9$

`0 \ 11 \ 2$

`1 \ 1`

`1 \ 10`

`0 \ 4 \ 3`

`0 \ 9 \ 1`

`0 \ 7 \ 2`

`1 \ 10`

`1 \ 6`

`color4.out`

`2 \ 5 \ 3 \ 3`