## Task

In a two-dimensional array with $M$ rows and $N$ columns containing elements of $0$ and $1$, several objects are represented. By object, we mean a group of adjacent $1$s in all directions (a $1$ value can have up to $8$ neighbors). Knowing that there is only one object with the maximum number of $1$ values, the task is:

1. To highlight the object with the maximum number of $1$ values (if it exists) using $2$ values (the $1$ values that compose it will be transformed into $2$ values).
2. To copy the maximal object (the one identified in point $1$) to another free position (with $0$ values), replacing the initial $0$ values with $3$ values if possible. The copy will be made without rotations or reflections (only a translation of the object is desired). If the object can be copied to multiple locations, any of the options can be chosen. The positions where the copy is made can be adjacent to $1$ or $2$ values.

## Input data

The input file `obmax.in` contains:

- The first line contains the numbers $M$ and $N$ separated by a space
- The following $M$ lines contain $N$ values of $0$ and $1$ (the values on the same line are separated by a space)

## Output data

In the output file `obmax.out` you will print the given two-dimensional array, in which the object with the maximum number of $1$ values (if it exists) is marked with $2$ values, and in which the positions occupied by a copy of the object with the maximum number of $1$ values (if copying is possible) are marked with $3$ values. Basically, $M$ lines with $N$ values each will be printed, representing the transformed two-dimensional array.

## Constraints and clarifications

$1 \leq M$
$N \leq 15$

## Example

`obmax.in`
```
6 8
0 0 0 0 0 1 1 0
0 1 1 1 0 0 0 0
0 1 1 0 0 0 0 1
0 1 1 1 0 0 0 1
0 0 0 0 0 0 0 0
0 0 1 1 0 0 0 0
```

`obmax.out`
```
0 0 0 0 0 2 2 0
0 2 2 2 0 0 0 0
0 2 2 0 0 0 0 3
0 2 2 2 0 0 3 3
0 0 0 0 0 0 3 3
0 0 3 3 0 0 0 0
```