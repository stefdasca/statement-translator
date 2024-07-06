Gigel needs to design the water installation in his own yard. The yard has infinite dimensions and is not fenced. He knows the coordinates of the point where the water source is located and the coordinates of the point where he will install a tap. The pipeline must be designed so that the two points are connected. For this, he has $n$ pipes in the form of segments whose lengths are known, but which cannot be cut. Two pipes will be connected so that the angle between them is $90 \\degree$, $180 \\degree$, $270 \\degree$, or $360 \\degree$, meaning any horizontal or vertical coupling (up, down, left, right). Some pipes are red while others are painted blue. The red ones can be connected only vertically and the blue ones only horizontally. There can be pipes of the same color and equal lengths, but each pipe will be used in the installation only once.

# Task

Write a program that determines the minimum pipe length necessary to connect the two points.

# Input data

The file `pipe.in` has the following format:

* the first line contains the number $n$;
* the next line contains the Cartesian coordinates of the water source $x_i$, $y_i$, natural numbers separated by a space;
* the next line contains the Cartesian coordinates of the point where the tap will be placed $x_f$, $y_f$, natural numbers separated by a space;
* the next $n$ lines describe each pipe as follows: the character `A` for the color blue or `R` for the color red, followed by a space and then a natural number representing the length of the pipe.

# Output data

The file `pipe.out` will contain the first line a number representing the determined minimum length or the word `impossible` if it is not possible to connect the points with the available pipes.

# Constraints and clarifications

* $1 \\leq n \\leq 100$
* $1 \\leq$ the length of each pipe $\\leq 290$
* $0 \\leq x_i, y_i, x_f, y_f \\leq 32 \ 000$

# Example

`pipe.in`
```
8
2 3
6 8
A 9
R 3
R 13
R 8
A 2
R 4
A 15
R 12
```

`pipe.out`
```
37
```

## Explanation

~[pipe.png|width=38em]