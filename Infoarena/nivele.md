## Levels

A binary tree is called strict if all its internal nodes have exactly two children. We define the level of a node in the tree, recursively, as follows:
The level of the root node is $1$
The level of any node other than the root node is the level of its parent $+1$
We will call level sequence any sequence of numbers that can represent the levels of the leaves of a strict binary tree when traversed in preorder. Given $T$ sequences of numbers, determine for each if they are level sequences.

## Input data

The input file `nivele.in` contains the first line with the number $T$. The following $T$ lines contain one sequence of numbers each: $N \ A_1 \ A_1 \ \dots \ A_N$.

## Output data

In the output file `nivele.out`, $T$ lines will be written, one for each sequence from the input file. If a sequence of numbers is a level sequence, the line will contain $DA$; otherwise, it will contain $NU$.

## Constraints and clarifications

$1 \leq T \leq 10$

$1 \leq N \leq 50\ 000$

$1 \leq A_i \leq 10^9$

## Example

`nivele.in` `nivele.out`

`2` `3 2 3 3` `3 2 3 4`

$DA$

$NU$

## Explanation

For the first example, we can construct the following strict binary tree: