```markdown
For any two positive integers $N, M,$ we define $lattice(N, M)$ to be those points $(x, y)$ for which $N$ divides $x$ and $M$ divides $y$, and where $x, y$ are non-negative integers. In other words, $lattice(N, M)$ are those points you can reach from $(0, 0)$ by moving a multiple of $N$ steps to the right and a multiple of $M$ steps up. For example, $lattice(2, 3)$ looks like this.

~[lattice1.png|align=center]

# Task

Given $K$ and a list of $P$ points $(x_1, y_1), \dots , (x_P, y_P)$ with integer coordinates in the plane, answer the following problem: For how many positive integer values of $x$ is it true that $lattice(x, x)$ contains at least $K$ of the $P$ points?

# Input data

The first line of input data contains the numbers $P$ and $K$. The next $P$ lines contain the points $(x_i, y_i)$.

# Output data

The first line of output data should contain the answer to the question.

# Constraints and clarifications

* $1 \leq x_i, y_i \leq 1 \ 000 \ 000$
* $1 \leq K \leq P \leq 200 \ 000$

| # | Score | Constraints          |
| - | ------- | ------------------- |
| 1 | 16      | All input values are smaller or equal to $1 \ 000$ |
| 2 | 11      | All input values are smaller or equal to $100 \ 000$      |
| 3 | 15      | $x_i = y_i$ for all points      |
| 4 | 21      | The sequence $x_1, \dots , x_P, y_1, \dots , y_P$ contains pairwise distinct elements.      |
| 5 | 37      | No additional constraints.      |

# Example 1

`stdin`
```
3 2
1 3
3 6
4 2
```

`stdout`
```
1
```

## Explanation

In the first example, only $lattice(1, 1)$ contains at least $2$ points.

# Example 2

`stdin`
```
5 2
2 2
5 10
6 4
15 5
1 7
```

`stdout`
```
3
```

## Explanation

Here, $lattice(1, 1)$ contains all the points, $lattice(2, 2)$ contains the first and third points, and $lattice(5, 5)$ contains the second and fourth points. Below is a graphic showing all the lattices. $lattice(1, 1)$ is the entire graph, $lattice(2, 2)$ is marked by $\\color{red}\\text{red x's}$, and $lattice(5, 5)$ is marked by $\\color{blue}\\text{blue x's}$. Points in all three lattices are marked by $\\color{purple}\\text{purple x's}$. The $P$ points from the input are marked by filled circles $(\bullet)$, and the color indicates in which lattices they are: if a point is only in $lattice(1, 1)$ it is $\\color{gray}\\text{gray}$, if it is in $lattice(1, 1)$ and $lattice(2, 2)$ it is $\\color{red}\\text{red}$, and if it is in $lattice(1, 1)$ and $lattice(5, 5)$ it is $\\color{blue}\\text{blue}$.

~[lattice2.png|align=center]
```