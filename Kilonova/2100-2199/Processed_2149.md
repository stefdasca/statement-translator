# Task

An Omegazoid wants to draw with a pencil. He is in the 3rd grade, and it is fashionable there to draw without lifting the pen from the paper.
Can the Omegazoid draw without lifting the pen from the paper and without joining the same 2 points twice? Moreover, the drawing should start from the first point and end where it began.

# Input data

The first line contains $N$ (the number of points in the drawing) and $M$ (the lines he wants to draw between points).
The next $M$ lines each contain a pair of numbers $a, b$; he wants points $a$ and $b$ to be joined in the drawing.

# Output data

Print $YES$ or $NO$, depending on whether it is possible (see example).

# Constraints and clarifications

* $1 \leq N \leq 10^5$
* $1 \leq M \leq min(2 \cdot 10^5,\ \frac{N \cdot (N-1)}{2})$
* $1 \leq a, b \leq N$, $a \neq b$.
* The pairs of points do not repeat.
* If he has multiple drawings on the same sheet, he needs to complete only the drawing containing point 1.

# Example 1

`stdin`
```
3 3
1 2
2 3
1 3
```

`stdout`
```
YES
```

## Explanation

We can start at the first point, then go to the third point, from where we can go to the second point, and then back to point 1.

# Example 2

`stdin`
```
5 8
1 5
2 3
5 4
1 4
2 1
4 3
1 3
2 4
```

`stdout`
```
NO
```

## Explanation

Drawing:

~[Screenshot 2024-01-15 202243.png]

There is no way to achieve this.