After escaping from `Spân` and becoming an emperor, `Harap-Alb` decided to build a new castle in his empire, which can be represented with the Cartesian coordinate system. He knows that `Roș-Împărat` has built $N+1$ rectangular fences, but he also knows that `Roș-Împărat` is quite stingy and didn't use the best materials.

`Harap-Alb` has learned from mistakes, and now he tries to avoid dangers as much as possible. Therefore, he wants to place his castle at a point in the Cartesian system that is inside at least $N$ of the $N+1$ fences.

# Task
Given the non-zero natural number $N$ and the coordinates of the $N+1$ fences (pairs of top-left and bottom-right corners), determine (if it exists) the point **closest to the origin of the coordinate system** where `Harap-Alb` can place his castle so that it is inside at least $N$ fences.

# Input data

The input file `castel.in` contains the non-zero natural number $N$ on the first line, with the above significance. The next $N+1$ lines contain four natural numbers $a_i$, $b_i$, $c_i$, $d_i$, $(1 \leq i \leq N+1)$, separated by spaces, representing the coordinates of the fences. The top-left corner of fence $i$ is at point with abscissa $a_i$ and ordinate $b_i$, and the bottom-right corner is at point with abscissa $c_i$ and ordinate $d_i$.

# Output data

The output file `castel.out` contains on the first line two natural numbers, representing the abscissa and the ordinate of the determined point according to the task. If there are multiple such points, choose **the one with the minimum abscissa**. If there is no such point, print the message **NU**.

# Constraints and clarifications

* $1 \leq N < 200\ 000$;
* $0 \leq a_i$, $b_i$, $c_i$, $d_i < 100\ 000$ and $a_i \leq c_i$, $d_i \leq b_i$, for each $i$: $1 \leq i \leq N+1$;
* **The sides of all rectangles are parallel to the axes of the Cartesian coordinate system**;
* The origin of the coordinate system is at point $(0,0)$;
* The interior of a fence includes the fence itself (the outline);
* There may be degenerate rectangles, i.e., segments (parallel to the coordinate axes) or points;
* There may be identical rectangles;
* The distance between two points located at coordinates $(a,b)$ and $(c,d)$ is equal to $\\sqrt{(c-a)^2+(d-b)^2}$.

|# | Score | Constraints|
| - | -- | ------------|
| 1 | 19 | $N < 200$ and $a_i,b_i,c_i,d_i < 200$, for each $i$: $1 \leq i \leq N + 1$. |
| 2 | 30 | $N < 2\ 000$ |
| 3 | 51 | No other additional constraints |

# Example 1

`castel.in`
```
3
1 4 3 2
4 2 5 0
2 3 4 2
2 3 5 1
```

`castel.out`
```
2 2
```

## Explanation

The hatched area in red represents the points that are inside at least $3$ rectangles. The point $(4,2)$ also meets the requirement. Among all these points, $(2,2)$ is the closest to the origin.

~[t-00.jpg]

# Example 2

`castel.in`
```
4
1 4 5 2
2 5 3 1
4 5 5 1
3 6 4 5
2 5 5 4
```

`castel.out`
```
NU
```

## Explanation

No point is inside at least $4$ fences, as can be seen in the diagram below.

~[t-01.jpg]