# Snooker

Ronnie "The Rocket" O'Sullivan has finally understood that defensive tactics are also useful in snooker. To practice, Ronnie has bought a $(N+2) \times (M+2)$ table, without pockets, and a set consisting of a white ball and $K$ red balls, all having radius $1$. The bottom-left corner of the table has coordinates $(-1, -1)$ and the top-right corner has coordinates $(N+1, M+1)$. Thus, we observe that a ball placed in the bottom-left corner will have its center at coordinates $(0, 0)$, and a ball placed in the top-right corner will have its center at coordinates $(N, M)$. Ronnie will practice as follows: he places the $K$ red balls on the table, all at points with natural coordinates. Then, Ronnie chooses two points $A$ and $B$ with natural coordinates $(Xa, Ya)$ and $(Xb, Yb)$, respectively. He places the white ball with its center at point $A$ and tries to hit it with the cue in such a way that, after rolling on the table, it stops with its center at point $B$ without touching any of the red balls. Due to the arrangement of the red balls, the hit might not be possible directly but only with the cushion. The table Ronnie bought is of superior quality, so the white ball bounces off the cushion at the same angle it was hit (see figure).

## Task

Given $N$, $M$, the coordinates of points $A$ and $B$, the number $K$ of red balls and their coordinates, determine the angle in radians under which the white ball must be hit, such that it does not touch any red ball and its center reaches point $B$.

## Input data

The input file `snooker.in` will contain on the first line six natural numbers: $N$, $M$, $Xa$, $Ya$, $Xb$, $Yb$.

The second line contains the natural number $K$.

Each of the following $K$ lines contains a pair of numbers $(x, y)$ representing the coordinates of a red ball.

## Output data

The output file `snooker.out` will contain a real number, representing the measure in radians of the angle under which Ronnie must hit the white ball.

## Constraints and clarifications

$10 \leq N$

$10 \leq M$

$N \leq 100$

$M \leq 100$

$1 \leq K$

$K \leq 50$

All numbers in the input data are natural.

The cushion is defined as the raised edge of the table, more precisely the contour of the rectangle with corners at points $(-1, -1)$ and $(N+1, M+1)$.

It is guaranteed that for each test, there is a solution for which the white ball hits the cushion a maximum of 5 times.

Any solution where the white ball hits the cushion a maximum of 10 times and does not touch any red ball before reaching point $B$ will be accepted.

The white ball is considered to touch a red ball if the distance from the center of the red ball to the trajectory of the white ball is strictly less than $2$ (twice the radius $1$).

The result will be checked with a precision of $0.0001$.

Important! For displaying the answer it is recommended to use the `atan2(y, x)` function from the cmath library for C/C++ programmers or the `arctan2(y, x)` function for Pascal programmers. Both functions take parameters $y$ and $x$ and return the value in radians of the angle made by point $(x, y)$ with the origin $(0, 0)$. Given a point $(X, Y)$ on the initial trajectory of the white ball (before hitting a cushion) and the point $(Xa, Ya)$, the answer you need to print is `atan2(Y-Ya, X-Xa)` or `arctan2(Y-Ya, X-Xa)`. More details about the two functions can be found on C++ Reference and FreePascal.org

Score thresholds

For 20% of the tests, the hit can be executed directly.

For another 20% of the tests, the hit must be executed with at least one cushion.

For another 15% of the tests, the hit must be executed with at least two cushions.

For another 15% of the tests, the hit must be executed with at least three cushions.

For another 15% of the tests, the hit must be executed with at least four cushions.

For another 15% of the tests, the hit must be executed with at least five cushions.

## Example

`snooker.in`
```
10 10 5 0 4 7 2 8 5 5 5
```

`snooker.out`
```
2.176341
```

## Explanation

There are 4 correct answers: $-2.480549$, $2.480549$, $-2.176341$, $2.176341$ (corresponding to the angles $-142.09, 142.09, -124.68,$ and $124.68$ degrees). Since the white ball is right next to the cushion, if we hit at a negative angle (towards the cushion), the white ball will bounce immediately and follow the trajectory given by the absolute value of the angle. Thus, the first two answers correspond to the blue trajectory, and the last two correspond to the orange trajectory.