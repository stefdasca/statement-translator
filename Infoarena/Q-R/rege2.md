## Task

King Leonidas needs to select an army of $300$ Spartans. Surprised by the large number of volunteers who want to join him in the upcoming battle of Thermopylae, the king needs to make a selection of the warriors. Thus, he decided to give them the following problem: Given a tree with $N$ nodes (labeled with consecutive numbers starting from $1$) rooted at node $1$, where each edge is associated with a cost. A downward chain in the tree is defined as any simple chain that connects a node $A$ with another node $B$ in $A$'s subtree. In other words, a downward chain is a chain from $A$ to $B$ where $A$ is an ancestor of $B$. We define the cost of a downward chain as the sum of the costs of the edges that form the chain. We call a coverage of a tree a partitioning of the edges into disjoint chains, whose union is the initial tree. King Leonidas wants to cover the entire tree with downward chains, but has a limited number of chains, denoted with $S$. The task is to determine the smallest number $K$ for which there exists a complete partitioning of the tree with at most $S$ chains such that the cost of each chain is at most $K$. If there is no such number $K$, output $-1$. Because you also want to fight alongside Leonidas for the freedom of Sparta, you need to solve this problem to secure a place among the first $300$ Spartans. Leonidas is a wise king. To ensure that there will be no Spartans attempting to guess the result, he asks you to answer $T$ such problems.

## Input data

The input file `rege.in` contains in the first line the number $T$, representing the number of tests in the file. The $T$ tests follow. Each test is described over several lines in the file. The first line contains the numbers $N$ and $S$. On the next $N-1$ lines, there are three numbers $x$, $y$, $z$, signifying that there is an edge between nodes $x$ and $y$ with a cost $z$.

## Output data

The output file `rege.out` must contain $T$ lines: on the line $i$, it contains the answer for the test number $i$.

## Constraints and clarifications

$1 \leq T \leq 5$   
$1 \leq N, S \leq 100\ 000$   
$1 \leq$ Cost of any edge $\leq 10\ 000$   

## Example

`rege2.in`

```
2
10 6
2 1 1
3 2 1
4 1 3
5 3 1
6 5 2
7 5 3
8 2 2
9 8 3
10 5 2
6 4
2 1 4
3 2 3
4 3 2
5 4 2
6 4 4
```

`rege2.out`

```
4
4
```

## Explanation

We have $T = 2$ tests.

For the first test, we have a tree with $N = 10$ nodes. We want to cover the tree with at most $S = 6$ chains. The tree can be covered with the following chains:
$1-4$ (cost $3$)  
$1-2-8$ (cost $3$)  
$8-9$ (cost $3$)  
$2-3-5-6$ (cost $4$)  
$5-10$ (cost $2$)  
$5-7$ (cost $3$)  

There are exactly $6$ chains (we are allowed a maximum of $6$), and the highest cost of a chain is $4$. It is not possible to make a coverage with a maximum cost less than or equal to $4$ with at most $6$ chains.

For the second test, the tree has $N = 6$ nodes and we want to cover it with at most $4$ chains. The tree can be covered with the following chains:
$1-2$ (cost $4$)  
$2-3$ (cost $3$)  
$3-4-5$ (cost $4$)  
$4-6$ (cost $4$)  

There are exactly $4$ chains (we are allowed a maximum of $4$), and the highest cost of a chain is $4$. It is not possible to make a coverage with a maximum cost less than or equal to $4$ with at most $4$ chains.