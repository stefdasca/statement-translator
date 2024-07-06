# Task

Write a program that reads two natural numbers \( N \) and \( K \) and determines for Andrei:

1. the number of children in the circle who have cards of the same color as their neighbors' cards;
2. the maximum number of cards of the same color held by children placed at \( K \) consecutive positions in the formed circle.

# Input data

The input file `culori.in` contains:
* The first line contains the natural numbers \( N \) and \( K \), separated by a space.
* Each of the next \( N \) lines contains a natural number. The \( N \) numbers represent the color codes of the cards, in the order the children are numbered, starting with child \( 1 \).

# Output data

The output file `culori.out` contains:
* The first line contains the natural number determined for task 1;
* The second line contains the natural number determined for task 2.

# Constraints and clarifications

* \( 2 < N \leq 1 \ 000 \);
* \( 2 < K \leq N \);
* The color codes are non-zero natural numbers, consecutive, less than or equal to \( 100 \);
* If \( C \) is the maximum code associated with a color (\( 1 \leq C \leq 100 \)), then there are at least \( C \) cards with distinct codes: \( 1, 2, 3, \dots, C \);
* \( 30 \%\) of the score is awarded for correctly solving task 1;
* \( 70 \%\) of the score is awarded for correctly solving task 2;

# Example

`culori.in`
```
8 5
3
1
2
1
1
1
3
3
```

`culori.out`
```
2
4
```

## Explanation

~[culori.png|align=right]
There are two children who each have cards identical to those of their two neighbors (child \( 5 \) and child \( 8 \)).
The maximum number of cards of the same color held by children placed at \( K = 5 \) consecutive positions in the formed circle is \( 4 \) (among children \( 2, 3, 4, 5, 6 \) only children \( 2, 4, 5, \) and \( 6 \) have cards of color \( 1 \)).