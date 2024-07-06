An ant moves in the `xOy` coordinate system. The ant starts from the origin. If the ant is at coordinates `(x,y)`, it will move in a straight line to one of the following six points:
1. `(x+1, y+1)`
2. `(x+2, y+2)`
3. `(x+3, y+3)`
4. `(x+1, y-1)`
5. `(x+2, y-2)`
6. `(x+3, y-3)`

The ant will move such that at no point during the movement does it reach a point with a negative `y` coordinate. **In the end, the ant will reach the `Ox` axis**.

# Task
Given the number of moves of each of the six types, choose an order in which these moves can be performed such that the area bounded below by the `Ox` axis and above by the ant's path has the minimum area.

# Input data
The input file `minarea.in` will contain `6` natural numbers `a, b, c, d, e, f` separated by a space, representing the number of moves of type `1, 2, 3, 4, 5` respectively `6`.

# Output data
The output file `minarea.out` will contain a single number representing the minimum area.

# Constraints and clarifications
* `0 \ \leq a, b, c, d, e, f \ \leq 1\ 000\ 000\ 000`
* `a + 2b + 3c = d + 2e + 3f`
* for tests worth `10` points, `c=f=0`

# Example
`minarea.in`
```
2 0 1 1 2 0
```
`minarea.out`
```
13
```

Explanations
---
The minimum area is `13`. This area can be obtained in several ways. In the figure below, all six ways in which the ant's path and the `Ox` axis could bound an area of `13` are described.

~[minarea.png]

`minarea.in`
```
219 221 5 108 47 158
```
`minarea.out`
```
1760
```

Explanations
---
The minimum area is `1760`.