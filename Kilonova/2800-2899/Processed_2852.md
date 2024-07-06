# Task

RAU-Gigel is testing a game involving draws and prizes. The game consists of a series of actions that occur at specific moments in time. The actions can be: (1) the appearance of prizes or (2) draws. Prizes appear at certain heights for a well-defined time interval. Draws occur at specific moments in time and propagate instantaneously in space. RAU-Gigel earns one point for each prize hit.

Unfortunately, RAU-Gigel did not calibrate his shooter well, so each draw becomes active only between two given heights: $[ h1, h2 ]$, an interval called the range. Thus, RAU-Gigel will only earn points for the prizes within the range of each draw.

If a draw occurs exactly at the same moment a prize appears within its range, it is considered "hit." Similarly, if a prize is scheduled to disappear at a moment when a draw occurs and it is within the range of the draw, then the point is considered won. A hit prize remains in the game and can generate additional points until the moment it is scheduled to disappear. There cannot be two draws at the same moment, but there may be multiple prizes at the same height at the same time, and all can generate points.

Given the number $N$ of type $1$ or $2$ operations, where:

* Operation $1 \\ t \\ d \\ h$ – represents a prize: $t$ is the moment it appears, $d$ is the number of time units it is scheduled to exist, and $h$ is the height at which it appears;
* Operation $2 \\ t \\ h1 \\ h2$ – represents a draw, $t$ is the moment it occurs, and $h1$ and $h2$ represent the heights at which the draw is active (range).

Determine how many points RAU-Gigel earns for each draw and what his final score is when the game ends.

# Input data

The input file `lasere.in` contains:
- The first line contains a natural number $N$. 
- The next $N$ lines contain the operations, in increasing order of the moment $t$ starts, of type $1$ and $2$, in the form:

* $1 \\ t \\ d \\ h$, where $t$, $d$, $h$ are $3$ natural numbers separated by a space, with the above significance, representing a type $1$ operation;
* $2 \\ t \\ h1 \\ h2$, where $t$, $h1$, $h2$ are $3$ natural numbers separated by a space, with the above significance, representing a type $2$ operation.

# Output data

The output file `lasere.out` will contain the answers, in the order requested, for the type $2$ operations, one per line, and on the last line, RAU-Gigel's score at the end of the game.

# Constraints and clarifications

* $2 \\leq N \\leq 100 \ 000$
* $1 \\leq t, d, h, h1, h2 \\leq 1 \ 000 \ 000 \ 000$, $h1 < h2$

# Example 1

`lasere.in`
```
4
1 2 8 4
2 3 5 10
1 5 6 7
2 8 3 8
```

`lasere.out`
```
0
2
2
```

## Explanation

There are $4$ actions, of which $2$ are draws (type $2$). In the first draw RAU-Gigel does not hit the only prize existing at the moment of the draw (moment $3$) because it is not within his range.

In the second draw, at moment $8$, RAU-Gigel hits both prizes.

Total: $0+2=2$.

# Example 2

`lasere.in`
```
6
2 2 4 5
1 2 8 4
2 3 5 10
1 5 6 7
2 10 4 8
1 10 3 7
```

`lasere.out`
```
1
0
3
4
```

## Explanation

There are $6$ actions, of which $3$ are draws. At moment $2$ there are $2$ actions: a draw and the appearance of a prize. Because the prize, located at height $4$, is within the range of this draw, namely in the interval $[ 4-5 ]$, RAU-Gigel earns one point.

In the second draw, he hits nothing, the only existing prize at that moment being outside his range.

In the third draw, RAU-Gigel earns $3$ more points, those prizes being within the range of the draw (interval $4-8$). The first prize, scheduled to exist until moment $10$, which is also the moment of the draw, is also counted. The last prize, appearing exactly at the moment of the draw, is also counted.

Total: $1+0+3=4$.