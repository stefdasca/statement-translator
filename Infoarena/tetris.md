# Tetris

Note. This problem has been modified from the original because the previous version was incorrect. Older sources will not be re-evaluated because they work with the incorrect version. You are playing Tetris. There is a board with $N$ rows and 2 columns. The pieces are in the shape of a vertical line, with a piece $i$ occupying $L[i]$ rows in one column. The pieces fall in the classic manner. The goal is to choose the column where you want each piece to fall. The game ends either when you want it to or when the next piece can no longer be placed fully on the board. A piece can only be used if all the pieces before it have been correctly placed on the board.

## Task

Find all configurations $(a, b, c)$ that can be obtained. $a$ represents the height of the first column occupied on the board, $b$ the height of the second column, and $c$ the number of pieces placed.

## Input data

The input file `tetris.in` contains on the first line the number $N$ of rows and the number of pieces $K$. The following lines contain $K$ numbers $L[i]$.

## Output data

The output file `tetris.out` contains on the first line the required number.

## Constraints

$1 \leq N \leq 2\ 000$
$1 \leq K \leq 500$
$1 \leq L[i] \leq N$

## Example

`tetris.in`
```
4 
4 
2 
2 
2 
2 
```

`tetris.out`
```
9 
```

## Explanation

$(0, 0)$, $(2, 0)$, $(4, 0)$, $(0, 2)$, $(2, 2)$, $(4, 2)$, $(0, 4)$, $(2, 4)$, $(4, 4)$