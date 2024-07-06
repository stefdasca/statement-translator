```markdown
# Task

RAU-Gigel has a sequence of points, not necessarily distinct, located on the first bisector. The points are characterized by two coordinates (abscissa and ordinate), both integers. When he copied them onto his notebook, carelessly, RAU-Gigel mixed up the coordinates of the $N$ points and omitted the ordinate of one of them. Can you help find it?

# Input data

The input file `bisectoare.in` contains an odd number of lines $(2 \cdot N-1)$, each line containing a single integer $x$ with the significance given in the statement.

# Output data

The output file `bisectoare.out` will contain on the first line an integer representing the ordinate mistakenly omitted.

# Constraints and clarifications

* $1 \leq N \leq 10\ 000$, $-1\ 000\ 000\ 000 \leq x \leq 1\ 000\ 000\ 000$
* the first bisector has the equation $y = x$

# Example

`bisectoare.in`
```
1
-3
5
-3
1
```

`bisectoare.out`
```
5
```
```