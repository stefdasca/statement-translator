```markdown
On the planet Quadratia, the inhabitants use square shapes in everything they build. They have sent $N$ special defense machines, called rovers, to the planet's surface, which move along trajectories that describe squares. The planet's map can be viewed as a two-dimensional grid with an infinite number of rows and columns, starting from $1$. Each element of this grid is identified by the row number and the column number it is positioned in.

Each rover is described by $3$ positive natural numbers $L, C$, and $R$, representing the position (row $L$ and column $C$) of the element in the top-left corner of the square that describes the trajectory, and the length $R$ of its side, respectively. All rovers initially start from the element in the top-left corner of the square that describes their trajectory, moving clockwise, traversing one element per second. They are programmed to follow this trajectory without stopping. It is possible for multiple rovers to be at the same position on the map at the same time.

The Rectilinians are the only enemies of the Quadratians, differing from them by consistently using straight lines in everything they build. The Rectilinians have built a powerful laser weapon, which they want to use to destroy the Quadratian rovers. The weapon has been placed at position $(1,1)$ on the planet's map, i.e., the element in the first row and the first column.

The weapon can emit a single destructive ray, for one second, deactivating all the rovers that are on the main diagonal of the grid describing the planet's map during that second. The weapon cannot be detected during the first $S$ seconds. The rovers' trajectory may pass through the position where the weapon is placed without being able to detect it during the first $S$ seconds.

~[raza.png]

In the image, we have two rovers, identified by the triplets of numbers $4, 2, 6$ and $6, 9, 4$. The trajectory of the first rover starts from position $(4, 2)$ and has a side length of $6$. The numbers on the trajectory represent the second at which the respective element of the grid is traversed. The rover will return to the initial position at seconds $21, 41, 61, \ldots$ The first rover intersects, on its first pass, the main diagonal at two points: $(4, 4)$ at second $3$ and $(7, 7)$ at second $9$. The second rover intersects the main diagonal at one point, $(9, 9)$ at seconds $10, 22, 34, \ldots$.

# Task

Write a program that solves the following tasks:

1. Determine the number of rovers whose trajectory intersects the main diagonal of the grid describing the map.
2. Determine the maximum number of rovers that can be destroyed simultaneously, in a single second, before the end of the $S$ seconds, as well as the earliest second this can happen.

# Input data

The input data is read from the file `raza.in`, which has the following structure:

* The first line contains the natural number $T \in \{1, 2\}$, indicating the task number to be solved.
* The second line contains the positive natural numbers $N$ and $S$, separated by a space, representing the number of rovers and the number of seconds during which the weapon is not detected.
* The following $N$ lines each contain $3$ positive natural numbers, $L \\ C \\ R$, separated by a space, representing the coordinates of the initial position and the side length of the trajectory of each rover.

# Output data

The output data is printed in the file `raza.out`, which has the following structure depending on the task:

* If $T = 1$, the first line will print the number of rovers whose trajectory intersects the main diagonal;
* If $T = 2$, the first line will print two positive natural numbers, separated by a space, representing the maximum number of deactivated rovers and the earliest second this can happen.

# Constraints and clarifications

* $1 \leq N \leq 10 \ 000$
* $1 \leq S \leq 100 \ 000$
* $1 \leq L, C \leq 50 \ 000$
* $3 \leq R \leq 1 \ 000$
* $1 \leq$ Maximum number of rovers that intersect with the weapon's ray $\leq 1 \ 000$
* For $28$ points, $T = 1$
* For $72$ points, $T = 2$

# Example 1

`raza.in`
```
1
2 100
4 2 6
6 9 4
```

`raza.out`
```
2
```

## Explanation

The task is $1$. The example represents the drawing from the statement.

# Example 2

`raza.in`
```
2
2 5
4 2 6
6 9 4
```

`raza.out`
```
1 3
```

## Explanation

The task is $2$. Only the first rover is destroyed, and the moment when this rover is destroyed is $3$.

# Example 3

`raza.in`
```
1
5 10000
3 3 3
4 7 4
6 4 3
9 2 3
9 7 5
```

`raza.out`
```
4
```

## Explanation

The task is $1$. Four rovers intersect the diagonal.

# Example 4

`raza.in`
```
2
5 10000
3 3 3
4 7 4
6 4 3
9 2 3
9 7 5
```

`raza.out`
```
2 3
```

## Explanation

The task is $2$. The maximum number of rovers that can be destroyed is $2$. This can be achieved earliest at second $3$.
```