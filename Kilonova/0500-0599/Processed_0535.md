Ernest found a Pacman game in his family's garage. The maze in the game can be represented as a matrix with $N$ rows and $N$ columns. In each row and each column, there is exactly one obstacle. We will denote with $(L, C)$ the position on row $L$ and column $C$. 

The matrix is circular: if Pacman moves to the right from position $(L, N)$, it reaches $(L, 1)$, and if it moves to the left from position $(L, 1)$, it reaches $(L, N)$, for any row $L$ in the matrix. Similarly, if it moves up from $(1, C)$, it reaches $(N, C)$, and if it moves down from $(N, C)$, it reaches $(1, C)$, for any column $C$. Initially, Pacman is at $(1, 1)$ and wants to reach $(N, N)$ where there is a yellow dot that will help him defeat the colored ghosts.

The rules of this game version allow only $4$ types of movements for Pacman, relative to the current position:
- `U` - moves **up** until it hits an obstacle or reaches $(N, N)$.
- `D` - moves **down** until it hits an obstacle or reaches $(N, N)$.
- `L` - moves to the **left** until it hits an obstacle or reaches $(N, N)$.
- `R` - moves to the **right** until it hits an obstacle or reaches $(N, N)$.

It is important to note that once Pacman reaches $(N, N)$, he will no longer be able to leave this position, regardless of any further movements he might make.

# Task

The problem consists of two tasks:
**Task 1.** A sequence of moves consisting of the letters **U**, **D**, **L**, **R** is read, describing the moves of Pacman in order. By moving according to this sequence, will Pacman reach the yellow dot at coordinates $(N, N)$ from $(1, 1)$?
**Task 2.** What is the minimum number of moves **U**, **D**, **L**, **R** for Pacman to reach the yellow dot at coordinates $(N, N)$ from $(1, 1)$?

# Input data

Each input file will contain $T$ tests.
The first line of the file contains the task number $C \in \{1, 2\}$ and the number of tests $T$. The first line of each test $i$ contains $N_i$, the size of the matrix for test $i$, and the second line contains $N_i$ numbers $P_1$, $P_2$, ..., $P_{N_i}$. For each $1 \leq j \leq N_i$, obstacle $j$ has the coordinates $(j, P_j)$. If $C = 1$, the third line of each test contains the moves written as a sequence of characters without spaces, from the set **$\{U, D, L, R\}$**.

# Output data

On each of the $T$ lines of the output file, there will be the answer for the corresponding test. If $C = 1$, "`Won`" will be displayed if the answer to the task is affirmative, otherwise "`Lost`" will be displayed. If $C = 2$, the minimum number of required moves will be displayed, or $\-1$ if it is not possible to reach $(1, 1)$ to $(N, N)$.

# Constraints and clarifications
* $1 \leq T \leq 5 * 10^4$;
* $2 \leq N_i$, for any test $1 \leq i \leq T$;
* The sum of all $N_i$ values, for $1 \leq i \leq T$, is $\leq 10^5$;
* $1 \leq P_j \leq N_i$ and $P_j \neq P_k$ for any $j \neq k$.
* For $C = 1$, the sum of the lengths of all move sequences from all $T$ tests does not exceed $1 \ 000 \ 000$.
* It is guaranteed that $(1, 1)$ and $(N, N)$ are not blocked by an obstacle ($P_1 \neq 1$ and $P_N \neq N$).

|#| Points| Constraints|
| - | - | ---------- |
| 1 | 18| $C = 1$, $1 \leq \sum_{i=1}^T N_i \leq 1 \ 000$, the sum of the lengths of move sequences from all $T$ tests does not exceed $10 \ 000$ |
| 2 | 19| $C = 1$ |
| 3 | 33| $C = 2$, $1 \leq \sum_{i=1}^T N_i \leq 1 \ 000$ |
| 4 | 30| $C = 2$ |

# Example 1

`arcade.in`
```
1 3
5
2 1 3 5 4
LDLDL
4
3 1 4 2
RDRUL
6
3 2 1 6 5 4
RURU
```

`arcade.out`
```
Won
Lost
Won
```

## Explanation

~[img1.png]

# Example 2

`arcade.in`
```
2 3
5
2 1 3 5 4
6
6 5 4 3 2 1
6
3 2 1 6 5 4
```

`arcade.out`
```
4
-1
4
```

## Explanation

~[img2.png]