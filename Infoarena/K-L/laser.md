## Task

Gigel has finished another day of work at his father's store. Now he just needs to turn off the neon lights, lock the showcases, and he can go home. We will consider the store as the $xOy$ coordinate plane. The neon lights will be given as segments in the plane. Gigel is at the coordinates $(0,0)$ and has a laser weapon with which he can shoot in any direction. When Gigel shoots the laser in a certain direction, all the neon lights that intersect with that ray change state (from off to on and from on to off). Knowing the position and initial state of the neon lights, indicate to Gigel in which directions he should shoot to turn off all the neon lights. It is known that the weapon can no longer function after $10\ 000$ shots, so a solution with a number of shots less than or equal to this limit must be indicated.

## Input data

The first line of the input file `laser.in` contains a natural number $N$, the number of neon lights.
The next $N$ lines contain four natural numbers each: $x_1$ $y_1$ $x_2$ $y_2$, the coordinates of the points $(x_1, y_1)$ and $(x_2, y_2)$ representing the ends of the neon lights. The last line of the file contains $N$ numbers with the following meaning: if the $i$th number is $1$, then the neon $i$ is on, otherwise the neon is off.

## Output data

The first line of the output file `laser.out` contains $X$, the number of shots.
The next $X$ lines contain one number each, representing the angle that the direction of the $i$th shot makes with the $Ox$ axis.

## Constraints and clarifications

To receive points on a certain test, $ \ X \leq 10\ 000$

$ 1 \leq N \leq 512 $

$ -10\ 000 \leq x_1, y_1, x_2, y_2 \leq 10\ 000 $

The coordinates of the ends of the segments will be integers.

The solution is not unique, but there is always at least one solution.

The neon lights can intersect each other.

There will be no two ends of neon lights collinear with the origin.

The result will be checked with a precision of $0.00001$, meaning that if the ray representing the direction in which Gigel shoots passes within $0.00001$ of a neon, it will change its state.

Recommendation: display the angles with $6$ decimal places.

The angles for the shots will be expressed in degrees and will be in the interval $[0, 360]$.

## Example

`laser.in`
```
4 
2 1 1 2 
4 5 1 -3 
3 -2 -3 -2 
-1 3 -3 1 
1 1 1 1
```

`laser.out`
```
2 
45.000000 
270.000000
```

## Explanation