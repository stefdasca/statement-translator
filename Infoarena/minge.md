## Task

Cristina, Ruxandra, Adriana, and their classmates are playing with a ball in the schoolyard. There are a total of $N$ girls participating in the game. At the beginning, they choose a number $K$ $( 1 \leq K \leq \frac{N}{2} )$, and then they stand in a circle. The first girl passes the ball to the $K$-th girl to her right. This girl, in turn, passes it to the next $K$-th girl, and the process repeats until the ball reaches the first girl again. Ruxandra is upset that the ball does not reach her during the game, so she asks you to find a number $K$ such that the ball will pass through all the girls exactly once. To make the game even more interesting, she wants to choose that number $K$ which ensures that the ball will be played by all the girls and, in addition, to be the maximum with this property. For example, if there are $7$ girls, we can choose $K$ equal to $3$. For this case, the girls will receive the ball in the order $1$, $4$, $7$, $3$, $6$, $2$, $5$, after which the ball returns to the first girl in the sequence.

## Input data

The input file `minge.in` contains a single natural number $N$ on the first line, representing the number of girls.

## Output data

The first line of the output file `minge.out` will contain the maximum number $K$ $(1 \leq K \leq \frac{N}{2})$ that ensures the ball will pass through each girl exactly once.

## Constraints and clarifications

$3 \leq N \leq 10^4$

$1 \leq K \leq \frac{N}{2}$

## Example

`minge.in` 
$7$

`minge.out` 
$3$