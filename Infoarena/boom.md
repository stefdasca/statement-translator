Boom

Let's guess who is the protagonist of this problem. It is not very hard to imagine that his name will also be Petrică. What he is doing this time is quite unique: he is playing with the crafty rat. The latter is located in an underground gallery that presents itself as a succession of $N$ rooms arranged in a line and which are numbered from $1$ to $N$ in order of their traversal from one end to the other. Petrică does not know where the rat is located but wants at any cost to wipe it off the face of the earth. Thus, he can detonate poisonous bombs in some of the rooms of the gallery (sometimes even in several simultaneously) to kill the rat. If the rat is in one of the gassed rooms, it dies instantly; if not, the room is undamaged and the rat can move through it immediately after the bomb is detonated. Here's how things stand: the two enemies play fairly, so after Petrică detonates a set of bombs that will explode simultaneously, if the rat has not died, it will move to one of the adjacent rooms to the one it is in (the rooms at the ends have only one adjacent room). Petrică has devised an attack plan consisting of $M$ barrages. For each barrage, the cost of implementing it and the gassed rooms if it is put into practice are known. At each step, Petrică will choose only one of the $M$ barrages to gas certain rooms.

## Task

Help Petrică find a minimum-cost strategy by which the rat will be killed regardless of its initial position.

## Input Data

The first line in the input file boom.in contains two integers separated by a single space $N$ and $M$, representing the number of rooms in the gallery and the number of barrages. The next $M$ lines contain the information regarding each barrage (they are numbered from $1$ to $M$ in the order they are found in the input file). Thus, each line contains two integers $P$ and $Q$, representing the cost and the number of gassed rooms in the barrage. Following are $Q$ numbers ($Q$ is not greater than $4$) representing the gassed rooms.

## Output Data

The first line in the output file boom.out will contain an integer representing the minimum cost of a strategy by which the rat will be dead. The next line contains a number $T$ representing the number of barrages that will surely kill it. The following $T$ lines contain the numbers of the barrages used by Petrică (these are given in the order they were used).

## Constraints and clarifications

$1 \leq N \leq 20$

$1 \leq M \leq 50$

The rat cannot stay in place

If there are multiple solutions with the same minimum cost, any of them can be displayed

A barrage can be used multiple times

## Example

boom.in 
```
3 2
1 2 1 3
2 1 2
```
boom.out 
```
2
2
1 1
```

## Explanation

Petrică detonates barrage 1 twice. Wherever the rat is, it will die: if it is in room $1$ or $3$, it will die after the first gassing; if it is in the second room, it will be forced to move to one of rooms $1$ and $3$ in the next step, thus being caught by the second gassing. The total cost is $2$, the lowest possible.