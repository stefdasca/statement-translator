
Matei the Erinaceid has a garden divided into plots in the form of a two-dimensional array, the rows and columns of the garden are numbered starting from `0`.

In the garden, there are `N` fruits, either apples or pears. The `i`-th fruit can be described by a triplet $(x_i, y_i, z_i)$, representing the row, column, and type of fruit (`1` for apples and `2` for pears). Each fruit is located in the center of a plot, and in each plot, there can be at most one fruit.

Initially, Matei is in the `(0, 0)` plot of the garden. He can at any moment move either by row or by column by one unit (from plot `(x, y)` he can move either to plot `(x + 1, y)`, or to plot `(x, y + 1)`).

# Task
Being a hungry erinaceid, Matei wants to gather as many fruits as possible. However, to maintain a balanced diet, he wants the absolute difference between the quantity of apples and pears gathered to be minimal for a solution with the maximum number of fruits collected.

# Input data
The first line contains the number `N` which represents the number of fruits in Matei's garden. The following `N` lines contain the triplets $(x_i, y_i, z_i)$.

# Output data
Print the maximum number of fruits collected and the minimal absolute difference.

# Constraints and clarifications
* `1 \leq N \leq 35\ 000`
* $1 \leq x_i, y_i \leq N$ for any `1 \leq i \leq N`
* $z_i \in \{1, 2\}$ for any `1 \leq i \leq N$

## Subtask 1 (5 points)
* `1 \leq N \leq 100`
## Subtask 2 (5 points)
* `1 \leq N \leq 400`
## Subtask 3 (10 points)
* `1 \leq N \leq 3\ 500`
## Subtask 4 (15 points)
* `1 \leq N \leq 5\ 000`
## Subtask 5 (25 points)
* `1 \leq N \leq 15\ 000`
## Subtask 6 (40 points)
* `1 \leq N \leq 35\ 000`

# Examples

`stdin`

```
4
1 3 1
2 4 1
3 1 2
4 2 2
```

`stdout`

```
2 2
```
Explanations
---

One possible solution is:
$
\\\\ \text{X \\ O \\ O \\ O \\ O} 
\\\\ \text{X \\ O \\ O} \ \\text{\\color{red}{ O} } \ \\text{O } 
\\\\ \text{X \\ O \\ O \\ O } \ \\text{\\color{red}{O}} 
\\\\ \text{X } \ \\text{\\color{lime}{X }}  \text {\\ X \\ O \\ O}
\\\\ \text{O \\ O } \ \\text{\\color{lime}{X} } \ \text {O \\ O \\\\} 
$

`X` denotes the path taken by Matei; `\\color{red}{red}` marks plots containing apples and `\\color{lime}{yellow}` marks plots containing pears.
```
