# Harry Potter

Harry and his wizard friends have to solve a new project in the Defense Against the Dark Arts course at Hogwarts. Each of the 4 houses (Gryffindor, Hufflepuff, Ravenclaw, Slytherin) has $N$ representatives with distinct indices from $1$ to $N$. They are seated at a square table, each house along one side. At a given time, a wizard can cast a spell to send a beam to another wizard from a different house if the beam satisfies the following 2 properties:
- The indices of the 2 wizards are equal.
- The beam does not intersect any other previously drawn beam, not even at the ends.

The beam can be represented as a line segment connecting the positions of the 2 wizards. Given the positioning of the $4 * N$ students at the square table, find the maximum number of spells that can be performed.

## Input data

The input file `harrypotter.in` will contain on the first line a natural number $N$, representing the number of students in each house. The next $4$ lines will contain a permutation each, representing the positioning of the wizards at the square table. All the $4 * N$ wizards are given in the clockwise order (the first permutation describes the top side of the square from left to right; the second permutation describes the right side from top to bottom; the third permutation describes the bottom side from right to left; the fourth permutation describes the left side from bottom to top).

## Output data

The output file `harrypotter.out` will contain a single natural number representing the maximum number of spells that can be performed.

## Constraints and clarifications

$1 \leq N \leq 600$

For tests worth $20$ points $N \leq 50$

For tests worth $50$ points $N \leq 100$

## Example

`harrypotter.in`

```
4
2 3 1 4
2 1 4 3
3 2 1 4
4 3 1 2
```

`harrypotter.out`

```
6
```

## Explanation

The 6 spells performed are as follows:
- The child with index $2$ from the top together with the one with index $2$ from the left.
- The child with index $3$ from the top together with the one with index $3$ from the left.
- The child with index $1$ from the top together with the one with index $1$ from the bottom.
- The child with index $4$ from the left together with the one with index $4$ from the bottom.
- The child with index $2$ from the right together with the one with index $2$ from the bottom.
- The child with index $3$ from the right together with the one with index $3$ from the bottom.