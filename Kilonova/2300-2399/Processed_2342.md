~[zuzu.png|align=right]

On planet **Zuzu**, all objects are characterized by the fact that they have a parallelepiped shape. Moreover, even the clouds have the shape of rectangular parallelepipeds. At a given time, the sky darkens and above a region of the planet **Zuzu**, there appear $n$ clouds, all in the shape of rectangular parallelepipeds. Considering a 3D coordinate system with Ox, Oy and Oz axes perpendicular to each other, it is observed that all clouds have all sides parallel to the axes. For each cloud, the coordinates (given in meters) of two corners are known: the top-left-back corner (point $A$) and the bottom-right-front corner (point $B$), as shown in the adjacent figure:

The clouds can pass through each other and can move only in six directions: along the Ox axis (direction denoted by $1$), opposite to the Ox axis (direction denoted by $2$), along the Oy axis (direction denoted by $3$), opposite to the Oy axis (direction denoted by $4$), along the Oz axis (direction denoted by $5$), opposite to the Oz axis (direction denoted by $6$). At each time unit, each cloud moves by $1$ meter in its direction of movement. By interpenetration and merging of clouds, **cloud formations** can form (a cloud formation can also consist of a single cloud). A cloud is part of a cloud formation if it shares at least one rectangular parallelepiped or one rectangle with another cloud in it. The clouds disappear suddenly after $t$ time units.

# Task

Determine the maximum volume of a cloud formation and the time at which this formation is achieved. If there are multiple formations with the same maximum volume, the required time is the minimum one at which such a formation is obtained.

# Input data

The input file `zuzu.in` contains on the first line the natural numbers $n$ and $t$ separated by a space, and on the next $n$ lines seven real numbers $x_A, y_A, z_A, x_B, y_B, z_B, s$ separated by a space. The first three numbers are the coordinates of corner $A$, the next three numbers are the coordinates of point $B$, and $s$ can be one of the digits $1, 2, 3, 4, 5, 6$ and represents the direction of movement for the respective cloud.

# Output data

The output file `zuzu.out` will contain on the first line the volume **(its integer part)**, and on the second line the number of time units from the task.

# Constraints and clarifications

* $2 \leq n \leq 40$
* $1 \leq t \leq 15$
* The coordinates of the parallelepipeds' corners are real numbers with a maximum of $5$ decimal places and do not exceed in absolute value the number $1000$.

# Example

`zuzu.in`
```
3 15
0 0 30 10 10 20 6
20.05 0 5 25 5.3 0 1
10 0 10 20 10 0 2  
```

`zuzu.out`
```
2000
10
```

## Explanation

After $0$ time units, the largest cloud formation has a volume of $1000$ and consists of cloud $1$. After $10$ time units, the largest cloud formation has a volume of $2000$ and consists of clouds $1$ and $3$ (they share a common face). For $15$ time units, no more cloud formations are determined, as they disappear.