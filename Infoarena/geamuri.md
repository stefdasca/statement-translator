# Windows

Annoyed by so many problems on InfoArena that he couldn't solve and so many rounds of GInfo with identical problems, Geminski grabs his gun and goes to shoot some windows. Once at the scene, he finds himself in front of $N$ rectangular windows, each well-defined with respect to the orthogonal Cartesian system. Geminski has $M$ bullets. When he decides to shoot a bullet, he establishes a well-defined point with respect to the orthogonal Cartesian system, and then he shoots! However, Geminski has some limitations, so he can only shoot from points with coordinates between $1$ and $C$. Each window that contains that point will break. Geminski wants that when he shoots the $i$-th bullet, to break exactly $K_i$ windows.

## Task

Write a program that determines for each bullet Geminski shoots from how many positions he can shoot it to break exactly $K_i$ windows.

## Input data

The first two lines of the input file `geamuri.in` contain the integers $C$ and $N$. The following $N$ lines each contain $4$ integers $x_0$, $y_0$, $x_1$, $y_1$ representing the coordinates of the windows given by the bottom-left and top-right corner $(1 \leq x_0 \leq x_1 \leq C, 1 \leq y_0 \leq y_1 \leq C)$. The next line contains the integer $M$, and the following $M$ lines contain the numbers $K_i$ $(1 \leq i \leq M)$, one per line.

## Output data

The output file `geamuri.out` will contain $M$ lines, with the searched number on each line.

## Constraints and clarifications

$1 \leq C \leq 1024$

$0 \leq K_i \leq N \leq 50000$

$1 \leq M \leq 50000$

The windows can overlap

## Example

`geamuri.in`
```
8
3
2 2 5 4
5 3 6 8
4 4 7 6
2
3
2
1
7
```

`geamuri.out`
```
2
3
2
1
7
```

## Explanations

The first bullet can only be shot from $(5, 4)$

The second from the coordinates $(4, 4)$, $(5, 3)$, $(5, 5)$, $(5, 6)$, $(6, 4)$, $(6, 5)$, $(6, 6)$