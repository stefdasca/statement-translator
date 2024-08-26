# Bibel

Miruna's birthday is approaching, and her friend Bibel wants to give her a set of marbles so that she doesn't have to borrow her brother's marbles anymore. Since Bibel has only a single 50 bani coin in his pocket, he thinks about gambling it at the casino. Bibel's favorite game is quite simple. It consists of multiple game levels, and at each level, Bibel must collect several marbles on the table using a hook. At the beginning of each level, new marbles are placed on the table. A level ends when all marbles on the table have been collected. What Bibel can do is move the hook in a straight line from its current position above a marble and pick up the marble from the table. Initially, the hook is at the origin, $(0, 0)$. The time needed to collect a marble is negligible. The time needed to move the hook is equal to the square of the distance between the initial and final points (adjusting the unit of measure accordingly). Since the final score depends on how quickly Bibel finishes the game, Bibel wants to know the minimum total time at the end of each level if that level were the last and he played optimally (see the example). Help Miruna receive her gift.

## Input Data

The input file `bibel.in` contains a description of a game. Each level is described through multiple lines. The last line in the description of a level contains a single number, $1$, and the other lines describe the coordinates of each marble that will be placed on the table at the beginning of the level. The format is `0 x y` where $(x, y)$ represents the coordinates in the plane of a marble. The last line in the file contains a single number $2$ and marks the end of a game.

## Output Data

The output file `bibel.out` will print a number for each level, having the meaning described in the task.

## Constraints and clarifications

The coordinates of the marbles are integers $0 \leq x, y \leq 10000$

The maximum number of marbles placed on the table at the beginning of a level is $\leq 17$

The total number of lines in the input file is $\leq 200$

The order in which the marbles are picked up from the table does not matter, but at the end of each level, the table should be empty.

## Example

`bibel.in` `bibel.out`
```
0 0 2 
0 2 0 
2 2 1 
0 4 4 
0 6 6 
0 8 8 
1 2 
```
```
12 
40
```

## Explanation

The best way to finish the first level would be to pick up the marbles from the positions $(0, 2)$, $(2, 2)$, $(2, 0)$. The best way to finish the second level in minimum time would be to pick up the marbles from the positions $(0, 2)$, $(2, 0)$, $(2, 2)$ (end of the first level), $(4, 4)$, $(6, 6)$, $(8, 8)$ (end of the second level and game).