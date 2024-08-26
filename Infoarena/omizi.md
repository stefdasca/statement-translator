## Caterpillars

In a tree with $N$ nodes (numbered from $1$ to $N$), $M$ caterpillars (numbered from $1$ to $M$) have climbed up. Like any living being, our caterpillars were involved in politics, and like any politician, they wanted to climb as high as possible in the hierarchy of the tree, towards as many green and tasty leaves as possible. Although they have simple minds, each caterpillar is very committed to its political orientation. Thus, left-wing caterpillars always choose to go up and as far to the left as possible, while right-wing caterpillars go up and as far to the right as possible. To the biologists' surprise, caterpillars are very polite. Each caterpillar occupies a single position (node) in the tree and waits its turn for promotion. Thus, each day one promotion is carried out, namely, of the highest-ranking caterpillar that can climb higher in the hierarchy (has an unoccupied neighboring child node, with neighboring child node meaning an immediately following node situated higher up in the tree). If there are multiple caterpillars of the same rank, then a random draw decides. The caterpillar of the day chooses where it wants to climb if there are multiple possibilities according to its political orientation.

## Task

To be able to assess the damage and to save something from the path of the political caterpillars, the gardener has decided to appeal to you to find out the positions of the caterpillars after all promotions.

## Input Data

The first line of the input file `omizi.in` contains the natural numbers $N$ and $M$, with the meaning explained in the statement. On the next $N$ lines is the description of the tree. Specifically, on line $i+1$ is written the list of children of node $i$ from left to right as political orientation, ending with the number $0$. The children are separated by spaces. On the next $M$ lines are information about the caterpillars. Specifically, on line $N+1+i$ are a number $x$ and an uppercase letter $L$ separated by space ($x$ represents the number of the node where caterpillar $i$ is initially located, and $L$ is the political orientation of caterpillar $i$ - $S$ for left and $D$ for right).

## Output Data

The output file `omizi.out` will have $M$ lines, each containing a number from $1$ to $N$. Line $i$ contains the final position of caterpillar $i$ (after all promotions).

## Constraints and Clarifications

$3 \leq N$  
$2 \leq M$  
The root of the tree is always node $1$.  
The rank of a caterpillar is the distance in number of edges from the root to the node where it is located.  
Caterpillars will always choose accessible nodes according to their political orientation.  
For example, the preferred order for a caterpillar to be promoted, which is in a node with $3$ children, $4$, $5$, and $6$ (from left to right), is $4$, $5$, $6$ for a left-wing caterpillar and $6$, $5$, $4$ for a right-wing caterpillar, choosing the first child that is not already occupied.

## Example

`omizi.in`  
4 2  
2 3 0  
4 0  
0 0  
0  
1 S  
2 S  

`omizi.out`  
2  
4  

`omizi.in`  
10 5  
2 5  9 0  
0  
8 4 0  
0  
3 6 7 0  
0  
10 0  
0  
0  
0  
1 D  
6 S  
7 D  
5 S  
9 S  

`omizi.out`  
7  
6  
10  
8  
9