## Task

A flea is on a linear board divided into $N$ positions numbered from $1$ to $N$, where any two adjacent positions have consecutive numbers. Some of these positions are free, while each of the remaining positions has a sugar cube. Initially, the flea is on position $1$ (the far left) and wants to reach position $N$ (the far right).

To reach its goal, the flea can perform the following moves:

- Move to the right: Assuming the flea is on position $x$, it can move to position $x+1$, if it is free, consuming an amount of energy $W$
- Move to the left: Assuming the flea is on position $x$, it can move to position $x-1$, if it is free, consuming an amount of energy $W$
- Jump to the right: For the flea to jump, it needs a run-up. Thus, if its last $K$ $(K \geq 1)$ moves were all to the right, then the flea can jump between $1$ and $K+1$ positions. Assuming its position is $x$, after a jump to the right of $Q$ positions, the flea will be on position $x + Q$. This position must be free. Regardless of the number of positions it jumps over, the flea consumes an amount of energy $J$
- Jump to the left: If the flea's last $K$ $(K \geq 1)$ moves were all to the left, it can jump between $1$ and $K+1$ positions. Assuming its position is $x$, after a jump to the left of $Q$ positions, the flea will be on position $x - Q$. This position must be free. Regardless of the number of positions it jumps over, the flea consumes an amount of energy $J$
- Push to the right: Assuming the flea is on position $x$. If position $x + 1$ contains a sugar cube, the flea can push this cube one position to the right. Following this operation, all cubes from positions $x + 1, x + 2, \dots, x + K - 1$, where $x + K$ is the first free position to the right of the flea, will move one position to the right. If there is no free position to the right of the flea, then the operation is not allowed. For a push, the flea consumes an amount of energy $P$. After the push to the right, the new position of the flea will be $x + 1$
- Push to the left: Assuming the flea is on position $x$. If position $x - 1$ contains a sugar cube, the flea can push this cube one position to the left. Following this operation, all cubes from positions $x - 1, x - 2, \dots, x - K + 1$, where $x - K$ is the first free position to the left of the flea, will move one position to the left. If there is no free position to the left of the flea, then the operation is not allowed. For a push, the flea consumes an amount of energy $P$. After the push to the left, the new position of the flea will be $x - 1$.

Write a program that determines the minimum amount of energy the flea will consume to reach position $N$, as well as a sequence of its moves.

## Input data

The first line of the input file `purice.in` contains $4$ integers $N$ $W$ $J$ $P$ (having the meanings described above). 

The second line of the file contains a sequence of $N$ characters from the set $\{0,1\}$, describing the $N$ positions: $0$ means the position is free, and $1$ means it is occupied by a sugar cube.

## Output data

The first line of the output file `purice.out` will contain the minimum amount of energy needed by the flea to reach position $N$. 

In the following lines, you will describe the moves made by the flea (one move per line).

The moves will be encoded as follows: 
- "WR" - for a move to the right 
- "WL" - for a move to the left 
- "JR" $K$ - for a jump to the right; after the string `JR` follows a space and then an integer $K$ $(K \geq 1)$, representing the number of positions the flea will jump (after this operation, the flea's position will increase by $K$ units)
- "JL" $K$ - for a jump to the left; after the string `JL` follows a space and then an integer $K$ $(K \geq 1)$, representing the number of positions the flea will jump (after this operation, the flea's position will decrease by $K$ units)
- "PR" - for a push to the right
- "PL" - for a push to the left

## Constraints and clarifications

$2 \leq N \leq 100$

$0 \leq W \leq 100\ 000$

$0 \leq J \leq 100\ 000$
 
$0 \leq P \leq 100\ 000$

The flea's position must always be in the range $1 \dots N$. 

Initially, positions $1$ and $N$ are free. 

In the test cases used, there will be at least one valid sequence of moves for the flea to go from position $1$ to position $N$. 

For the evaluation, $20$ tests will be used. 

The score for each test will be given as follows:
- If the sequence of moves described in the output file is not valid or, after executing it, the flea does not reach position $N$ or the amount of energy consumed by the flea after executing all moves is not equal to the number written on the first line of the output file, you will receive $0$ points
- Otherwise, let's assume that $M$ is the minimal amount of energy consumed by the flea to reach the final position and $A$ is the amount of energy determined by your program:
  - If $A = M$, you will receive $5$ points
  - If $M < A \leq 1.15 * M$, you will receive $4$ points
  - If $1.15 * M < A \leq 1.5 * M$, you will receive $3$ points
  - If $1.5 * M < A \leq 2 * M$, you will receive $2$ points
  - If $A > 2 * M$, you will receive $1$ point

## Example

`purice.in` 
```
8 2 2 3 
00110010
```

`purice.out`
```
20 
WR 
PR 
PR 
WL 
JL 2 
WR 
WR 
WR 
JR 4
```