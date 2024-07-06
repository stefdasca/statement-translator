Ana and Bogdan have invented yet another game. The game involves white and black tokens initially arranged in a stack, in some order. We call a _configuration_ the sequence of colors of all tokens in the stack (in order, starting from the top of the stack). A white token is encoded by the letter $A$, and a black token by the letter $N$.

On each turn, a player can take any number of consecutive tokens from the top of the stack (but at least one token), provided that all tokens taken have the same color. The players alternate turns, with Ana going first. The game will be won by the player who takes the last token.
We say that a player has a _sure winning strategy_ if, by following this strategy, they win the game regardless of the moves of the other player.

# Task

Write a program that reads $T$ configurations and determines for each of the $T$ configurations whether Ana has a sure winning strategy.

# Input data

The input file `an.in` contains on the first line a natural number $T$ representing the number of configurations. The next $T$ lines contain the $T$ configurations, one configuration per line, in the form of a sequence of letters from the set $\\{A, N\\}$.

# Output data

The output file `an.out` will contain $T$ lines. On the $i$-th line, it will contain the value $1$ if Ana has a sure winning strategy for the $i$-th configuration from the input file, and the value $0$ otherwise.

# Constraints and clarifications

* $1 < T \leq 50$
* $0$ < number of tokens in any configuration $\leq 10 \ 000$

# Example

`an.in`
```
3
A
AN
NNNAA
```

`an.out`
```
1
0
1
```

## Explanation

First configuration: there is only one token, Ana takes it and wins.
Second configuration: Ana is forced to take the first token, Bogdan will take the second one and Bogdan wins.
Third configuration: Ana takes the first two tokens. Bogdan will be forced to take the third token. Ana takes the last two tokens and wins.