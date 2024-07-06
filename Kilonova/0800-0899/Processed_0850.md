A farmer owns a rectangular farm with a length of $m$ meters and a width of $n$ meters. Following the principle of crop rotation, the farmer devised a plan for sowing crops in the new year. Thus, he drew a rectangle divided into $m \cdot n$ cells, each corresponding to one square meter, and colored with different colors the areas corresponding to different crops. A crop can be sown on multiple plots. Two cells that share a common side belong to the same plot if they have the same color (are sown with the same crop). The farmer has the possibility to irrigate a single plot and wants to choose the plot with the largest area. Not satisfied with the resulting area, he wondered if he could change the crop on a single cell to obtain a larger plot area.

Farm example (_image 1_):

~[0.png]

# Task

Given the dimensions of the farm and for each cell the corresponding color of the sown crop, determine:

1. **Variant 1:** The maximum area of a plot in the initial plan.
2. **Variant 2:** The row number, respectively the column number of the cell on which another crop will be sown and the corresponding color of the new crop in order to obtain the largest possible plot.

# Input data

The input file `ferma.in` will contain:

* The first line contains a natural number $v$ ($1 \leq v \leq 2$) indicating the variant of the task to be solved.
* The second line contains two natural numbers $m$ and $n$ separated by a space, with the meaning from the statement.
* Each of the next $m$ lines contains $n$ characters (lowercase letters), representing the codes of the crops to be sown on the $n$ cells corresponding to each line.

# Output data

The output file `ferma.out` will contain:

**Variant 1** – for $v=1$:
* The first line contains the natural number $s$ representing the maximum area of a plot.

**Variant 2** – for $v=2$:
* The first line contains two natural numbers separated by a space, representing the row number, respectively the column number of the cell on which another crop will be sown to obtain a plot with the maximum area;
* The second line contains a character representing the color code of the new crop in the determined cell.

# Constraints and clarifications

* $2 \leq n, m \leq 400$
* The number of distinct crops is at least $2$ and at most $26$.
* $30\%$ of tests will have the value $1$ on the first line, and the remaining $70\%$ of tests will have the value $2$ on the first line.
* For variant $2$, any solution that results in obtaining a plot with the maximum area is scored. No partial scores are awarded.

# Example 1

`ferma.in`
```
1
7 8
rmmgggaa
mvvgggaa
mvvgvvvv
vvvrvvvv
vvrrrgga
vvrrrggg
aaaaaaag
```

`ferma.out`
```
11
```

## Explanation

~[1.png]
This image corresponds to both examples.

In **variant 1**, the maximum area of a plot is determined and displayed, which is $11$ and corresponds to plot $6$, colored green (coded with the letter $v$ in image 1 and in the input file).

# Example 2

`ferma.in`
```
2
7 8
rmmgggaa
mvvgggaa
mvvgvvvv
vvvrvvvv
vvrrrgga
vvrrrggg
aaaaaaag
```

`ferma.out`
```
3 4
v
```

## Explanation

For **variant 2**:
Changing the color of the cell at row $3$ and column $4$ to **green** ($v$) results in a plot with an area of $11+8+1=20$ (joining plots numbered $6$ and $8$).

Another correct solution is:
$4 \ 4$
$v$