In a research laboratory in the field of genetics, a breed of intelligent mice was obtained. To publicly demonstrate this, researchers introduced $k$ mice into cell $X$ of a maze consisting of $n \cdot n$ square cells. Some cells are accessible, while others are not.

On each wall that separates two accessible cells, there is a hole (mouse hole!) through which a single mouse can pass, and the passage takes one second.

The mice are voluntarily participating in this experiment and immediately understood that they have to reach cell $Y$ all together, in the shortest time possible.

# Task

Determine the minimum time needed for all the mice to reach cell $Y$.

# Input data

The file `smart.in` contains on the first line the natural numbers $n$ and $k$, representing the size of the maze and the number of mice who agreed to participate in the experiment, respectively.
On each of the following $n$ lines, there are $n$ characters encoding the maze. The character `0` denotes an initially unoccupied accessible cell, `1` an inaccessible cell, `X` is the accessible starting cell, and `Y` is the accessible destination cell.

# Output data

The file `smart.out` will contain a single line which will print a number $T$, representing the shortest possible time needed for all the mice to reach cell $Y$.

# Constraints and clarifications

* $1 \leq n \leq 50$
* $1 \leq k \leq 100$
* $2 \leq $ number of accessible cells $\leq 300$
* The mice's travel time inside a cell is negligible.
* Any number of mice can be in an accessible cell at a given moment.

# Example 1

`smart.in`
```
3 4
X00
010
0Y0
```

`smart.out`
```
5
```

## Explanation

The example is the one in the figure.

Let's denote the four mice as $s_1$, $s_2$, $s_3$, and $s_4$.
After the first second, $s_1$ passed into cell $B_1$ and $s_2$ into cell $A_2$.
After the second second, $s_1$ reached $C_1$, $s_2$ reached $A_3$, and $s_3$ entered $B_1$.
After the third second, $s_1$ reached $Y$, $s_2$ reached $B_3$, $s_3$ reached $C_1$, and $s_4$ reached $B_1$.
After 4 seconds, $s_2$ reached $C_3$, $s_3$ reached $Y$, and $s_4$ reached $C_1$.
After the fifth second, $s_2$ and $s_4$ reached cell $Y$.

~[pic.jpg]