# Game

Gicu and Nicu, computer science olympians and good friends, always try to combine their activities with computer science. For example, when they get bored during classes, they play a game based on the following rules: consider a matrix with integers with $N$ rows and $M$ columns each player alternates moves a token placed on an element of the matrix a move consists of placing the token on another position and adding the value from the matrix at that position to the score of the player who made the move; once the token is placed on a position, the next player can only move the token to another position within the rectangle formed by the top-left corner and the current position of the matrix the game ends when a player reaches the token in the top-left corner of the matrix at the start of the game, both players have a score of $0$, and the player who starts chooses the initial position of the token

## Task

Assuming that both players play optimally, and that Gicu will start the game, determine the initial position of the token such that the score difference between Gicu and Nicu is maximum!

## Input data

The first line of the file `joc.in` contains two integers $N$ and $M$, separated by a space, which represent the number of rows and columns of the matrix. The next $N$ lines contain $M$ integers each, separated by a space, which describe the matrix.

## Output data

The file `joc.out` will contain three integers separated by a space: the maximum score difference between Gicu and Nicu and the row and column where the token will be placed at the start of the game.

## Constraints and clarifications

$1 \leq N, M \leq 1\,000$  
The values in the matrix are in the interval $\left[ -1\,000, 1\,000 \right]$  
Rows are numbered from $1$ to $N$, and columns from $1$ to $M$  
By playing optimally, it is understood that Gicu will try to maximize the score difference, while Nicu will try to minimize it  
If there are multiple initial positions for which the maximum difference is obtained, then choose the one where the row number is the smallest, and in case of equality, the one where the column number is the smallest  

## Example

`joc.in`  
`1 6`  
`2 1 3 4 0 5`  

`joc.out`  
`3 1 6`  

## Explanation

Starting from $(1, 6)$ the optimal game is: Gicu takes $5$, Nicu takes $4$, Gicu takes $2$. Any other initial position of the token would have resulted in a smaller score difference.