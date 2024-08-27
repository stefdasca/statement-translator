## Apples

Santa Klaus and Mickey Mouse have a basket containing exactly $N$ apples. They have thought of playing a game with these apples, based on the following rules: The two will take turns moving alternately. Each player plays optimally (if there is a strategy that ensures their win, they will use it). Santa Klaus always moves first. The player on their turn must take a natural number between $1$ and $K$ apples from the basket. The game ends when there are strictly less than $K$ apples left in the basket, and the winner is declared as the one who has taken the most apples! If both players have collected the same number of apples, the game result is a draw. The two will play a total of $T$ such games.

## Input data

The input file `mere.in` contains a natural number $T$, representing the number of games. Each of the next $T$ lines contains two natural numbers $N$ and $K$, having the significance from the statement.

## Output data

The output file `mere.out` will contain $T$ lines. Each line $i$ out of the $T$ will contain the name of the winner of the $i$-th game, as follows:
- if Santa Klaus wins, it will display Santa Klaus
- if Mickey Mouse wins, it will display Mickey Mouse
- if the game ends in a draw, it will display Draw

## Constraints and clarifications

$1 \le T \le 100$  
$1 \le N \le 10^9$  
$1 \le K \le 10^9$  

If initially, the basket contains a number of apples strictly less than $K$, Santa Klaus cannot make the first move and the game will end in a draw.

## Example

`mere.in`
```
2
10 6
5 10
```
`mere.out`
```
Santa Klaus
Draw
```

## Explanation

For the first test, Santa Klaus will take $6$ apples from the basket. There will be exactly $4$ apples left in the basket, so the game ends. Santa Klaus has collected $6$ apples, and Mickey Mouse $0$. Therefore, Santa Klaus is the winner.

For the second test, Santa Klaus is not allowed to take apples from the basket since the basket does not have at least $10$ apples in it. The game ends in a draw because both have collected $0$ apples.