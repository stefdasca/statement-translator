## Task

There are $n$ trees of different heights, aligned in a straight line at equal distances, numbered from $1$ to $n$. For each tree, its height $H_i$ is known. Because the trees feel the need to socialize, each of them has friends among the other trees.

The friends of any tree $i$ can be located both to its left and right. Friendship relationships are defined as follows: for each tree $i$, consider a sequence $d_1, d_2, \\ldots, d_x$ representing the friends of tree $i$ located to its right and a sequence $s_1, s_2, \\ldots, s_y$ representing the friends of tree $i$ located to its left. The trees in the two sequences corresponding to a tree $i$ together form the list of its friends.

The sequences corresponding to tree $i$ are defined as follows:

* $d_i = i + 1$ (if $i=n$, then tree $i$ has no friends to its right, and the sequence $d$ remains empty)
* For each $k \\geq 2$, $d_k$ is the smallest index ($1 \\leq d_k \\leq n$) with the property that $d_k > d_{k-1}$ and $H_{d_k} > H_{d_{k-1}}$. If $d_k$ does not exist, then the list of friends to the right of tree $i$ ends, and the sequence construction stops at this step.
* $s_1 = i-1$ (if $i=1$, then tree $i$ has no friends to its left, and the sequence $s$ remains empty);
* For each $k \\geq 2$, $s_k$ is the largest index ($1 \\leq s_k \\leq n$) with the property that $s_k < s_{k-1}$ and $H_{s_k} > H_{s_{k-1}}$. If $s_k$ does not exist, then the list of friends to the left of tree $i$ ends, and the sequence construction stops at this step.

For example, in the figure below, $7$ trees are represented, each having its height indicated below it. The first tree on the left has the index $1$, and the last one has the index $7$.

~[Poza111.png]

Tree $1$ is friends with tree $2$ (since they are neighbors), and tree $5$ (because tree $5$ is the first tree to the right of $2$ with a height strictly greater than $2$). To the right of tree $5$, there is no tree with a height strictly greater than its own, so the only friends of tree $1$ are $2$ and $5$.

For tree $3$, the friends to its left are trees $2$ and $1$, and to its right are trees $4$ and $5$. For tree $6$, the only friend to its left is tree $5$, and to its right is tree $7$.

Tree $7$ can only have friends to its left, which are $6$ and $5$ (to the left of tree $5$, there is no tree with a height strictly greater than $8$).

Gardener Marian wants to choose $3$ different trees among the $n$ to plant them in another garden. He wants that among the $3$ trees, however he chooses $A$ and $B$, $2$ of them, then $A$ is friends with $B$ and $B$ is friends with $A$ (the friendship relationships are considered as initially established). Marian has several options and wonders how many distinct ways he can choose the $3$ trees with the required property.

## Task

Determine in how many ways $3$ different trees can be chosen among the $n$ with the property that however $2$ trees are chosen among the $3$, be they tree $A$ and tree $B$, then $A$ is friends with $B$ and $B$ is friends with $A$.

## Input data

The input file `copaci.in` contains the first line a natural number $n$, representing the number of trees, and the second line contains $n$ non-zero natural numbers, separated by a space, representing the heights of the trees.

## Output data

The output file `copaci.out` will contain on the first line a natural number representing the number of ways Marian can choose $3$ trees with the property from the statement.

## Constraints and clarifications

* $1 \\leq n \\leq 200\\ 000$
* $1 \\leq H_i \\leq 200$
* There will be no $2$ adjacent trees with the same height
* Two triplets of trees are considered distinct if there is at least one tree in the first triplet that is not in the second triplet
* For $30\\%$ of the tests, $1 \\leq n \\leq 200$

## Example

`copaci.in`
```
7
6 4 2 3 8 5 8
```

`copaci.out`
```
4
```

## Explanation

Tree $1$ is friends with trees: $2, 5$
Tree $2$ is friends with trees: $1, 3, 4, 5$
Tree $3$ is friends with trees: $1, 2, 4, 5$
Tree $4$ is friends with trees: $1, 2, 3, 5$
Tree $5$ is friends with trees: $1, 2, 4, 6, 7$
Tree $6$ is friends with trees: $5, 7$
Tree $7$ is friends with trees: $5, 6$
The ways in which Marian can choose the $3$ trees are: $(1, 2, 5)$, $(2, 4, 5)$, $(2, 3, 4)$, $(5, 6, 7)$