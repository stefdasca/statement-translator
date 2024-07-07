
Ionuț learned at school how to work with large numbers. He has a sequence of $N$ non-zero natural numbers at his disposal. From each number, he deletes **exactly** three digits, without changing the order of the remaining digits, so as to obtain the smallest possible natural **non-zero** number. For example, from the number ~[image.png|align=right] $20731049$ he obtains the number $20049$, and from the number $13004$ he obtains the number $10$. Replacing each read number with the number obtained through the above operation, Ionuț obtains a new sequence and writes its terms on the faces of some cubes as follows: he writes the first six numbers from the sequence on the first cube and labels it with $1$, he writes the next six numbers from the sequence on another cube which he labels with $2$, and so on.

These cubes were distributed in pyramids according to the model in the figure above. The pyramids were numbered with consecutive natural numbers. The pyramid with order number $1$ consists only of the cube with order number $1$ and has a single level, the pyramid with order number $2$ has on the first level the cubes $2, 3$ and $4$ and on the last level the cube $5$ and so on.

Two adjacent levels within a pyramid differ by exactly two cubes. The first level of a pyramid contains two cubes more than the first level of the previous pyramid. A pyramid is considered complete if on the last level it has a single cube.

# Task

Write a program that reads the non-zero natural numbers $N$ and $K$, then the $N$ natural numbers that are part of the initial sequence, and determines:

1. The number of complete pyramids constructed by Ionuț.
2. The numbers written on the cubes from the first $K$ pyramids.

# Input data

The file `cuburi.in` contains **two lines**: the first line contains two natural numbers, $N$ and $K$, and the second line contains $N$ natural numbers. Each line in the file contains numbers separated by a space.

# Output data

The file `cuburi.out` contains two lines: the first line contains the number of complete pyramids that have been constructed, and the second line contains all the numbers written on the cubes that form the first $K$ pyramids. The numbers are written separated by a space, in the order they appear in the newly obtained sequence.

# Constraints and clarifications

* $6 \leq N \leq 100 \ 000$
* It is guaranteed that at least $K$ complete pyramids can be constructed.
* The $N$ natural numbers on the second line of the input file have a minimum of four digits and a maximum of $9$ digits.
* $20\%$ of the points awarded for the problem will be granted for correctly solving only the first requirement.

# Example

`cuburi.in`
```
31 2
18250 9280 18250 953805 20800 6040065 24208 4405 8794 1720 98886 96400 45544 8560056 36055 60400 80200 11560 36475 26992 68320 69400 20296 72640 34048 57700 66520 47440 91232 26080 90280
```

`cuburi.out`
```
2
10 2 10 305 20 4005 20 4 4 1 86 40 44 5005 30 40 20 10 34 22 20 40 20 20 30 50 20 40 12 20
```

## Explanation

The first $6$ numbers are found on the cube forming the first pyramid, the next $24$ numbers are written, in this order, on the faces of the cubes forming the second pyramid.

Note: In this table, due to insufficient space, the numbers do not appear written on exactly two lines, as in the input/output files.
