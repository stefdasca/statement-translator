Ninel, Gigel's younger brother, received a Tetris game for his birthday in which all the pieces consist of a maximum of `3` squares. There are `4` types of such pieces which, considering the rotations of the pieces, can be placed on a grid in `9` distinct ways:  
\\
~[tris1.png]  
\\
The game contains at least `2` and at most `100` pieces of each type. He wants to place all the pieces such that they form a *cycle*, meaning any square has exactly two neighbors in the four directions (up, down, right, left) and the interior area of the cycle is *connected* in the four directions.

A set of squares is considered a *connected area* if from any square in the set one can reach any other square passing only through the squares in the set in the four directions.

# Task
Knowing the number of pieces of each type, help Ninel solve the problem.

# Input data
The file `tris.in` contains on a single line `4` natural numbers `a b c d`, separated by a space, representing the number of pieces of type `1x1, 2x1, 3x1`, and `L` in this order.

# Output data
The file `tris.out` will contain on the first line two numbers `n` and `m`, representing the dimensions of the solution matrix. On the following `n` lines will be `m` natural numbers from the set `{0, 1, ..., a+b+c+d}`, each element signifying:
* `0` – if there is no element on that position;
* `i` – if there is one of the `a+b+c+d` pieces, identified by the number `i`.

The pieces can be numbered in any order with numbers from `1` to `a+b+c+d`, provided they have distinct numbers.

# Evaluation
A solution is considered valid if and only if the following conditions are met:
- the matrix dimensions are at most `800x800`;
- each cell occupied by a piece has exactly `2` neighbors;
- the area occupied by the pieces forms a cycle;
- the interior area of the cycle is connected in the four directions.

# Constraints and clarifications
* for the input data, the problem always has a solution;
* for `32` points `10 \leq a, b, c, d \leq 100`;
* for `52` points `5 \leq a, b, c, d \leq 100`;
* for `72` points `3 \leq a, b, c, d \leq 100`;
* for `100` points `2 \leq a, b, c, d \leq 100`;
* tests have been added, and the points division has been changed.

# Example

`tris.in`
```
3 4 3 4 
```

`tris.out`
```
11 6
0 1 2 4 4 4
1 1 0 0 0 3
8 0 0 0 3 3
8 0 0 0 9 0
8 0 0 0 9 9
10 0 0 0 0 13
10 0 0 0 0 11
12 0 0 0 0 11
12 0 0 0 0 14
6 0 0 0 0 7
6 5 5 5 7 7
```

\\
~[tris2.png]

We have `3` pieces of type `1x1`  
We have `4` pieces of type `2x1`  
We have `3` pieces of type `3x1`  
We have `4` pieces of type `L`  
The solution matrix consists of `11` rows and `6` columns  

# Note:

\\
~[tris3.png]

The following matrix does not form a solution for multiple reasons:
- there are squares that do not have exactly two neighbors (see pieces `6, 9, 13` and `15`);
- the interior area of the cycle is not connected in the four directions. There are two interior connected areas with `3` squares and `13` squares, respectively.