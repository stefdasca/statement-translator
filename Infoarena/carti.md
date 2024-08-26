# Cards

Alice and Bob are playing a card game. They use poker cards with the following values: the ace has a value of $1$, the jack has a value of $11$, the queen has a value of $12$, and the king has a value of $13$. The other cards have values equal to the numbers written on them ($2$, $3$, $4$, $5$, $6$, $7$, $8$, $9$, $10$). Alice starts the game, and then the two players take turns alternately. In each turn, the player whose turn it is can pick up from the table at most $k$ cards, provided that these have consecutive values. The player who cannot make a move loses.

## Task

Given a card configuration, determine the winner of the game, assuming that both players play optimally.

## Input data

The first line of the file `carti.in` contains the natural number $c$, representing the number of card configurations written in the file. Each configuration will be described by two lines. The first line of the two contains two natural numbers separated by a space. The first represents the number of cards on the table at the beginning of the game, the second is the number $k$, having the meaning given in the statement. The second line describes the cards on the table in no particular order. On such a line, the card denominations are separated by a single space. A card will be described by a number from $2$ to $10$ inclusive or by the characters $A$ (ace), $J$ (jack), $Q$ (queen), or $K$ (king).

## Output data

The output file `carti.out` will contain exactly as many lines as there are configurations in the input file. Each line of the output file will contain $Alice$ or $Bob$, depending on the winner of the game.

## Constraints and clarifications

$1 \leq k \leq 13$ 

In the description of a configuration, each card will appear only once 

The number of configurations in the file will not exceed $15$ 

## Example

`carti.in`
```
4
13 3
A 2 3 4 5 6 7 8 9 10 J Q K
2 2
K J
2 2 
Q K 
2 1 
4 5
```

`carti.out`
```
Alice
Bob
Alice
Bob
```