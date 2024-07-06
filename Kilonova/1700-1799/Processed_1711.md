In the country of Oblio, everything is triangular. Even photographs are triangular. Photographs consist of pixels, which are, of course, triangles themselves as shown in the figure below.

~[triunghi.png]

The photographs are black and white, and each pixel is identified by its row and position, i.e., the nth triangle in the respective row counted from $1$, from left to right. Each pixel is either white or black. Each pixel has a size of $1$, but multiple neighboring pixels can form triangles with the apex upwards and of various side lengths. The figure on the right shows $3$ triangles of size $1$ (row $2$ position $1$, row $3$ position $1$, row $3$ position $3$) and one triangle of size $2$ (with corners: in row $2$ position $1$, row $3$ position $1$ and row $3$ position $3$).

It is known that the photograph has $n$ rows and $m$ white pixels, each pixel being identified by row and position.

# Task

Determine, for $p$ given side lengths, how many black-colored triangles (i.e., filled only with black pixels) with the apex upwards are found in the photograph for each length.

# Input data

The file `triunghi.in` contains on the first line, separated by spaces, the numbers $n$, $m$, $p$ as specified in the problem. The next $m$ lines contain two numbers each representing the row and position of each white pixel. The next $p$ lines contain one natural number each representing a side length of black-colored triangles that need to be counted.

# Output data

The file `triunghi.out` contains $p$ lines, each line contains the answer to one of the $p$ questions, in the required order from the problem statement.

# Constraints and clarifications

* $1 \leq n \leq 1\ 500$
* $0 \leq m \leq \min(n \cdot n, 10\ 000)$
* $1 \leq p \leq n$

# Example 1

`triunghi.in`
```
3 3 2
1 1
2 3 
3 5
2
1
```

`triunghi.out`
```
1
3
```

## Explanation

See the top-right figure.

# Example 2

`triunghi.in`
```
4 0 2
1
3
```

`triunghi.out`
```
10
3
```

