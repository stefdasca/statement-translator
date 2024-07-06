# The latest real estate project in the capital is composed of $N$ tower blocks, built next to each other, along a central boulevard and numbered from $1$ to $N$. For each tower, the number of floors it consists of is known, and it is also known that there are no two towers with the same number of floors. The latest urban regulations define the **beauty coefficient** of the tower numbered $T$, as being the number of towers in the sequence that starts with tower $S$, ends with tower $D$, and has the following properties:
* $1 \leq S \leq T \leq D \leq N$
* the number of floors of each tower in the sequence, except for tower $T$, is less than the number of floors of tower $T$
* If $S \neq 1$ then tower $S-1$ is the closest tower to the left of tower $T$, which has a strictly greater number of floors than tower $T$
* If $D \neq N$ then tower $D+1$ is the closest tower to the right of tower $T$, which has a strictly greater number of floors than tower $T$

**The beauty coefficient of the entire ensemble of towers** is the sum of the beauty coefficients of the component towers. The project developer wishes to replace one of the towers and build an underground restaurant in its place, considering this as a tower with **zero** floors. The developer wants to calculate the beauty coefficient of the tower ensemble for each possible location of the restaurant.

# Task

Given the number $N$ of towers and the number of floors of each, determine the beauty coefficient of the tower ensemble for all $N$ possible positions of the restaurant, at positions $1$, $2$, ..., $N$.

# Input data

The input data is read from the file `turnuri.in`, which has the following structure:

* The first line contains the natural number $N$, representing the number of towers.
* The second line contains $N$ non-zero natural values, separated by a space, representing the number of floors of the towers.

# Output data

The output data will be written in the file `turnuri.out`, on separate lines, as follows: on line $i$ ($1 \leq i \leq N$) there is a natural number representing the beauty coefficient of the ensemble if the restaurant were built in place of tower $i$.

# Constraints and clarifications

* $1 \leq N \leq 100\, 000$
* The number of floors of a tower is a natural number between $1$ and $1\, 000\, 000\, 000$
* $10$ points are awarded by default.

| Subtask | Points | Constraints          |
| - | ------- | ------------------- |
| 1 | 30      | $N \leq 100$ |
| 2 | 30      | $N \leq 2 \, 000$      |
| 3 | 30      | No additional constraints.      |

# Example

`turnuri.in`
```
7
10 3 1 7 8 6 5
```

`turnuri.out`
```
19
22
22
22
21
22
22
```

## Explanation

~[turnuri.png]

**Figure $1$** is the graphical representation of the input file. 
If the restaurant is built in place of tower $1$ (see **figure $2**), we have the following beauty coefficients:

* The restaurant has the coefficient $1$ (self)
* Tower $2$ has the coefficient $3$ (sequence composed of towers $1$, $2$, and $3$)
* Tower $3$ has the coefficient $1$ (self)
* Tower $4$ has the coefficient $4$ (sequence composed of towers $1$, $2$, $3$, and $4$)
* Tower $5$ has the coefficient $7$ (sequence composed of all towers)
* Tower $6$ has the coefficient $2$ (sequence composed of towers $6$ and $7$)
* Tower $7$ has the coefficient $1$ (self)