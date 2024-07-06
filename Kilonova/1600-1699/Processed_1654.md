In a mountain camp, children from $n$ different regions of the country have gathered. The camp has a sufficient number of identical cabins, each with $n$ beds. The camp director established the following rules for optimal socialization:

* Each cabin must accommodate exactly $n$ people, of which at least $n-1$ must be children, and at most one can be a teacher;
* The children accommodated in each cabin must come from different regions of the country;
* No child or teacher can be accommodated in more than one cabin.

# Task

Determine the maximum number $M$ of cabins that can be filled while respecting the above restrictions.

# Input data

The input file `tabara.in` contains on the first line two natural numbers $n$ and $p$, where $n$ is the number of regions, and $p$ is the number of teachers. The second line contains $n$ natural numbers $c_1$, $c_2$, $\dots$, $c_n$ separated by a space. The value $c_i$ represents the number of children coming from region $i$.

# Output data

The output file `tabara.out` will contain on the first line the natural number $M$.

# Constraints and clarifications

* $2 \leq n, p \leq 50\ 000$
* $1 \leq c_1, c_2, ..., c_n \leq 50\ 000$
* It is possible that not all children and/or teachers will be accommodated after filling the $M$ cabins.
* The total number of people that need to be accommodated will never exceed $2\ 000\ 000\ 000$.

# Example 1

`tabara.in`
```
2 2
1 3
```

`tabara.out`
```
3
```

## Explanation

Coding the two regions with $x$ and $y$, a maximum of $3$ cabins can be filled as follows: $[x_1, y_1]$, $[p_1, y_2]$, $[p_2, y_3]$.

$x_1$ represents the only child from region $1$. $y_1$, $y_2$, $y_3$ represent the three children from region $2$, and $p_1$, $p_2$ are the two teachers.

# Example 2

`tabara.in`
```
3 4
2 3 4
```

`tabara.out`
```
4
```

## Explanation

If the $3$ regions are $x$, $y$, $z$, then $4$ cabins can be filled as follows: $[x_1, y_1, z_1]$, $[x_2, p_1, z_2]$, $[p_2, y_2, z_3]$, $[p_3, y_3, z_4]$.

$x_1$, $x_2$ represent the two children from region $1$, etc. Teacher $p_4$ will not be accommodated.