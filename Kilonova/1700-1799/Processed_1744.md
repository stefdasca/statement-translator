
At the Romanian Institute of Nuclear Research, experiments are carried out to study the effects obtained by storing radioactive compounds in the storage spaces of an enclosure. The experiment takes place in a square-shaped enclosure with $N \cdot N$ identical storage spaces, arranged like the elements of a square matrix of size $N$. We agree to call the storage spaces cells.

Each cell contains a compound that emits radiation (the amount of radiation emitted is a strictly positive number), absorbs radiation (the amount of radiation â€œemittedâ€ is a strictly negative number) or is neutral in terms of radioactivity (the amount of radiation emitted is $0$). The compound in a cell influences not only the current cell but also the surrounding cells, at a given distance $k$. We define the radioactive factor of a cell as: the value in the current cell $\cdot\ 1$ + (the sum of the values in the cells of the matrix at distance $1$) $\cdot\ (1 - \frac{1}{k})$ + (the sum of the values in the cells of the matrix at distance $2$) $\cdot\ (1 - \frac{2}{k})$ and so on up to distance $k$ where the influence becomes $0$.

For example, for $n = 10$, $k = 4$ and the matrix

~[radioactiv.png]

The radioactive factor of the cell in row $5$ and column $5$ is calculated using the sums of the values in the cells marked by colors: $2 \cdot 1 + (0 + 1 - 1 + 1 + 0 + 2 + 0 + 1) \cdot (1 - \frac{1}{4}) + (0 + 1 + 0 - 1 - 2 - 1 - 3 - 1 + 0 + 1 + 0 + 0 + 0 + 1 + 0 + 0) \cdot (1 - \frac{2}{4}) + (1 + 0 + 2 + 1 + 2 + 0 + 0 + 0 + 0 - 1 + 0 + 2 + 1 - 5 + 0 + 3 + 0 - 1 - 2 + 2 + 0 + 0 + 1 + 1) \cdot (1 - \frac{3}{4})$ = $2 + 3 - \frac{5}{2} + \frac{7}{4}$ = $4.25$

The factor of the cell in row $10$ and column $2$ is: $(-1) \cdot 1 + (-1) \cdot (1 - \frac{1}{4}) + 4 \cdot (1 - \frac{2}{4}) + 0 \cdot (1 - \frac{3}{4}) = -1 + \frac{3}{4} + 2 + 0 = 1.75$

# Task

Determine the number of cells in the matrix where the radioactive factor is minimal.

# Input data

The input file `radioactiv.in` contains on the first line the natural values $n$ and $k$, and on the following $n$ lines, $n$ integer values separated by a space, representing the values in the matrix.

# Output data

The output file `radioactiv.out` will contain on the first line a single natural number representing the number of cells in the matrix where the radioactive factor is minimal.

# Constraints and clarifications

* $n \leq 1\ 000$
* $k \leq 20$
* the values in the matrix are integers with at most $2$ digits

# Example

`radioactiv.in`
```
10 4
1  2 -1 -3  4  1  1  1  1  1
0  1  2  0  0  0  0 -1  1  0
3  2  0 -1 -2 -1 -3  0  1  2
1  0  1  0  1 -1 -1  2  0  0
0  1  0  1  2  1  0  1  0  1
2  1  0  0  2  0  1 -5  0  0
0  1  0  1  0  0  0  0  2  1
1  0  0  2 -2 -1  0  3  1  2
0  0  0  0  1  1  1  1  1  1
-1 -1  0  1 -1  2 -1  3  0  2
```

`radioactiv.out`
```
2
```

## Explanation

The minimum radioactive factor is $-0.25$ and it is obtained in the cell in row $3$ and column $6$ and in the cell in row $4$ and column $6$.
