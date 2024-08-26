Aby

It is said that once, long ago, in the ancient land of Lapestina there was a magic castle. Recently, the evil Rainbowdash from Rasiel kidnapped Princess Lolita, and our hero, Abu, is prepared to do anything to save her. After an epic journey with many adventures, Abu finally discovers that the princess is held prisoner by Rainbowdash in the last room of the aforementioned castle. The castle consists of $N$ rooms (numbered from $0$ to $N - 1$) and $M$ magical walls that connect these rooms. These walls are special and a person with strong willpower (like our hero) can pass through them, but only in a predetermined direction. Since our hero has a magical teleportation device called lucoj, he only needs to reach Lolita (located in room $N - 1$) by passing through walls starting from the first room (numbered $0$) and then his adventure will end as he returns home with the princess. Unfortunately for us, things get complicated. Rainbowdash found out about Abu's plan and, being a powerful magician, has the following trick to prevent him from reaching Lolita: Because he cast some magical spells, every time Abu passes through a wall, Rainbowdash is forced to choose a room and all the walls facing that room will change their magical direction. For example, let's say we have a castle with $3$ rooms. There is a wall from room $0$ to room $1$ and a wall from room $1$ to room $2$. Abu can only move from room $0$ to room $1$. After this, Rainbowdash can enchant either room $1$, in which case the direction of the walls from $0$ to $1$ and from $1$ to $2$ will change, or room $2$, in which case the direction of the wall from room $1$ to room $2$ will change. Notice that in this case, Abu cannot save the princess. On the other hand, if there is also a wall from room $2$ to room $1$, whatever Rainbowdash does, Abu can reach room $2$. Abu obtained in his travels $T$ maps, one of which definitely corresponds to the castle, but not being sure which one, he asks you to tell him for each if it is possible to save the princess, assuming the evil Rainbowdash makes no mistakes in his moves.

## Task

## Input data

The input file `aby.in` contains on the first line a number $T$ of tests, and on the following lines, for each test, we have: one line with the numbers $N$ and $M$ and then $M$ lines containing pairs of numbers $X$ and $Y$ indicating that there is a wall oriented from room $X$ to room $Y$.

## Output data

In the output file `aby.out` you will print $T$ lines, each line $i$ containing the answer for the configuration of test $i$, namely $1$ if Abu can reach the last room, otherwise $0$.

## Constraints

$1 \leq T \leq 10^3$

$2 \leq N \leq 12$

$0 \leq M \leq 150$

There is a blank line between tests.

There can be multiple walls between two rooms.

There can be walls with both ends in the same room.

After each move by Abu, Rainbowdash is forced to choose a room and enchant it.

Abu and Rainbowdash make their moves optimally.

Lolita does not have a passport.

## Example

`aby.in`  
```
5 
3 2 
0 1 
1 2 

3 3 
0 1 
1 2 
2 1 

5 9 
0 1 
1 2 
2 1 
1 3 
4 1 
3 2 
4 2 
3 4 
4 4 

6 16 
0 2 
0 3 
1 3 
1 4 
1 5 
2 0 
2 1 
2 3 
3 2 
3 4 
4 0 
4 1 
4 5 
5 1 
5 2 
5 3 

6 15 
0 1 
1 0 
1 5 
2 1 
2 3 
2 4 
3 1 
3 3 
3 5 
4 0 
4 1 
4 4 
4 5 
5 2 
5 4 
```

`aby.out`  
```
0 
0 
1 
1 
0 
```

## Explanation

The first two tests were explained in the statement, and in the 3rd one, Abu will move from $0$ to $1$, Rainbowdash will enchant room $3$, Abu will move from $1$ to $2$, Rainbowdash will enchant room $3$ again, then Abu will move from $2$ to $1 \dots$ and so on, thus Abu will never reach the last room.

In the 4th test, Abu will move into $2$, if Rainbowdash enchants room $2$, Abu will go to $5$, so he must enchant room $1$ (being doubly connected to $5$). From here Abu moves to $3$, from where whatever Rainbowdash does, Abu will win in at most 3 moves.

In the 5th test, Abu can wander between room $0$ and room $1$, each time he moves the wizard enchants room $5$, leaving Abu stuck.