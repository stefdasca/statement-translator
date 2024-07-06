Several boys, after a small football game, decided to join the girls' open volleyball game. The girls are seated in a circle and do not change places. A boy can join the girls' game only if he sits between two girls and is strictly taller than both of them.

# Task

Given the number of girls and their heights, in the order they are seated in the circle, the number of boys and their heights, determine the maximum number of boys that can join the game and the position each one will occupy on the circle.

# Input data

From the input text file `volei.in` read:

- The first line contains a natural number $n$, the number of girls in the game;
- The second line contains $n$ non-zero natural numbers separated by a space, representing the heights of the girls, in the order on the circle, clockwise, starting from any girl;
- The third line contains a natural number $m$, the number of boys wanting to join the game;
- The fourth line contains $m$ non-zero natural numbers separated by a space, representing the heights of the boys who want to join the game.

# Output data

In the output text file `volei.out` write:

- The first line contains a natural number $k$, representing the maximum number of boys who can join the game;
- The next line contains $n + k$ natural numbers, separated by a space, representing the heights of the volleyball players, in the order on the circle, clockwise, starting from the same girl in the input file, with boys' heights written in parentheses.

# Constraints and clarifications

* $1 \leq n, m \leq 2 \ 000$
* The heights of the girls and the boys do not exceed the value $1\ 000$.
* If there are multiple possibilities to insert $k$ boys into the game, only one will be written.
* If the heights do not seem plausible, you can consider they represent the intelligence coefficients of each person.
* 40 points are awarded for the correct value of $k$, and the full solution (maximum $k$ and the correct configuration of the $n + k$ heights of the players) is worth 100 points.

# Example 1

`volei.in`
```
4
15 11 72 31
3
20 50 25
```

`volei.out`
```
2
15 (20) 11 72 31 (50)
```

## Explanations

~[volei.png]

Another correct solution is:

$2$
$15 \ (25) \ 11 \ 72 \ 31 \ (50)$

# Example 2

`volei.in`
```
6
15 8 20 19 16 30
3
20 30 16
```

`volei.out`
```
3
15 (16) 8 (30) 20 19 (20) 16 30
```

## Explanations

Another correct solution is:

$3$
$15 \ (16) \ 8 \ 20 \ (30) \ 19 \ (20) \ 16 \ 30$;

# Example 3

`volei.in`
```
4
10 20 15 100
2
20 8
```

`volei.out`
```
0
10 20 15 100
```
