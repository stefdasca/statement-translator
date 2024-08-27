# Stones

Macarie and Petronela are playing a very interesting game which they hope will further develop their intelligence. They have in front of them two piles of stones (with $A$ and $B$ stones, respectively). The game is played alternately (Macarie starts first), and at any given moment a player can take any number of stones from one pile or take the same number of stones from both piles. The player who cannot take any more stones loses.

## Task

You have to determine the winner for $T$ games, knowing that Macarie always starts the game.

## Input Data

The first line of the file `pietre.in` contains the number $T$ of tests. The next $T$ lines contain 2 integers $A$ and $B$ separated by a space, describing the number of stones in the two piles.

## Output Data

The file `pietre.out` will contain $T$ lines corresponding to the $T$ tests with the value 1 if Macarie wins the respective test and 2 if Petronela wins.

## Constraints and clarifications

$1 \leq A, B \leq 1\ 000\ 000$

$1 \leq T \leq 10$

## Examples

`pietre.in` `pietre.out` 
2 
1 2 
2 3 
2 
1 

## Explanations

In the first test, Macarie can take 1 stone from either pile, 2 stones from the second pile, or 1 stone from both piles. In all cases, Petronela can take all remaining stones and win the game. In the second test, Macarie wins by taking 2 stones from the second pile, and Petronela will lose according to the same considerations from example 1.