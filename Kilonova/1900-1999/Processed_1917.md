Here's the translated content:

--- 

Obtaining a triangular grid with side $n$ is done by decomposing an equilateral triangle with side $n$ into equilateral triangles with side $1$, using lines parallel to the sides of the initial triangle. For example, in the figures below, we have triangular grids with side $4$. We call the _nodes of the grid_ the vertices of the triangles with side $1$ used in the decomposition. Thus, in the first grid, we drew an equilateral triangle with vertices in the grid nodes, and in the second grid, we drew two equilateral triangles with vertices in nodes.

~[echilateral.png]

# Task

Write a program that for given $n$, $a$, and $b$, determines the number of equilateral triangles with vertices in the nodes of a grid with side $n$ and whose side lengths are between the values $a$ and $b$.

# Input data

The input file `echilateral.in` contains on the first line the numbers $n$, $a$, and $b$, separated by a space. 

# Output data

The output file `echilateral.out` will contain on the first line the number of equilateral triangles with vertices in the nodes of a grid with side $n$ whose side lengths are between the values $a$ and $b$, **modulo** $666\ 013$.

# Constraints and clarifications

* $1 \leq n \leq 10^9$;
* $1 \leq a \leq b \leq 10^6$;

# Example

`echilateral.in`
```
4 1 2
```

`echilateral.out`
```
29
```

## Explanation

We have $16$ triangles with side $1$ (those that cover the grid). We also have $6$ triangles with side $\sqrt{3}$ (similar to the triangle in the second figure and having one of the sides vertical). We also have $7$ more triangles with side $2$. In total, we have $16+6+7=29$ triangles.

---

I have double-checked the statement and made sure there are no grammar or syntax errors according to the rules of the English language.