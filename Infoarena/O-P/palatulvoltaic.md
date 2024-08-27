## Task

Tanaka has decided to visit the place where all the electricity in the universe comes from, namely, the Voltaic Palace. We can model the Voltaic Palace as a tree with $N$ nodes, where the nodes represent the palace towers, and the edges represent the palace corridors. In each room, a sport is played, and the steps of the matches in that sport provide electricity to the Voltaic Palace. It is known that for the sport in room $i$, you make exactly $v_i$ steps in a match. Once in a room, you can play any number of matches of the sport in that room. Tanaka also has a pedometer (a device that measures how many steps you take), which can count up to $K$ steps. More precisely, the moment Tanaka takes the $K+1$ step, it resets and starts again from 0 (like a car's odometer). During his visit, Tanaka starts his journey from a node $x$ chosen by him. Then, the palace organizers will give him a number $d$ chosen uniformly at random between $0$ and $N-1$. Tanaka then visits all nodes at a distance of at most $d$ from $x$, playing or not playing matches in those rooms. He will choose the matches he participates in such that at the end of his visit, the number of steps shown by his pedometer is maximized. Tanaka wants to know, for each possible value of $x$ from $1$ to $N$, what is the average value of the maximum number of steps his pedometer can show, taking into account that $d$ is chosen uniformly at random between $0$ and $N-1$. Can you calculate these values?

## Input data

The input file `palatulvoltaic.in` will contain, on the first line, the numbers $N$ and $K$. Then, on the next line, $N$ numbers, the values of $v$. On the following $N-1$ lines, each will contain a pair $a$, $b$, representing an edge from node $a$ to node $b$.

## Output data

In the output file `palatulvoltaic.out`, the values requested by Tanaka in order, for $x$ from $1$ to $N$. If a requested average can be written as the irreducible fraction $\frac{P}{Q}$, then it must be printed as $P \cdot Q^{-1} \mod (10^9 + 7)$, where $Q^{-1}$ is the modular inverse of $Q$ modulo $10^9 + 7$.

## Constraints and clarifications

- $1 \leq N \leq 300,000$
- $1 \leq v_i , K \leq 1,000,000,000$
- For 10 points, $N \leq 20$ - feedback tests 1, 3.
- For another 30 points, $N \leq 1,000$ - feedback tests 6, 13, 18.
- For another 10 points, $K$ is chosen uniformly at random between $1$ and $1,000,000,000$, and the values of $v$ are chosen uniformly at random independently between $1$ and $K$ - feedback tests 21, 24.
- The rest of the feedback tests are part of the largest tests

## Example

`palatulvoltaic.in`
```
5 11
1 2 3 4 5
1 2
2 3
3 4
3 5
```

`palatulvoltaic.out`
```
11
600000015
200000012
800000016
11
```

`palatulvoltaic.in`
```
5 11
2 4 5 6 3
1 2
2 3
3 4
4 5
```

`palatulvoltaic.out`
```
200000012
800000016
11
10
400000013
```