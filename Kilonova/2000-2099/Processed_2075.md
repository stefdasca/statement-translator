> *Colegiul Național “Frații Buzești�* ~[logos.png|align=right|width=20rem]
> *Centrul de Pregătire pentru Performanță în Informatică*
> **InfoCNFB** - Second Edition, Senior
> December 9, 2023

# Task

A number $T$ equal to $1$ or $2$ is given.
Next, a graph with $N$ nodes, having the structure of a forest of rooted trees, is given. This is represented by an array of parents $\\text{parent}$ as follows:
* $\\text{parent}[\\text{node}] = \\text{node}$, if the current node is the root of a tree in the forest;
* $\\text{parent}[\\text{node}] = \\text{parent}$, if the node is not a root.

On this forest of trees, $M$ operations of the following form will be executed:
(**ATTENTION**, the values $x$ and/or $y$, where applicable, will not be read explicitly, but must be calculated according to a formula based on the values of $T$, $\\text{coef\\_x}$ and/or $\\text{coef\\_y}$, as well as the response to the last query, as explained below).
* `1 coef_x coef_y` - $\\text{parent}[x]$ becomes $y$ (it is guaranteed that after this operation the graph will continue to have the form of a forest of trees);
* `2 coef_x` - display the number of nodes on the path from node $x$ to the root of the tree that $x$ is part of;
* `3 coef_x` - display the size (number of nodes) of the tree that node $x$ is part of;
* `4` - display the size of the largest tree in the forest;
* `5 coef_x coef_y` - display $\\text{lca}(x, y)$ if $x$ and $y$ are part of the same tree, otherwise display $0$.

The formula for generating `x` and/or `y` based on `T`, `coef_x`, `coef_y`:
* $T = 1$: `x = coef_x`; `y = coef_y`.
* $T = 2$:
    * Let $p$ be the response to the last question of type $2$, $3$, $4$, or $5$ (initially $p = 0$);
    * `x = coef_x ^ p`; `y = coef_y ^ p` (where `^` denotes the **XOR** operation between two values);
    * If the current query is of type $2$, $3$, $4$, or $5$, then **`p` will become the response to this query**.

# Input data

The first line of the file `harb.in` contains the number $T$. The following line contains a number $N$.
The following line contains $N$ numbers representing the elements of the array $\\text{parent}$.
The following line contains $M$ representing the number of operations to be answered.
The next $M$ lines will describe the $M$ operations, one on each line.

# Output data

The file `harb.out` will contain on each line the response to each query of type $2$, $3$, $4$, or $5$.

# Constraints and clarifications

|# | Points | Constraints|
| - | - | ------------|
|1|5|$T = 1$; $N, M \leq 1 \ 000$, it is guaranteed that there are only operations of type $1$ or $2$, and at any moment there is only one node `x` with `parent[x] = x`.|
|2|5|$T = 1$; $N, M \leq 1 \ 000$, it is guaranteed that there are only operations of type $1$ or $2$|
|3|5|$T = 1$; $N, M \leq 1 \ 000$, it is guaranteed that there are only operations of type $1$, $2$, $3$, or $4$|
|4|10|$T = 1$; $N, M \leq 1 \ 000$|
|5|10|$T = 1$; $N, M \leq 100 \ 000$, it is guaranteed that there are only operations of type $2$, $3$, or $4$|
|6|10|$T = 1$; $N, M \leq 100 \ 000$, it is guaranteed that there are only operations of type $2$, $3$, $4$, or $5$|
|7|35|$T = 1$; $N, M \leq 100 \ 000$, it is guaranteed that there are only operations of type $1$, $2$, $3$, or $4$|
|8|10|$T = 1$; $N, M \leq 100 \ 000$|
|9|10|$T = 2$; $N, M \leq 100 \ 000$|

# Example 1

`harb.in`
```
1
14
1 1 1 2 3 3 7 8 8 8 8 11 11 13
20
5 4 6
5 6 5
5 12 14
2 11
2 4
3 11
3 4
4
2 14
1 13 2
1 3 7
1 7 9
2 6
5 5 6
3 6
3 14
5 14 4
4
2 12
2 13
```

`harb.out`
```
1
3
11
2
3
7
6
7
4
5
3
9
5
2
9
3
3
```

## Explanation

The initial forest of trees looks like in the figure below:
~[harb_1.png|align=center]

$\\text{lca}(4, 6) = 1$, $\\text{lca}(12, 14) = 11$, the length of the path from $4$ to $1$ is $3$, the tree that contains $11$ has $7$ nodes, the one that contains $4$ has $6$ nodes, and for query of type $4$, the largest tree has $7$ nodes, etc.

After the 3 operations of changing parents, the forest of trees will look like this:
~[harb_2.png|align=center]

$\\text{lca}(14, 4) = 2$, $\\text{lca}(5, 6) = 3$, the tree that contains $6$ has $9$ nodes, and the one that contains $14$ has $5$ nodes, the path from node $6$ to node $8$ has a length of $5$, etc.

# Example 2

`harb.in`
```
2
14
1 1 1 2 3 3 7 8 8 8 8 11 11 13 
20
5 4 6
5 7 4
5 15 13
2 0
2 6
3 8
3 3
4
2 9
1 9 6
1 7 3
1 3 13
2 2
5 0 3
3 5
3 7
5 11 1
4
2 5
2 14
```

`harb.out`
```
1
3
11
2
3
7
6
7
4
5
3
9
5
2
9
3
3
```

## Explanation

This example is identical to the first one, the only difference being that the input is given according to the formulas for $T=2$.