# Figures

We consider $N$ rectangular pieces of colored paper, which are placed one after another on a white rectangular sheet. We know that the coordinate system has its origin at the center of the white sheet and that the axes are parallel to the sides of the white sheet. Thus, this white sheet can be divided into unit side squares. The pieces of paper have edges parallel to the white sheet and fit entirely on the sheet. Finally, if we look from above, we will see different figures of different colors. Two regions of the same color are part of the same figure if they have at least one square that has at least one neighboring square among its 8 neighbors, which is part of the other region of the same color.

## Task

Determine the area of each figure and the maximum number of sheets that overlap at least one common square.

## Input data

The first line of the file `figuri.in` contains three natural numbers $a$, $b$, and $N$, where $a$ represents the width of the sheet of paper (in the figure below: the number of squares horizontally), $b$ represents the length of the sheet of paper (the number of squares vertically), and $N$ represents the number of rectangular pieces of colored paper. The next $N$ lines each contain 5 integers: $x_1$, $y_1$, $x_2$, $y_2$, and $c$, where $x_1$ and $y_1$ represent the coordinates of the bottom-left corner of the respective rectangle, $x_2$ and $y_2$ represent the coordinates of the point on the sheet where the top-right corner of the rectangle will be placed, and $c$ represents its color. The color is a natural number. The order of the lines in the input file corresponds to the order of placement of the rectangles.

## Output data

The output file `figuri.out` will contain one line describing each "monochromatic" figure. On each line, two integers $c$ and $d$ will be written, where $c$ represents the color code of the figure being described, and $d$ represents the area of that figure. On the last line of the file, a single natural number will be written, representing the maximum number of pieces of paper that overlap at least one common square. We will also count the initial white sheet.

## Constraints

$1 \leq N \leq 1000$

$1 \leq a, b \leq 200$

$a$ and $b$ are even numbers

$1 \leq c \leq 1000$

The color white is coded as 1

$x_1 < x_2$, $y_1 < y_2$

$[-a/2] \leq x_1, x_2 \leq \frac{a}{2}$

$[-b/2] \leq y_1, y_2 \leq \frac{b}{2}$

Among the colored rectangles, we may also have white-colored rectangles. The initially given white sheet (parts of it) can be part of a figure.

The final number of figures does not exceed 1000.

Figures will be described in the output file in ascending order by color code; if there are multiple such figures, the order will be ascending by area.

## Example

`figuri.in`

```
20 12 6
-7 -5 -3 -1 4
-5 -3 -2 5 2
-4 -2 -2 2 4
-2 -3 -1 12 3
1 -7 5 1
3 -3 4 -2 12
```

`figuri.out`

```
1 172
2 46
4 8
12 12
```