# PScNv

The preOni committee was running out of interesting problems to propose for the final stage to the most talented computer scientists in the country. Problems had already been selected for all age groups, but there was still a need for a simple problem for the XI-XII classes. A priority in choosing problems for the contest, and especially for the final, was the existence of a large number of solutions so that competitors could be easily differentiated. Thus, the simple problem with multiple levels emerged: A directed graph with $n$ nodes and $m$ arcs is given, each arc has a weight $k_i$. Two nodes $x$ and $y$ are given. The task is to determine the minimum value of $k$ such that there is a path from node $x$ to node $y$ with the property that each arc on the path has a weight $k_i$ less than or equal to $k$. There will always be a path between nodes $x$ and $y$.

## Task

Find the minimum number $k$!

## Input Data 

The file `pscnv.in` will contain on the first line four integers representing the values of $n$, $m$, $x$, and $y$. On the next $m$ lines will contain three integers $x_i$, $y_i$, and $k_i$ separated by a single space representing an arc, $x_i$ being the node from which the arc starts, $y_i$ the node it reaches, and $k_i$ representing the weight of the arc.

## Output Data

The file `pscnv.out` will contain a single integer representing the minimum value of $k$.

## Constraints and clarifications

$1 \leq n \leq 250\,000$

$1 \leq m \leq 500\,000$

$1 \leq k_i \leq 1\,000$

There can be multiple arcs between two nodes. Also, there can be arcs from a node to itself.

ATTENTION! In case of working in C/C++, it is recommended to read with functions such as `fgets` due to the large size of the input files!

Levels

For 30% of the score 

$n \leq 1\,000$

$m \leq 10\,000$

For 50% of the score 

$n \leq 25\,000$

$m \leq 50\,000$

For 80% of the score 

$n \leq 100\,000$

$m \leq 200\,000$

## Example

`pscnv.in`

```
4 5 1 4
1 2 3
1 3 1
2 4 2
3 2 2
3 4 3
```

`pscnv.out`

```
2
```

## Explanation

The path $1 \to 3 \to 2 \to 4$ has the arc weights 1, 2, and 2 respectively.