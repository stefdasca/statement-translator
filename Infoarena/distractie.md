## Task

Adrian, the wonder child of computer science, has finally discovered the lucky treasure behind his house and was rewarded with his first job: painter. His workplace has the shape of a matrix with $N$ rows and $M$ columns, and initially he is in the top-left cell $(1, 1)$ and wants to reach the bottom-right cell $(N, M)$. Each cell in the matrix has an associated color, represented by a natural number between $1$ and $2000$. During his journey, Adrian must satisfy the following conditions:

- From a cell $(i, j)$, he can only move to the adjacent cell to the right $(i, j+1)$ or the cell below $(i+1, j)$ (he cannot exceed the boundaries of the matrix).
- The next cell he moves to must have the same color as the current cell.

The second condition cannot always be met, but Adrian has profound verses that if he sings, the rooms will change color. Thus, when Adrian sings, one of the following two events occurs, at his choice:

- The color of the current cell (where he is) changes to a color chosen by Adrian.
- The color of an adjacent cell (left, right, above, and below) to the cell in which Adrian is located will change to one chosen by him.

Determine the minimum number of songs Adrian needs to sing to get from cell $(1, 1)$ to cell $(N, M)$, meeting all the imposed conditions.

## Input data

The input file `distractie.in` contains on the first line, separated by a space, two natural numbers $N$ and $M$, representing the number of rows and columns of the matrix, respectively. On the next $N$ lines there are $M$ natural numbers between $1$ and $2000$, representing the color of each cell in the matrix.

## Output data

In the output file `distractie.out` write on the first line a single number: the minimum number of songs Adrian needs to sing in order to reach the destination, meeting all the conditions imposed on him.

## Constraints and clarifications

$1 \leq N \leq 800$

$1 \leq M \leq 800$

$1 \leq$ all numbers in the matrix $\leq 2000$

## Example

`distractie.in`

```
3 4
1 1 1 2
4 5 6 2
6 7 4 3 2
```

`distractie.out`

```
2
```

## Explanation

A possible scenario is as follows: Adrian leaves from cell $(1, 1)$ and goes to cell $(1, 3)$, where he will sing a song and change the color of the current cell from $1$ to $2$, in order to be able to move to the right. He continues his journey (on the last column) and reaches the position $(2, 4)$, where he will sing the second song and change the color of the adjacent cell $(3, 4)$ from $3$ to $2$, in order to reach the next step at the end of the road.