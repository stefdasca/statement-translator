# The Smokin' Tree

Andrei listens to Bob Marley's songs and thus learns about the Rastafari movement. Impressed, he decides to create his own religion. From the Rastafari movement, he will adopt only one part which he liked the most. Also, at the same time, he becomes the administrator of infoarena.ro, which, unsurprisingly, he chooses green as its color. At the same time, he creates a list of important problems of the site, some ideas from that list are still relevant to this day. The young Rastaman wants to find an initiation ritual for his students, to determine if they are worthy of being part of the cult. Thus, a young person on the path to initiation is brought to the Temple of Tricks, to the Smokin' Tree. The tree can be viewed as a tree with $n$ nodes, with edge costs. The root of the tree is node $1$. After smoking the peace pipe, the distances on the tree change. Andrei gives the novice a pair of numbers $(A, B)$. The distance between 2 nodes $x$ and $y$ is calculated as follows: we take each edge on the unique path from $x$ to $y$. If the edge brings us closer to the root, its cost is multiplied by $A$. If the edge takes us farther from the root, its cost is multiplied by $B$. In the end, we sum the numbers obtained for each edge. Andrei gives $m$ constraints of the form $(x, y, valmin, valmax)$: the distance between nodes $x$ and $y$ is between $valmin$ and $valmax$. Then, there are $q$ queries of the form $(A, B)$: For a pair $(A, B)$ given by Andrei, are all the $m$ constraints satisfied? Answer correctly to the $q$ queries for a greener life.

## Input data

The input file `copacsmenar.in` contains on the first line the numbers $n$, $m$, and $q$. The second line contains the description of the tree through 3 numbers: $x$, $y$, and $c$, representing that there is an edge between $x$ and $y$ with the cost $c$. The next $m$ lines describe the constraints through 4 numbers: $x$, $y$, $valmin$, $valmax$, signifying that the distance between nodes $x$ and $y$ is between $valmin$ and $valmax$. The next $q$ lines describe the queries, through a pair of numbers $(A, B)$.

## Output data

The output file `copacsmenar.out` will contain $q$ numbers. The $i$-th number corresponds to the $i$-th query. If the pair corresponding to the query satisfies all the constraints, print $1$. Otherwise, print $0$.

## Constraints

$1 \leq n \leq 50$

$1 \leq m \leq n*(n-1)$

$1 \leq q \leq 100000$

The costs of the edges are integers which, in absolute value, do not exceed $1000$.

The values of $valmin$ and $valmax$ are integers which, in absolute value, do not exceed $10^7$.

The values of $A$ and $B$ in the queries are integers which, in absolute value, do not exceed $10^7$.

The ordered pairs $(x, y)$ from the $m$ constraints are distinct two by two, and $x \neq y$.

Despite the specific constraint of $n$, the problem has no relation to the TopCoder platform :(

## Example

`copacsmenar.in`

```
3 1 3
1 2 1
1 3 -1
2 3 0 10
1 1
20 10
21 10
```

`copacsmenar.out`

```
1
1
0
```

## Explanation

We have a single restriction to meet: the distance from node $2$ to node $3$ should be between $0$ and $10$. The path from $2$ to $3$ consists of the edges $2-1$ and $1-3$. The $2-1$ edge brings us closer to the root, and the $1-3$ edge takes us farther from it. Therefore, the cost of the path is the cost of the edge from $2$ to $1$ multiplied by $A$ + the cost of the edge from $1$ to $3$ multiplied by $B$. Thus, the cost of the path is $A - B$. It needs to be between $0$ and $10$. For the $3$ queries, the results are $1$, $1$, and $0$, so only the first $2$ queries satisfy the restriction.