The Game Store has released the latest version of the **Z game**, to help 8th-grade students better understand how to identify the coordinates of a point on a plane, in an orthogonal axis system.

We call **Z sign** the figure obtained in the xOy plane with the help of $4$ **distinct** points $A(x_A, y_A), B(x_B, y_B), C(x_C, y_C), D(x_D, y_D),$ connected as in fig.1, where $x_A = x_C , x_B = x_D , y_A = y_B , y_C = y_D$.

~[image1.png|align=left]

On the screen, a math sheet and the orthogonal axis system $xOy$ are displayed. Successively, the integer coordinates of some points on the plane appear. The player must mark each point on the sheet and draw a segment that connects the point (except for the first marked point) with the previously marked one.

In the example from fig.2, the points were successively marked: $(-8,4)$, $(-5,6)$, $(-2,6)$, $(1,6)$, $(-2,2)$, $(-5,-2)$, $(-5,2)$, $(1,2)$, $(-5,-2)$, $(1,-2)$, $(-1,2)$, $(2,6)$, $(-1,2)$, $(1,-2)$. It can be noticed that points can repeat.

~[image2.png|align=left]

At the end of the game, the player must count how many times they passed through the origin of the coordinate system $O(0,0)$ and the maximum number of distinct $Z$ signs formed with marked points.

# Task

Given $N$ (the number of points displayed successively on the screen) and the coordinates of the $N$ points on the plane, write a program that determines:

1. The number of times the point passes through the origin of the coordinate system.
2. The maximum number of distinct $Z$ signs formed with marked points.

# Input data

The input file `z.in` contains on the first line a natural number $P$ representing the task that needs to be solved ($1$ or $2$). The second line contains the natural number $N$, representing the number of points displayed successively on the screen. On the next $N$ lines, there are two **integer numbers**, $x$ and $y$, separated by a space, representing the coordinates of a point $(x,y)$ on the plane, in the order they appear on the screen.

# Output data

If the task is $P=1$, then on the first line of the `z.out` file a natural number representing the number of times passing through the origin of the coordinate system will be written.

If the task is $P=2$, then the `z.out` file will contain the maximum number of distinct $Z$ signs formed with marked points.

# Constraints and clarifications

* $4 \leq N \leq 1\ 000$
* $-1\ 000 \leq x, y \leq 1\ 000$
* $0$ crossing through the origin of the coordinate system is determined by drawing a segment that contains the origin and has endpoints different from the origin.
* For correctly solving the first task, $20\%$ of the score will be awarded, and for correctly solving the second task, $80\%$ of the score will be awarded.

# Example 1

`z.in`
```
1
14
-8 4
-5 6
-2 6
1 6
-2 2
-5 -2
-5 2
1 2
-5 -2
1 -2
-1 2
2 6
-1 2
1 -2
```

`z.out`
```
2
```

## Explanation

Passed twice through the origin of the coordinate system.

# Example 2

`z.in`
```
2
14
-8 4
-5 6
-2 6
1 6
-2 2
-5 -2
-5 2
1 2
-5 -2
1 -2
-1 2
2 6
-1 2
1 -2
```

`z.out`
```
3
```

## Explanation

$3$ Z signs were formed, represented in figures $3$, $4$, and $5$.
~[image6.png|align=left]