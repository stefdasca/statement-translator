Below is the translated problem statement:

---

Consider a tower consisting of $n$ cubes: the first one (at the bottom) has a side length $L$. Each cube placed above another has a side length smaller than the one below it, such that it is positioned with the vertices of its base exactly in the middle of the edges of the upper base of the preceding cube.

~[cuburi.png|align=right]

The drawing shows a tower consisting of three cubes which comply with the specified conditions.

# Task:

1. Display the volume of the obtained body;
2. Display the total area of the obtained body (including the lower base of the bottom cube and the upper base of the top cube).
3. Display the height of the tower.
4. Display the minimum number of cubes needed to form a tower with a height of at least $h$, starting from the cube with side length $L$ in the first position (the bottom one). If there are not enough $30 000$ cubes, display the number $-1$.

# Input data

The input file `cuburi.in` contains in the first line the numbers $L$, $n$, and $h$, separated by a space.

# Output data

The output file `cuburi.out` will contain on its first four lines the four results, in the order of: volume, area, height, and the number of cubes necessary to reach the height $h$ (or the value $-1$ if applicable).

# Constraints and clarifications

* $L$ is a strictly positive real number;
* $n$ is a natural number ($n \leq 1\, 000$);
* $h$ is a strictly positive real number.
* Calculations will be done with real numbers, and the display should have $5$ decimal places.
* If a contestant cannot calculate an answer, they will write the number $-1$ on the corresponding line in the output file, otherwise partial points will be lost. Example: if the height (from requirement b) and the area (from requirement c) are missing, the output file will still have $4$ lines as follows: volume in the first line, $-1$ in the second line, $-1$ in the third line, and the required number of cubes in the fourth line.
* Lengths are in $cm$, areas are in $cm^2$, and volumes are in $cm^3$.
* For requirements $1$ and $3$, $10\\%$ of the score is awarded for each, and for requirements $2$ and $4$, $40\\%$ of the score is awarded for each.

# Example 1

`cuburi.in`
```
10.00 2 20
```

`cuburi.out`
```
1353.55339
800.00000
17.07107
3
```

# Example 2

`cuburi.in`
```
10.00 3 40
```

`cuburi.out`
```
1478.55339
900.00000
22.07107
-1
```

---

The translation has preserved the file structure, formatting, and custom image format exactly as required.