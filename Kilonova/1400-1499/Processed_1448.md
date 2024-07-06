~[img1.jpg|align=right|width=auto] The winter holidays have just ended. Florinel wants to help his parents take down the decorations from the Christmas tree. The light tube they used this year is special. It has $N^3$ light bulbs numbered from 1 to $N^3$, and each light bulb that is marked with a prime number will always stay lit. The box in which the tube must be placed is a cube with side length $N$. The light bulb numbered 1 must be placed at the coordinate corner $(1,1,1)$, the rest in a spiral until the level is filled, then the next level in the opposite direction, and so on.
| Level 1 | Level 2 | Level 3 |
|---------|---------|---------|
|~[n1.jpg]|~[n2.jpg]|~[n3.jpg]|

| Face 1 (back) | Face 2 (right) | Face 3 (front) | Face 4 (left) |
|----------------|------------------|------------------|---------------|
|~[f1.jpg]|~[f2.jpg]|~[f3.jpg]|~[f4.jpg]|

# Task
Knowing the side length $N$ of the cube, the cube should be filled with the light tube (the bulbs being connected in ascending order), then determine:
1. The coordinates $(x,y,z)$ of the bulb numbered $V$. ($x$ - row, $y$ - column, $z$ - height);
2. The number of light bulbs placed on each face of the cube.

# Input data

The input file `cub.in` contains on the first line a natural number $p$. For all input tests, the number $p$ can only have the value $1$ or the value $2$. The second line of the input file contains two natural numbers $N$ and $V$ separated by a space representing the size of the cube and the value of the bulb for which the coordinates need to be determined.

# Output data

* If the value of $p$ is $1$, **only Task $1$ will be resolved**. In this case, the output file `cub.out` will contain three natural numbers $x \\ y \\ z$, separated by a space, representing the coordinates of the bulb with the value $V$.
* If the value of $p$ is $2$, **only Task $2$ will be resolved**. In this case, the output file `cub.out` will contain $4$ lines. On each line $i$, a natural number $f_i$ will be written, representing the number of bulbs inscribed with prime numbers on face $i$.

# Constraints and clarifications

* $1 \leq N \leq 200$;
* $1 \leq V \leq N^3$;
* For the correct resolution of the first task, 20 points are awarded, and for the second task, 80 points are awarded.
* For $20\%$ of the tests: $1 \leq N \leq 20$;
* For $30\%$ of the tests: $21 \leq N \leq 100$;
* For $50\%$ of the tests: $101 \leq N \leq 200$.

# Example 1

`cub.in`
```
1
3 10
```

`cub.out`
```
2 2 2
```

## Explanation

**Attention! Only Task 1 is solved for this test**. Row $2$, column $2$, level $2$ – this is bulb $10$.

# Example 2

`cub.in`
```
2
3 10
```

`cub.out`
```
4
3
4
3
```

## Explanation

**Attention! Only Task 2 is solved for this test**.
* $4$ – bulbs inscribed with prime numbers on face $1$: $2$, $3$, $17$, $19$
* $3$ – bulbs inscribed with prime numbers on face $2$: $3$, $5$, $23$
* $4$ – bulbs inscribed with prime numbers on face $3$: $5$, $7$, $13$, $23$
* $3$ – bulbs inscribed with prime numbers on face $4$: $7$, $11$, $19$