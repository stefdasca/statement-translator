## Task

Miruna recently managed to bribe the public officials in Wonderland and thus gained the right to build the much-dreamed-of Tunnel of Terror in the amusement park. Miruna believes that once it opens, the tunnel will be the most important attraction in the park. It consists of several dark paths, which sometimes meet at intersections. It is known that there are $N$ such intersections, and $M$ dark paths connecting $2$ intersections. For each path, the time required to traverse it is known. The tunnel has $2$ doors through which you can enter or exit. These are located at intersections numbered $1$ and $N$. Initially, the brave ones who dare to try the tunnel will enter through the door at intersection $1$, and then this door will close behind them. Then, to exit, they must find the intersection numbered $N$. Once they reach intersection $N$ their journey ends, the door opens and they are forced to leave the tunnel. Because it is dark, they can barely see anything, and when they reach an intersection, there is an equal probability that they will continue their path on any of the paths that have one end in that intersection. Because she is a little and greedy girl, Miruna would like to know the average time required to traverse the paths from intersection $1$ to $N$. This way she could estimate her profits and how quickly she would recover the money invested in public officials.

## Input data

The input file `tunel.in` will contain $2$ integers $N$ and $M$, having the meaning given in the statement. The next $M$ lines will contain $3$ numbers $A$, $B$, and $C$, meaning that there is a bidirectional path between intersections $A$ and $B$ which takes $C$ minutes to traverse.

## Output data

In the output file `tunel.out` you will write a single real number representing the average time to traverse the paths from intersection $1$ to $N$. The result is accepted with an error of $0.001$.

## Constraints and clarifications

$2 \leq N \leq 255$

$N - 1 \leq M \leq 100000$

The time required to traverse any path is less than $1000$.

From intersection $1$ you can reach any other.

There may be several paths connecting the same intersections.

## Example

`tunel.in`

```
4 3
1 2 1
2 3 1
3 4 1
```

`tunel.out`

```
9
```