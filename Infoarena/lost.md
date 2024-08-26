Lost

## Task

An astronaut from ASR (Romanian Space Agency) was "left behind" on the $N$-th level of a Romanian space station. He wants to descend to level 1, where the communication devices are located, so he can contact a spaceship to pick him up. Unfortunately, the astronaut doesn’t know how much time the spaceship would take to reach the station; therefore, the astronaut wants to gather as much space food as possible before calling the spaceship. Each level of the space station has $16$ rooms, arranged in a matrix with $4$ rows and $4$ columns (rows are numbered from $1$ to $4$; the same for columns). Each room contains a certain amount of space food. The astronaut can move freely inside the space station, but he cannot visit the same room twice. Moreover, once he descends to a lower level, he cannot go back up to a higher level. Each day, from the room he is currently in, the astronaut can move north, south, east, or west relative to the current room (on the same level) or down to the lower level, in the room on the same row and column as the current room. Moving down is only allowed if there is a door to the lower level in the current room. For each level, the astronaut has a map showing which rooms have doors to the level below. The astronaut does not stay in the same room for two consecutive days and moves only once per day. Each time he enters a room, the astronaut takes the amount of space food located in that room. The ration of food for an astronaut is defined as the ratio between the total amount of space food collected during his walk through the station and the number of days spent inside the space station before calling the spaceship. It is considered that the astronaut spends the first day in the room where he starts his journey, on level $N$, and takes the amount of food from that room. Determine a sequence of moves for the astronaut that will bring him from the room where he initially is, on level $N$, to a room on level $1$. This sequence of moves should maximize his food ration. The astronaut's walk through the station does not have to end immediately when he reaches a room on level $1$. He can walk through multiple rooms on level $1$ before ending his journey and calling the spaceship.

## Input data

The first line of the input file `lost.in` contains a single integer $N$, representing the number of levels of the space station. Then follow the descriptions of the $N$ levels, in order, from level $N$ to level $1$. For each level, there will be $8$ lines in the input file. The first $4$ lines contain $4$ integers each, separated by a space, representing the quantity of space food available in each room on that level (the $j$-th number on the $i$-th line among the $4$ will represent the amount of food in the room on row $i$ and column $j$). The next $4$ lines will contain $4$ integers each, separated by a space, having values $0$ or $1$. $1$ means that there is a door from that room to the level below, and $0$ means there is no door. Level $1$ will have only $0$ values on these $4$ lines. The last line of the file contains $2$ integers, $l$ and $c$, representing the row and column of the room on level $N$ where the astronaut initially is.

## Output data

The first line of the output file `lost.out` will contain the maximum food ration the astronaut can obtain, with $4$ decimal places. The second line will contain the length of his path (print $0$ if the astronaut doesn’t leave the room he initially is in). If the length of his path is $L$ $(L > 0)$, then the third line will contain $L$ characters from the set $\{'N','E','S','W','D'\}$, each character corresponding to a movement direction (north, east, south, west, and down). If there are multiple paths with the same maximum food ration, you can print any of them.

## Constraints and clarifications

$1 \leq N \leq 16$

The amount of space food in a room is between $1$ and $255$, inclusive.

If $L$ is the length of the astronaut's path, then he spends $L+1$ days inside the space station before calling a spaceship.

For each test, the astronaut will be able to reach a room on level $1$ from the room where he initially is.

## Example

`lost.in`

```
2 
1 20 1 1 
1 1 1 1 
1 1 1 1 
1 1 1 1 
1 
1 
1 
1 
0 0 0 0 
0 0 0 0 
0 0 0 0 
0 0 0 0 
1 1 1 1 
20 1 1 1 
1 1 1 1 
1 1 1 1 
1 1 1 1 
0 0 0 0 
0 0 0 0 
0 0 0 0 
0 0 0 0 
1 1 
```

`lost.out`

```
8.6000 
4 
EDSW
```