To take a well-deserved break from cleaning, Hetty went on a trip to Praid to visit the local salt mine. The salt mine consists of $N$ rooms interconnected by $M$ bidirectional tunnels. Hetty noticed that in each room $i \\ (1\\leqi\\leqN)$, there is a sign indicating the number $P_i$ of the room towards which visitors should head in case of an emergency evacuation. Therefore, we say that a room $i$ can be evacuated through a room $k$ if and only if one of the following conditions is true:

1. Room $i$ is the actual room containing the exit $(i=k)$.
2. Room $P_i$ can be evacuated through room $k$ and there is a direct tunnel between rooms $i$ and $P_i$.

Currently, it is known that all rooms in the salt mine can be evacuated through room $X$. However, this is about to change because the salt mine owners want to close the exit from room $X$ and open another one in room $Y$. For the salt mine to reopen, the owners need to change some of the signs $P_i$. A sign in a room $i$ needs to be changed if the number $P_i$ written on it needs to be modified so that room $i$ can be evacuated through room $Y$. Hetty now wonders what is the minimum number of signs that need to be changed to evacuate all the rooms in the salt mine through room $Y$, for every $Y$ from $1$ to $N$.

# Task

# Input data

The input file `evacuare.in` contains on the first line $3$ natural numbers, $N, M,$ and $X$ representing the number of rooms, the number of tunnels in the salt mine, and the room that initially contains the exit. The next $M$ lines contain two natural numbers each, representing a pair of rooms that are connected by a direct tunnel. The last line contains $N$ natural numbers. The $i$-th of these represents the number $P_i$ written on the sign found in room $i$.

# Output data

In the output file `evacuare.out` will contain $N$ lines. The $i$-th line will contain the minimum number of signs that need to be changed so that the salt mine can be evacuated through room $i$.

# Constraints and clarifications

* $2 \\leq N \\leq 500 \\ 000$
* $1 \\leq M \\leq 600 \\ 000$
* For $20\\%$ of the tests $M = N-1$.
* For $30\\%$ of the tests $2 \\leq N \\leq 2 \\ 000$
* There is no tunnel that connects a room to itself.

# Example

`evacuare.in`
```
4 4 3
1 2
2 3
2 4
3 4
2 3 4 3
```

`evacuare.out`
```
2
1
0
0
```

## Explanation

To evacuate the salt mine through room $1$, we'll need to change the number $P_2$ from $3$ to $1$ and $P_3$ from $4$ to $2$.

Thus, we can evacuate the $4$ rooms through the routes:

* $1: 1$
* $2: 2 \rightarrow 1$
* $3: 3 \rightarrow 2 \rightarrow 1$
* $4: 4 \rightarrow 3 \rightarrow 2 \rightarrow 1$

We notice that we could also change $P_4$ to $2$ to evacuate room $4$ via route $4 \rightarrow 2 \rightarrow 1$, but this option does not lead to the minimum number of signs changed.