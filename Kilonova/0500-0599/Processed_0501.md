# Problem Statement

On a field resembling a chessboard with $M$ rows and $N$ columns, a ewe is located in the cell with coordinates $(1, 1)$ in the top-left corner of the board and wants to reach the cell with coordinates $(M, N)$ in the bottom-right corner of the board. She can make jumps of length at most $P$ to the right, length at most $Q$ downward, length at most $R$ diagonally to the bottom-right, as well as a knight's jump, that is, two cells to the right and one downward or two downward and one to the right. Any jump must change the position of the ewe.

An integer $C$ is given.
- If $C = 1$, determine the minimum number of jumps needed to reach the cell with coordinates $(M, N)$.
- If $C = 2$, determine the number of ways she can reach the cell with coordinates $(M, N)$, not necessarily with the minimum number of jumps.

It is guaranteed that for the input data there is at least one way to reach the cell $(M, N)$.

# Input data
The first line of the input file contains the number $C$, the second line contains the integers $M$ and $N$, and the third line contains the integers $P$, $Q$, and $R$.

# Output data
The output file will display, corresponding to the value of $C$, the required number. The result will be displayed modulo $1\ 000\ 000\ 007$.

# Constraints and clarifications
- $1 \leq M, N \leq 1000$
- $0 \leq P \leq N-1$
- $0 \leq Q \leq M-1$
- $0 \leq R \leq \min(M-1, N-1)$
- If $P = 0$, she cannot jump to the right, if $Q = 0$, she cannot jump downward, and if $R = 0$, she cannot jump diagonally.
- For 26 points, $C = 1$, $M = 1$.
- For 15 points, $C = 1$, $M = 2$.
- For 7 points, $C = 1$, $M = 3$.
- For 7 points, $C = 1$, $1 \leq M, N \leq 200$.
- For 8 points, $C = 1$, $1 \leq M, N \leq 1000$.
- For 11 points, $C = 2$, $1 \leq M, N \leq 5$.
- For 12 points, $C = 2$, $1 \leq M, N \leq 200$.
- For 14 points, $C = 2$, $1 \leq M, N \leq 1000$.

# Examples
`turcane.in`
```
1
4 3
2 3 1
```
`turcane.out`
```
2
```

`turcane.in`
```
2
2 3
2 1 1
```
`turcane.out`
```
8
```

# Explanations
We denote by $O_i$ the jump to the right by $i$ cells, by $V_i$ the jump downward by $i$ cells, by $D_i$ the diagonal jump by $i$ cells, by $Cd$ the knight's jump to the bottom-right, and by $Cj$ the knight's jump to the right-bottom.

For the first example, the minimum number of jumps is $2$, and we have six solutions: $V_3 − O_2$ or $Cd − V_2$ or $Cj − D_1$ or $O_2 − V_3$ or $V_2 − Cd$ or $D_1 − Cj$.

~[turcane1.png]

For the second example, the number of distinct solutions is $8$: $O_1 − O_1 − V_1$ or $O_1 − V_1 − O_1$ or $O_1 − D_1$ or $O_2 − V_1$ or $D_1 − O_1$ or $V_1 − O_1 − O_1$ or $V_1 − O_2$ or $Cd$.

~[turcane2.png]