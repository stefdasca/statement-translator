## Task

Fat-Frumos has to save Ileana Cosanzeana from the palace of the Evil Zmeu. However, Ileana does not want to be rescued, so they decide to play a game. If Ileana wins, she stays with Zmeu, otherwise she leaves with Fat-Frumos. The Zmeu's palace has $N$ rooms, with some pairs of rooms connected by corridors, such that from any room one can uniquely reach any other room. Initially, the lights are turned on in all the rooms. The two start the game in different rooms and will move alternately $\text{--}$ this is possible because both Ileana and Fat-Frumos have mobile phones. In a move, each character turns off the light in the current room they are in, chooses a neighboring room where the light is on, and moves there. Both Ileana and Fat-Frumos play optimally: if one of them has a strategy to secure victory regardless of the opponent's moves, they will follow it. Ileana will make the first move. The loser will be the one who cannot make any move anymore, meaning the light is off in all adjacent rooms to the room where they are. In other words, the winner is the one who moves last. Since the author of the story does not know which rooms the two characters start in, you will need to determine, considering all possible initial positions, how many games Ileana Cosanzeana will win. 

## Input data

The input file `trigame.in` contains on the first line the value of $N$. The next $N -1$ lines contain two different natural numbers $a$ $b$, with values between 1 and $N$, signifying that there is a corridor between rooms $a$ and $b$. 

## Output data

The output file `trigame.out` will contain a single number, representing the number of games Ileana Cosanzeana will win. 

## Constraints and clarifications

$2 \leq N \leq 2048$ 

For 40% of the test data, $2 \leq N \leq 64$ 

For another 20% of the test data, $2 \leq N \leq 256$ 

## Example

`trigame.in` 

`5 1 2 2 3 2 4 1 5` 

`trigame.out` 

`12` 

## Explanation

Out of the 20 possible games, Ileana will win 12 games, the ones in which the initial positions are: (1, 3) (1, 4) (1, 5) (2, 3) (2, 4) (2, 5) (3, 1) (3, 4) (3, 5) (4, 1) (4, 3) (4, 5) $\text{--}$ the first number in the pair is Ileana's position, the second is Fat-Frumos' position. For example, for (3, 5), Ileana will move to room 2, Fat-Frumos to room 1, and the last move will be Ileana's, who will move to room 4, winning the game.