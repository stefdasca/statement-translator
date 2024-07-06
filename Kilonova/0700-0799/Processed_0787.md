Nicușor is a 6th-grade student who thought he was old enough to invent a new game. He only has a sheet of paper and a pen. First, he writes $n$ natural numbers in a circle. These form the ***Number Roulette***. The game proceeds according to the following rules:

* The sequence of numbers is traversed in the direction of the clock’s hands;
* It always starts from the same element;
* Each time a complete rotation is performed;
* Each non-zero element is subtracted from the immediately following element only if it is less than or equal to it and non-zero;

**Example.** If we denote with $R_1, R_2, R_3, R_4, R_5, R_6, R_7, R_8$ the sequence of numbers that form the roulette in figure $1$, then, a complete rotation makes the following changes to the numbers in the list:

~[ruleta1.png|width=35em] ~[ruleta2.png|width=23em]

* The roulette stops when a complete rotation is executed, and no value in the sequence of elements is changed.

**Example.** For the roulette in figure $1$, $4$ rotations are executed (of which $3$ make changes):

~[ruleta3.png]

# Task

Write a program to determine, for a sequence of $n$ natural numbers indicating the initial state of the roulette, the number $r$ of complete rotations performed according to the game rules until its completion and the number $t$ of non-zero elements in the sequence at the end of the game.

# Input data

The input file `ruleta.in` contains the number $n$ of natural numbers arranged in a circle on the first line, and on the second line, separated by spaces, the $n$ values, in the direction of movement, starting with the element from which the roulette begins.

# Output data

The output file `ruleta.out` contains on the first line, separated by a space, the values $r$ and $t$ (in this order).

# Constraints and clarifications

* $2 \leq n \leq 10 \ 000$;
* The numbers on the roulette are natural numbers less than or equal to $30 \ 000$.
* For correctly determining the number $r$ of rotations, 70% of the score per test is awarded; the full score is awarded if both displayed values are correct.

# Example

`ruleta.in`
```
8
1 2 3 4 3 2 3 1
```

`ruleta.out`
```
4 3
```

