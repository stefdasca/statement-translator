```markdown
In the Cartesian coordinate system xOy, $N$ segments parallel to the y-axis are given. Each segment is determined by its endpoints $(x, y_1)$ and $(x, y_2)$.

# Task
Determine a line that intersects each segment at exactly one point.

# Input data
The file `oypara.in` contains on the first line a natural number $N$, representing the number of segments. The next $N$ lines describe the $N$ segments. More precisely, on line $i+1$, there are $3$ integers separated by a space $x \ y_1 \ y_2$ which represent the segment $i$, having the endpoints $(x, y_1)$ and $(x, y_2)$.

# Output data
On the first line of the file `oypara.out` four integers separated by a space $A1 \ B1 \ A2 \ B2$. The distinct points $(A1, B1)$ and $(A2, B2)$ determine the required line.

# Constraints and clarifications
There can be three collinear segment endpoints.
* $3 \leq N \leq 100\ 000$
* $1 \leq x \leq 100\ 000\ 000$
* $1 \leq y_1 < y_2 \leq 100\ 000\ 000$
* $1 \leq A1, B1, A2, B2 \leq 100\ 000\ 000$
* The points $(A1, B1)$ and $(A2, B2)$ must be distinct.
* $A1, A2$ represent the abscissas (coordinates on the x-axis).
* $B1, B2$ represent the ordinates (coordinates on the y-axis).
* If the line passes through an endpoint of a segment, it is considered to intersect that segment.
* For the test data, there is always a solution.

# Example

`oypara.in`
```
5 
3 1 5
7 6 12
9 3 9
10 8 10
14 8 14
```

`oypara.out`
```
1 3 14 13
```
```