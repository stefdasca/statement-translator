```markdown
Several frogs from the city, taking a walk through the central park and discovering a mosaic similar to a chessboard of size $n \times n$, have come up with a game with the following rules:
- each frog starts from the center of the square located in the upper-left corner of the board, passes through each square of the mosaic, and returns to the square from where it started;
- it can jump from the center of any square to the center of any adjacent squares in the directions: N, S, E, W, NE, NW, SE, SW;
- if the centers of the squares are connected in the order in which they have been traversed, a closed line is obtained which must not self-intersect.

One of the frogs – more reckless – bets its weight in flies, that it can find an order in which to cover the mosaic with jumps such that the length of the path traveled cannot be exceeded. The length is in a geometric sense: the path between the centers of two squares sharing a common side is $1$, and between the centers of two squares that only have a common vertex, the distance is $\\sqrt{2}$.

# Task
Unfortunately, the frog doesn't really know how to proceed, so it asks you to indicate the order in which to traverse the squares of the board so that it doesn't lose the bet.

# Input data
The input file `frog.in` contains on the first line the value of $n$.

# Output data
In the output file `frog.out`, on line $i$ ($i = 1 \dots n^2 + 1$), two pairs of values separated by a space will be written, representing the coordinates of the square where the frog must jump at step $i$ (it is considered that in the upper-left corner we have the coordinates $(1, 1)$ and the location of a square is done as in a matrix).

# Constraints and clarifications
- $2 \\le n \\le 250$

# Example
`frog.in`
```
4
```
`frog.out`
```
1 1
2 2
2 1
3 1
3 2
4 1
4 2
3 3
4 3
4 4
3 4
2 3
2 4
1 4
1 3
1 2
1 1
```

## Explanation
This solution respects the rules of the game, but it will not win the frog's bet!
```