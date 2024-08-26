# Easygraph

As the name of the problem suggests, this is a simple graph problem. And on the occasion of the winter holidays, Santa Claus thought of shortening the problem statement and rewarding you with $100$ points if you solve it correctly! You are given a directed acyclic graph with $N$ nodes and $M$ edges. Each node $i$ has a value $v[i]$. Find and display the maximum sum of a chain in the graph. The sum of a chain is the sum of the values of the nodes contained in it.

## Input data

The input file `easygraph.in` contains on the first line the number of tests, $T$. Next, for each test, the first line will contain two natural numbers $N$ and $M$, with the meaning given in the statement. On the second line, $N$ integers will be found, the elements of the array $v[i]$. On the next $M$ lines, two numbers $x$ and $y$ will be found, meaning that there is an arc from node $x$ to node $y$.

## Output data

The output file `easygraph.out` will contain $T$ lines, with the answer for test $i$ on line $i$.

## Constraints and clarifications

$T = 20$  
$1 \leq N \leq 15000$  
$1 \leq M \leq 30000$  
$-10^6 \leq v[i] \leq 10^6$  
There can be multiple arcs between the same nodes $X$ and $Y$.  
The found maximum sum chain must contain at least $1$ node.

## Example

`easygraph.in`
```
1
4 3
-3 -1 15 5
1 3
3 2
2 4
```

`easygraph.out`
```
19
```

## Explanation

The chain with the maximum sum is: $3 \rightarrow 2 \rightarrow 4$. The sum of the chain is $19$.