
A company produces a new type of rectangular diamonds of different qualities. To calculate the quality of a diamond, the company divides the diamond into `N*M` small squares forming a matrix with `N` rows numbered from `1` to `N` and `M` columns numbered from `1` to `M`. The square on row `i` and column `j` can influence the quality of the diamond in the following way (`1 \leq i \leq N, 1 \leq j \leq M`):
* if the square contains impurities, it is marked with `-1` and will decrease the diamond's quality by `i*j`
* if the square is empty, it is marked with `0` and does not change the diamond's quality
* if the square contains gold, it is marked with `+1` and will increase the diamond's quality by `i*j`.

Each square will be marked with one of the three numbers `(-1, 0, +1)`.

A wealthy client wants to buy as many different diamonds as possible of the same quality `X`. Two diamonds are different if there is at least one square on row `i` and column `j` marked differently in the two diamonds.

# Task

Help the company respond to such requests by writing a program that finds the number of different diamonds of quality `X`.

# Input data

The first line of the input file `diamant.in` contains three integers `N M X` separated by a space, representing the number of rows, the number of columns of a diamond, and the requested quality, respectively.

# Output data

The first line of the output file `diamant.out` will contain the number of different diamonds with the requested quality, modulo `10000`.

# Constraints and clarifications

* `0 < N < 21`
* `0 < M < 21`
* $-2^{31} < X < 2^{31}$

# Example

`diamant.in`
```
2 2 7
```
`diamant.out`
```
3
```

Explanation
---
The matrices corresponding to the `3` diamonds are:
```
-1 +1     +1  0      +1 +1
+1 +1     +1 +1       0 +1
```
```
