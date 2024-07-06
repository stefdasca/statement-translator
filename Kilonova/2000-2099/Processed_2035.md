Nemo has decided to create a game for his friends. Because he doesn't have 3D graphics knowledge, he decided to make a 2D game. In the $XOY$ coordinate system, he draws $N$ non-degenerate rectangles with integer coordinates for corners, and the sides are parallel to the coordinate axes. Additionally, in this system, he has two points with integer coordinates $(x_S, y_S)$ and $(x_F, y_F)$. The game's goal is to find the minimum distance from point $(x_S, y_S)$ to point $(x_F, y_F)$ bypassing the interiors of the rectangles but being able to move on their borders. Since Nemo doesn't have such knowledge, he offers you 100 points if you play this game for him.

# Input data

The first line of the file `game2d.in` contains the value $N$ representing the number of rectangles. The second line contains the four numbers $x_S, y_S, x_F, y_F$. The following $N$ lines contain the coordinates of each rectangle given by the top-left corner $(x_{ST}, y_{ST})$ and the bottom-right corner $(x_{DR}, y_{DR})$.

# Output data

The first and only line of the file `game2d.out` must contain a real number with 6 decimals representing the required minimal distance.

# Constraints and clarifications

* $1 \leq N \leq 750$
* $1 \leq x, y \leq 2\, 000\, 000\, 000$ (for any coordinates appearing in the problem data)
* It is guaranteed that any two rectangles do not intersect at any point.
* It is guaranteed that the start point and the end point are outside any rectangle.
* The area of any rectangle will not exceed $10\, 000\, 000$
* Maximum score is given only if the difference between your result and the correct result is less than $10^{-6}$.
* Nemo advises you to use `long long` and `double` types in the implementation.

# Example 1

`game2d.in`
```
2
1 1 4 5
1 5 2 4
4 2 5 1
```

`game2d.out`
```
5.000000
```

## Explanation

The minimum distance between the point $(1,1)$ and the one with coordinates $(4, 5)$ is exactly the distance between the two points.

# Example 2

`game2d.in`
```
4 
6 5 1 1
5 4 6 3
2 4 4 2
2 6 4 5
1 8 2 7
```

`game2d.out`
```
6.812559
```

# Example 3

`game2d.in`
```
3 
1 4 4 4
1 2 4 1
2 5 3 3
1 7 4 6
```

`game2d.out`
```
3.828427
```

# Example 4

`game2d.in`
```
4 
1 9 8 1
2 3 3 1
6 3 7 1
4 5 5 2
1 7 8 6
```

`game2d.out`
```
12.187601
```

# Example 6

`game2d.in`
```
4 
1 1 5 6
1 5 2 4
2 3 3 2
3 5 4 4 
4 2 5 1
```

`game2d.out`
```
6.708204
```

