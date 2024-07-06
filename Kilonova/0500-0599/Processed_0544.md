Sure, here's the translated text with the specified instructions applied:

---

Because he is bored and very intelligent, Radu asked his friend, the scholar Feder, to create an activity that would challenge his mind. The scholar Feder brought $N$ rectangular pieces with natural numbers written on them and placed them on the table in increasing order of the values written on them, on consecutive positions, one next to the other. Then he gives Radu, one by one, other $M$ rectangular pieces with natural numbers written on them in any order. When Radu receives a piece, he must place it in the sequence on the table at the **smallest possible position** so that the pieces in the sequence remain in increasing order. Evidently, the sequence on the table changes as Radu places the pieces in the sequence.

# Task
Knowing the sequence of pieces on the table, in the order they are placed, as well as the $M$ pieces Radu successively receives, write a program that displays for each of the $M$ pieces the position where it is placed in the sequence on the table.

# Input data
The file `dominew.in` contains on the first line the natural number $N$. The second line contains $N$ natural numbers, in increasing order, representing the values of the pieces in the initial sequence on the table. The third line contains the natural number $M$. The fourth line contains $M$ natural numbers, representing the values of the pieces Radu receives, in the order he receives them. The numbers on the same line are separated by a space.

# Output data
The output file `dominew.out` will contain a single line with $M$ values separated by a space, the $i$-th value being the position where the $i$-th piece received by Radu is placed in the sequence on the table ($1 \\leq i \\leq M$).

# Constraints and clarifications

* $2 \\leq N \\leq 1 \\ 000 \\ 000$;
* $1 \\leq M \\leq 8 \\ 000$;
* The values written on the pieces are natural numbers $\\leq 10^9$;
* The positions of the elements in the sequence on the table are numbered starting from 1.

|# | Score | Constraints|
| - | -- | ------------|
| 1 | 8  | $M = 1$ |
| 2 | 14 | $1 < N, M \\leq 100$ |
| 3 | 8  | $100 < N \\leq 50 \\ 000$, $100 < M \\leq 250$ |
| 4 | 24 | $N \\leq 100 \\ 000$, $250 < M \\leq 1 \\ 000$ |
| 5 | 46 | $N \\leq 1 \\ 000 \\ 000$, $1 \\ 000 < M \\leq 8 \\ 000$ |

# Example 1

`dominew.in`
```
6
2 5 5 9 10 11
3
5 1 12
```

`dominew.out`
```
2 1 9
```

## Explanation

Initially, there are $N=6$ pieces on the table, in increasing order.
`2 5 5 9 10 11`
Radu receives $M=3$ pieces.
The first piece has the value $5$ and will be placed in the sequence on the table at position $2$. The sequence will become `2 5 5 5 9 10 11`.
The second piece has the value $1$ and will be placed in the sequence on the table at position $1$. The sequence will become `1 2 5 5 5 9 10 11`.
The third piece has the value $12$ and will be placed at position $9$ in the sequence on the table. The sequence will become `1 2 5 5 5 9 10 11 12`.

# Example 2

`dominew.in`
```
14
2 2 2 4 7 8 9 10 12 16 20 21 23 24
7
18 7 20 1 16 25 23
```

`dominew.out`
```
11 5 13 1 12 20 18
```

## Explanation

After the first $3$ insertions, the sequence will be `2 2 2 4 7 7 8 9 10 12 16 18 20 20 21 23 24`, with the value $20$ reaching position $13$.
