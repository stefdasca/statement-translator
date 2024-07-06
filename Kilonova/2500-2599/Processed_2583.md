Mrs. Romanian language teacher recommended Tedi to read "Legends of Olympus." Last week she read the legend of Theseus and the Minotaur. In this legend, the hero Theseus decides to enter the labyrinth that hides the legendary half-man, half-bull beast, the Minotaur, with the intention of killing it and winning the hand of the Cretan princess, Ariadne.

The Minotaur's labyrinth is enchanted because it is constructed by the sculptor Daedalus following some recursive rules.

The labyrinth is located in a square matrix of side $2^N$. The rows and columns of the matrix are numbered from $1$ to $2^N$ (from top to bottom, respectively from left to right). It consists of a single path that passes exactly once through each cell of the matrix. The path starts from the bottom left corner of the matrix, i.e., the cell with coordinates $(2^N, 1)$, and ends in the bottom right corner of the matrix, i.e., the cell with coordinates $(2^N, 2^N)$.

The simplest matrix is represented in Figure 1. A matrix of side $2^N$ is formed using the matrix of side $2^{N-1}$. In the bottom left part, a matrix of side $2^{N-1}$ rotated by $90$ degrees in the clockwise direction is placed. In the top left part, the unmodified matrix of side $2^{N-1}$ is placed and connected with the one in the bottom left. In the top right part, the unmodified matrix of side $2^{N-1}$ is placed and connected with the one in the top left.
In the bottom right part, the matrix of side $2^{N-1}$ rotated by $90$ degrees in the counterclockwise direction is placed and connected with the one in the top right.
~[img1.jpg|align=center]

In Figure 2, the way the matrix is formed in the case $N = 2$ is represented, and in Figure 3, for $N = 3$.
~[img2.jpg|align=center]
~[img3.jpg|align=center]

The Minotaur is in a cell in the labyrinth and Theseus can encounter it after crossing $P$ cells on the contour of the labyrinth, starting from the bottom left corner of the matrix, i.e., from the cell with coordinates $(2^N, 1)$.

# Task
Given $N$ and $P$, help Theseus find the row and column of the cell where the Minotaur is located.

# Input data

The input file `minotaur.in` contains on the first line the natural numbers $N$ and $P$, separated by a space.

# Output data

The output file `minotaur.out` contains a single line on which will be written two numbers separated by a space, $lin$ and $col$, which represent the row and the column of the cell where the Minotaur is located.

# Constraints and clarifications

* $1 \leq N \leq 15$
* $1 \leq P \leq 2^{2N}$

| # | Points | Constraints |
|---|--------|-------------|
| 1 | 24     | $N \leq 7$  |
| 2 | 21     | $8 \leq N \leq 12$ |
| 3 | 55     | No additional constraints |

# Example 1

`minotaur.in`
```
1 4
```

`minotaur.out`
```
2 2
```

## Explanation

In the first example, Theseus crosses, in order, the cells $(2, 1), (1, 1), (1, 2), (2, 2)$.

# Example 2

`minotaur.in`
```
2 5
```

`minotaur.out`
```
2 1
```

## Explanation

In the second example, Theseus crosses, in order, the cells $(4, 1), (4, 2), (3, 2), (3, 1)$ and stops in the cell $(2, 1)$.

# Example 3

`minotaur.in`
```
3 10
```

`minotaur.out`
```
6 4
```

