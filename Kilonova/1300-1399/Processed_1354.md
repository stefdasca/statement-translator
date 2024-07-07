
The shooting range is a specially arranged field where exercises are conducted and shootings with firearms are executed. The commander places targets at all points at distances $R_i$, $1 \leq i \leq n$ from the shooting point (origin) and which have Cartesian coordinates that are only non-zero natural numbers.

Romanian armament specialists have recently created a new weapon in the form of a laser cannon that launches its beams on a __straight line__ trajectory and has the ability to destroy all targets on the shooting direction.

# Task

Knowing that the laser cannon is located at the origin of the coordinate system, write a program to determine:

* the number of targets
* the minimum number of laser cannon shots needed to destroy all targets
* the number of targets hit with each shot

~[Poza1.png|align=right]

For example, if we have $n = 6$ distances ($ 5, 7, 10, 13, 15, 17 $) for which targets are being placed, then in the range there will be $10$ targets, $6$ shots will be needed to hit all targets, and respectively $1, 1, 3, 3, 1, 1$ targets will be hit with each shot.

# Input data

The input file `poligon.in` contains on the first line the number $n$ of distances where targets will be placed, and on the second line $n$ distinct non-zero natural numbers separated by a space, representing these distances.

# Output data

The output file `poligon.out` will contain $3$ lines. The first line will contain the number of targets placed in the range. The second line will contain the minimum number of laser cannon shots needed to hit all targets, and the third line will contain the number of targets hit with each shot, separated by a space, in increasing order of the direction angles with the $OX$ axis.

# Constraints and clarifications

* $1 \leq n \leq 1 \ 000$
* $1 \leq R_i \leq 1 \ 000$
* for each input dataset, the range will have at least one target

|#|Points|Constraints|
|:--:|:--:|:--:|
| 1 | $20$% |for the correct determination of the number of targets|
| 2 | $40$% |correct determination of the minimum number of shots|
| 3 | $40$% |correct determination of the number of targets hit with each shot|

# Example

`poligon.in `
```
6
5 10 15 7 13 17
```

`poligon.out `
```
10
6
1 1 3 3 1 1
```

# Explanation

We have $6$ distances: $5, 10, 15, 7, 13, 17$

In the range, there will be $10$ targets (black dots marked on the figure) that can be hit with $6$ shots, and respectively $1, 1, 3, 3, 1, 1$ targets will be hit with each shot.
