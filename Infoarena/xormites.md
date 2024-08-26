## Task

You might be familiar with the following game: given a sequence of $N$ natural numbers, two players take turns, with each turn consisting of extracting a value from one of the ends of the sequence (either the left or the right end). The value is removed from the sequence and then added to the player's total score. The game ends when the sequence becomes empty, and the winner is the player with the higher sum. This game is now a part of history. All the cool kids are playing the "xor" variant of this game. Specifically, the game proceeds identically, but a player's score is calculated as the xor sum of the chosen values. Given a sequence of $N$ numbers, you must decide whether the game would be won by the first player (defined as the one making the first move), by the second player, or if it will end in a tie. For this purpose, you will assume that both players act optimally: if a winning strategy is available to a player, they will use it.

## Input data

The input file `xormites.in` will contain on its first line the value $T$, the number of tests in the file. Following are the $T$ tests, with the structure of a test being the following: the first line contains the value $N$, representing the number of values in the sequence. Following are $N$ natural numbers, representing the sequence values.

## Output data

The output file `xormites.out` will contain a string of $T$ characters, representing the results of the games described in the input file. The $i$-th character of the string will be equal to $2$ if the game ends in a tie, $1$ if it is won by the first player, and $0$ if the game is won by the second player.

## Constraints and clarifications

$1 \leq T \leq 12$  
$1 \leq N \leq 100\,000$  
$0 \leq V[i] \leq 1\,000\,000\,000$  

For tests worth 20 points $1 \leq N \leq 100$ and $0 \leq V[i] \leq 150$  
For other tests worth 20 points $1 \leq N \leq 1000$

## Example

`xormites.in`
```
3
2
3 3
2
3 5
3
4 4 4
```

`xormites.out`
```
210
```