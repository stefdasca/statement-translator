## Task

An undirected tree with $N$ nodes, labeled from $1$ to $N$, and its root at node $1$ is given, with each edge having a value. Additionally, there are $M$ operations of the following types:
1. **node $s$** $\to$ the value of the edge between the node and its parent becomes $s$
2. **nr $k x 1 x 2 \dots x nr$** $\to$ print the number of unordered pairs $(x, y)$, with $x$ and $y$ belonging to the set of $nr$ elements read, such that the sum of the values on the path from $x$ to $y$ is divisible by $k$

## Input Data

The input file `hardtask.in` contains on the first line the natural numbers $N$ and $M$ separated by a space. 
On lines from $2$ to $N$, there are two natural numbers **parent** and **value** representing the parent of **node $i$**, and the value of the edge between **node $i$** and its parent. 
On the next $M$ lines, there is an operation: the first value is **type**, and if **type** is $1$ then followed by 2 natural numbers **node** and $s$ as described above, and if **type** is $2$ then followed by 2 natural numbers **nr** and **k** as described above and a sequence of **nr** distinct numbers representing the set of nodes.

## Output Data

In the output file `hardtask.out`, print the answer for operations of type $2$, each on a separate line.

## Constraints and clarifications

$1 \leq N, M \leq 10^5$  
Sum of the numbers of elements $\leq 10^5$  
$1 \leq k \leq 10^9$  
$0 \leq s, value \leq 10^9$  
The number of pairs and the sum of the edge values exceed the int data type  
For every curse directed to the committee for this problem, George will start to hiccup!

## Example

`hardtask.in`
```
11 4
1 2
1 1
2 3
2 4
3 1
3 2
1 5 8
3 5 3 5 2 2 5 3 2 4 5 10 11
1 5 3
2 5 3 2 4 5 10 11
2 4 2 1 3 6 7
```

`hardtask.out`
```
4
6
2
```

## Explanation

$\dots$