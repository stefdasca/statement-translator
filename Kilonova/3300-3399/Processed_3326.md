An _interesting octagon_ is a convex figure with a non-zero area and _at most $8$_ sides, where each side is either parallel to the coordinate axes or forms a $45\\degree$ angle with them. All sides parallel to the axes must have an integer length; the other sides must have an integer multiple length of $\\sqrt 2$. Below, we can see some examples of interesting polygons.

~[img1.png|align=center|width=24em]

Let's assume we move along the sides of an interesting polygon counterclockwise. We can observe that the path consists of segments of length $1$ and $\\sqrt 2$ that connect two consecutive points on the path. Thus, these segments can be divided into $8$ different categories, depending on their orientation: north, northeast, east, southeast, south, southwest, west, and northwest.

# Task

Given the maximum number of segments that can be used from each category, determine how many interesting octagons can be formed.

# Input data

The first and only line of the input data contains $8$ integers separated by spaces — the maximum number of segments from the $8$ categories: north, northeast, east, southeast, south, southwest, west, and northwest.

# Output data

Print the number of interesting polygons, modulo $10^9 + 7$.

# Constraints and clarifications

* Let $N$ be the maximum value among the eight input values.
* $N \\leq 1 \\ 000 \\ 000 \\ 000$
* Two interesting octagons are identical if one can be moved over the other _without using rotations_. Additionally, two interesting octagons are identical if and only if they use the same number of segments from each of the $8$ categories.

| # | Points | Constraints          |
| - | ------- | ------------------- |
| 1 | 9      | There are no diagonal segments. |
| 2 | 17      | $N \\leq 100$      |
| 3 | 29      | $N \\leq 2 \\ 000$      |
| 4 | 29      | $N \\leq 200 \\ 000$      |
| 5 | 16      | Without additional constraints      |

# Example 1

`stdin`
```
1 0 1 0 1 0 1 0
```

`stdout`
```
1
```

## Explanation

In the first example, there exists only one interesting octagon, a square of dimensions $1 \\times 1$.

# Example 2

`stdin`
```
1 1 1 1 1 1 1 1
```

`stdout`
```
19
```

## Explanation

In the second example, there are $19$ interesting octagons.

# Example 3

`stdin`
```
2 2 2 2 2 2 2 2
```

`stdout`
```
228
```

# Example 4

`stdin`
```
1 2 3 4 4 3 2 1
```

`stdout`
```
135
```

# Example 5

`stdin`
```
100 100 100 100 100 100 100 100
```

`stdout`
```
636061137
