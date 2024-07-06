# Task

On the pavement, a hopscotch grid is drawn with chalk, consisting of $n \times n$ squares, each having the same dimensions (with $n$ squares on each of the $n$ rows).

In every square, there is an integer written from the interval $[-100, 100]$. 

Each player has a stone which they throw into a square of the hopscotch grid, and hopping on one foot, they push the stone from one square to another, along a certain path such that the score obtained from the sum of the numbers on the path chosen is as high as possible.

The numbers in the squares of the hopscotch grid are written in two colors: blue and white, in such a way that no two adjacent squares (in the four directions: North, East, South, West) have numbers written in the same color. It is always the case that the first square in the first row of the hopscotch grid has a number written in blue.
The following rules of the game are then established:

~[Poza1.png|align=right]

* At the start of the game, the stone can be thrown into any square of the hopscotch grid. From that position, the player leads the stone to the end of the path they establish.
* From a square where the number is written in blue, the stone can be moved only to the neighboring square in the North direction.
* From a square where the number is written in white, the stone can be moved only to the neighboring square in the East direction.
* The player can choose any square (including the one where they threw the stone) to end the game, as long as the stone does not leave the hopscotch grid.

# Task

Write a program that determines the highest score that can be obtained by playing hopscotch according to the established rules.

# Input data

The input file `sotron.in` contains on the first line the dimension $n$ of the hopscotch grid, and on the following $n$ lines, $n$ numbers separated by spaces representing the numbers written in the hopscotch grid.

# Output data

The output file `sotron.out` will contain on the first line a single number representing the maximum score that can be obtained by playing hopscotch.

# Constraints and clarifications

* $1 \leq n \leq 240$

# Example

`coduri.in`
```
5
0 -6 -5 -17 2
1 -4 7 10 5
-3 -2 3 -8 -8
-20 3 5 3 -5
-10 -15 2 2 -4
```

`coduri.out`
```
21
```

## Explanation

The score obtained is $3 + (-2) + 3 + 7 + 10 = 21$