Certainly! Here is the translated problem statement:

---

Consider $N$ distinct points in the plane defined by the Cartesian coordinate system $XOY$. Each point is defined by two positive natural numbers representing its abscissa and ordinate. In the plane, we can draw a square anywhere with sides parallel to the system's axes, with side length being a positive natural number.

# Task

Write a program that determines the minimum side length of a square that can be drawn so that it includes at least $K$ points out of the $N$ given points.

# Input data

The input file `puncte.in` contains on the first line the pair of natural numbers $N$ and $K$, representing the number of points in the plane and the minimum number of points that must be within the square of minimum side length, respectively. On the following $N$ lines, there are two natural numbers, $x$ and $y$, separated by a space, representing, in this order, the abscissa and ordinate of each of the $N$ points.

# Output data

The output file `puncte.out` contains on the first line a positive natural number, which represents the determined minimum side length of the square.

# Constraints and clarifications

* $2 \leq N \leq 32\ 000$;
* $2 \leq K \leq N$;
* $1 \leq x_i \leq 5\ 000$ and $1 \leq y_i \leq 5\ 000$, for any $1 \leq i \leq N$;
* A point located on any side of the square, or at any vertex, is considered included in the square;
* For $30\%$ of the input tests $1 \leq N \leq 100$;
* For $50\%$ of the input tests $1 \leq x_i \leq 1\ 000$ and $1 \leq y_i \leq 1\ 000$.

# Example

`puncte.in`
```
7 4
3 2
1 1
1 2
4 3
3 4
6 6
5 2
```

`puncte.out`
```
2
```

## Explanation

The square with the bottom left corner at the point $(3, 2)$ and side length $2$ contains $4$ points, namely: $(3, 2)$, $(4, 3)$, $(3, 4)$ and $(5, 2)$.

---

I have translated the text and ensured the format and mathematical notations remain consistent with the original. Any grammatical or syntax errors have been corrected to comply with English language rules.