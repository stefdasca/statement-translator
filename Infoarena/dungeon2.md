## Dungeon2

Dungeon Crawl: Paper Soup has just become the most popular game, and you are about to try it. The game takes place on a rectangular field with $N$ rows and $M$ columns, where each cell is one of the five types described below:
• free cell $'.'$ ;
• wall $'\#'$ ;
• cell with a coin $'o'$ ;
• cell with an explosive mine $'X'$ ;
• starting cell $'S'$ ;
It is guaranteed that on the first and last row and column there are walls (it is impossible to move through walls). The field may contain one or more starting cells. When the game starts, the player will initially be positioned in one of the starting cells marked with $'S'$. Since the game takes place in a cave system with limited visibility (see the name of the game), the player can only see a restricted visibility area, represented by a $3 \times 3$ square centered at their current position. Furthermore, in this visibility area, mines and start cells appear as free cells (they are invisible to the player). At each step, the player can move north, south, east, or west. If they reach a position with a coin, they collect the coin, and it disappears from the map. If they reach a position with a mine, the cave system collapses, the player loses all the coins collected up to that point, and the game ends. Fortunately, by following various guides on the internet, you have found the exact map of the field, but you do not know which of the starting points you will be assigned to - however, it is guaranteed that you will start from a start cell. Considering that you will adopt the best strategy, what is the maximum number of coins you can be guaranteed to obtain, regardless of where you start?

## Input Data

The first line of the input file $dungeon2.in$ contains the values $N$ and $M$: the dimensions of the field where the game will take place, according to the internet guides. The next $N$ lines each contain a string of length $M$, representing the map, according to the encoding described in the statement.

## Output Data

The output file $dungeon2.out$ will contain a single natural number, the maximum number of coins that can be guaranteed on that field.

## Constraints and Clarifications

Let $S$ be the number of start cells on the map.
$1 \leq S \leq 60$
$1 \leq N,M \leq 400$

Additionally:

## Constraints

1 
$3$
$S = 1$ . There are no mines. Except for the first and last rows and columns, there are no walls.

2 
$7$
$N = 3$

3 
$12$
$S = 1$

4 
$23$
$S = 2$

5 
$41$
$1 \leq N,M \leq 250$, $1 \leq S \leq 12$

6 
$14$
No additional constraints

## Example

`dungeon2.in` 
`dungeon2.out`
```
3 7 
#######
#Soooo#
#######
4
```
```
3 8
########
#SoXooS#
########
1
```
```
7 18
##################
#................#
#.o...SX.......o.#
#.o...X..X.....o.#
#.o.....XS.....o.#
#................#
##################
0
```
```
7 18
##################
#....#...........#
#.o...SX.......o.#
#.o...X..X.....o.#
#.o.....XS.....o.#
#.........#......#
##################
6
```
```
7 18
##################
#......X..S....oo#
##################
#..o..S.X......o.#
##########X#######
#o.....S...X.....#
##################
1
```

## Explanation

**Example 1**

There is a single start position, so we know exactly where the player will start. In this case, the player can collect all the coins.

**Example 2**

There are two start positions, and the player can deduce where they are positioned based on the visibility area ($*@*$ is the player's position):
```
###    ###
#@o    o@#
###    ###
```
The maximum number of coins the player can collect if they start on the left side is $1$, and $2$ if they start on the right side. So, in the worst case, we can collect one coin.

**Example 3**

In any direction the player initially moves, there is a mine in that direction in the worst case. The initial visibility area is:
```
...
.@.
...
```

**Example 4**

The player can figure out which cell they were initially placed in by analyzing the visibility area. More precisely, they look to see if they initially see a wall in the top-left or bottom-right; this way, they know exactly how to position themselves to avoid the mines. The initial visibility areas corresponding to the two positions are:
```
#..    ...
.@.    .@.
...    ..#
```

**Example 5**

The player moves $2$ steps to the left. If they see a coin to the left, they deduce they are in the middle area, collect it, and end the game. If not, they know they are not in the middle area, so they move to the right $4$ steps. Observing if there is a free space in the top-right (mines are seen as free spaces), they can deduce if they are in the top area or the bottom area. In both cases, they are free to collect the corresponding coin/coins. In the worst case, however, they will be able to collect only one coin. It can be observed that the player could not move initially to the right because they would risk hitting the center mine in the worst case.