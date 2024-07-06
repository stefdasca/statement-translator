Sure! Here's the translated document:

---

## Valutar

Valutar is a game that can be played by any number of players. At the beginning of the game, each player receives $L$ lei and $E$ euros, as well as a token numbered with the player's number. More specifically, if there are $M$ players, there will be $M$ tokens, numbered from $1$ to $M$.

The game board is the map of a city where a circular route containing $N$ currency exchange houses is illustrated, numbered in order on the route from $1$ to $N$. Being circular, after house $N$ comes house $1$. For each currency exchange house, two values $C$ and $V$ are known ($C$ represents how many lei a player has to pay if they want to buy $1$ euro from that house, and $V$ represents how many lei the player receives if they want to sell $1$ euro). Each house has a certain color depending on which the player who reaches that point must perform a certain action as follows:

|Color|Code|Effect|
|-|-|--------|
|White|A|The player does nothing on this turn.|
|Red|R|The player receives a card named "pass". A player who has a pass card will use the card (only once, after which the card will be removed from the game) and thus avoid performing an action that they cannot perform, to avoid being eliminated from the game.|
|Yellow|G|The player has to buy $i$ euros (where $i$ is the number of the currency exchange house they are at). If they do not have enough lei to do this and do not have a pass card, the player is eliminated from the game. If they have a pass card, the player will use it and not perform the action, without being eliminated from the game.|
|Green|V|The player has to sell $i$ euros (where $i$ is the number of the currency exchange house they are at). If they do not have enough euros to do this and do not have a pass card, the player is eliminated from the game. If they have a pass card, the player will use it and not perform the action, without being eliminated.|

Initially, all players start from currency exchange house $1$ which is white. There are $N$ currency exchange houses and $M$ players. Players move in turn in the order of the tokens. First player $1$ moves, then $2, 3, \dots, M$. After player $M$, player $1$ moves again, etc. On a move, a player who has not been eliminated from the game:

* "rolls" the electronic dice; the dice will display an integer $nr$;
* advances by $nr$ positions (i.e., if their token is at house $i$, they will reach house $i+nr$);
* performs the action associated with the currency exchange house they have reached, depending on its color.

The electronic dice work as follows: on move number $j$, the number $nr_j$ is generated calculated by the formula $nr_j = (a \cdot nr_{j-1}+b)\ \ \% \ \ N+1$, where $nr_{j-1}$ is the number generated on move $j-1$; $a, b$ and $nr_0$ are three known values, and $\%$ represents the remainder of the integer division (mod).

## Task

Write a program that solves the following tasks:

* Determine the number of players remaining in the game after $X$ moves;
* Determine the player who remains in the game and has the most euros after $X$ moves.

## Input data

The input file `valutar.in` contains: the first line contains the task that needs to be solved ($1$ or $2$).
The second line contains the natural numbers $a, b$ and $nr_0$, with the meaning from the statement.
The third line contains the natural numbers $N, M, L, E, X$, representing the number of currency exchange houses, the number of players, how many lei and how many euros each player receives at the beginning of the game, respectively the number of moves in the game. The next $N$ lines describe the currency exchange houses, one house per line, in order from $1$ to $N$, in the form $Code \ C \ V$, with the meanings from the statement. The values written on the same line are separated by a space.

## Output data

The output file `valutar.out` will contain a single line. If the task is $1$, the line will contain a natural number representing the number of players remaining in the game after $X$ moves. If the task is $2$, the line will contain the number of the token of the player who remains in the game and has the most euros after $X$ moves.

## Constraints and clarifications

* $1 \leq M, C, V \leq 100$;
* $1 \leq a, b, nr_0, N, X \leq 10\ 000$;
* $1 \leq L, E \leq 10^6$;
* All currency exchange houses have enough lei and euros for any action.
* It is guaranteed that for the test data in task $2$, a single player will remain in the game with the maximum euro amount after $X$ moves.
* For each task, $50$% of the points obtained on tests are awarded.

## Example 1

`valutar.in`
```
1
3 2 7
5 3 2 3 8
A 1 1
G 5 4
G 6 4
V 6 5
R 2 3
```

`valutar.out`
```
1
```

## Example 2

`valutar.in`
```
2
3 2 7
5 3 2 3 8
A 1 1
G 5 4
G 6 4
V 6 5
R 2 3
```

`valutar.out`
```
2
```

## Explanation

The numbers obtained when rolling the dice are generated as follows: $nr_j = (3 \cdot nr_{j-1}+2)\%5+1$, where $nr_0=7$. There are $5$ currency exchange houses and $3$ players in the game. All players initially have $2$ lei and $3$ euros and are at the first currency exchange house which is white. $8$ moves are made as follows:

|Move|Player|nr|From where|To where|Action|Lei|Euro|Notes|
|-|-|-|-|-|-|-|-|--------|
|1|1|4|1|5|R|2|3|Received a pass card|
|2|2|5|1|1|A|2|3|Does nothing|
|3|3|3|1|4|V|2|3|Must sell $4$ euros, but only has $3$, does not have a pass card, so is removed from the game.|
|4|1|2|5|2|G|2|3|Must buy $2$ euros, which cost $2 \cdot 5 = 10$ lei, does not have enough money but has a pass card which is used, so remains in the game|
|5|2|4|1|5|R|2|3|Received a pass card|
|6|1|5|2|2|G|2|3|Must buy $2$ euros, which cost $2 \cdot 5 = 10$ lei, does not have enough money nor any pass cards, so is eliminated from the game|
|7|2|3|5|3|G|2|3|Must buy $3$ euros which cost $6 \cdot 3 = 18$ lei, does not have enough money but has a pass card which is used, so is not eliminated from the game|
|8|2|2|3|5|R|2|3|Receives a pass card|

## End of Example

---