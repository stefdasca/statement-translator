Floricel receives an interesting task during art class. He first draws a rectangle with natural number sides and makes from paper as many identical figures as he wants. By joining such figures, called elementary figures, Floricel can construct squares and rectangles of various sizes.
Help Floricel to select **a minimum number of identical figures with the initial rectangle** so that, by joining them, he can build a square. Note, the elementary figures must not overlap and cannot be rotated.

### Example

Floricel first draws a rectangle with length $3$ and width $2$ as in figure $a)$:
~[desen-a.png|align=center]
The smallest square that can be obtained by joining such figures, without overlaps and rotations, is the one in figure $b)$, has a side of $6$ and is composed of $6$ identical figures as the one in figure $a)$.
~[desen-b.png|align=center]

# Task

Knowing the dimensions of the initial rectangle, determine the side of the smallest square Floricel can build and the number of identical figures with the initial rectangle necessary for this construction.

# Input data

The file `desen.in` contains on the first line the length and the width of the initial rectangle, values separated by a space.

# Output data

The file `desen.out` will contain on the first line the side of the constructed square and on the second line the number of identical figures with the initial rectangle required for this construction.

# Constraints and clarifications

* The sides of the rectangle are non-zero natural numbers, less than or equal to $10\ 000\ 000$
* The minimum number of figures used is at least $1$

# Example

`desen.in`
```
6 3
```

`desen.out`
```
6
2
```

## Explanation

The initial figure has sides of $6$ and $3$ respectively. The smallest square that can be built by joining such figures has a side of $6$ and $2$ such figures are used for this construction.