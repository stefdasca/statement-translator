Ioana and Maria have just learned about multiples of a natural number in mathematics. To practice working with the new concept, they decide to play the following game: each chooses a nonzero natural number and for a given closed interval (in closed intervals, the endpoints are part of the interval), they calculate how many multiples their chosen number has in that interval. The winner is the one who has chosen the number with more multiples in the given interval, or it is a tie if the number of multiples is the same.

# Task

Knowing the numbers chosen by the two girls as well as the numbers that determine the given intervals, determine who wins the game and which number leads to winning the game.

# Input data

The keyboard contains six values: $x$, $a$, $b$, $y$, $c$, $d$, which represent, in order, the number chosen by Ioana and the endpoints of her interval, the number chosen by Maria and the endpoints of her interval.

# Output data

The screen will contain the name of the girl who wins and a value $P$ that represents the number which leads to winning the game, separated by a space. In case of a tie, print `Tie` followed by a space and the equal number of multiples.

# Constraints and clarifications

* $1 \leq x, y \leq 1\ 000\ 000$
* $1 \leq a, b \leq 1\ 000\ 000\ 000$
* $1 \leq c, d \leq 1\ 000\ 000\ 000$

# Example

`stdin`
```
7
9
30
9
60
20
```

`stdout`
```
Maria 4
```

## Explanation

$7$ has three multiples in the interval $[9, 30]$: $\{14, 21, 28\}$. $9$ has four multiples in the interval $[20, 60]$: $\{27, 36, 45, 54\}$. Therefore, the number chosen by Maria is the winner, having $4$ multiples in the given interval.