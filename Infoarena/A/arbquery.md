## Task

Manuela has a tree with $N$ nodes, where each edge has a length. A chain is a sequence of distinct nodes such that there is an edge between any two adjacent nodes. We define the length of a chain as the sum of the lengths of the edges that connect the adjacent nodes along the path. For each edge $(x, y)$ let $d(x, y)$ be the sum of the lengths of all chains that contain the edge from $x$ to $y$. Manuela has $Q$ queries, each in the form of a chain. She wants to calculate the sum $\% 10^9 + 7$.

## Input data

The first line of the input file `arbquery.in` contains the numbers $N$ and $Q$. The next $N - 1$ lines each contain three values $x$, $y$, $l$, indicating the existence of an edge from $x$ to $y$ with length $l$. The next $Q$ lines each contain two values $x$, $y$, representing a query on the unique chain from $x$ to $y$.

## Output data

The output file `arbquery.out` contains the answers to the $Q$ queries, in order.

## Constraints and clarifications

Subtasks:

$$ 
Subtask~1~(10~points)  
$$

$$ 
N, Q \leq 20 
$$

$$ 
Any~edge~has~a~length~of~at~most~10^5 
$$

$$ 
Subtask~2~(30~points)  
$$

$$ 
N, Q \leq 2,000 
$$

$$ 
Any~edge~has~a~length~of~at~most~10^5 
$$

$$ 
Subtask~3~(10~points)  
$$

$$ 
N, Q \leq 100,000 
$$

$$ 
Any~node~has~at~most~2~incident~edges 
$$

$$ 
Any~edge~has~a~length~of~at~most~10^5 
$$

$$ 
Subtask~4~(10~points)  
$$

$$ 
N, Q \leq 100,000 
$$

$$ 
At~most~one~node~has~more~than~1~incident~edge 
$$

$$ 
Any~edge~has~a~length~of~at~most~10^5 
$$

$$ 
Subtask~5~(40~points)  
$$

$$ 
N, Q \leq 100,000 
$$

$$ 
Any~edge~has~a~length~of~at~most~10^5 
$$

## Example

`arbquery.in`

```
3 3
1 2 1
2 3 100
1 2
2 3
1 3
```

`arbquery.out`

```
102
201
303
```

We observe that there are three chains: $1 - 2$ with a cost of $1$, $2 - 3$ with a cost of $100$, and $1 - 2 - 3$ with a cost of $101$. Thus $d(1, 2) = 102$, $d(2, 3) = 201$. Therefore, the result for $1, 2$ is $d(1, 2) = 102$, for $2, 3$ is $d(2, 3) = 201$, and for $1, 3$ is $d(1, 2) + d(2, 3) = 303$.