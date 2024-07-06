After an hour of practicing foreign languages, Viitorel wants to relax and invites Mr. Boca to a game of volleyball. The hall they are in is actually the orthonormal system $xOy$ (it is an infinite hall, without walls). When Viitorel attacks the ball, it can reach any point at distance $d_V$ from him. Similarly, Mr. Boca can receive a ball from any point at distance $d_B$ from him.

Obviously, depending on their positions and distances $d_V$ and $d_B$, Mr. Boca can receive the ball attacked by Viitorel from 0, 1, or 2 points.

# Task

Determine the points from which Mr. Boca can receive the ball attacked by Viitorel (0, 1, or 2). Also, if applicable, calculate the distance between these points.

# Input data

The file `volei.in` will contain:
* The first line contains the natural numbers $x_V$, $y_V$, $d_V$, representing Viitorel's position and the distance where the ball attacked by him can reach.
* The second line contains the natural numbers $x_B$, $y_B$, $d_B$, representing Mr. Boca's position and the distance from which he can receive the ball.

# Output data

The file `volei.out` will contain on the first line a natural number $N\\ (N \\in \\{0, 1, 2\\})$, the number of points from which Mr. Boca can receive the ball attacked by Viitorel. On the second line, a number $r$, the required distance, with **three exact decimals**. If $N = 0$ or $N = 1$, `0.000` will be printed.

To print the variable `x` with three exact decimals in the file `fout`, include the `iomanip` library and use the instruction `fout << std::fixed << std::setprecision(3) << x;`.

# Constraints and clarifications

* $-20000 \\leq x_V, y_V, x_B, y_B\\leq 20000$
* $1 \\leq d_V, d_B \\leq 20000$
* It is guaranteed that the points $(x_V, y_V)$ and $(x_B, y_B)$ are distinct.
* It is recommended to use the `double` data type for real numbers (instead of `float`).

# Example

`volei.in`
```
3 4 2
9 6 5
```

`volei.out`
```
2
2.641
```

## Explanation

~[circlefin.png|width=40%]