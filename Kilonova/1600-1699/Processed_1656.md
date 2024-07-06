Here's the translated problem statement:

## Task

There are $n$ cubes of the same size, with colored faces. The colors are coded by a letter from `A` to `M`. For each cube, the colors of the faces are known in the order: base, top, front face, right side face, back face, left side face. Determine the maximum number of cubes that, flipped and rotated conveniently, can be stacked one on top of another to form a tower with uniformly colored faces (each face of the tower has the same color, from the first to the last cube of the tower).

## Input data

From the file `cuburi.in`, the first line will contain $n$, a natural number. The next $n$ lines (without spaces between letters) will contain the colors of each cube in the order: base, top, front face, right side face, back face, left side face, $c_{ij}$ being the $j$-th color of the $i$-th cube.

## Output data

In the file `cuburi.out`, print a single number representing the maximum number of cubes that, flipped and rotated conveniently, can be stacked one on top of another to form a tower with uniformly colored faces.

## Constraints and clarifications

* The cubes that form a tower are placed only one on top of another, not side by side;
* The colors of the faces of a cube can repeat for two or more of its $6$ faces;
* Any cube can be rotated or flipped to bring it into a convenient position;
* The colors of the faces of the cubes that do not form the lateral faces of the tower are of no importance;
* $0 \leq n \leq 50\ 000$, a natural number;
* $c_{ij}$ are capital letters of the English alphabet, $c_{ij} \in \{ A, B, \dots, M \}$

## Example

`cuburi.in`

```
3
ACADEB
FBCDAE
AEDCBB
```

`cuburi.out`

```
2
```

## Explanation

The first cube can be kept in its position, having the lateral faces `A`, `D`, `E`, `B` (front, right side, back, left side), while the third cube can be flipped to have the tops `B` and `C`, and rotated to have the lateral faces also be `A`, `D`, `E`, `B`.