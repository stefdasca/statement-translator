Two friends, Gigel and Costel, bored after finishing reading the story _"The Clumsy Dove"_, thought of the following problem: Given a tree with $N$ nodes, each node in the tree having a value **on** the node. Gigel proposes to Costel to find for a given node, what is the maximum sum of a path that passes through that node. Costel immediately realizes that the problem is very easy, so, being confident, he believes he will be able to solve it for **all** the nodes in the tree! Thinking a bit, he realized that he needs your help so he won't embarrass himself in front of his friend!

# Task
Help Costel find for each node of the tree the maximum cost of a path that passes through that node! A tree with $N$ nodes is a connected acyclic graph with $N - 1$ edges. A path is a list of nodes such that each node in the tree appears **at most once**, and between every two adjacent nodes in the list, there **exists an edge** between them. The set of nodes of a path **cannot** be empty. The cost of a path is the sum of the values of the nodes in the current path.

# Input data
The first line of the input file will contain the number $N$, which represents the number of nodes in the tree.
The next $N - 1$ lines will contain two numbers: $x_i$ and $y_i$, which signify that there exists an edge between nodes $x_i$ and $y_i$.
On the $N + 1$ line will contain $N$ values, where $v_i$ represents the value of the node $i$.

# Output data
The first line of the output file will contain $N$ values, where the $i$-th value represents the answer for node $i$. The answers will be printed with a space between them.

# Constraints
- $1 \leq N \leq 10^5$
- $-10^9 \leq v_i \leq 10^9$
- It is recommended to use the `long long` data type.

# Scoring
| # | Points | Constraints         |
| - | ------ | ------------------- |
| 1 | 10     | The tree is a path, $N \leq 500$. |
| 2 | 30     | $N \leq 1\ 000$     |
| 3 | 60     | No additional constraints. |

# Example
`cosgigmax.in`
```
10
1 2
1 5
1 7
2 4
2 3
7 6
7 8
6 10
6 9
2 -5 -2 3 3 1 4 -10 -8 -7
```

`cosgigmax.out`
```
10 5 0 5 10 10 10 -1 2 3 
```