In the country of Smar, there are `N` highways, represented as straight lines in a plane. It is known that at intersections of roads (including highways), there is a high risk of accidents. Therefore, the police in this country have decided to establish a compact area that includes all intersections and closely monitors the traffic within it. For financial reasons, the area must have a minimal perimeter.

# Task
Write a program that determines the area of the chosen surveillance zone.

# Input data
From the file `inter.in`, the first line will contain the number of highways, and each of the following `N` lines will contain four real numbers, separated by spaces, representing the coordinates of two distinct points that determine a line. They are given in the order `X1 Y1 X2 Y2`, meaning the abscissa and ordinate of point `1`, then the abscissa and ordinate of point `2`.

# Output data
In the file `inter.out`, the first line will contain a single real number, with two exact decimal places (with truncation), representing the area of the chosen surveillance zone.

# Constraints and clarifications
* Between any two highways, there is exactly one intersection.
* The area of the surveillance surface is strictly positive for the test data.
* For `50` points `N < 501`.
* `2 < N < 5001`

# Example

`inter.in`
```
4
0 0 1 0
0 0 0 2
0 2 1 0
-2 0 0 1
```

`inter.out`
```
3.00
```