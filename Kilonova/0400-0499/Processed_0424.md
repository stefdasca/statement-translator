Here is the translated competitive programming problem statement in English:

---

We have a grid sheet with width $L$ and height $H$, meaning $L$ cells horizontally and $H$ cells vertically. The cells have side length $1$. Thus, there are $L+1$ vertical lines and $H+1$ horizontal lines (including the border lines). We consider that the leftmost line coincides with the `OY` axis and the bottommost line coincides with the `OX` axis. The sheet is colored red, from bottom to top, in each column up to a certain height. Above that, it is white. Each cell is either fully red or it remains white. A broken line must be drawn, composed of segments of length $1$ which satisfy the following properties:
- Starts from the point with coordinates $0,0$;
- Ends at the point with coordinates $L,0$;
- Is continuous;
- Consists only of horizontal and vertical segments overlapping the sides of the cells;
- Each drawn segment has at most one adjacent cell (out of the two on either side of it) colored red;
- There can be consecutive segments of length $1$, each prolonging the previous one along the drawn line, as in the example;
We denote by $B$ the number of white cells that remain "under" the drawn line.
Determine $A$, the minimum length of such a line. Also determine the minimum value of $B$ for which we can draw a line of length $A$.

# Input data

The `foaia.in` file contains the following:
On the first line, a natural number $C$ representing the task. The second line contains two natural numbers, $L$ and $H$. The next $L$ lines each contain a non-zero natural number representing the number of red cells in the respective column (thus, the red cells are at the bottom of the column, without being interspersed with white cells).

# Output data

The `foaia.out` file contains:
On the first line, only the number $A$ if in the input file we have $C = 1$, respectively only the number $B$ if in the input file we have $C = 2$.

# Constraints and clarifications

* $1 \leq L \leq 100\ 000$;
* $1 \leq H \leq 1\ 000\ 000$;
* The values in the array are natural numbers, less than or equal to $H$;
* For tests worth 34 points, we have $C = 1$.

# Examples

## Example 1

`foaia.in`
```
1
4 5
2 4 1 2
```

`foaia.out`
```
12
```

## Example 2

`foaia.in`
```
2
4 5
2 4 1 2
```

`foaia.out`
```
1
```

# Explanation

~[foaia.png]

---

Feel free to confirm any details or ask further questions!