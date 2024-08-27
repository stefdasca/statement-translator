# Mostenire2

Fibocel has just inherited a gigantic rectangular forest that he wants to transform into an amusement park for children. Realizing that there is a lot of work to be done and not knowing where to start, he decided to count how many little forests are in the inherited forest. A little forest is a rectangular area completely surrounded by trees, with at least one clearing somewhere inside. A clearing is an area without trees. Since Fibocel realized that this task is also difficult to accomplish, he decided to ask you for help!

## Task

Given Fibocel's inherited forest in the form of a rectangle with $N$ rows and $M$ columns having only values of $0$ and $1$, where $0$ means area without a tree and $1$ means area with a tree, determine how many little forests are inside the inherited forest.

## Input data

The input file `mostenire2.in` contains on the first line two natural numbers $N$ and $M$ separated by exactly one space representing the size of the forest. Each of the next $N$ lines contains exactly $M$ characters without spaces between them, having only values of $0$ and $1$.

## Output data

The output file `mostenire2.out` will contain exactly one number representing the answer requested by Fibocel.

## Constraints

$1 \leq N \leq 100$

$1 \leq M \leq 1000$

Little forests can intersect each other.

For $15\%$ of the tests, $N,M \leq 30$.

For another $35\%$ of the tests, $M \leq 100$.

## Example

`mostenire2.in`

```
5 4
1111
1010
1111
1010
1110
```

`mostenire2.out`

```
3
```