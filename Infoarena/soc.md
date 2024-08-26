## Soc

A group of $N$ business people met for a conference. Some of them are friends, others are not. Each of them has a bank account containing a certain amount of money in euros. Whenever they meet, they think about starting a new business. This time, they decided to form a company where the shareholders will be a subset of them such that any two business people who are shareholders of the company are friends, and the capital of the company (equal to the total amounts in the shareholders' accounts) is maximized. To determine the shareholders of this company, they hired you and, if you provide them with the answer in a timely manner, you will be rewarded with a handsome sum. Before you get to work, the $N$ business people provided you with information regarding their bank accounts and the friendships between them.

Analyzing the problem, you concluded that the friendships can be represented as an undirected graph with $N$ vertices (corresponding to the $N$ business people); between any two different vertices there is an edge if the two business people corresponding to the two vertices in the graph are friends (friendship is reciprocal). The graph has a special structure, more precisely it is a cograph. A graph is called a cograph if it fulfills at least one of the following 3 conditions:
- It is a graph with a single node
- It is the union graph of two or more cographs
- It is the complement graph of a cograph

By taking the union of two graphs, one with $i$ nodes and edges between these $i$ nodes, another with $j$ nodes and edges between these $j$ nodes, you get a graph with $i+j$ nodes, containing all the edges from the two graphs, without introducing any extra edge. For example, for two graphs, one having nodes labeled 1 and 2 and containing the edge $[1,2]$, and another having nodes labeled 9, 10, 11, and containing the edges $[9,10]$ and $[9,11]$, the union graph will contain 5 nodes labeled 1, 2, 9, 10, 11, and exactly three edges: $[1,2]$, $[9,10]$, and $[9,11]$. The complement graph of a graph is obtained as follows:
- For any pair of distinct nodes $[a,b]$ between which there is an edge in the initial graph, there will NOT be an edge in the complement graph;
- For any pair of distinct nodes $[a,b]$ between which there is NOT an edge in the initial graph, there will be an edge in the complement graph.

For example, for the graph having 3 nodes, labeled 4, 11, 20, and 2 edges $[4,11]$ and $[11,20]$, the complement graph will contain all 3 nodes and a single edge: $[4,20]$.

## Task

In the input file `soc.in`, the first line contains the integers $N$ and $M$, separated by a space. The next line contains the integers $E_i$, $i=1,2,\dots,N$, separated by spaces, representing the amounts in the accounts of the $N$ business people. The number $E_K$ represents the amount in the account of the business person numbered $K$. The next $M$ lines contain two integers $a$ and $b$ in the range $[1,N]$, indicating that the business people numbered $a$ and $b$ are friends.

## Output data

In the output file `soc.out`, print on the first line the maximum capital of the company. On the next line, print the number $A$, representing the number of shareholders of the company. On the third line, print the numbers of the business people who will be shareholders, separated by spaces. If there are multiple ways to choose the shareholders such that the capital is maximized, you can print any of them.

## Constraints and clarifications

$1 \leq N \leq 256$  
$0 \leq M \leq N*(N-1)/2$  
$0 \leq E_i \leq 1\ 000\ 000$, for $i=1,2,\dots,N$  
If there are multiple correct solutions, any of them will be accepted  

## Example

`soc.in`
```
5 4
5 4 3 3 3
2 1
3 4
4 5
5 3
```
`soc.out`
```
9
3
3 4 5
```