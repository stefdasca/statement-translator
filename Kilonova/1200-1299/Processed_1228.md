~[antena.png|align=right]

In the Danube Delta, there is a wild area, cut off from the joys and sorrows of modern civilization. In this area, there are only $n$ houses, their positions being specified by cartesian coordinates on the map. The ONI $2005$ radio station wants to broadcast to all the residents in the area, and therefore, it will need to install a special transmission antenna for this purpose. An antenna transmits radio waves in a circular area. The center of the area coincides with the point where the antenna is positioned. The radius of the area is called the antenna's power. The higher the antenna's power, the more expensive the antenna is.

Therefore, an optimal position for placing the antenna must be selected so that each house is inside or on the boundary of the circular area in which the antenna transmits, and the antenna's power is minimized.

# Task

Write a program that determines an optimal position for placing the antenna, as well as its minimum power.

# Input data 

The input file `antena.in` contains on the first line a natural number $n$, representing the number of houses in the area. The next $n$ lines contain the positions of the houses. More exactly, on line $i+1$ there are two integers separated by a space $x \\ y$, representing the abscissa and the ordinate of house $i$. There are no two houses in the same location.

# Output data

The output file `antena.out` contains on the first line two real numbers separated by a space $x \\ y$ representing the abscissa and the ordinate of the optimal position for placing the antenna. On the second line, a real number representing the antenna's power will be written.

# Constraints and clarifications

* $2 < N < 15\ 001$;
* $-15\ 000 < x, y < 15\ 001$;
* The real numbers in the output file must be written with three decimal places rounded.
* During evaluation, it is checked if the difference between the displayed solution and the correct one (in absolute value) is < $0.01$.

# Example 1

`antena.in`
```
7
5 0
2 6
4 5
2 2
0 2
3 6
5 2
```

`antena.out`
```
3.250 2.875
3.366
```

## Explanation

The antenna will be placed at the coordinates ($3.250, 2.825$), and the antenna's power is $3.366$.