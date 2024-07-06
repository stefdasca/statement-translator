Mihai thinks that I am good at computer science and asks me to help him with some calculations. He told me that during the vacation he went to his grandparents' country house. His grandparents are involved in fish farming and have taken over an area of land with lakes, ponds, and pools. Special taxes are paid based on the areas of these water bodies.

His grandfather suspects that the records at the office where the taxes are paid have incorrect data about the areas of these water bodies and asked Mihai to approximately calculate these areas. Mihai studied the problem and decided to walk around each body of water, tracing its outline.

His step length is 1 meter. With each step, Mihai uses a compass and notes in a notebook the direction in which the step was taken $North, South, East,$ or $West$. After each step, Mihai also updates the number of steps he has taken.

# Task

It is required to determine, for each route:

1. The dimensions in the $West - East$ and $North - South$ directions of a minimum rectangular area that contains the entire water surface;
2. The direction in which the route was traveled: $0$ for clockwise, and $1$ for counterclockwise;
3. The area of the enclosed water surface, inside the route.

# Input data

The input file `ape.in` contains on the first line the number $P$ of steps in the route. On the second line, there is a string of $P$ uppercase letters, without spaces between them, from the set $\\{ N,S,E,W \\}$ representing the route.

# Output data

The output file `ape.out` will contain four natural numbers separated by a space: the first number represents the dimension in the $West - East$ direction, and the second number represents the dimension in the $North - South$ direction of the minimum rectangular area that contains within or on its edges the water surface delimited by the route; the third number represents the direction of traversal, and the fourth number represents the area.

# Constraints and clarifications

* $1 \\leq P \\ 10\ 000$
* For $30$% of the tests, the routes will have a maximum length of $2\ 000$
* If the dimensions of the minimum rectangular area are correctly determined, then $10\\%$ of the score/test will be awarded
* If the direction of the route is correctly determined, then $10\\%$ points/test will be awarded
* The area of the water surface is a non-zero natural number

# Example

`ape.in`
```
16
NNVVSVSSESEEENNV
```

`ape.out`
```
3 3 1 5
```

# Explanation

~[Poza1.png]

The cells marked with $-$ represent the route, and the brown squares represent the water.

The area bounded by the bold line represents the minimum rectangular area containing the brown squares, which represent the water.

The cell marked with $*$ is the starting position.