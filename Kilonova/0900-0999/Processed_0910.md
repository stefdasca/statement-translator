Sindbad discovered a container that holds a magical potion and an inscription describing how to open the gate of a temple. Following the instructions in the inscription, Sindbad reached a tunnel covered with square tiles, aligned to form rows and columns. The tunnel has several rows, and each row has $N$ tiles. The tiles in the tunnel are numbered starting from $1$, such that, traversing them row by row and each row from left to right, a strictly increasing sequence of consecutive natural numbers is obtained.

Sindbad is at the entrance, in front of the first row. To open the temple gate, he must reach the tile numbered $P$, stepping on a minimum number of tiles. If there are multiple such solutions, he will choose the one for which the total consumption of magical potion drops is minimal. During the journey, he must follow these rules:

* From the entrance, he can jump onto any tile in the first row without consuming magical potion;
* From a tile numbered $X$, Sindbad can jump either to the tile numbered $X + 1$, consuming **one drop** of magical potion, or to the tile numbered $2 \cdot X$, consuming **two drops** of magical potion.

# Task

Write a program that reads the values $N$ and $P$ as described in the statement and solves the following tasks:
1. Display the minimum number of tiles he must step on to open the gate;
2. Display the natural number $T$, representing the minimum number of magical potion drops required to open the gate.

# Input data

The input file `poarta.in` contains the first line a natural number $C$ representing the task from the problem that needs to be solved ($1$ or $2$). The second line contains the natural number $N$, and the third line contains the natural number $P$ as described in the statement.

# Output data

The output file `poarta.out` will contain a single line which will contain a natural number representing the answer to the task $C$.

# Constraints and clarifications

* $2 \leq N < 10\ 000$;
* $P$ is a non-zero natural number with at most $1\ 000$ digits; for a part of the tests, worth a total of $60$ points, $P$ has at most $18$ digits.
* The container holds a sufficient amount of magical potion.
* For solving task $1$, up to $60$ points can be awarded, and for solving task $2$, up to $30$ points can be awarded.

# Example 1

`poarta.in`
```
1
5
9
```

`poarta.out`
```
3
```

## Explanation

The tunnel has $5$ tiles in each row. Sindbad must reach the tile numbered $9$. The minimum number of tiles he must step on to reach tile $9$ to open the gate is $3$. From the entrance, he can jump:
- to the tile numbered $4$ (consumes 0 drops of magical potion);
- from the tile numbered $4$ to the one numbered $8$ (consumes $2$ drops of magical potion);
- from the tile numbered $8$ to the one numbered $9$ (consumes $1$ drop of magical potion).

# Example 2

`poarta.in`
```
2
5
9
```

`poarta.out`
```
3
```

## Explanation

In order to reach tile number $9$, he needs at least $3$ drops of magical potion.