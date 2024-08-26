# Little Game

Being bored, Tom and Jerry decide to play a game together. The game is played on a board of size $1 \times C$, where each cell contains an integer. A move consists of extracting a cell from either of the two ends or two cells, one from each end. At the end, the score obtained by each player represents the sum of the numbers extracted by him. Determine the maximum difference between the score of the first and the second player, a difference that can be obtained in the worst case, regardless of how the second player plays.

## Input data

The input file `joculet.in` will contain on the first line the number of cells $C$. The next line will contain the $C$ numbers describing the game board.

## Output data

The output file `joculet.out` will contain a single number, representing the maximum difference.

## Constraints and clarifications

$1 \leq C \leq 2\,000$  
All numbers in the input file are 32-bit signed integers.

## Example

`joculet.in`  
`6`  
`1 -5 9 8 12 -5`

`joculet.out`  
`24`