On an agricultural land near the city of Austin, in the state of Texas, there are $N$ trajectories, numbered: $1, 2, \ldots, N$, where tractors can be used. The trajectories are disjoint from each other and have the shape of **circles** with radii of positive natural numbers. The direction of movement on each trajectory is described by three **distinct** points (from the Cartesian coordinate system) on the trajectory, in the order in which they are visited by the tractor. Thus, if a tractor follows trajectory $i$, the tractor starts from the point $(x_{i, 1}, y_{i, 1})$, reaches $(x_{i, 2}, y_{i, 2})$, then $(x_{i, 3}, y_{i, 3})$ and, finally, returns to $(x_{i, 1}, y_{i, 1})$, where the tractor is stopped, making **exactly one complete rotation on the circle**.

Each trajectory $i$ out of the $N$ is associated with a value $V(i)$ equal to: $V(i) = r(i) \cdot r(i) \cdot w(i)$, where $r(i)$ represents the radius length of the circle describing trajectory $i$, and $w(i) = 1$ if the movement on trajectory $i$ is counterclockwise (i.e., counter to the clock) or $w(i) = -1$ if the movement is clockwise.

While on vacation at their grandparents' houses in Austin, **Sam** and **John** want to help take care of the farmland. Thus, **Sam** chooses a **non-empty** set $A = \{a_1, a_2, \ldots, a_k\}$ consisting of $k$ distinct trajectories out of $N$ ($1 \leq k < N$), while **John** is left with the **non-empty** set $B = \{b_1, b_2, \ldots, b_{N-k}\}$ consisting of the remaining $(N-k)$ trajectories not chosen by **Sam**. 

Of course, their work is rewarded based on performance, so after each of them finishes using tractors on the chosen trajectories, **Sam** receives: $k \cdot (V(a_1) + V(a_2) + \ldots + V(a_k))$ points at the bowling alley, and **John** receives: $(N-k) \cdot (V(b_1) + V(b_2) + \ldots + V(b_{N-k}))$ points. **The points obtained can be less than or equal to $0$.**

# Task

To ensure balance between the two scores obtained, the grandparents choose a natural number $L$. Determine how many distinct ways the two young people can divide the two sets of trajectories $A$ and $B$ such that the **absolute value** of the difference between the score obtained by **Sam** and the score obtained by **John** is less than or equal to the number $L$.

# Input data

The first line contains the natural number $N$, as described above.
On each of the next $N$ lines there are six natural numbers separated by a space; thus, on the $(i+1)$-th line, there are in order, the values $x_{i, 1}$, $y_{i, 1}$, $x_{i, 2}$, $y_{i, 2}$, and $x_{i, 3}$, $y_{i, 3}$, for each $i$: $1 \leq i \leq N$. On the next line, there is the natural number $L$.

# Output data

The first line contains a single integer, representing the number of distinct ways determined. If there is no such way, then this number will be equal to $-1$.

# Constraints and clarifications

* $2 \leq N \leq 34$ and $0 \leq L \leq 10^{17}$.
* $0 \leq x_{i, j}, y_{i, j} \leq 1\ 000\ 000$ and $x_{i, j}, y_{i, j}$ are natural numbers, for each $(i, j)$: $1 \leq i \leq N$ and $1 \leq j \leq 3$.
* $r(i) > 0$ and $|V(i)| \leq 10^{12}$, for each $i$: $1 \leq i \leq N$.
* The circles describing each of the $N$ trajectories have the coordinates (abscissa and ordinate) of the center with values being natural numbers less than or equal to $1\ 000\ 000$.
* A circular trajectory consists only of the points on the contour of the circle that describes the trajectory, and two trajectories are disjoint if the circles that describe them do not have any point in common.
* For a circle $C$ of radius $r$ ($r > 0$), which has the center at the point with coordinates $(x_C, y_C)$, **all** points on the circle are at the same distance from the center, equal to the radius length. Thus, $(x - x_C)^2 + (y - y_C)^2 = r^2$, for **each** $(x, y) \in C$ (where $x$ and $y$ are real numbers).
* **During the movement of a tractor on trajectory $i$, each real coordinate point on the circle describing the trajectory is visited exactly once, except for the point $(x_{i, 1}, y_{i, 1})$, which is visited twice: once at the start of the movement and once at the end of the movement.**
* *Entry to the bowling alley is paid in points, not in dollars.*

|# | Points | Constraints|
| - | - | ------------|
|1|4|$N = 2$|
|2|7|$N = 3$|
|3|8|$N \leq 15$ and $(x_{i, 1}, y_{i, 1})$, $(x_{i, 2}, y_{i, 2})$ and $(x_{i, 3}, y_{i, 3})$ can describe a right triangle, for each $i$|
|4|34|$N \leq 15$|
|5|8|All $N$ trajectories are counterclockwise.|
|6|39|No further additional constraints.|

# Example 1

`stdin`
```
3
0 1 1 0 2 1
7 14 13 6 10 5
14 10 12 12 12 8
30
```

`stdout`
```
-1
```

## Explanation

The centers of the circles describing the $N = 3$ trajectories are at the points $(1, 1)$, $(10, 10)$, and $(12, 10)$. The circles have radii lengths equal to $1$, $5$, and $2$ respectively.

The first trajectory is described by a circle with radius $r(1) = 1$ and is counterclockwise, so $w(1) = 1$. Therefore, $V(1) = 1$. Similarly, $V(2) = -25$ and $V(3) = 4$.

There are, **in total**, six distinct ways in which **Sam** and **John** can divide the two non-empty sets $A$ and $B$:

* If $A = \{1\}$, while $B = \{2, 3\}$, **Sam** gets one point and **John** $(-42)$ points. The absolute value of the difference $1 - (-42)$ is equal to $43$.
* If $A = \{1, 2\}$, while $B = \{3\}$, **Sam** gets $(-48)$ points, and **John** gets $4$ points. The absolute value of the difference $(-48) - 4$ is equal to $52$.
* If $A = \{1, 3\}$, while $B = \{2\}$, **Sam** gets $10$ points, and **John** gets $(-25)$ points. The absolute value of the difference $10 - (-25)$ is equal to $35$.
* If $A = \{2\}$, while $B = \{1, 3\}$, **Sam** gets $(-25)$ points, and **John** gets $10$ points. The absolute value of the difference $(-25) - 10$ is equal to $35$.
* If $A = \{2, 3\}$, while $B = \{1\}$, **Sam** gets $(-42)$ points, and **John** gets one point. The absolute value of the difference $(-42) - 1$ is equal to $43$.
* If $A = \{3\}$, while $B = \{1, 2\}$, **Sam** gets $4$ points, and **John** gets $(-48)$ points. The absolute value of the difference $4 - (-48)$ is equal to $52$.

In this example, there is no way to choose sets $A$ and $B$ such that the absolute value of the difference between the two scores is less than or equal to $L = 30$.

# Example 2

`stdin`
```
3
0 1 1 0 2 1
7 14 13 6 10 5
14 10 12 12 12 8
43
```

`stdout`
```
4
```

## Explanation

There are four distinct ways to choose the sets $A$ and $B$ such that the absolute value of the difference between the two scores is less than or equal to $L = 43$, as follows:
* $A = \{1\}$ and $B = \{2, 3\}$;
* $A = \{1, 3\}$ and $B = \{2\}$;
* $A = \{2\}$ and $B = \{1, 3\}$;
* $A = \{2, 3\}$ and $B = \{1\}$.