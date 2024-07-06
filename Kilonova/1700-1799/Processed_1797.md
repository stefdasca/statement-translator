*The X High School, the best computer science high school in Romania, is beginning to conduct experiments to optimize the educational experience. Of course, being a specialized computer science high school, the $N$ classrooms of the school are arranged in the form of a **tree**, connected through $N - 1$ bidirectional corridors so that it is possible to reach any classroom from any other. The renowned teachers of the high school have realized that efficiency in education depends both on the number of classrooms and the maximum number of corridors connected to a single classroom. More specifically, the teachers are interested in the following information: for each $K$ from $1$ to $N$, what is the size of the largest subset of connected classrooms we could select, such that no classroom in the subset is directly connected to more than $K$ other classrooms in the subset.*

More formally, a tree $A$ with $N$ nodes is given. We define a subtree of $A$ as being a connected subset of nodes $S$. For any subtree $S$ of $A$, we define the degree of a node $x$ in $S$ relative to $S$ as the number of nodes in $S$ to which $x$ is directly connected by edges. We define the degree of the subtree $S$ as the maximum degree of the nodes in $S$ (relative to $S$). We are asked to calculate, for $K = 1, 2, ..., N$, the maximum size of a subtree of $A$ with a degree **at most $K$**.

# Interaction Protocol
The contestant will implement the function `solve`, with the following signature:
```cpp
std::vector<int> solve (int N, std::vector<int> a, std::vector<int> b);
```

The parameters of this function have the following meaning:
* $N$ the number of nodes of the tree $A$;
* The arrays $a$ and $b$ contain the vertices of the edges of the tree $A$. More precisely, there is a bidirectional edge between the nodes $a[i]$ and $b[i]$, for any $0 \le i < N$.

The function will return an STL vector containing the $N$ required numbers in result, in order. The element corresponding to position $i$ in the result will be the answer for $K = i + 1$. **The contestant will NOT implement a main function**.

## Subtask 1 (13 points)
* $1 \le N \le 2\ 000$
## Subtask 2 (15 points)
* At most $2\ 000$ nodes are neighbors to more than $2$ nodes.
* $1 \le N \le 100\ 000$
## Subtask 3 (38 points)
* $1 \le N \le 70\ 000$
## Subtask 4 (34 points)
* $1 \le N \le 200\ 000$

# Examples
`Input`
```
5
3 1
3 5
3 4
1 2
```
`Output`
```
2
4
5
5
5
```
`Input`
```
7
4 2
4 5
7 4
4 1
4 3
7 6
```
`Output`
```
2
4
5
6
7
7
7
```

`Input`
```
10
9 4
9 2
9 8
9 1
3 9
10 7
9 5
6 3
6 10
```
`Output`
```
2
6
7
8
9
10
10
10
10
10
```

`Input`
```
12
1 8
1 11
11 9
12 6
1 5
1 12
5 2
11 4
1 3
5 7
5 10
```
`Output`
```
2
5
9
11
12
12
12
12
12
12
12
12
```

`Input`
```
20
8 13
16 12
20 4
20 8
16 2
5 9
16 5
16 17
8 3
16 7
5 10
5 14
16 11
16 6
8 19
20 16
5 18
5 1
20 15
```
`Output`
```
2
6
10
14
16
18
19
20
20
20
20
20
20
20
20
20
20
20
20
20
```

Explanations
---
For the first example:
~[arborex.jpg]

For the second example:
~[arborex1.jpg]

For the third example:
~[arborex2.jpg]

For the fourth example:
~[arborex3.jpg]

For the last example:
~[arborex4.jpg]