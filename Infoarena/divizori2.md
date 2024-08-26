## Task

Let $A$ and $B$ be two undirected trees. We define the sum $A + B$ as the set of all undirected trees that can be obtained by connecting trees $A$ and $B$ with a single edge between any node in $A$ and any node in $B$. Similarly, we define the product of a scalar $K$ and a tree $A$ as $K * A = A + A + \dots A$ $K$ times. We say that a tree $A$ divides a tree $B$ if there exists a non-zero natural number $K$ such that $B$ is included in the set $K * A$. We notice that similar to divisibility in the case of natural numbers, any tree divides at least itself and the "unit," i.e., the tree formed by a single node. Given a tree $T$, it is required to count how many distinct trees are its divisors.

## Input data

The input file `divizori2.in` will contain on its first line the number $N$. The following $N - 1$ lines will contain the edges of the tree $T$, pairs in the form $x \ y$.

## Output data

The output file `divizori2.out` will contain a single number: the number of divisors of $T$.

## Constraints

$1 \leq N \leq 100\ 000$

For 50% of the score $N \leq 5\ 000$

Two trees are considered distinct if they are not isomorphic; in other words, if they do not have the same number of nodes or if there does not exist a renumbering of the nodes in the first to obtain the second.

## Example

`divizori2.in`

```
8
2 1
3 1
4 1
6 5
7 5
8 5
1 5
```

`divizori2.out`

``>
3
```

## Explanation

The 3 trees are: the tree with a single node, the tree from the input, and the "star" graph formed by 4 nodes.