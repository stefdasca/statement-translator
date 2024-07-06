```markdown
In the Triangle commune of Romania, there are $n$ peasants identified by the numbers $1, 2, \ldots , n$. After the year $1990$, the restitution of land areas owned before collectivization began. Each peasant has a document proving they own a single triangular plot of land. Unfortunately, these documents have become troublesome for the mayor (who is in charge of the land restitution), because some portions of the land appear on multiple documents.

In this commune, there is a water well, and it is possible that several peasants claim it. A land area is defined by the coordinates of its three corners, while the well is considered a point, given by its coordinates and surrounded by land only within the plot, not outside.

# Task

Write a program to determine:

1. The codes of the peasants who have documents with land areas that contain the well either inside or on the boundary.
2. The code of the peasant who has a document with a land area that includes all other areas.

# Input data

The input file `triunghi.in` contains the number $n$ of peasants on the first line, and on the next $n$ lines, each line contains $6$ integer values separated by spaces, in the format: $x_1$, $y_1$, $x_2$, $y_2$, $x_3$, $y_3$, which represent the coordinates of the three corners of the triangular area owned by a peasant. ($x_1, x_2, x_3$ are abscissae, and $y_1, y_2, y_3$ are ordinates).

On line $i+1$ are the coordinates of the corners of the triangular land area owned by peasant $i$, $i = 1,2, \ldots , n$.

The last line of the file (line $n+2$) will contain the coordinates of the well in the format $x \ y$, with space between them ($x$ abscissa, and $y$ ordinate).

# Output data

The output file `triunghi.out` will contain on the first line the answer to point $1$, that is: the number of peasants who meet the condition from the task and then their codes (in ascending order), with a space between them. If there are no peasants meeting the condition from the task, the figure $0$ will be written on the first line.

On the second line will be the answer to point $2$, that is: the code of the peasant with the required property, or the figure $0$ if there is no such peasant.

# Constraints and clarifications

* $2 \leq n \leq 65$
* the coordinates of the corners of the land areas and the well are integers in the range $[-3000, 3000]$
* the three corners of each land area are distinct and non-collinear
* there are no two peasants owning the same land area
* no partial scores are given

# Example

`triunghi.in`
```
3
10 0 0 10 10 10
0 100 100 0 -100 0
0 0 10 0 0 10
10 5
```

`triunghi.out`
```
2 1 2
2
```

# Explanation

In point $1$, there are two peasants who own land areas that have the well either inside or on the boundary, with codes $1$ and $2$.

In point $2$, the peasant with code $2$ owns a land area that includes the land areas owned by the other peasants (with codes $1$ and $3$).
```