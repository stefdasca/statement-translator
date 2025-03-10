Viitorel has several matches (of the same length) at his disposal and he has decided to make triangles (with $3$ sides) and hexagons (with $6$ sides) out of them.

~[gons.png|align=center|width=35%]

# Task

Knowing the number of matches Viitorel has, what is the minimum and the maximum number of geometric figures (triangles and hexagons) he can construct so that **he is left with as few matches as possible**?

# Input data

You are given a natural number representing the number of matches Viitorel has at his disposal.

# Output data

Two natural numbers **separated by space** will be printed: the first represents the minimum number of triangles and hexagons he can construct, and the second represents the maximum number of triangles and hexagons.

# Constraints and clarifications

* The number of matches is between $0$ and $10^9$ inclusive.
* Each match can be used for at most one geometric figure (the same match cannot be used for multiple figures).

# Example

`stdin`
```
16
```

`stdout`
```
3 5
```

## Explanation

For the minimum number of figures: he can construct two hexagons and one triangle, leaving him with one unused match.  
For the maximum number of figures: he can construct five triangles, leaving him with one unused match.