After visiting all the tourist attractions in the city of Iași, Ioana and Maria invented a game. They have $n$ boxes arranged in a straight line, numbered from $1$ to $n$, and $m$ balls that can be placed in some of these boxes. Some boxes are damaged, so the balls disappear if they are placed in those boxes. A move consists of choosing a ball and positioning it in one of the neighboring boxes (the previous or the next box). The balls can be moved according to the following rule: when a ball is moved in a certain direction for the first time, then the ball keeps the direction of movement for subsequent moves (for example, if a ball is moved to the left for the first time, then any subsequent moves of this ball can only be to the left). The game ends when no player can make any move. The first player who cannot make a move loses. The girls play $T$ such games.

# Task

Knowing that Ioana is the first to move, and then the girls move alternately, determine for each of the $T$ games if she has a guaranteed winning strategy.

# Input data

The file `cutie.in` contains on the first line a natural number $T$, which represents the number of games the two girls play. The following lines contain, in order, the description of the $T$ games. Each game is described by $3$ lines: the first line will contain, in order, three natural numbers $n,k,m$ separated by a single space ($n$ represents the number of boxes, $k$ represents the number of damaged boxes and $m$ represents the number of balls), the second line will contain $k$ natural numbers, separated by a single space, representing the indices of the damaged boxes, and the third line will contain $m$ natural numbers representing the indices of the boxes that contain balls at the beginning of the game.

# Output data

The file `cutie.out` will contain on the first line a string of $T$ values of $0$ and $1$ not separated by spaces, having the following meaning: the value at position $i$ in the string $(i \in \{ 1,2, \ldots ,T \})$ is $1$ if the game $i$ is won by Ioana or $0$ if the game $i$ is lost by Ioana.

# Constraints and clarifications

* $1 \leq T \leq 10$
* $1 \leq n, m \leq 10 000$
* $0 \leq k \leq 10 000$
* It is assumed that a ball cannot be moved to the left from the first box or to the right from the last box
* Initially, no ball is in the first box, the last box or a damaged box
* In the input file, the positions of the balls and the positions of the damaged boxes are sorted in ascending order
* Multiple balls can be in one box
* For $20\%$ of the tests, $k$ has the value $0$ or $1$

# Example

`cutie.in`
```
2
10 1 1
6
3
10 1 2
5
4 4
```

`cutie.out`
```
10
```

# Explanation

For the first game, Ioana has a guaranteed winning strategy (to win she will move the ball to the right), and for the second game, she does not have a guaranteed winning strategy.