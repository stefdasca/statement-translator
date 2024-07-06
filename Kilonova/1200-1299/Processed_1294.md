Here is the translated text according to your instructions:

---

As you know from fables, the cricket $\\text{Cri}$ wants to impress the ant $\\text{Fi}$ with his artistic performances. In our story, $\\text{Fi}$ is on a rectangular field, consisting of $m$ rows of plots (numbered from $1$ to $m$), with $n$ plots in each row (numbered from $1$ to $n$). All plots have the same dimensions and in each plot there is exactly one breadcrumb. $\\text{Fi}$ is initially in the plot $(a, b)$, on row $a$, in position $b$ and follows a well-established route, taking the breadcrumb found in each visited plot.

The first plot visited when arriving on a row is considered the reference plot of that row. After visiting the reference plot (on any row $i$), she first visits $k$ plots to the left of the reference plot, then returns to the reference plot on the same path and continues to visit $k$ plots to the right of the reference plot, then proceeds to the next row (row $i + 1$), the reference plot being the one adjacent to the last visited plot on the previous row (row $i$), as shown in the sketch below. On each row $\\text{Fi}$ proceeds the same way, and if at any point the number of plots to the left or right of the reference plot is less than $k$, on that direction she only visits the plots available up to the edge of the field.

~[fi-si-cri.png|align=center]

After visiting $p$ plots, $\\text{Fi}$ reaches the plot with coordinates $(c, d)$ where she meets the persistent $\\text{Cri}$, armed with a collection of the latest melodies.

# Task

Determine the row and the ordinal number within the row of the plot where $\\text{Cri}$ is, as well as the total number of breadcrumbs, $t$, that $\\text{Fi}$ has collected by the time she meets $\\text{Cri}$.

# Input data

In the input file `fi.in`:
* The first line contains $m$ and $n$ (two natural numbers separated by a space)
* The second line contains $k$ and $p$ (two natural numbers separated by a space)
* The third line contains $a$ and $b$ (two natural numbers separated by a space)

# Output data

In the output file `fi.out`:
* The first line contains, separated by a space, the values $c$ and $d$ (the row number and the plot within the row where $\\text{Cri}$ is);
* The second line contains the value $t$ (the total number of breadcrumbs collected).

# Constraints and clarifications

* $1 \\leq m, n \\lt 10 ^ 9$
* $1 \\leq k \\leq \\lfloor \\frac{n}{2} \\rfloor$
* $p \\leq m \\cdot n$
* $1 \\leq a \\leq m$
* $1 \\leq b \\leq n$

# Example 1

`fi.in`
```
4 7
2 17
1 4
```

`fi.out`
```
3 6
12
```

## Explanation

There are $m = 4$ rows with $n = 7$ plots each. $\\text{Fi}$ moves $k = 2$ plots to the left and right of each reference plot, and the $17$ plots visited in order are: $(1, 4)$, $(1, 3)$, $(1, 2)$, $(1, 3)$, $(1, 4)$, $(1, 5)$, $(1, 6)$, $(2, 6)$, $(2, 5)$, $(2, 4)$, $(2, 5)$, $(2, 6)$, $(2, 7)$, $(3, 7)$, $(3, 6)$, $(3, 5)$, $(3, 6)$. She has collected $12$ breadcrumbs (from the plots listed above).

# Example 2

`fi.in`
```
4 10
2 17
1 4
```

`fi.out`
```
1 7 
7
```

## Explanation

There are $m = 4$ rows with $n = 10$ plots each. $\\text{Fi}$ moves $k = 5$ plots to the left and right of each reference plot, but the first row does not have enough plots on the left. The $10$ plots visited in order are: $(1, 4)$, $(1, 3)$, $(1, 2)$, $(1, 1)$, $(1, 2)$, $(1, 3)$, $(1, 4)$, $(1, 5)$, $(1, 6)$, $(1, 7)$. She has collected $7$ breadcrumbs (from the plots listed above).

---

Please let me know if there are any other instructions or if you need further modifications.