# Mushrooms

A tree is super-balanced if it has the following properties:
● It is binary, so each node has a maximum of $2$ children.
● For each node, the absolute difference between the number of nodes in the left subtree and the number of nodes in the right subtree is at most $1$.
We are given $Q$ queries of the type "How many super-balanced trees with $N$ nodes exist?". Since the number of these trees can be quite large, the result will be calculated modulo $666013$.

## Input data

The input file `ciuperci.in` contains on the first line $Q$, the number of queries. The next $Q$ lines contain one number $N_i$ on line $i+1$, representing the number of nodes for query $i$.

## Output data

The output file `ciuperci.out` contains $Q$ numbers, one on each line. The number on line $i$ represents the answer to query $i$.

## Constraints

$1 \leq Q \leq 10^5$

$1 \leq N_i \leq 10^{16}$

$a$ modulo $b$ represents the remainder of the division of $a$ by $b$

Two trees are considered different if their in-order traversal is different

In-order traversal is the order: Left\_child, Root, Right\_child

Attention! It is recommended to use the `long long` type for those implementing in `C/C++` and `int64` for those implementing in Pascal

## Example

`ciuperci.in`
```
4
1
2
4
5
```

`ciuperci.out`
```
1
2
4
4
```

## Explanation

For $1$ we have only the root. For $2$ we have the root with one left child or one right child, so $2$ solutions.