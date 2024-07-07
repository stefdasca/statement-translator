
Consider $n$ points in a 2D plane. You are required to compute the square of the minimum distance between any two of the first two points, then the first three points, and so on until the $n ^ {th}$ point.

# Input

The first line will contain the integer $n$ ($1 \leq n \leq 10 ^ 5$).

The following $n$ lines will each contain two integers, the two coordinates of each point.

$- 10 ^ 9 \leq x, y \leq 10 ^ 9$ where $x$ and $y$ are the coordinates.

For tests worth $20$ points it is guaranteed that $(1 \leq n \leq 1 \ 000)$.

# Output

You will print $n - 1$ lines, each representing the square of the minimum distance between the first two, then three, then four points and so on.

# Example

`stdin`
```
4	
1 2
3 6
9 10
1 1
```

`stdout`
```
20
20
1
```

Explanation
---

The square of the distance between the first two points is $((1 - 3)^2 + (2 - 6)^2) = 20$.

The square of the distance between the third and first point is $128$, and between the third and second point is $52$, so the minimum distance remains $20$.

The distance between the fourth and first point is $1$.
