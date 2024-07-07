When Vlad saw this problem, he said bleah... Miki has a collection of parallelepipeds that he remembers by their side dimensions, given by three integer variables $x$, $y$, and $z$. 
~[bleah1.png|align=center]
She spent quite a lot of time thinking about parallelepipeds and invented a multiplication operation for them, which she defines as follows: for two parallelepipeds $p = (p_x, p_y, p_z)$ and $c = (c_x, c_y, c_z)$, the resulting parallelepiped has dimensions:
$$
p \times c = (p_y \cdot c_z - p_z \cdot c_y, p_z \cdot c_x - p_x \cdot c_z, p_x \cdot c_y - p_y \cdot c_x)
$$

She mentions that this is not ordinary multiplication and does not have its properties. Specifically, this operation is neither associative, so $a \times (b \times c)$ is not necessarily equal to $(a \times b) \times c$, nor is it commutative, so $a \times b$ is not necessarily equal to $b \times a$. Therefore, the order and parenthesization of an expression containing the multiplication of several parallelepipeds is very important, but, because we are very nice and do not want you to parse such an expression, we will express it with the help of a binary tree! Thus, you are given a tree with $N$ nodes. The nodes are indexed from $1$ to $N$ and it is known that node $1$ is always the root. Nodes can be of two types:
* Type $1$, leaf node (which has no children) in which we find a parallelepiped $(x, y, z)$.
* Type $2$, internal node (which has exactly two children): left child indexed with $s$ and right child indexed with $d$.

We define the value of a node $\text{val}(node)$ as:
* For a node of type $1$ its value is $(x, y, z)$, where $(x, y, z)$ are the dimensions of the parallelepiped found in that leaf.
* For a node of type $2$ its value is $\text{val}(s) \times \text{val}(d)$, where $s$ is the left child and $d$ is the right child of that node.

# Task

You are given $Q$ questions of the form:
* Given a leaf $f$ and a parallelepiped $(x, y, z)$, we want to know what the value of the root, $\text{val}(1)$, would be if we replaced the parallelepiped in leaf $f$ with the given parallelepiped.

For each question, you are asked to print the remainders of division by $1\ 000\ 000\ 007$ for the three numbers that compose the value of the root.

# Input data

The first line contains two natural numbers, $N$ and $Q$, separated by a space. The next $N$ lines describe the nodes of the tree. The $i$-th line among the $N$ describes the node with index $i$ as follows:
* $1 \ x \ y \ z$: node $i$ is a leaf and the dimensions of the parallelepiped in it are $(x, y, z)$.
* $2 \ s \ d$: node $i$ is an internal node, $s$ is its left child and $d$ is its right child.

The next $Q$ lines describe the questions. Each of these lines has the format:
* $i \ x \ y \ z$ where $i \leq N$ represents the index of the leaf whose dimensions change to $(x, y, z)$.

**Note!** The questions are only hypothetical; therefore, a change is not preserved for future questions.

# Output data

Print $Q$ lines, the answers to the questions in order. Each of these $Q$ lines must contain three natural values smaller than $1\ 000\ 000\ 007$, separated by a space.

# Constraints and clarifications

* $1 \leq N, Q \leq 200\ 000$
* $0 \leq x, y, z \leq 1\ 000\ 000\ 000$
* It is guaranteed that the input data describe a binary tree with the root at node $1$.
* It is guaranteed that all nodes given in the questions are leaves (type $1$ nodes) in the tree.

| # | Points | Constraints |
| - | ------- | ---------- |
| 1 | 22 | $1 \leq N, Q \leq 1\ 000$ |
| 2 | 25 | $1 \leq N, Q \leq 50\ 000$ and it is guaranteed that the tree has depth $\leq 15$. |
| 3 | 18 | $1 \leq N, Q \leq 200\ 000$ and it is guaranteed that only $x$ is different in the new parallelepiped. |
| 4 | 11 | $1 \leq N, Q \leq 50\ 000$ |
| 5 | 24 | No additional constraints |

# Example 1

`stdin`
```
5 3
2 2 3
1 1 0 1
2 4 5
1 0 2 1
1 1 1 1
4 1 2 3
5 0 1 1
4 0 2 2
```

`stdout`
```
1000000005 0 2
0 1 0
1000000005 2 2
```

## Explanation

For the first question, the tree modifies as follows:

~[bleah2.png|align=center]

# Example 2

`stdin`
```
15 10
2 2 3
2 4 5
2 6 7
2 8 9
2 10 11
2 12 13
2 14 15
1 1 5 2
1 2 2 2
1 1 1 0
1 12 0 1
1 1 3 1
1 4 1 1
1 5 1 0
1 5 1 2
10 1 7 1
11 2 3 1
9 2 1 1
14 1 0 3
8 1 2 3
15 5 1 0
15 2 1 9
13 1 2 1
8 0 1 2
10 1 3 1
```

`stdout`
```
999989503 999992207 51040
188 724 999998599
999999173 999999497 3960
2488 999999959 999989671
632 999998927 999998247
0 0 0
999991679 144 34464
999999351 999999767 704
632 999998927 999998247
999996335 999993823 20768
