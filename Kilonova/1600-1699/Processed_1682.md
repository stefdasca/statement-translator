```markdown
We define the set of lattice points as the set of pairs of points in the plane $(x, y)$ with the property that $x$ and $y$ are integer numbers.

Let $R$ be a positive natural number and $C(O, R)$ the circle with center at the **origin** of the coordinate system and radius $R$. We denote by $P_1$, $P_2$, $P_3$, $\\dots$, $P_k$ the lattice points found on the circle $C(O, R)$, in a counterclockwise order, starting with the point of coordinates $(R, 0)$. Write a program that determines the number of lattice points $N$ with the following properties:

* **are found** inside or on the circle $C(O, R)$;
* **are not found** inside or on the sides of the polygon $P_1 P_2 P_3 \\dots P_k$.

# Example

For $R = 4$ there are $N = 8$ points with the required properties, as shown in the adjacent figure.

~[points.png|align=right]

# Input data

The input file `points.in` contains the first line number $R$, with the above significance.

# Output data

The output file `points.out` will contain the first line number $N$, with the above significance.

# Constraints and clarifications

* $1 \leq R \leq 5 \cdot 10^7$;

# Example 1

`points.in`
```
4
```

`points.out`
```
8
```

## Explanation

On the circle $C(O, 4)$ we find the following 4 lattice points $P_1(4, 0)$, $P_2(0, 4)$, $P_3(-4, 0)$, $P_4(0, -4)$. The number of lattice points located inside or on the circle $C(O, 4)$ and outside the polygon $P_1 P_2 P_3 P_4$ is $8$.

# Example 2

`points.in`
```
764123
```

`points.out`
```
666556106540
```

## Explanation

There are $666\ 556\ 106\ 540$ points that satisfy the problem's requirements.
```