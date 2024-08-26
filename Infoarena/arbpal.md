# Arbpal

Given a tree with $N$ nodes. In each node, there is a character from $'a'$ to $'z'$. Let $P(x,y)$ be the function that returns the string of characters formed on the path from node $x$ to node $y$. Determine how many pairs $(x,y)$ exist with the property that $P(x,y)$ returns a palindrome string.

## Task

## Input data

The input file `arbpal.in` will contain on the first line a natural number $N$. The following $N - 1$ lines will contain pairs $(x,y)$ representing the fact that there is an edge from node $x$ to node $y$. On the next line, there will be $N$ characters from $'a'$ to $'z'$ separated by a space. The $i$-th character represents that in node $i$ there is that character.

## Output data

The output file `arbpal.out` will contain a single natural number representing the answer.

## Constraints and clarifications

$1 \leq N \leq 5\ 000$

## Example

```
arbpal.in 
4
1 2
1 3
1 4
b a a a
```

```
arbpal.out 
10
```