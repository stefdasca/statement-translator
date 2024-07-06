```markdown
Two of the most mischievous Dacians in all of history, Danillo and Stegano, thought it would be amusing to dig some tunnels that lead nowhere. They knew that future historians would be very confused about the existence of senseless tunnels and would try to find the reason for their construction, when in fact these tunnels have no purpose.

They found an immense wall where they could start digging, but unfortunately, some parts of the wall are indestructible, so they will have to go around them. For aesthetic reasons, the entrance to the tunnel must be circular.

More precisely, the wall can be described as a Cartesian plane with coordinates $x$ in the interval $[0,M]$ and coordinates $y$ in the interval $[0,N]$. The parts that are indestructible are squares with sides parallel to the axes, of length $1$ and with corners at integer coordinates. The map of areas that can be dug can be described through a binary matrix with $N$ lines numbered from $0$ to $N-1$ and $M$ columns numbered from $0$ to $M-1$. If the element on line $l$ and column $c$ is $1$, then all points $(x,y)$ with $c \leq x \leq c+1$ and $l \leq y \leq l+1$ can be dug. **Pay attention to the difference between the coordinates $(x, y)$ in the plane and the coordinates $(l, c)$ as elements of the matrix.**

When digging a tunnel, the two choose a point with **integer** coordinates $(x,y)$ as the center of the tunnel, and then they choose a radius $r$, and finally, they start digging through all the points that are inside the disk centered at $(x,y)$ with radius $r$. **Be aware that the disk includes all points inside it, not just its circumference, and that the disk must be completely within the defined plane.**

# Task

They want their tunnel to be as noticeable as possible, so they want the tunnel with the largest possible radius. For simpler construction, if there are multiple such tunnels, they will choose the easiest to build among them. If we consider the center of a tunnel to be at coordinates $(x,y)$, they will prefer the tunnel with the smallest $y$. If there are still multiple such tunnels, they will choose the one with the smallest $x$ among these.

# Input data

The first line will contain two integers $N$ and $M$ in this order, defining the plane as well as the size of the binary matrix.

The next $N$ lines each contain a binary string of length $M$ consisting of $0$s and $1$s, representing the elements of the matrix defined above.

# Output data

Print on a single line three integers separated by spaces $x$, $y$ and $R$. $(x, y)$ represents the coordinates of the center of the tunnel that Danillo and Stegano will dig, and $R$ represents the radius of the circle, squared and approximated to the nearest integer. If there is no circle with positive coordinates, print `0 0 0`.

# Constraints and clarifications

* $1 \leq N, M \leq 3\ 000$

| # | Points | Constraints          |
| - | ------- | ------------------- |
| 0 | 0       | The examples |
| 1 | 4      | The matrix contains exactly four cells with $1$.|
| 2 | 9      | The values of $1$ in the matrix form a rectangle with sides parallel to the axes.      |
| 3 | 14     | $N, M \leq 50$    |
| 4 | 15      | $N, M \leq 600$   |
| 5 | 21      | The matrix is randomly generated.    |
| 6 | 37      | No additional constraints    |

# Example 1

`stdin`
```
5 6
011110
111110
011111
111111
011110
```

`stdout`
```
3 2 4
```

## Explanation

~[circles-explanation.png]

# Example 2

`stdin`
```
3 3
010
101
010
```

`stdout`
```
0 0 0
```
```