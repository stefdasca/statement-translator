
~[rotativa_stelara.gif|align=right]

# Task

Evening has settled over the village where young Vasile is, so he can no longer play with the ants. He returns indoors in search of new games in the absence of the internet. Inside, on the table in the living room, rested the trusted flashlight of his grandparents, which according to their words, "illuminates even the stars."

Vasile went outside to count the stars in the sky with his flashlight, but with a small "twist." He can only see the stars that are lit by his flashlight. Because there are no lights at his place in the countryside, the beam of light from the flashlight seems to reach the stars.

The sky is populated by $N$ stars, each with a position in space defined by the coordinates $(x_{s}, y_{s}, z_{s})$. Vasile is now in his yard, at a fixed position considered at coordinates $(0, 0, 0)$. He points the flashlight he uses towards a point with coordinates $(x_i, y_i, z_i)$, and wonders how many of the stars in the sky are visible with the help of the flashlight.

Since Vasile's grandparents noticed he was having fun while he played, they decided to bring him more flashlights, giving him now a total of $L$ different flashlights.

Each flashlight has a visibility angle in the form of a light cone, defined by a maximum angle $\psi$ (in radians). A star is considered visible if the angle between the direction in which the flashlight is pointed and the direction towards the star, being $\theta$, is less than this maximum angle $\psi$. That is, for a star to be visible, we have:

* $\theta < \psi$

# Input data

The first line contains a natural number, $N$, representing the number of stars in the sky, and on the following $N$ lines, three real numbers, $(x_{s}, y_{s}, z_{s})$, representing the coordinates of the stars. The next line contains a natural number $L$, the total number of flashlights. On the following $L$ lines there are four real numbers, $x_i, y_i, z_i, \psi$, where the first three are the coordinates where the flashlight is directed, and $\psi$ represents the maximum angle of the flashlight **in radians**.

# Output data

Vasile wants to find out how many of the stars in the sky he managed to see this evening, even if he knows the answer already.

# Constraints and clarifications

* $1 \leq N \leq 10 \ 000$;
* $1 \leq L \leq 100$;
* $0 \leq x, y, z \leq 5 \ 000$;
* $(x, y, z) \neq (0, 0, 0)$;
* $0 \leq \psi \leq \frac{\pi}{2}$ and it has at most 10 decimals.
* Each coordinate will have exactly two decimal places.

# Example 1

`stdin`
```
5
1.00 1.00 0.00
2.00 2.00 0.00
0.00 1.00 1.00
1.00 0.00 1.00
2.00 0.00 0.00
2
1.00 1.00 0.00 0.8
0.00 1.00 1.00 0.6
```

`stdout`
```
4
```

## Explanation

See the gif above.
$A: 1.0 \text{ } 1.0 \text{ } 0.0$
$B: 2.0 \text{ }2.0\text{ } 0.0$
$C: 0.0 \text{ }1.0\text{ } 1.0$
$D: 1.0 \text{ }0.0\text{ } 1.0$
$E: 2.0 \text{ }0.0\text{ } 0.0$
The first flashlight sees stars A, B, and E. The second flashlight sees star C.
```
