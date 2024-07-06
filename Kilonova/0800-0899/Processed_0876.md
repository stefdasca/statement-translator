On a rectangular area with sides of lengths $N$ and $M$, there are $N \times M$ squares with a side length of $1$. In the center of each square, there is a pin with negligible thickness. Each pin is described by its height. This area can be represented as a two-dimensional array of size $N$ and $M$, and each element in the matrix represents the height (a positive natural number) of each pin. In the center of the square $(N,M)$, there is a state-of-the-art mobile camera that can rotate $360\degree$ in any plane, located at ground level. The dimensions of the camera are negligible.

For example, if we have the area in the form:
~[0.png|width=20em]
From square $(4,4)$, in the direction `N` (north), the camera will obtain Fig. 1, and in the direction `V` (west) it will obtain Fig. 2.
~[1.png|width=25em]
For the direction `N`, the camera will fully see the pin at coordinates $(3,4)$, and the pin $(2,4)$ will only be partially visible. The pin $(1,4)$ is not visible because it is completely covered by $(2,4)$.
In the direction `V`, the camera will only see the pin $(4,3)$ because $(4,2)$ and $(4,1)$ are completely covered by $(4,3)$.
For the other directions, pins $(3,3)$, $(3,2)$, $(3,1)$, $(2,3)$, $(1,3)$, $(2,2)$, $(2,1)$, $(1,2)$ will be partially or fully visible. The pin $(1,1)$ is not visible due to the pin $(2,2)$, which completely covers it. The pin $(2,2)$ is only partially visible because a part of it is covered by the pin $(3,3)$.

# Task
1. How many pins does the camera see if it can rotate in a vertical plane, only in the directions `N` and `V`?
2. How many pins does the camera see if it can rotate in any plane and in any direction?

# Input data
The input file `ace.in` contains on the first line the number $P$ which can be either $1$ or $2$, for the first or the second task respectively.
The second line contains the numbers $N$, $M$ representing the dimensions of the array, followed by the next $N$ lines with $M$ natural numbers each, separated by a space, representing the heights of the pins.

# Output data
The output file `ace.out` will contain on the first line the number of visible pins for the task indicated by the value of the number $P$.

# Constraints and clarifications
- $2 \leq N \le 1\ 000$
- $2 \leq M \le 1\ 000$
- The elements of the matrix are positive natural numbers smaller than $1\ 000$, except for the number on the line $N$ and column $M$ which is $0$.
- A correct solution for the first task is worth 20 points, a correct solution for the second task is worth 70 points, and 10 points are granted by default.
- For the second task, there are tests worth 20 points with $N,M \leq 50$.
- For the second task, there are tests worth 45 points with $N,M \le 100$.

# Example 1
`ace.in`
```
1
4 4
8 5 4 7
2 7 4 6
5 5 3 2
6 6 3 0
```
`ace.out`
```
3
```
## Explanation
For the first task, we have the directions `N` and `V`:
- For the direction `N`, the camera will fully see the pin at coordinates $(3,4)$, and the pin $(2,4)$ will only be partially visible. The pin $(1,4)$ is not visible because it is completely covered by $(2,4)$.
- In the direction `V`, the camera will only see the pin $(4,3)$ because the pins $(4,2)$ and $(4,1)$ are completely covered by the pin $(4,3)$.

# Example 2
`ace.in`
```
2
4 4
8 5 4 7
2 7 4 6
5 5 3 2
6 6 3 0
```
`ace.out`
```
11
```
## Explanation
For the second task, the camera will see the 3 pins in the directions `N` and `V` (see above) and 8 more - in other directions pins $(3,3)$, $(3,2)$, $(3,1)$, $(2,3)$, $(1,3)$, $(2,2)$, $(2,1)$, $(1,2)$ will be partially or fully visible.

The pin $(1,1)$ is not visible due to the one at $(2,2)$ which completely covers it.
The pin $(2,2)$ is only partially visible because part of it is covered by the pin $(3,3)$.

# Example 3
`ace.in`
```
2
4 3
5 4 7
6 4 6
5 3 2
6 3 0
```
`ace.out`
```
8
```
## Explanation
For the second task, the camera will see in direction `N` pins $(3,3)$ and $(2,3)$, and in direction `V` it will see pin $(4,2)$. In other directions, the camera will see partially or fully pins $(3,2)$, $(3,1)$, $(2,2)$, $(1,2)$, $(1,1)$.