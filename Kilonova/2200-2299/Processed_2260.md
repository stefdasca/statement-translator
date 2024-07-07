
The territory of Metalopolis can be seen as a Cartesian plane. In this territory, Zeratul has managed to infiltrate $N$ invisible soldiers with the mission of defeating his enemy forces, Jim Raynor. The soldiers can be considered points with integer coordinates $(X_S, Y_S)$. To defend himself, Jim Raynor launches $M$ nuclear bombs. Bomb $i$ eliminates all soldiers located at a distance less than or equal to $R_i$ from the point $(XB_i, YB_i)$ where it exploded. To maximize the efficiency of the attack, Raynor ensures that no area of Metalopolis is affected by more than one nuclear bomb. For each bomb $i$, Zeratul wants to know how many soldiers he lost.

# Task

Given the coordinates of the $N$ soldiers, the coordinates, and the ranges of the $M$ bombs, determine for each bomb how many soldiers it eliminates.

# Input data

The first line of the file `nuke.in` contains two natural numbers $N$ and $M$, as described above. The next $N$ lines each contain two integers $XS_i$, $YS_i$ representing the coordinates of the soldiers. The next $M$ lines each contain three integers $XB_i$, $YB_i$, $R_i$ representing the coordinates and the radius of each bomb.

# Output data

In the output file `nuke.out`, print $M$ lines, each line $i$ containing a single natural number representing the number of soldiers eliminated by bomb $i$. The bombs are considered in the order they appear in the input file.

# Constraints and clarifications

* $1 \leq N \leq 200\ 000$
* $1 \leq M \leq 100\ 000$
* $1 \leq R_i \leq 10^9$
* $-10^9 \leq XB_i, YB_i, XS_i, YS_i \leq 10^9$
* A soldier at a distance equal to $R_i$ from bomb $i$ will be eliminated
* The areas of effect of any two bombs do not have any point in common.

# Example

`nuke.in`
```
7 3
4 5
0 5
-1 6
5 1
-1 -2
-3 6
1 4
5 4 3
1 1 1
-1 6 2
```

`nuke.out`
```
2
0
3
```

## Explanation

The first bomb eliminates the soldiers $(4, 5)$, $(5, 1)$.
The second bomb does not eliminate any soldier.
The third bomb eliminates the soldiers $(0, 5)$, $(-1, 6)$ and $(-3, 6)$.
```
