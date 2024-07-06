# Andreea and Ioana have $N$ towers of different heights. They place the towers on the table in a straight line, numbering the towers from $1$ to $N$ from the leftmost to the rightmost. The two girls then place a toy soldier in each tower. The soldier in tower $i$ can see any tower $j$ to its left $(j < i)$ if there is **no** tower $k (j < k < i)$ such that tower $k$ has a height strictly greater than tower $i$.

We define the **total visibility** of the soldiers as the sum of the number of towers seen by each soldier. For each tower $i (1 \leq i \leq N)$, the two girls wonder what the total visibility of the soldiers would be if they eliminated tower $i$ from the table.

# Task

Determine the sum of the total visibilities of the soldiers obtained by sequentially eliminating each of the $N$ towers.

# Input data

The first line of the input file `turnuri.in` will contain the natural number $N$, representing the number of towers. The next $N$ lines will each contain the height of tower $i$ on line $i+1$.

# Output data

The output file `turnuri.out` will contain a single line that will print the sum of the total visibilities of the soldiers, total visibilities obtained by sequentially eliminating each of the $N$ towers.

# Constraints and clarifications

* $2 \leq N \leq 1 \ 000 \ 000$;
* The heights of the towers are natural numbers from the interval $[1,2 \cdot 10^9]$ and are **distinct** from each other.

# Example

`turnuri.in`

```
4
7
10
2
5
```

`turnuri.out`

```
10
```

## Explanation

On the table, there are $4$ towers, with heights in order from left to right $7$, $10$, $2$, and $5$. If we eliminate tower $1$, we get the sequence of towers $10, 2, 5$.

|#|$v_1$|$v_2$|$v_3$|
|-|-|-|-|
|Tower height|10|2|5|
|Visibility of soldier|0|1|2|

The total visibility is $3$.

If we eliminate tower $2$, we get the sequence of towers $7, 2, 5$:

|#|$v_1$|$v_2$|$v_3$|
|-|-|-|-|
|Tower height|7|2|5|
|Visibility of soldier|0|1|2|

The total visibility is $3$.

If we eliminate tower $3$, we get the sequence of towers $7, 10, 5$:

|#|$v_1$|$v_2$|$v_3$|
|-|-|-|-|
|Tower height|7|10|5|
|Visibility of soldier|0|1|1|

The total visibility is $2$.

If we eliminate tower $4$, we get the sequence of towers $7, 10, 2$:

|#|$v_1$|$v_2$|$v_3$|
|-|-|-|-|
|Tower height|7|10|2|
|Visibility of soldier|0|1|1|

The total visibility is $2$.