# Tournament

In a football tournament, $N$ teams participate, with each team playing exactly one match against every other team. The winning team of a match scores one point, and if a match ends in a draw, each team scores half a point. At the end of the tournament, the number of points accumulated by each team is recorded, and a ranking is formed. Due to the large number of teams, it is possible that the points are not always recorded correctly.

## Task

Write a program that, given an input array of $N$ rational numbers, decides whether these can be the scores obtained from a football tournament.

## Input data

The first line of the file `turneu.in` contains an integer $T$ representing the number of score arrays to be analyzed. Each of the next $T$ lines contains a natural number $N$ representing the number of teams in the tournament and then $N$ rational numbers with at most one decimal place, in ascending order, representing the scores of each team.

## Output data

For each of the $T$ tests, print in the output file `turneu.out` a line containing YES if the array can be the result of a tournament, or NO otherwise.

## Constraints and clarifications

$1 \leq N \leq 100\,000$

$1 \leq T \leq 10$

For $50\%$ of the tests $N \leq 1\,500$

## Example

`turneu.in`

  7

  4 0 1 2 3

  4 0 1 2.5 2.5

  4 1.5 1.5 2 2

  4 0 2 2 2

  4 0 1 1 4

  5 0 1 2 3 3

  10 1 1 1 1 5 5 7 7 8 9

`turneu.out`

  YES

  YES

  NO

  YES

  NO

  NO

  NO