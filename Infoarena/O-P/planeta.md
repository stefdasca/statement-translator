## Task

Tired of so many stars, Miruna moved to Planet Moldova. Here she heard for the first time the concepts of binary tree and binary search tree. A binary tree is recursively defined as follows:

- it is a tree with no nodes.
- it is a tree consisting of a special node called the root and two other binary trees, called the left subtree and the right subtree of the root.

Each node of a binary tree with $N$ nodes will contain a number between $1$ and $N$. We will consider that a binary tree is a binary search tree if the following conditions are met for each node of the tree:

- all the values in the left subtree are strictly smaller than the value in the node 
- all the values in the right subtree are strictly larger than the value in the node 

Below we have an example of a binary search tree with six nodes:

The preorder traversal of a binary search tree is a sequence of numbers obtained as follows:

- the preorder traversal of a tree with no nodes is an empty sequence
- the preorder traversal of a non-empty tree is obtained as follows: let $L$ be the sequence representing the preorder traversal of the left subtree of the root, $V$ the value in the root and $R$ the sequence representing the preorder traversal of the right subtree of the root.

The preorder traversal of the tree is obtained by concatenating $V$, $L$, and $R$. For the example above, the preorder traversal is the sequence: $3 \ 1 \ 2 \ 4 \ 6 \ 5$.

Miruna analyzes all binary search trees with $N$ nodes that contain the numbers $1, 2, \dots, N$ and traverses them in preorder. Then she sorts the sequences representing the traversals lexicographically. You will need to answer Miruna to a very simple question: what is the $K$-th sequence in lexicographic order?

## Input data

The first line of the input file `planeta.in` contains two integers $N$ and $K$, with the meanings from the statement.

## Output data

In the output file `planeta.out`, you will print a permutation of the numbers from $1$ to $N$, representing the $K$-th preorder traversal in lexicographic order.

## Constraints

$1 \leq N \leq 30$

$K$ will be an integer that fits in a signed 64-bit number.

It is guaranteed that there are at least $K$ preorder traversals.

For 30% of the tests $1 \leq N \leq 10$

## Example

`planeta.in`
```
2 2
15 14023
```

`planeta.out`
```
2 1 15 8 7 6 14 9 12 10 11 13
```