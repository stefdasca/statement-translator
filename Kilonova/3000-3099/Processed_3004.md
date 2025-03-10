
The following sequence of numbers is given: 
$1$;  $1 \\ 2 \\ 2$; $1 \\ 2 \\ 3 \\ 3 \\ 3$; $1 \\ 2 \\ 3 \\ 4 \\ 4 \\ 4 \\ 4$; $1 \\ 2 \\ 3 \\ 4 \\ 5 \\ 5 \\ 5 \\ 5 \\ 5$; $\\dots$

In the sequence, we have groups formed according to the following rule: the group $g$ contains natural numbers from $1$ to $g$ in increasing order, followed by $g-1$ values equal to $g (g=1, 2, \\dots)$.

# Task

Write a program that reads a value $k$ and outputs the $k$-th term of the above sequence.

# Input data

The input file `ksir.in` contains on the first line the natural number $k$.

# Output data

The output file `ksir.out` will contain a single line on which a natural number representing the $k$-th element of the sequence will be written.

# Constraints and clarifications

* $1 \\leq k \\leq 20 \\ 000 \\ 000 \\ 000$
* The positions of terms in the sequence are numbered starting with $1$.
* For tests worth $10$ points $1 \\leq k \\leq 20 \\ 000 \\ 000$
* For tests worth $40$ points $20 \\ 000 \\ 000 < k \\leq 2 \\ 000 \\ 000 \\ 000$
* For tests worth $40$ points $2 \\ 000 \\ 000 \\ 000 < k \\leq 20 \\ 000 \\ 000 \\ 000$
* $10$ points are awarded by default.

# Example

`ksir.in`
```
8
```

`ksir.out`
```
3
```
