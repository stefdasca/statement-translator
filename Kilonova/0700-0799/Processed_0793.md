```markdown
The Lucky Gigel just received from his grandfather Nelu, an immense orchard of fruit trees. A former geometry teacher, Nelu rigorously planted fruit trees in $m$ parallel rows, and in each row he planted exactly $n$ fruit trees. However, for reasons more or less objective, Mr. Nelu did not plant all the trees of the same variety in each row, but from several different varieties. The varieties of trees planted in the orchard are coded with natural numbers between $1$ and $p$.
Engulfed by the fever of mathematical rigor and statistics, Gigel defined the notion of *majority variety* as follows: if in a row $k$ consisting of $n$ fruit trees, we have at least $\\lfloor n/2 \\rfloor + 1$ trees of the same variety $x$, then we say that *the variety $x$ is the majority variety in row $k$ (where $\\lfloor y \\rfloor$ denotes the integer part of the real number $y$)*.

# Task

Given the numbers $m, n$ and $p$, as well as the variety of each tree in each row of the plantation, help Gigel determine:

* The number of rows in the orchard that have a majority variety;
* The largest number of consecutive trees of the same variety in a row.

# Input data

The input file `livada.in` contains in the first line three natural numbers $m, n$ and $p$ with the meaning from the statement, and on each of the following $m$ lines there are $n$ numbers, separated by a space, representing the varieties of trees in the respective row.

# Output data

The output file `livada.out` will contain two lines:

* The first line will contain a natural number representing the number of rows in the orchard that have a majority variety;
* The second line will contain a natural number representing the largest number of consecutive trees of the same variety in a row.

# Constraints and clarifications

* $1 \leq m \leq 100$;
* $1 \leq n \leq 700\ 000$;
* $1 \leq m \cdot n \leq 700\ 000$;
* $1 \leq p \leq 998\ 560\ 000$;
* In each row, the difference between the maximum value and the minimum value is at most $250\ 000$.
* If only the value on the first line is correct, $40$% of the score is awarded. If only the value on the second line is correct, $60$% of the score is awarded. If both values are correct, $100$% of the test score is awarded.

# Example

`livada.in`
```
4 7 9
2 1 2 3 8 2 2
4 7 2 4 9 7 4
5 5 2 5 5 5 7
2 3 2 3 2 3 1
```

`livada.out`
```
2
3
```

## Explanation

The plantation consists of $m = 4$ rows, and in each row we have $n = 7$ trees. For a variety to be a majority in a row, there must be at least $\\lfloor 7/2 \\rfloor + 1$ = $4$ trees of that variety in that row. There are majority varieties in two rows: the first and the third. In the third row, there are $3$ consecutive positions where trees of the same variety (variety $5$) are found.
```