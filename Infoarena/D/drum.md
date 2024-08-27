# Path

Consider a $5 \times 5$ board with 25 square pieces, each piece having one of the following shapes: $(1)$ $(2)$ $(3)$. It is observed that piece $(1)$ has connected edges $N-S$ and $E-W$, piece $(2)$ has connected edges $N-E$ and $S-W$, and piece $(3)$ has connected edges $N-W$ and $S-E$. Note that the two lines in piece $1$ do NOT intersect but pass "one under the other."

## Task

The task is to place the 25 pieces on the board in such a way that a path is formed which:
1. Passes through each square exactly once;
2. Does not intersect itself;
3. Starts from the $NW$ corner of the board (row $1$, column $1$), starting from outside the board (either from the north or from the west);
4. Ends at the $SE$ corner of the board (row $5$, column $5$) and exits the board.

## Input data

The first line of the file `drum.in` will contain the numbers $N_1$, $N_2$, and $N_3$, representing the number of pieces of types $1$, $2$, and $3$. It is guaranteed that their sum is $25$.

## Output data

The file `drum.out` will contain a matrix with $5 \times 5$ numbers separated by spaces, representing the type of piece placed in each square. If there are multiple solutions, any one of them may be printed. If there is no solution, the file will contain the message "imposibil."

## Example

`drum.in`
```
6 9 10
```

`drum.out`
```
1 2 3 1 2 
3 3 1 3 3 
1 3 3 2 2 
1 2 2 3 3 
2 1 3 2 2
```

`drum.in`
```
25 0 0
```

`drum.out`
```
imposibil
```