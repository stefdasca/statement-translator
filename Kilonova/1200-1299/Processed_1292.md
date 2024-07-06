~[melci.png|align=right]
Andrei and Mihai found two snails in the garden of their house. To see how fast they move, they took them into the house where there is a staircase with $n$ steps, each step being $p$ centimeters high and $p$ centimeters wide. Andrei placed his snail on the first step, and Mihai went upstairs and placed his snail on the last step, as shown in the drawing. Thus, the two snails will start moving by traversing the step they are on. To cross the width of a step, the snail moves exactly $p$ centimeters, and to climb or descend a step, the snail also moves $p$ centimeters. The snails' movements are made along the wall.
**Andrei's snail travels** $2$ centimeters in one second. After traveling $2$ centimeters, if it is on an ascending portion, it rests (stays in place) for one second and then continues, but if it is on a step, it does not stop and continues moving.
**Mihai's snail travels** $3$ centimeters in one second. After traveling $3$ centimeters, if it is on a step, it rests for $2$ seconds and then continues, but if it is in descent, it does not rest and continues moving.

# Task

Write a program to determine in which second the two snails collide with each other.

# Input data

The input file `melci.in` contains on the first line the natural numbers $n$ and $p$, separated by a space, where $n$ represents the number of steps and $p$ represents the number of centimeters corresponding to the width and height of a step.

# Output data

The output file `melci.out` will contain on the first line a single natural number, representing the determined number of seconds.

# Constraints and clarifications

* $1 \leq n, p \leq 500$
* A step is a horizontal area without edges and corners; the edges and corners of the steps are part of the ascending or descending portions.

# Example 1

`melci.in`
```
3 2
```

`melci.out`
```
3
```

## Explanation

After the first second, Andrei's snail has traversed the step and is in the corner (so in an area considered ascending) and will have to stay here for one second, so after the first $2$ seconds, it will be in the same place.
After the first second, Mihai's snail has traversed the step and $1 \text{cm}$ of the descending portion. In the second second, it will continue. After the second second, it will reach the edge of the second step (so in an area considered descending) and will continue. In the third second, the snails will collide with each other.

# Example 2

`melci.in`
```
4 1
```

`melci.out`
```
2
```

## Explanation

After the first second, Andrei's snail has traversed the step and the ascending portion and is at the edge (so in an area considered ascending) and will have to stay here for one second, so after the first $2$ seconds, it will be in the same place.
After the first second, Mihai's snail has traversed the step, the descending portion, and the next step, reaching its edge (so in an area considered descending). In the second second, it will continue, and the snails will collide with each other.