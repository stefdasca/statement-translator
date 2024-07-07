
# Task

Geo has learned a method to fix $n$ points on a circle of radius $r$, such that they divide the circle into $n$ equal-length chords. Then he chose a number $k$ and started connecting the points successively, from $k$ to $k$, keeping the same direction, until he returned to the starting point. Thus, if he fixed $n=10$ points on the circle which he numbered $1, 2, \dots, 10$ (see the figure) and chose $k=6$, then he connects point $1$ to $7$, then $7$ to $3$, then $3$ to $9$, then $9$ to $5$, and finally $5$ to $1$.
Then he colored the polygon formed inside, starting from the center of the circle and without crossing any of the drawn lines. He finally wonders how many sides the colored polygon has and what its area is.

For given natural numbers $n$, $k$, and $r$, determine the number of sides $L$ of the colored polygon and its area $S$ (to 2 decimal places).

~[poligon.png]

# Input data

From the file `poligon.in`, read three natural numbers $n$, $k$, and $r$ separated by spaces.

# Output data

In the file `poligon.out`, write on different lines two values: the first line will contain the number $L$ of sides of the colored polygon, and the second line will contain the real number representing its area.

# Constraints and clarifications

* $3 < n < 10\ 001$ natural number
* $0 < k < n$ natural number
* for even $n$, $2 \cdot k \neq n$
* $10 < r < 501$
* For each test, if the determined number of sides is correct, you receive $20\\%$ of the maximum score for that test. Additionally, if the determined area is correct, you receive the maximum score.
* The area is considered correct if the absolute difference between the correct result and the one provided by the contestant does not exceed $0.0001$.
* For $70\\%$ of the tests used for evaluation, $n < 501$

# Example 1

`poligon.in`
```
10 6 100 
```

`poligon.out`
```
5
3468.9319
```

# Example 2

`poligon.in`
```
30 13 200
```

`poligon.out`
```
30
5452.0431
```
