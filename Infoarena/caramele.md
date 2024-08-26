## Task

El Marac spent his two-week vacation at his grandmother's house, and she took advantage of the occasion to spoil him with his favorite foods. Unfortunately, all good things come to an end. The vacation is nearly over, and his grandmother promised El Marac some caramels. Specifically, as his grandmother has a lot of caramels but doesn’t want to give them unmerited, she proposes the following game: on his grandfather’s checkerboard, there are $N$ pieces; Marac will receive one caramel for each triangle he observes that has the following properties:
- Its vertices are pieces on the board
- The triangle is a right isosceles triangle
- Its legs are parallel to the edges of the board

As Marac wants to eat as many caramels as possible, he is only interested in the maximum number of caramels he can obtain for certain piece configurations. Since Marac is still busy with his grandmother's roast, he asks you to help him find this maximum number of caramels.

## Input data

The input file `caramele.in` contains, on the first line, $N$, the number of pieces on the board. The next $N$ lines contain the coordinates of the pieces.

## Output data

In the output file `caramele.out` print the number of special triangles required, on a single line.

## Constraints and clarifications

$1 \leq N \leq 30 \ 000$

The coordinates of the pieces are integers with absolute values less than $30 \ 000$

There will be no two pieces with the same coordinates.

## Subtasks

### Index

### Score

## Constraints and clarifications

1 
5 points 

$N \leq 100$

2 
30 points 

$N \leq 1 \ 000$

3 
65 points 

$N \leq 30 \ 000$

## Example

`caramele.in`
```
7 
1 1 
1 2 
2 1 
2 2 
2 3 
3 2 
3 3 
```

`caramele.out`
```
10 
```