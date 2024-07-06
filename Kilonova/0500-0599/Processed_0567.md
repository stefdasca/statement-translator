Ținutul ManTeleor este format dintr-un grid infinit în care există $N$ stupi de albine, pentru fiecare stup cunoscându-se poziția acestuia, dată de coordonatele **întregi** $XS[i]$ și $YS[i]$. Întreg ținutul este luminat de o lampă aflată în poziția $(X_L, Y_L)$ (coordonate întregi) care luminează toate zonele aflate la o distanță Alexandria mai mică sau egală cu $D$.

# Task
Aladdin wants to build a house in a position $(X_C, Y_C)$ representing the corner or the center of a square in the grid, so that the construction is illuminated by the lamp, and the Alexandria distance to the nearest beehive is maximized, because our protagonist is *apiphobic* (afraid of bees).

# Input data
The `lampa.in` file will contain on the first line $4$ integers $N, X_L, Y_L, D$, with the meaning described in the statement. Then there will be $N$ lines, each containing two integers, representing the coordinates of a beehive.

# Output data
The first line of the `lampa.out` file will contain $3$ numbers: the Alexandria distance to the nearest beehive, followed by the coordinates of the house, $X_C$ and $Y_C$, separated by a space.

# Constraints and clarifications
* $1 \leq N, D \leq 100\ 000$
* $-1\ 000\ 000\ 000 \leq X_L, Y_L \leq 1\ 000\ 000\ 000$
* $-1\ 000\ 000\ 000 \leq X_C, Y_C \leq 1\ 000\ 000\ 000$
* $-1\ 000\ 000\ 000 \leq XS[i], YS[i] \leq 1\ 000\ 000\ 000$
* The house can be built at integer coordinate points or at the center of squares in the grid.
* The Alexandria distance between two points at coordinates $(x_1, y_1)$ and $(x_2, y_2)$ is defined as $|x_1 - x_2| + |y_1 - y_2|$, where $|x|$ represents the absolute value of $x$.
* For tests worth $20$ points, $N \leq 200, D \leq 100$
* For tests worth another $20$ points, $N \leq 500, D \leq 600$
* For tests worth another $20$ points, $D \leq 750$

# Example:
`lampa.in`
```
3 6 3 2
2 9
1 -1
-2 1
```
`lampa.out`
```
11 8.0 3.0
```

Explanation
---
If we choose the house at the point of coordinates $(8, 3)$, the nearest beehive will be at Alexandria distance $11$.