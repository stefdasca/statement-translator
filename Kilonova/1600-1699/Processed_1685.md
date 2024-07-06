```markdown
We have a toy consisting of $N \times N$ squares with side $1$ arranged like in a matrix with $N$ rows and $N$ columns. The rows and columns of the matrix are numbered from $1$ to $N$, and $N$ is always odd. The squares can be white and we will code them as $0$, or black and we will code them as $1$. We divide the matrix into concentric zones as follows: zone $1$ consists of row $1$, column $N$, row $N$, and column $1$; zone $2$ consists of row $2$, column $N - 1$, row $N - 1$, column $2$ etc. There are $ \lfloor \frac{N}{2} \rfloor$ such zones. In the middle of the matrix, there is obviously a single element, $N$ being odd. On any zone, we can apply a rotation operation, **only to the left**. Here is the effect of a rotation operation "of length" $3$ on a zone in the figure below.

~[cubic1.png]

In the figures below, the background colors of the squares only serve to highlight the zones (the dark gray is zone $1$ and the lighter gray is zone $2$). We want to apply a set of rotations to the toy so as to "solve the toy." This means that **all the squares on the middle row and those on the middle column become black**.

~[cubic2.png]

We observe in the right figure that row $3$ and column $3$ are full of $1$. For this, we applied a rotation of length $2$ on zone $1$ and a rotation of length $0$ on zone $2$. We encode this solution with $(2, 0)$. Another solution is the one encoded by $(2, 2)$.

# Task

Given the encoding of the toy, as well as the maximum "length" allowed for a rotation in any zone, determine the number of possibilities to apply rotations to the zones so as to solve the toy. Obviously, a single rotation of a certain length within $0$ and the allowed maximum length can be applied to any zone.

# Input data

The file `cubic.in` contains on the first line two numbers $N$ and $P$, separated by a space, representing the size of the toy respectively the maximum allowed length for rotations in any zone. Each of the next $N$ lines contains $N$ numbers that can be $0$ or $1$, not separated by spaces.

# Output data

The file `cubic.out` contains on the first line the number of possibilities to apply rotations to the zones to solve the toy. Two possibilities are considered distinct if they differ in the length of the rotation in at least one zone. Because this number can be very large, the remainder of its division by $9\ 901$ will be displayed.

# Constraints and clarifications

* $3 \leq N \leq 999$, $N$ is odd.
* $0 \leq P \leq 100\ 000$;

# Example

`cubic.in`
```
5 3
11001
00111
11111
11111
11111
```

`cubic.out`
```
4
```

## Explanation

The solutions are $(2, 0)$, $(3, 0)$, $(2, 2)$, $(3, 2)$.
```