```markdown
> *National College "Frații Buzești"* ~[logos.png|align=right|width=20rem] 
> *Training Center for Informatics Performance* 
> **InfoCNFB** - Second Edition, Juniors 
> December 9, 2023 

# Task 

Our Tetris game is played on a rectangular board where pieces "fall" from row $1$. At some point, some cells of the board are occupied, others are free, and a new piece is about to "fall". 

Unfortunately, the keys are stuck and the player can no longer move the piece or "rotate" it. Effectively, it falls until it reaches the bottom of the board or part of it stops immediately above an occupied cell. If, when the piece stops, one or more rows become fully occupied cells, these rows disappear and the cells above these rows are translated down on the same column, each cell being translated by the number of rows representing the value of those disappeared below it. 

Given the configuration of the board and the piece that "falls", determine how the board looks after the piece falls. 

It is guaranteed that for the given configuration of the board (before the piece falls) there are no rows with all cells occupied. 

There are two types of pieces, both consisting of $h$ occupied cells:
* Type $1$ ($h$ occupied cells one below the other): 

~[tetris_1.png|align=center] 

* Type $2$ ($h-1$ occupied cells one below the other, and immediately to the right of the top cell, there is one more occupied cell): 

~[tetris_2.png|align=center] 

The pieces fall exactly in the middle of the board. If the width of the board ($m$) is odd, a type $1$ piece "falls", and if the width is even, a type $2$ piece "falls". 

# Input data 

The first line of the `tetris.in` file contains three numbers $n$, $m$, and $h$, separated by space, representing respectively: the number of rows, the number of columns of the rectangular board, and the number of cells occupied by a piece, as described above. The next $n-h$ lines contain $m$ values that can be $0$ or $1$ ($1$ means an occupied cell). These values are separated by a space. We consider that above these $n-h$ lines, there are $h$ more lines without any occupied cells. 

# Output data 

The `tetris.out` file will contain the configuration of the game board without the completely empty rows above (each printed line will have $m$ elements $0$ or $1$, separated by a space). 

# Constraints and clarifications 

* $1 \leq n \leq 1 \ 000$;
* $2 \leq m \leq 1 \ 000$;
* $2 \leq h \leq n-1$;
* For $51$ points, we have $m$ even;
* It is guaranteed that at least one occupied cell remains on the board at the end. 

# Example 

`tetris.in`
```
9 4 5
1 0 0 0
1 0 1 1
1 0 1 1
1 1 0 1
```

`tetris.out`
```
0 1 1 0
1 1 0 0
1 1 0 1
```

## Explanation 

We are in the case with $m$ even, the piece is of type $2$ and falls on the middle columns, $2$ and $3$. 

We imagine the game board as follows ($h$ free lines above):
```
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
1 0 0 0
1 0 1 1
1 0 1 1
1 1 0 1
```

Falling, the piece stops as follows:
```
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 1 1 0
1 1 0 0
1 1 1 1
1 1 1 1
1 1 0 1
```

The last two rows become full with $1$ and disappear. 
The $4$ lines full of $0$ above are no longer printed.
```
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 1 1 0
1 1 0 0
1 1 0 1
```
```