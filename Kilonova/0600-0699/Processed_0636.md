```markdown
Two twin squirrels discovered a deposit of hazelnuts with a very strange shape. More precisely, the deposit has the form of an $N \times N$ matrix with $N$ odd. Each position in the matrix is a room, and in each room lies a hazelnut.

The rooms are numbered by their row and column number. The first squirrel, named Chip, is initially in room $(1, 1)$, and the second, named Dale, is in room $(N, N)$. The squirrels want to collect all the hazelnuts and meet in the central room of the deposit. For this, they will traverse the rooms, passing from one to another without ever crossing a room one of them has passed through before. They can move from one room to another (obviously, without exiting the deposit or entering an already visited room). When Chip passes from one room to another, he notes his path as follows:
- If he moves to the right room, from room $(L, C)$ to room $(L, C+1)$, he notes the passage with `0`.
- If he moves to the left room, from room $(L, C)$ to room $(L, C-1)$, he notes the passage with `1`.
- If he moves to the upper room, from room $(L, C)$ to room $(L-1, C)$, he notes the passage with `2`.
- If he moves to the lower room, from room $(L, C)$ to room $(L+1, C)$, he notes the passage with `3`.

Interestingly, for every passage Chip makes from one room to another, Dale moves in the exact opposite direction, meaning:
- If Chip moves to the right, Dale moves to the left.
- If Chip moves to the left, Dale moves to the right.
- If Chip moves up, Dale moves down.
- If Chip moves down, Dale moves up.

Meticulously, Chip calculates and records in lexicographical order all possible paths through which all the hazelnuts in the deposit can be collected. For example, for $N = 9$, the path from position $P = 12345$ is noted as follows: `0000311113333333000211200000022213312213`, corresponding to the scheme below:

~[veverite.png|width=30%|align=center]

# Task
Knowing $N$, respond to $Q$ questions of the form: "What path did Chip note at position $P$?".

# Input data
The input file contains the numbers $N$ and $Q$ on the first line, as described above. The following $Q$ lines contain the questions. Thus, on line $i+1$ contains a single number $P_i$.

# Output data
The output file contains $Q$ lines. Each line contains a string of characters `0`, `1`, `2`, or `3`, not separated by space. The string on line $i$ will contain the encoding of Chip's path corresponding to position $P_i$.

# Constraints and clarifications
- $3 \leq N \leq 9$ and $N$ is odd.
- $1 \leq Q \leq 1\ 000$.
- $1 \leq P_i \leq maxP$, where $maxP$ is the maximum number of possible paths for $N$.

| # | Points | Constraints |
| - | ------ | ------------ |
| 1 | 4      | $N = 3$      |
| 2 | 7      | $N = 5$      |
| 3 | 8      | $N = 7, P_i \leq 10$ |
| 4 | 13     | $N = 7, P_i \leq 564$ |
| 5 | 19     | $N = 9, P_i \leq 10$ |
| 6 | 21     | $N = 9, P_i \leq 1\ 000$ |
| 7 | 28     | $N = 9, P_i \leq 93\ 866$ |

# Examples
`veverite.in`
```
5 3
1
2
3
```
`veverite.out`
```
000031111300
000031303112
000033311120
```

\
`veverite.in`
```
9 1
12345
```
`veverite.out`
```
0000311113333333000211200000022213312213
```
```