Sure, here is the translated text in English with all required specifications:

---

A football field is used for helicopter landings. The grass on the stadium is divided into squares of the same size, with sides parallel to the edges of the field. The rows with squares of grass are numbered from top to bottom with numbers $1, 2, \dots, m$, and the columns with squares of grass are numbered from left to right with numbers $1, 2, \dots, n$. Due to the different type of grass, it is known which of the grass squares are affected by shadow. This is specified by a two-dimensional array $a$ with $m$ rows and $n$ columns, with elements $0$ and $1$ ($a_{ij} = 0$ means that the square located in row $i$ and column $j$ is affected by shadow, and $a_{ij} = 1$ means that the square located in row $i$ and column $j$ is not affected by shadow). Each helicopter has $3$ wheels on which it rests. The wheels of each helicopter determine an isosceles right triangle. Helicopters land in such a way that the triangles formed have their legs parallel to the edges of the field. In the following example, we have four helicopters.

~[elicop.png|width=30em]

To specify the position of a helicopter on the field, it is sufficient to know the row and column of the hypotenuse vertices and the position of the top (coded with $1$) or below the hypotenuse (coded with $-1$). For example, the top left helicopter is given by $(1, 1), (3, 3)$ and $-1$, the top right one by $(1, 9), (5, 5)$ and $1$, the bottom left one by $(5, 1), (6, 2)$ and $1$, and the bottom right one by $(5, 9), (6, 8)$ and $1$.
A helicopter is considered to have landed *wrongly* if the triangle formed under it (defined above) has more than half of the squares affected by shadow.
The football field administrator wants to determine the number $N_1$ of helicopters that do not affect any square on the field and the ordinal numbers of the helicopters that have landed *wrongly* in ascending order: $e_1, e_2, \dots, e_{N_2}$, knowing that there are $k$ helicopters coded by the numbers $1, 2, \dots, k$.

# Task

Write a program that determines, for the data file from the statement: the number of helicopters $N_1$, that do not affect any square on the field, and the ordinal numbers of the helicopters that have landed *wrongly* in ascending order, preceded by their number $N_2$.

# Input data

The first line of the input file `elicop.in` contains two natural numbers $m$ and $n$, separated by a space, with the meaning from the statement. The next $m$ lines contain $n$ numbers $0$ or $1$, separated by a space with the meaning $0$ – square grass that is affected by shadow, respectively $1$ - square that is not affected by shadow. The line $m+2$ contains the number of helicopters $k$, and in the next $k$ lines (in the order of their coding $1, 2, \dots, k$) five numbers separated by a space, for the rows and columns of the hypotenuse and the position of the top ($1$ or $-1$), the right-angled triangles associated with the helicopters: $L_1 \ C_1 \ L_2 \ C_2 \ p$.

# Output data

The output file `elicop.out` will contain two lines: the first line the number $N_1$ of helicopters, which do not affect any square on the field, the second line with the natural numbers $N_2, e_1, e_2, \dots, e_{N_2}$ separated by a space, in ascending order.

# Constraints and clarifications

* $2 \leq m, n \leq 100$
* $1 \leq k \leq 40$
* There are no overlapping triangles associated with two helicopters.
* The triangles associated with helicopters contain at least three squares.
* Correct determination of the $N_1$ values achieves $40$\% of the score of a test, and correct determination of the $N_2, e_1, e_2, \dots, e_{N_2}$ values achieves $60$\% of the score of a test.

# Example

`elicop.in`
```
7 9
1 1 1 1 1 1 1 1 1
0 0 0 0 1 1 1 1 0
0 0 1 0 1 1 1 0 0
1 1 1 0 1 1 0 1 1
0 0 1 1 1 1 0 1 1
1 1 1 1 1 1 0 1 1
1 1 1 1 1 1 0 0 1
4
1 1 3 3 -1
1 9 5 5 1
5 1 6 2 1
5 9 6 8 1
```

`elicop.out`
```
2
2 1 3
```

## Explanation

Helicopters $2$ and $4$ do not affect any square of grass. Helicopters $1$ and $3$ each affect more than half of the number of squares associated with the right triangles and therefore land *wrongly*. Helicopter $1$ shadows $6$ squares, of which $4$ are affected. Helicopter $3$ shadows $3$ squares, of which two are affected.

