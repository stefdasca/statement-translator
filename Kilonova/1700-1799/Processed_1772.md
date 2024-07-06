```markdown
Given is a tree $T$ with $n$ nodes, numbered from $1$ to $n$, having its root at node $1$. Each edge $(x, y)$, from node $x$ to node $y$, of the tree has a given length, $d_{(x, y)}$. The root sends a message to all other nodes in the tree. The time after which a leaf receives the message is equal to the sum of the lengths of the edges on the path from the root to this leaf.

It is desired that the message transmission duration from the root to each leaf is identical. For this, we have the _increment operation_ at our disposal, which can be applied to any edge $(x, y)$ and consists of increasing the length of the edge by one unit. The cost of applying the increment operation to an edge $(x, y)$ is $c_{(x, y)}$. The operation can be applied repeatedly to the same edge.

# Task

Determine the total minimum cost of the operations required for the message to reach the leaves at the same time.

# Input data

The first line of the input file `arb.in` contains the natural number $n$. The next $n - 1$ lines contain four natural numbers $x$, $y$, $d_{(x, y)}$, $c_{(x, y)}$, separated by a single space, having the meaning from the statement.

# Output data

The output file `arb.out` will contain on the first line the required minimum cost.

# Constraints and clarifications

* $1 \leq n \leq 100\ 000$
* $1 \leq d \leq 10\ 000$
* $1 \leq c \leq 10\ 000$
* For $10\%$ of the tests, $n$ will be equal to $3$.
* For $50\%$ of the tests, the cost of the increment operation for any edge will be equal to $1$.

# Example 1

`arb.in`
```
7
1 2 2 1
2 4 2 1
2 5 1 1
1 3 1 1
3 6 2 1
3 7 1 1
```

`arb.out`
```
3
```

## Explanation

The edges $(2, 5)$, $(1, 3)$, and $(3, 7)$ will be incremented by one unit. Since all have a cost of $1$, the answer will be $3$.

# Example 2

`arb.in`
```
9
1 2 3 1
2 4 4 1
2 5 2 1
1 3 2 10
3 6 4 1
3 7 1 10
7 8 1 2
7 9 1 1
```

`arb.out`
```
12
```

## Explanation

The edges will be incremented as follows:

* $(2, 5)$ until the length is $4$ with a cost of $2$;
* $(3, 6)$ until the length is $5$ with a cost of $1$;
* $(7, 8)$ until the length is $4$ with a cost of $6$;
* $(7, 9)$ until the length is $4$ with a cost of $3$;

The required minimum cost is $2+1+6+3=12$.
```