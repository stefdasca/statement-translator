
# Task

In a geometric design workshop, a skilled craftsman receives a fascinating challenge. On his table lies a rectangular board made of a precious material, with sides $a$ and $b$. His task is to cover the entire surface of this board using only right isosceles triangles – perfect triangles, with equal legs and a well-defined hypotenuse.

But the challenge does not stop there. Each triangle used must have maximum dimensions so that the hypotenuse is as large as possible, and the entire board is completely covered, without gaps or overlaps. All triangles used must have the same dimensions.

Determine the hypotenuse of the ideal triangle for this project and how many such triangles will be necessary to complete the geometric mosaic.

# Input data

The first line of the input file `mozaic.in` contains two natural numbers $a$ and $b$, representing the sides of the rectangular board.

# Output data

The first line of the output file `mozaic.out` should contain, on a single line, separated by a space, the value that represents the hypotenuse length squared and the number of triangles needed.

# Constraints and clarifications

* $1 \leq a, b \leq 1 \ 000 \ 000\ 000$;

# Example

`mozaic.in`
```
12 18
```

`mozaic.out`
```
72 12
```

## Explanation

The square of the hypotenuse of the largest possible right triangle is $72$ and $12$ such triangles are needed to cover the entire surface.
