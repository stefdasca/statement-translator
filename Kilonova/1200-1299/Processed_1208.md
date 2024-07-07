
Consider that all points with integer coordinates in the plane are colored black, except for $n$ points which are colored red. Two red points on the same horizontal line or on the same vertical line (that is, points that have the same ordinate or the same abscissa) can be connected by a segment. We color red all integer-coordinate points on this segment. We repeat the operation as long as new red points are obtained.

# Task

Given the coordinates of the $n$ points that were originally red, find the maximum number of red points that will exist in the end.

# Input data

The first line of the input file `puncte.in` contains the number $n$. The next $n$ lines contain the coordinates of the points, separated by a single space.

# Output data

The output file `puncte.out` will contain a single line which contains the maximum number of red points in the end.

# Constraints and clarifications

* $0 \leq n \leq 100\ 000$ 
* The coordinates are integers in the interval $[0, 1\ 000]$.

# Example

`puncte.in`
```
4
0 2
3 1
1 4
4 4
```

`puncte.out`
```
12
```

## Explanation
~[puncte.png|width=30em]
```

Make sure to double-check the translated text for any issues related to grammar or syntax to ensure it conforms to standard English language norms.