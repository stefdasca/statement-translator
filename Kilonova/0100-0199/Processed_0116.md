Ovi is a very smart little boy who likes to write on the asphalt with chalk and hop around. He draws a rectangle with red chalk that is exactly `2` meters wide and `N` meters long, which he divides into equal squares with a side length of `1` meter, some of the interior sides being drawn with red chalk, and the rest of the interior sides with white chalk. Ovi starts from the square located in the top-left corner of the rectangle, hopping from one square to an adjacent one either in the same row or column, provided that the side separating the two squares is not colored red. He wishes that through successive hops he can reach all the squares of the rectangle, but he has noticed that only for certain colorings of the sides of the squares is this possible.

In the examples below (with `N=2`), the thickened interior lines are colored red, and the dotted ones are colored white. In the example from `fig. 1`, starting from the top-left corner, it is possible to reach any other square, but in the example from `fig. 2`, it is not possible to reach the squares on the right side.
\
~[patrate1.png]

# Task
Help Ovi to count how many possible ways there are to color the interior sides of the squares with red such that starting from the top-left corner, he can reach any other square through hopping.

# Input data
The file `patrate.in` contains a single natural number `N` representing the length in meters of the rectangle.

# Output data
In the file `patrate.out`, you will write a single natural number (followed by a newline character) representing the number of requested possibilities.

# Constraints and clarifications
* `2 \leq N \leq 1000`

# Example

`patrate.in`
```
2
```

`patrate.out`
```
5
```

Explanation
---
The `5` possibilities are:
\
~[patrate2.png]