```markdown
James Bond (JB) has a new mission: he must destroy $N$ two-dimensional planets, where there are secret bases (obviously not for JB) of villains. Each planet is shaped like a circle, having a certain number of secret bases on its circumference.
JB will have to place a single bomb on each planet. The bomb can be planted in any of the planet's secret bases. After planting the bomb, JB moves to another planet in a straight line, being able to land only in one of its secret bases. After landing on a new planet, JB can move or not on its circumference to any other secret base, after which he will place a bomb and depart for another planet.
JB cannot return to a planet he previously landed on.
JB has three transportation vehicles at his disposal:

* the teleporter: with which he can move between any two secret bases on different planets.

~[jb1.png]

* the dietachron: with which he can move between any two secret bases on different planets, as long as the path does not intersect the interiors of the departure and/or destination planets. He may intersect the surface of other planets. (see drawings below)

~[jb2.png]

* the hang glider: with which he can move between any two secret bases on different planets, as long as the path does not intersect any planet (including the departure and destination ones).

~[jb3.png]

Regardless of the vehicle used, JB will move between two bases on the same planet only on the circumference of the circle, and the total distance traveled will be the sum of curvilinear path lengths together with the lengths of the straight paths traveled.
On the mission, JB can use only one of the three transportation vehicles. He asks you to calculate the minimum distance he would need to travel using each available vehicle.
Our hero can start his mission at any base of any planet. The mission will end immediately after bombs are placed on all planets. At that moment, JB will destroy them by simultaneously detonating all bombs.

# Task

Determine the three minimum distances.

# Input data

The file `jb.in` contains on the first line $N$ - the number of planets. On the next $2 \cdot N$ lines, the $N$ planets are described, with two lines for each planet. The first line contains four numbers: $X_i \\ Y_i \\ R_i \\ B_i$, representing the coordinates of the center, radius, and number of secret bases on planet $i$.
On the second line, there are $B_i$ pairs of real numbers, representing the coordinates of the bases on planet $i$.

# Output data

The file `jb.out` will contain on the first line three numbers, representing the minimum costs in case of using the teleporter, dietachron, and hang glider respectively.

# Constraints and clarifications

* $1 \leq N \leq 10$
* $1 \leq B_i \leq 50$
* $-1 \ 000 \ 000 \leq X_i, Y_i \leq 1 \ 000 \ 000$
* $0 \leq R_i \leq 100 \ 000$
* If there is no solution for a certain vehicle, print $-1$.
* The numbers will be displayed with $6$ decimals.
* In the ten tests, $N$ will take the following values: $2 \ 3 \ 5 \ 6 \ 7 \ 8 \ 10 \ 10 \ 10 \ 10$
* For each test, you will receive: $3$ points if the first number is correct, $3$ points if the second number is correct, and $4$ points if the third number is correct.
* A number is considered correct if it differs by at most $0.0001$ from the correct value.

# Example

`jb.in`
```
3
100 100 10 4
90 100 100 110 110 100 100 90
0 50 10 3
-10 50 0 60 0 40
0 100 10 2
10 100 -10 100
```

`jb.out`
```
121.231056 161.415927 161.415927
```
```