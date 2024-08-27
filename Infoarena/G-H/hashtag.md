## Task

Formally, a hashtag of size $N \times M$ is a binary matrix that meets the following conditions: 
There exist indices (indexed from $0$) $L_1$ $L_2$ $L_3$ $L_4$ $C_1$ $C_2$ $C_3$ $C_4$ with the following properties: 
$1 \leq L_1 \leq L_2$ 
$L_2 + 2 \leq L_3 \leq L_4 \leq N - 2$ 
$1 \leq C_1 \leq C_2$ 
$C_2 + 2 \leq C_3 \leq C_4 \leq M - 2$

The cell $(i, j)$ will be equal to the character '#' if and only if $i$ is in the interval $[L_1, L_2]$ or in the interval $[L_3, L_4]$, and $j$ is in the interval $[C_1, C_2]$ or in the interval $[C_3, C_4]$.

In other words, a hashtag is composed of two vertical bars and two horizontal bars that do not necessarily have equal thickness. Additionally, from the above relations, we can observe that two parallel bars cannot touch, and the four corners of the matrix can never be part of the hashtag.

Given a matrix of dimensions $N \times M$ with characters from the set $\{\texttt{'.', '#'}\}$, what is the minimum number of cells in the matrix that need to be changed for the matrix to become a hashtag? 

## Input data

The input file `hashtag.in` will contain the numbers $N$ and $M$ on its first line. Each of the next $N$ lines will contain an array of $M$ characters, each of them being either '.' or '#'.

## Output data

The output file `hashtag.out` will contain an integer representing the minimum number of cells that need to be changed to obtain a hashtag.

## Constraints and clarifications

$5 \leq N, M \leq 30$ 

## Example

`hashtag.in` 
```
7 7 
..##.#. 
####### 
.##..#. 
####### 
..##.#. 
..#..#. 
.#.#.#. 
```

`hashtag.out` 
```
5 
```

## Explanation

For the resulting hashtag, the indices will be $C_1 = 2$, $C_2 = 3$, $C_3 = 5$, $C_4 = 5$, $L_1 = 1$, $L_2 = 1$, $L_3 = 3$, $L_4 = 3$.