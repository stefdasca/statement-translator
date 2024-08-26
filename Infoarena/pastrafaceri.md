# Pastrama and Business

The country where businessman Sorin Pastrama lives contains $N$ cities, connected by $M$ bidirectional roads. This country is somewhat dubious because it contains only odd-length cycles. In other words, the country is a graph with $N$ nodes and $M$ edges, connected, containing only odd-length cycles. Of course, Pastrama has a business in each city. As with any business, some are profitable, others are not. Thus, we denote the "profit" of the business in city $i$ by an integer $val_i$.

## Task

Keeping all businesses may not bring Pastrama any profit, so he asks for your help to tell him the maximum value he can obtain if he chooses to keep a subset of businesses that are connected to each other. In other words, he wants to know the maximum sum of the values of a connected subgraph.

## Input data

The input file pastrafaceri.in contains on the first line the natural numbers $N$ and $M$, as described in the problem statement. On the next line, there are $N$ integers, with $a_i$ being the value of node $i$. The next $M$ lines each contain two natural numbers $x$ and $y$, indicating that there is a bidirectional edge between nodes $x$ and $y$.

## Output data

The output file pastrafaceri.out will contain a natural number that represents the maximum value that can be obtained.

## Constraints and clarifications

$1 \leq N \leq 3 \cdot 10^5$

$1 \leq M \leq 4 \cdot 10^5$

$-10^6 \leq val_i \leq 10^6$

A cycle is any path that starts from a node, returns to the same node, and passes through each edge at most once. Its length is the number of edges traversed (this means that it is possible to pass through a node multiple times but not through an edge). The given graph will contain only odd-length cycles. It is possible to select no nodes, which would result in a value of $0$. Pay attention to the input file name - pastrafaceri.in instead of pastramasiafacerile.in. Pay attention to the output file name - pastrafaceri.out instead of pastramasiafacerile.out. Sorin Pastrama's pocket speaks any language it desires.

## Example

`pastrafaceri.in `

```
4 4 
-1 3 -2 4 
1 2 
2 3 
3 1 
1 4 
```

`pastrafaceri.out `

```
6 
```

## Explanation

We choose nodes $1$, $2$, and $4$ which have a sum of values equal to $6$. A higher value could have been obtained by selecting only nodes $2$ and $4$, but these are not connected to each other.