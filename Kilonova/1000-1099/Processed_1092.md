Ana and Bogdan are playing a new game – JBB ("Candy Jars Game"). On the game board, there are $N$ jars with candies. It is known how many candies are in each jar: in jar $i$ there are $B_i$ candies.

As usual, Ana starts the game, and then the two players take turns alternately. Being the first to move, Ana chooses a jar from which she will take all the candies. On the game board, there are arrows connecting the jars. More precisely, from each jar $i$ there is a single arrow pointing to another jar $j$. The arrows indicate how players move on the game board. If there is an arrow from jar $i$ to jar $j$, and a player took the candies from jar $i$, then their opponent is forced to move to jar $j$. If they find candies in jar $j$, they are obligated to take them all. If jar $j$ is empty, the opponent can choose another jar containing candies and continue the game.

Obviously, the goal of each player is to have, at the end of the game (when all jars have been emptied), as many candies as possible.

# Task

Determine the maximum number of candies that Ana could obtain while respecting the rules of the game. Of course, both Ana and Bogdan play optimally (meaning that at each step, each player will make the best move they can).

# Input data

The input file `jbb.in` contains on the first line the natural number $N$, representing the number of jars. The second line contains $N$ non-zero natural numbers separated by a space $B_1$, $B_2$, $\\dots$, $B_N$ representing the number of candies in each jar. The third line contains $N$ natural numbers separated by space $S_1$, $S_2$, $\\dots$, $S_N$, where $S_i$ represents the jar pointed to by the arrow starting from jar $i$.

# Output data

The output file `jbb.out` will contain a single line that contains a natural number representing the maximum number of candies that Ana can obtain.

# Constraints and clarifications

* $1 \\leq N \\leq 10 \\ 000$
* $1 \\leq B_i \\leq 1 \\ 000$, for any $1 \\leq i \\leq N$
* $1 \\leq S_i \\leq N$, $S_i \\neq S_j$, for any $1 \\leq i < j \\leq N$

# Example

`jbb.in`
```
8
3 1 8 20 7 5 6 10
6 5 7 4 3 8 2 1
```

`jbb.out`
```
36
```

## Explanation

**Ana moves first and chooses jar $7$ and takes $6$ candies.**
Bogdan is forced to move to jar $2$ and takes $1$ candy.

**Ana is forced to move to jar $5$ and takes $7$ candies.**
Bogdan is forced to move to jar $3$ and takes $8$ candies.

Ana is forced to move to jar $7$, but it is empty, so she can choose another full jar.
**Ana chooses jar $4$, from which she takes $20$ candies.**
Bogdan is forced to move to the same jar $4$, but it is already empty, so he can choose another full jar. Bogdan chooses jar $8$ from which he takes $10$ candies.

**Ana is forced to move to jar $1$ from which she takes $3$ candies.**
Bogdan is forced to move to jar $6$ from which he takes $5$ candies.

The game ends because all jars have been emptied.
Ana obtained a total of: $6$ + $7$ + $20$ + $3$ = $36$ candies.