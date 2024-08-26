# Xerox

Because the exam period is approaching and she didn't attend university during the year, Miruna found herself needing to photocopy her classmates' lecture notes. By mistake, when she decided to go to the photocopier, Miruna picked up a stack of papers from the table other than the one containing the lecture notes. Thus, the girl has $N$ sheets, which instead of containing useful information for exams, are good for throwing away. But Miruna doesn't want to waste paper, so she is thinking about what she could use the sheets she picked up from the table for. She notices that they only contain some points, drawn randomly. Since she got bored of playing with her little brother's marbles, the girl thinks of a new game. Let's assume we have 2 players who will take turns. At each turn, one of the players chooses a sheet and draws a simple closed curve that passes through at least one of the points that were initially drawn on the sheet and does not touch any of the previously drawn lines. The player who moves last is declared the winner.

## Task

Knowing the dimensions of the sheets and the positioning of the points on each of them, determine if the first player has a sure winning strategy or not.

## Input data

The input file `xerox.in` contains a single natural number $T$ on the first line, representing the number of tests. For each test, the first line will contain $3$ natural numbers $N$, $DX$, $DY$, representing the number of sheets and their dimensions, respectively. On the following $N$ lines, the necessary information for each sheet will be found. First, a natural number $M$, representing the number of points on the sheet, then $M$ pairs of natural numbers $X_i$ and $Y_i$, representing the coordinates of the points if we fix a coordinate system with the origin in the bottom left corner of the sheet.

## Output data

For each test, print on a separate line in the output file `xerox.out` the value $1$ if the first player has a sure winning strategy, and $0$ otherwise.

## Constraints and clarifications

$1 \leq T \leq 20$ 

$1 \leq N \leq 100$ 

$1 \leq M \leq 200$ 

$1 \leq DX, DY \leq 1000$ 

For any test, $0 < X_i < DX$ 

$0 < Y_i < DY$.

The points on the same sheet will be distinct.

## Example

`xerox.in` 
`
1 
2 10 10 
1 6 6 
1 5 5
`

`xerox.out` 
`
0
`