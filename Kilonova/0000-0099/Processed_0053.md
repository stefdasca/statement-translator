Păcală received, as per the agreement, a piece of land from the lord's estate. The land is entirely enclosed with straight segments of fence that are supported at both ends by sturdy stakes. In a new contest, Păcală wins again and gains the right to move some stakes, one by one, as he wishes, in order to extend his land area. However, the agreement states that each stake can be moved in any direction, but not by a distance greater than a given value (written on each stake) and each segment of the fence, being quite fragile, can be rotated and extended from one end, with the other end remaining stationary.

Given the initial positions of the stakes and the values written on each stake, the task is to find the maximum area by which Păcală can extend his property. It is known that the stakes are given in a random order, their initial positions are given by integers of at most $3$ digits, the distances by which each stake can be moved are strictly positive natural numbers, and the figure formed by the initial land is a non-convex polygon.

# Input data
The file `mosia.in` contains $n+1$ lines with the following values:
$n$ – the number of stakes
$x_1 \\ y_1 \\ d_1$ – the initial coordinates and the distance by which stake $1$ can be moved
$x_2 \\ y_2 \\ d_2$ – the initial coordinates and the distance by which stake $2$ can be moved
...
$x_n \\ y_n \\ d_n$ – the initial coordinates and the distance by which stake $n$ can be moved

# Output data
In the file `mosia.out`, print a real number with $4$ decimal places that represents the maximum area by which the estate can be enlarged.

# Constraints and clarifications:
* $3 < N \leq 200$ natural number
* $−1\ 000 < x_i,y_i < 1\ 000$ integers
* $0 < d_i \leq 20$ integers
* The non-convex polygon is defined as a convex polygon with some collinear vertices
* The positions of the stakes are given in a random order
* The polygon obtained after moving the stakes can be concave
* The final positions of the stakes are not necessarily natural numbers

# Example

`mosia.in`
```
4
-3 0 2
3 0 3
0 6 2
0 -6 6
```

`mosia.out`
```
30.0000
```

Explanation
---
Explanation: By moving stake $1$ and stake $2$ by $2$ and $3$ units respectively, we get a land with an area $30$ units larger than the initial land.

---