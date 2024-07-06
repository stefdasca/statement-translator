## Lensu was challenged by Buzdi and Cosmin to play a game called "Linked". This game takes place in a palace with $N$ rooms, numbered from 1 to $N$, connected by $M$ one-way doors, such that you cannot return to a room you have already been in during the game. This game consists of $N$ rounds, played as follows:

* In round `i`, Lensu will be placed in a different starting room from those in the last `i - 1` rounds and will be blindfolded.
* He must go through at most $L$ doors.
* During the game, Lensu can say "STOP", at which point, if he is in room $N$, he is the winner and the game ends. If he is not in room $N$, he will move to the next round.

If Lensu is not the winner after the $N$ rounds, he loses the game.

# Task

Lensu wants to make a bet with Buzdi and Cosmin. To know how much to bet, he wants to find out what the probability of winning the game is.

# Input data

The first line contains the natural numbers $N$, $M$, and $L$. The next $M$ lines contain two natural numbers `x y`, separated by a space, indicating that there is a door leading from room `x` to room `y`.

# Output data

Print a single natural number $P$, representing the probability that Lensu will win the game. This number will be printed modulo $1 \ 000 \ 000 \ 007$.

# Constraints and clarifications

* $2 \leq N \leq 100 \ 000$
* $1 \leq M \leq 500 \ 000$
* $1 \leq L \leq 100$
* $P = \frac{nr \ cazuri \ favorabile}{nr \ cazuri \ posibile}$
* The probability $P$ is a fraction $\\frac{a}{b}$ expressed as $a \\times b^{-1}$, where $b^{-1}$ is the modular inverse of $b$ modulo $1 \ 000 \ 000 \ 007$.
* Lensu does not necessarily play optimally; he only knows how many doors he has opened.
* For 21 points, $2 \leq N \leq 100, 1 \leq M \leq 200$

# Example

`stdin`
```
8 10 3
6 2
4 2
2 8
3 8
2 3
1 3
7 4
4 5
1 6
1 7
```

`stdout`
```
305555558
```

## Explanation

There are $11$ situations where he reaches room $8$ and says "STOP" after going through at most $3$ doors. In each situation, he will pass through the rooms in the order:

* $(8)$
* $(2, 8)$
* $(3, 8)$
* $(1, 3, 8)$
* $(6, 2, 8)$
* $(4, 2, 8)$
* $(2, 3, 8)$
* $(6, 2, 3, 8)$
* $(4, 2, 3, 8)$
* $(7, 4, 2, 8)$
* $(1, 6, 2, 8)$

The total number of situations where he passes through at most $3$ doors and says "STOP" in one of the rooms is $36$. Therefore, the probability that Lensu wins is $\\frac{11}{36}$, and $\\frac{11}{36}$ modulo $1 \ 000 \ 000 \ 007$ = $305555558$