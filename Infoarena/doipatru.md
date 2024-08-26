# DoiPatru

The members from the National Informatics Team are very proud of their newly invented game, which they named similarly to a problem from the 2001 International Olympiad in Informatics, which they liked very much. Thus, the game is called DoiPatru. For this game, $N$ piles are used, each containing at least $0$ and at most $4$ balls. The total number of balls in all piles is $2N$. Two players take turns alternatively. When it's their turn, each player must make a valid move. A valid move consists of choosing two piles, where the first pile has more balls than the second one. The player takes a ball from the first pile and moves it to the second pile. The move is considered valid only if the number of balls in the second pile after moving the ball is not greater than the number of balls remaining in the first pile. The game ends when no valid move can be made (if you think about it a bit, you'll realize this happens when each pile contains two balls). The winner of the game is the one who holds more piles at the end of the game. Of course, if both players hold an equal number of piles, the game is considered a draw. A player holds a pile if the pile has two balls, and this number (of two balls) results from a move made by that player. For example, if a player chooses a pile with $4$ balls and one with $1$ ball, after making the move, they will hold the second pile (which will have two balls), but the first one will not belong to any of the players for now. If they choose a pile with $3$ balls and one with $0$ balls, the player will become the owner of the first pile, because, after making the move, that pile will remain with two balls. If they choose a pile with $3$ balls and one with $1$ ball, after making the move, they will hold both piles (both now have two balls). If a player is the owner of a pile at a certain point in the game, it does not mean that the pile will remain in their possession until the end. For example, let's assume player $1$ owns a pile with two balls and it's player $2$'s turn to move. If player $2$ chooses a pile with $4$ balls and the pile with two balls belonging to player $1$, after making the move, both piles will have $3$ balls, and the number of piles owned by player $1$ will decrease by $1$ (the pile they previously owned no longer belongs to either player, as it no longer has two balls). If at the beginning of the game there are some piles with two balls, they are equally distributed to the two players. If the number of piles with two balls is odd, then player $2$ will receive one more pile than player $1$. Player $1$ is the one who makes the first move.

## Task

Write a program that, for a given $N$ and a set of initial game configurations with $N$ piles, decides the outcome of each game configuration.

## Input data

The first line of the input file `doipatru.in` contains two integers: $N$ and $S$, representing the number of piles used in the game and the number of initial game configurations described below. The next $S$ lines contain $N$ integer values in the range $[0, 4]$, whose sum is equal to $2N$, each representing an initial game configuration.

## Output data

In the output file `doipatru.out`, for each initial game configuration described in the input file, in the order they are described, print the final outcome of the game, assuming both players play optimally. You will print the value $1$ if the game is won by the first player, the value $2$ if the game is won by the second player, or the value $0$ if the game ends in a draw.

## Constraints and clarifications
$$3 \leq N \leq 30$$ 
$$1 \leq S \leq 1000$$ 

## Example

`doipatru.in`
```
5 4 
0 3 4 1 2 
2 2 2 2 2 
1 1 2 2 4 
4 3 2 1 0 
```

`doipatru.out`
```
1 
2 
1 
1 
```