~[arhitect.jpg|align=right|width=20em]

The construction of a new building has been completed! Frank, the famous architect, took a picture of the facade. However, he is not quite satisfied with the picture because he noticed an inclination of the picture relative to the horizontal. This can be fixed by rotation, and Frank wonders if the straightening process could be automated.

To this end, the image is transformed into a set of segments in the plane, automatically detected with special algorithms, as shown in the image to the right. The segments obtained are identified by their two endpoints, points with natural number coordinates, in the *xOy* system: ($x_1$, $y_1$), ($x_2$, $y_2$). A segment is called *aligned* with the axes if it is horizontal (parallel to the *Ox* axis, so $y_1=y_2$) or vertical (parallel to the *Oy* axis, so $x_1=x_2$). By rotating the image as a whole, some of the segments become *aligned* with the two axes.

# Task

Write a program that for a set of segments determines the maximum number of segments that can be *aligned* by rotating all segments by the same angle. The angle of rotation can be any real number.

# Input data

The input file `arhitect.in` contains on the first line the number of segments $N$ and on the following $N$ lines four integers separated by a space $x_1$, $y_1$, $x_2$, $y_2$, in this order, with the meaning given in the statement, the coordinates defining the endpoints of the segments.

# Output data

The output file `arhitect.out` contains on the first line the determined maximum number of segments.

# Constraints and clarifications

* $1 \leq N \leq 100\ 000$ and $1 \leq x_1, y_1, x_2, y_2 \leq 1\ 000\ 000\ 000$;
* All segments have non-zero length;
* For $40$ points, the initial segments are parallel to *Ox*, *Oy*, or the bisectors of the coordinate axes.
* For $60$ points, without additional restrictions.

# Example 1

`arhitect.in`
```
3
1 1 1 3
4 1 1 4
5 2 7 4
```

`arhitect.out`
```
2
```

## Explanation

The initial segments are parallel to the axes or bisectors. 
If we rotate the image by 45° degrees, the second segment becomes vertical while the last one becomes horizontal. We can align a maximum of 2 segments.

~[ex1_v2.jpg]

# Example 2

`arhitect.in`
```
6
1 7 9 9
4 5 8 6
9 3 4 2
2 7 3 2
9 2 8 6
5 2 4 6
```

`arhitect.out`
```
4
```

## Explanation

A maximum of 4 segments can be aligned, namely:
```
1 7 9 9
4 5 8 6
9 2 8 6
5 2 4 6
