Mihai received a special chess game for his birthday. The game board is square-shaped, with a dimension of $N$, but some positions are marked as obstacles and cannot be occupied by pieces. In addition, his game has a single piece, called the “bishop�. Two positions on the board are designated as the initial position and the final position. Mihai wants to determine a way to move the bishop, with a minimum number of moves, so that it reaches from the initial position to the final position. Mihai will follow the bishop’s movement rules from chess, meaning that from the current position, the bishop can move only diagonally, in any of the $4$ directions, any number of positions at a time but without jumping over obstacles. Additionally, Mihai is allowed one exception to this rule: he is permitted to make **at most** two moves following the knight's moving rule in chess. ~[img1.jpg|align=right]

For clarification, in the following figure, the position of the knight is marked with $X$. It can be moved to any of the positions marked with $Y$. During a move following the knight’s rule, the state of the positions over which it jumps does not matter, only that the final position does not represent an obstacle.

The chessboard has the rows numbered from top to bottom with natural numbers between $1$ and $N$, and the columns from left to right with natural numbers between $1$ and $N$. A position on the board is identified by a pair $(i, j)$ where $i$ represents the row and $j$ the column of that position.

# Task

Given the chessboard configuration as well as the initial and final positions of the piece, determine the minimum number of moves required to move the piece between the two positions.

# Input data

The file `sah.in` contains on the first line the numbers $N, i_1, j_1, i_2, j_2,$ separated by a space, representing: $N$ – the board dimension; $(i_1, j_1)$ – the initial position of the piece; $(i_2, j_2)$ – the final position of the piece. The following $N$ lines contain $N$ numbers from the set $\{0,1\}$. The value $1$ represents a position marked as an obstacle on the board, and the value $0$ a free position. The numbers on the same line **are not separated by spaces**.

# Output data

The file `sah.out` contains on the first line a natural number representing the minimum number of moves required.

# Constraints and clarifications

* $1 \leq N \leq 500$;
* The piece cannot leave the game board;
* It is guaranteed that the initial and final positions are not marked as obstacles;
* It is guaranteed the existence of at least one possibility to move the piece between the initial and final positions;
* It is recommended to read the data from the file line by line and not character by character;

# Example

`sah.in`
```
4 1 1 4 1
0100
1000
0010
0000
```

`sah.out`
```
2
```

## Explanation

The bishop starts from $(1,1)$ using the knight’s move to reach position $(3,2)$, then from that position, using the diagonal movement jumps to the final position $(4,1)$. Another solution can be achieved by making the moves: $(1,1) \Rightarrow (2,3)$ ; $(2,3) \Rightarrow (4,1)$.