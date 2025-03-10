
# Task

We have a sequence of non-zero natural numbers. These represent the heights of some towers placed next to each other in a line (not touching). We ask questions of the form: for a given value $p$, if I draw horizontal lines backwards (to the left) from somewhere between positions $p$ and $p+1$, how many distinct towers can I reach?

~[towers.png|align=center]

For the query with $p=8$, we observe that only tower $8$ is considered reached (even if tower $7$ before it has the same height).

# Input data

The file `towers.in` contains on the first line the number $n$. The second line contains $n$ natural numbers representing the heights of the towers, given in the order of the positions from $1$ to $n$. The next line contains the number of queries $k$. The following line contains the $k$ values $p$ with the above-mentioned significance.

# Output data

The file `towers.out` contains on the first line $k$ numbers, representing the answer for each query, in the order they appear in the input file.

# Constraints and clarifications

* $1 \leq n \leq 100\ 000$;
* $1 \leq k \leq 100\ 000$;
* The heights of the towers are non-zero natural numbers with a maximum of $9$ digits.
* $1 \leq p \leq n;$ in the case $p=n$ we consider lines drawn from anywhere after the last tower.

# Example

`towers.in`
```
8
3 2 6 1 4 2 5 5
2
6 8
```

`towers.out`
```
3 2
```
