Below is the translated text according to the specified instructions:

```markdown
We define the set of **ordered lattice points** as the set of point pairs in the plane $(x,y)$ with properties: $x$ and $y$ are natural numbers and $x \\geq y$.
# Task
Considering a natural number $N$, write a program that determines the number $T$ of distinct triangles that simultaneously meet the conditions:
* one of the vertices of the triangle is the point with coordinates $(0,0)$;
* the other two vertices are found in two **ordered lattice points** with both coordinates $\\leq N$;
* **inside** or on the **edge** of the triangle **there are no other** **ordered lattice points**.
# Examples
* for $N = 2$, the following triangles exist, so $T = 3$.
~[img1.jpg|width=auto]
* for $N = 3$, the following triangles exist, so $T = 7$.
~[img2.jpg|width=auto]
# Input data
The input file `emptri.in` contains on the first line the natural number $N$, with the above meaning.
# Output data
The output file `emptri.out` will contain on the first line the natural number $T$.
# Constraints and clarifications
* $ 1 \\leq N \\leq 1 \\ 000 \\ 000$;
* Two ordered lattice points $(x_1, y_1)$ and $(x_2, y_2)$ are distinct if $x_1 \\neq x_2$ or $y_1 \\neq y_2$;
* Two triangles are distinct if they differ by at least one lattice point associated with the vertices.

# Example 1

`emptri.in`
```
2
```

`emptri.out`
```
3
```

## Explanation

$N = 2$. There are $3$ triangles having one vertex at the origin and the other two in ordered lattice points with coordinates $\\leq 2$, that do not contain any other ordered lattice points inside or on the edge.

# Example 2

`emptri.in`
```
3
```

`emptri.out`
```
7
```

## Explanation

$N = 3$. There are $7$ triangles having one vertex at the origin and the other two in ordered lattice points with coordinates $\\leq 3$, that do not contain any other ordered lattice points inside or on the edge.
