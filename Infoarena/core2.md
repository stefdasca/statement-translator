## Task

You have just bought a processor with $2$ cores, hoping that your favorite games will run much better (higher dynamism, better graphics quality, etc.). Being eager to test the new processor, you want to play all the $N$ favorite games as soon as possible. The games are numbered from $1$ to $N$ and for each game $i$ the duration of the game $d_i$ and the satisfaction brought $s_i$ are known. You'll quickly find that although the processor is more technologically advanced, your favorite games are not able to fully use the new capabilities. Thus, the games from $1$ to $X$ can only be run on core $1$, while the games $X+1,\dots,N-1$ can only be run on the second core. Game $N$ is special and requires the parallel use of both cores. Knowing that at any given time no more than one game can be executed on one core and that you don't mind playing two games in parallel (one on each core), and that you only have the time interval $[0,T]$ available (after which you have to go to school), determine which games you will play so that the total satisfaction obtained is maximized. An additional constraint is given by the fact that in the time interval $[T_{1,N}, T_{2,N}]$, your best friend will visit, and you want to impress him; therefore, if you decide to play game $N$ (the special one), you will only do so in the presence of your friend (in other words, game $N$ can only be played in an interval of time completely included in $[T_{1,N}, T_{2,N}]$). A game contributes to the total satisfaction only if it is played entirely within the available time interval.

## Input data

The first line of the input file `core2.in` contains $3$ integers: $N$, $X$, and $T$. The next $N-1$ lines contain two integers each, $d_i$ and $s_i$, representing the duration of game $i$ and the satisfaction caused by it (the $i$-th of these lines corresponds to game $i$). The last line contains $4$ integers, separated by a space: $d_N$, $s_N$, $T_{1,N}$, $T_{2,N}$.

## Output data

In the output file `core2.out` you will print a single number, representing the maximum total satisfaction you can obtain by playing games within the available time interval.

## Constraints

$3 \leq N \leq 50$

$1 \leq X \leq N-2$

$1 \leq d_i \leq T \leq 1000$

$0 \leq T_{1,N} < T_{2,N} \leq T$

$1 \leq d_N \leq T_{2,N} - T_{1,N}$

$1 \leq s_i \leq 1000$

Once started, a game has to be played until the end (in other words, if you choose to play game $i$, it must be played for a time interval of duration $d_i$).

The time interval in which you play a game $i$ $(1 \leq i \leq N)$ must be completely included in the interval $[0,T]$.

The time interval in which you play game $N$ (if you play it) must be completely included in the interval $[T_{1,N}, T_{2,N}]$.

## Example

`core2.in`
```
7 3 70 
16 20 
29 13 
41 32 
23 8 
17 19 
66 2 
20 30 14 60 
90
```

## Explanation

Games $1, 2$ and $3$ can only be run on core $1$, while games $4, 5$ and $6$ can only be run on core $2$. Game $7$ requires both cores in parallel. The maximum total satisfaction equal to $90$ is obtained as follows: you will play game $1$ in the interval $[0,16]$, game $7$ in the interval $[17,37]$, game $2$ in the interval $[37,68]$, game $5$ in the interval $[0,17]$ and game $4$ in the interval $[37,60]$. The total satisfaction is $s_1 + s_2 + s_4 + s_5 + s_7 = 20 + 13 + 8 + 19 + 30 = 90$. Note that in the interval $[17,37]$ (when you play game $7$), no other game is played on either of the $2$ cores, as they are exclusively used by game $7$.