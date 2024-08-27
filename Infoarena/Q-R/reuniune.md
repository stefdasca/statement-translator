## Union

Zaharel has been challenged by Eugenia to solve the following problem: given three rectangles in the plane with sides parallel to the $OX$ and $OY$ axes. Determine the area and perimeter of the union of the three rectangles (the union of the rectangles represents the set of points that belong to at least one rectangle).

## Task

Help Zaharel create a program that calculates the required data.

## Input Data

The file `union.in` will contain three lines, one for each rectangle. Each line will contain four integers $X_0$ $Y_0$ $X_1$ $Y_1$ representing the bottom-left and top-right corners of the respective rectangle.

## Output Data

The file `union.out` will contain a single line with two natural numbers: the area and perimeter of the union.

## Constraints

- $-1\ 000\ 000\ 000 \leq X_0$
- $Y_0$
- $X_1$
- $Y_1 \leq 1\ 000\ 000\ 000$

## Example

`union.in`
```
0 0 8 6
4 2 11 9
2 -2 6 4
```

`union.out`
```
89 44
```

## Explanation