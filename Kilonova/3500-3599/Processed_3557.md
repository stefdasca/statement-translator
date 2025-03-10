
~[ciulini.png|align=right|width=20%]

# Task

In a field, there is a line of thistles (plants), each numbered from $1$ to $n$ (from left to right). At some point, a whirlwind appears which lifts the thistles into the air, one by one, in a certain order, following the rule described below:

- If $n$ is odd, the first thistle lifted is the one at the middle position.
- If $n$ is even, there are two central elements and the one on the left is lifted first.

~[ciulini2.png|align=center|width=40%]

After lifting the first thistle, the whirlwind continues to lift the remaining thistles in an alternating order: a thistle from the right, the closest to the position of the previously lifted thistle, followed by one from the left, also the closest to the position of the previously lifted thistle.

Write a program that solves the following two tasks:
1. The program receives the total number of thistles, $n$, then determines the order numbers of the thistles in the order in which the whirlwind lifts them.
2. For a given position $k$, the program determines in which order the thistle initially at this given position is lifted.

# Input data

The input file `ciulini.in` contains:
* The first line contains the value $c$ ($1$ or $2$) representing the task to be solved.
* The second line contains the number $n$ (if the task is $1$) or the numbers $n$ and $k$ separated by a space (if the task is $2$).

# Output data

The output file `ciulini.out` will contain:
* if $c=1$, a sequence with $n$ distinct numbers from $1$ to $n$, separated by a space, representing the answer for task 1;
* if $c=2$, a number, representing the answer for task 2.

# Constraints and clarifications

* For $c = 1$, $1 \leq n \leq 100 \ 000$;
* For $c = 2$, $1 \leq k \leq n \leq 1 \ 000 \ 000 \ 000$;
* For tests worth $23$ points, $c = 1$.

# Example 1

`ciulini.in`
```
1 
8
```
`ciulini.out`
```
4 5 3 6 2 7 1 8
```

## Explanation

For $c = 1$, $n = 8$:
* Initial array of thistles: $1, 2, 3, 4, 5, 6, 7, 8$.
* Lifting order: $4, 5, 3, 6, 2, 7, 1, 8$.

# Example 2

`ciulini.in`
```
2 
8 5
```
`ciulini.out`
```
2
```

## Explanation

For $c = 2$, $n = 8$, $k = 5$:
* Initial array of thistles: $1, 2, 3, 4, 5, 6, 7, 8$.
* The thistle at position $k = 5$ is lifted second.
```
