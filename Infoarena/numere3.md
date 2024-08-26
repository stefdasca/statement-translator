# Numbers 3

Ionel has a weakness for puzzle games. He is trying to solve a game where he has a matrix of size $M \times N$ whose elements are integers. A move consists of decreasing the value of an element by the number of neighbors at that position and increasing the values of the neighboring elements by one. The neighbors for a given position are the elements on the horizontal and vertical axis, so a position can have $2$, $3$, or $4$ neighbors. Certain known positions in the matrix are sensitive to decrease, meaning no moves can be made at these positions. The number of such positions is $K$. Ionel's goal is to achieve a matrix where all elements have the same parity, starting from the initial matrix, by performing the minimum number of moves.

## Input data

The input file `numere3.in` contains on the first line three numbers, $M$, $N$, and $K$ as specified above. The next $M$ lines contain $N$ integers each, representing the initial matrix. The following $K$ lines contain two integers separated by a space, representing the coordinates of the positions sensitive to decrease (the first number represents the row, the second the column).

## Output data

The output file `numere3.out` will contain on the first line the minimum number of moves $MIN$ that solve the game. The next $MIN$ lines will contain the moves, one move per line (two integers representing the row and column of the move). If there is no solution, it will print $-1$.

## Constraints and clarifications

$2 \leq M$, $N \leq 12$ 

$0 \leq K \leq M \times N$ 

The elements of the matrix are integers ranging from $1$ to $10000$ inclusive, but during the game, the values in the matrix can be outside this range 

If there are multiple solutions, any of them can be displayed 

## Example

`numere3.in`
```
2 2 1
2 1 
1 2 
2 1 
```

`numere3.out`
```
1
1 1
```