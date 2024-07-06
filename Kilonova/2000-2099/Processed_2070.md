```markdown
> *Colegiul Național “Frații Buzești”* ~[logos.png|align=right|width=20rem]
> *Centrul de Pregătire pentru Performanță în Informatică*
> **InfoCNFB** - Edition II, Juniors
> December 9, 2023

# Task

Given a matrix containing $0$ and $1$. It is known that the $1$ elements on each row are adjacent. Determine a full submatrix consisting of $1$, with the top row on the first row of the matrix, and with the maximum area.

# Input data

The file `mmx.in` contains on the first line two numbers $n$ and $m$ representing the dimensions of the given matrix ($n$ represents the number of rows and $m$ the number of columns).

The next $n$ lines contain two numbers separated by a space. The values on the $i$-th of these $n$ lines represent the position of the first and last column where $1$ elements are on the $i$-th row of the matrix.

# Output data

The file `mmx.out` contains on the first line a natural number representing the determined area.

# Constraints and clarifications

* $1 \leq n, m \leq 100\ 000$;
* It is guaranteed that the numbers on lines $2, \dots, n+1$ in the input file are between $1$ and $m$;
* For $21$ points we have $n, m \leq 20$;
* For another $35$ points we have $n, m \leq 100$;

# Example

`mmx.in`
```
4 7
2 6
4 7
1 5
5 5
```

`mmx.out`
```
6
```

## Explanation

```
0 1 1 1 1 1 0
0 0 0 1 1 1 1
1 1 1 1 1 0 0
0 0 0 0 1 0 0
```
```