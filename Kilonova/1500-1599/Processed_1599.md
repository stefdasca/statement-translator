
Ionuț, a young programmer, is entering the computer game developers' market. The game he designed is called RGB. In the game, there are $N$ alien characters. Since Ionuț does not agree with the theory of green little men, his characters come in three colors:

* $R$ red aliens;
* $G$ green aliens;
* $B$ blue aliens.

Each alien has a certain power, expressed as an odd natural number, with the powers of any two aliens being different. During the game, each alien will fight every other alien. The result of a fight between two aliens depends on their power and their color. In a fight between two aliens of the same color, the one with the greater power wins. In a fight between two aliens of different colors, their powers are modified as follows, and after the modification, the alien with the greater power wins:

* The power of a red alien is doubled if the opponent is a green alien.
* The power of a green alien is doubled if the opponent is a blue alien.
* The power of a blue alien is doubled if the opponent is a red alien.

After each fight, the aliens' powers return to their initial values, in case they were modified.

# Task

Write a program that, knowing the colors and powers of the aliens, solves the following two tasks:
1. Determine the power of the alien that wins the most fights; if there are multiple such aliens, the minimum power will be displayed.
2. Determine for each alien the number of fights they have won.

# Input data

The input file `rgb.in` contains on the first line four natural numbers $C, R, G$ and $B$, where $C$ is the task that needs to be solved ($1$ or $2$), $R$ represents the number of red aliens, $G$ the number of green aliens, and $B$ the number of blue aliens.
The second line contains $R$ odd natural numbers in strictly increasing order, representing the powers of the $R$ red aliens.
The third line contains $G$ odd natural numbers in strictly increasing order, representing the powers of the $G$ green aliens.
The fourth line contains $B$ odd natural numbers in strictly increasing order, representing the powers of the $B$ blue aliens.
The values on the same line are separated by a space.

# Output data

For $C = 1$, the output file `rgb.out` will contain a single line with the power of the alien that wins the most fights; if there are multiple aliens that win a maximum number of fights, the minimum power will be displayed.

For $C = 2$, the output file `rgb.out` will contain three lines. The first line will contain the number of fights won by each red alien. The second line will contain the number of fights won by each green alien. The third line will contain the number of fights won by each blue alien. For each color, the values will be displayed considering the order of the aliens in the input file. The values on the same line will be separated by a space.

# Constraints and clarifications

* $N = R + G + B$;
* $1 \leq R, G, B \leq N-2$;
* $1 \leq$ the power of any alien $\leq 2 * N - 1$;

|#|Score|Constraints|
|-|-|--------|
|1|21|$C = 1$ and $N \leq 500\ 000$|
|2|18|$C = 2$ and $N \leq 1\ 000$|
|3|25|$C = 2$ and $1\ 000 \leq N \leq 100\ 000$|
|4|36|$C = 2$ and $100\ 000 \leq N \leq 500\ 000$|

# Example 1

`rgb.in`
```
1 1 2 2
3
1 7
5 9
```

`rgb.out`
```
7
```

## Explanation

$C = 1$, therefore the first task will be solved. There is one red alien with power $3$, two green aliens with powers $1$ and $7$, and two blue aliens with powers $5$ and $9$. The alien with power $7$ is the only one who will win the most fights (in this case, all of them):

* When fighting the green alien with power $1$, it wins because it has greater power.
* When fighting the red alien with power $3$, the red alien will double its power (to $6$), but it will still be insufficient to win the fight.
* When fighting the blue alien with power $9$, its power will be doubled (to $14$), therefore it will also win this fight.

# Example 2

`rgb.in`
```
2 1 2 2
3
1 7
5 9
```

`rgb.out`
```
1
0 4
2 3
```

## Explanation

$C = 2$, therefore the second task will be solved.

* The alien with power $3$ can win only one fight (against the alien with power $1$).
* The alien with power $1$ cannot win any fights.
* The alien with power $7$ can win all the fights (see the explanation in the previous example).
* The alien with power $5$ can win two fights (against the aliens with powers $1$ and $3$).
* The alien with power $9$ can win $3$ fights (against the aliens with powers $1, 3$ and $5$).
