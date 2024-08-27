## Task

Mescheriakov has a binary matrix of size $N \times M$. He wants to choose a set of elements that form a spiral as follows: Initially, Mescheriakov sets a direction for the spiral traversal (clockwise or counterclockwise). Then he chooses an element in the matrix which he considers the starting point of the spiral. Going forward, Mescheriakov can extend the spiral by adding a new element that meets the following conditions: 
1. It is not already part of the spiral.
2. It is adjacent to the last added element (in one of the 4 directions: up, down, left, or right).
3. The half-line formed by the last element and it does not intersect any other element that is already part of the spiral.
4. If the direction of movement changes, it must respect the initially chosen direction.

Help Mescheriakov find the longest spiral that contains only elements of $0$!

## Input data

The input file `spirala3.in` will contain on the first line two natural numbers $N$ and $M$ as described. The following $N$ lines will contain $M$ numbers from the set $\{0, 1\}$ representing the binary matrix.

## Output data

The output file `spirala3.out` must contain the maximum length of a spiral of $0$.

## Constraints and clarifications

$1 \leq N, M \leq 50$

## Example

```
spirala3.in
3 5
0 0 0 0 0
1 0 1 1 0
1 0 0 0 0
```

```
spirala3.out
11
```

```
spirala3.in
3 5
0 1 1 1 1
0 1 1 0 0
0 0 0 0 0
```

```
spirala3.out
9
```

```
spirala3.in
3 5
0 0 0 1 1
1 1 0 1 1
1 1 1 0 0
```

```
spirala3.out
5
```

## Explanation

In the first example, the spiral is given by the positions $(2,2) \rightarrow (3,2) \rightarrow (3,3) \rightarrow (3,4) \rightarrow (3,5) \rightarrow (2,5) \rightarrow (1,5) \rightarrow (1,4) \rightarrow (1,3) \rightarrow (1,2) \rightarrow (1,1)$.

For the second example, the longest path appears at the positions $(2,4) \rightarrow (2,5) \rightarrow (3,5) \rightarrow (3,4) \rightarrow (3,3) \rightarrow (3,2) \rightarrow (3,1) \rightarrow (2,1) \rightarrow (1,1)$.

In the third example, there are two spirals of maximum length, the first from position $(1,1)$ to position $(3,3)$, and the second from position $(1,3)$ to position $(3,5)$.