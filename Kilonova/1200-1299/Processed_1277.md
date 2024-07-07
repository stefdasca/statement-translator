
A binary matrix $B$ (with values $0$ or $1$) with $N$ rows and $M$ columns is considered, with the rows and columns being numbered from $1$ to $N$ and from $1$ to $M$, respectively.

The matrix $B$ is generated according to the rule $B_{ij} = R_i \oplus C_j$, where $R$ and $C$ are binary arrays of length $N$ and $M$, respectively. We call a rectangle with corners ($x_1, y_1$), ($x_2, y_2$) with $x_1 \leq x_2$ and $y_1 \leq y_2$, the set of elements $B_{ij}$ with $x_1 \leq i \leq x_2$ and $y_1 \leq j \leq y_2$. The area of such a rectangle is ($x_2-x_1+1) \cdot (y_2-y_1+1$).

# Task

Determine the maximum number of elements equal to $0$ in a rectangle whose area is exactly $A$, as well as the number of rectangles for which this maximum number is obtained.

# Input data

The input file `matrice.in` contains:

- The first line contains the natural numbers $N$, $M$, $A$ separated by a space.
- The second line contains $N$ values $0$ or $1$ separated by a space, representing the elements of the array $R$.
- The third line contains $M$ values $0$ or $1$ separated by a space, representing the elements of the array $C$.

# Output data

The output file `matrice.out` will contain a single line with two natural numbers separated by a single space $Z_{max} \ N_{sol}$, representing in order the maximum number of elements equal to $0$ in a rectangle whose area is exactly $A$, as well as the number of rectangles for which this maximum number is obtained.

# Constraints and clarifications

* $1 \leq N, M \leq 30\ 000$;
* $1 \leq A \leq 5\ 000\ 000$;
* For $40$\% of the tests $N, M \leq 300$;
* By $x \oplus y$ is understood the exclusive or operation, more precisely:

|$x \oplus y$|$0$|$1$|
|-|-|-|
|$0$|$0$|$1$|
|$1$|$1$|$0$|

# Example

`matrice.in`
```
2 4 4
0 1
1 0 0 1
```

`matrice.out`
```
2 5
```

## Explanation

Matrix $B$:

```
1 0 0 1
0 1 1 0
```

The maximum number of $0$ values in a rectangle of area $4$ is $2$. The $5$ rectangles of area $4$ with the maximum number of $0$ are:
* ($1, 1$), ($1, 4$);
* ($2, 1$), ($2, 4$);
* ($1, 1$), ($2, 2$);
* ($1, 2$), ($2, 3$);
* ($1, 3$), ($2, 4$);
```
