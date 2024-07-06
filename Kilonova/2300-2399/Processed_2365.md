# Statement

Nargy and Fumeanu are playing a game called *Nakhla*. The game is played with chips on a board of length $N$ and width $M$.

Nargy's chips are white, and Fumeanu's chips are black. At the beginning of the game, each player has $N$ chips, placing one chip per row, under the condition that in each row the white chip is to the left of the black chip.

After placing the chips, the two players make moves alternately, the first move being made by the player with the white chips. A move consists of moving a chip as follows: Nargy will choose a white chip and move it to the right; Fumeanu will choose a black chip and move it to the left. A move can only be made if the condition that in each row the white chip is to the left of the black chip is still respected. The game ends when no more moves can be made, and the player who made the last move is the winner.

# Task

Write a program that plays the game *Nakhla* as Nargy, against Fumeanu.

# Interaction Protocol

Your program will not perform operations with any file. It will have to implement the function
```cpp
void solve(int N, int M, std::vector<std::pair<int, int>> moves);
```
where the array `moves` contains $N$ pairs of integers $A_i \\ B_i\\ (A_i < B_i)$ signifying that Nargy placed a chip on row $i$ and column $A_i$, and Fumeanu placed a chip on row $i$ and column $B_i$.

Then, to play against the jury, you will need to call the function
```cpp
std::pair<int, int> move(int i, int j);
```
where the parameters $i \\ (1 \\leq i \\leq N)$ represent the row on which the move is made and $j \\ (j > 0)$ the number of columns the chip will be moved to the right. The function will return a pair of other numbers $i \\ j$ representing Fumeanu's move. The number $i \\ (1 \\leq i \\leq N)$ represents the row on which the move is made, and $j \\ (j > 0)$ is the number of columns the chip will be moved to the left.

When no more moves can be made, the program will terminate its execution, regardless of the player who made the last move.

~[image.png|align=right]

# Example
The function `solve(3, 6, {{1,3},{2,5},{1,6}})` is called by the jury.
The contestant calls `move(3, 1)` (Nargy's move), which returns `{3, 3}` (Fumeanu's move).
The contestant calls `move(2, 1)` (Nargy's move), which returns `{2, 1}` (Fumeanu's move).
The contestant calls `move(1, 1)` (Nargy's move).
The game ends, and the program stops execution.

# Constraints and clarifications

* $1 \\leq N \\leq 100\\ 000$;
* $1 \\leq M < 2^{31}$;
* At no point can there be two chips in the same location on the board;
* If your program plays optimally, it is guaranteed that for any test Nargy will always have a winning strategy;
* If your program plays optimally, it is guaranteed that the jury program will play so that the game ends in at most $150\\ 000$ moves. If your program exceeds this number of moves, no points will be awarded.