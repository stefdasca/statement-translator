# Trees

After working his entire life, Macarie decides in his old age to retreat to an island to find inner peace and dedicate himself to nature. Thus, he buys an island where he cultivates fruit trees. The island can be represented as a polygon (not necessarily convex) in a system of positive coordinate axes. The trees are planted only at natural coordinates.

## Task

Macarie is interested in the number of trees that can be planted strictly inside the island. For this purpose, he provides the trees that determine the island (the vertices of the polygon). 

## Input data

The first line of the file `copaci.in` contains the integer $N$, the number of trees on the line. The next $N$ lines contain two integers each, separated by a space, which describe the coordinates of the $N$ trees given in a certain order (counterclockwise or clockwise).

## Output data

The first line of the file `copaci.out` will contain a number that will represent the number of trees strictly inside the island.

## Constraints and clarifications

$3 \leq N \leq 100\ 000$

The coordinates of the trees have integer values from the interval $[0, 2\ 000\ 000]$

More than $2$ trees can be given on a side of the island's polygon (as seen in the example, the penultimate tree)

## Example

`copaci.in`

```
13
3 1
6 3
9 2
8 4
9 6
9 9
8 9
6 5
5 8
4 4
3 5
2 4
1 3
```

`copaci.out`

```
21
```