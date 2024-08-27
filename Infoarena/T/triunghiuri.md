## Task

A new criminal group, $Z$, has appeared in your city and is trying to ruin Christmas. It is known that the city's map is a plane with various important locations represented as points on this plane. $Z$ operates in a very specific way: they always attack $3$ points of interest, but only if the area of the triangle formed by these points is an integer (including $0$). Since you are the most skilled programmer, the authorities have asked for your help to save the holidays. Knowing the $N$ initial locations and $Q$ modifications that the map undergoes, you need to create a program that calculates in how many ways the criminals could target $3$ points, both for the initial configuration and after each modification.

## Input data

The input file `triunghiuri.in` contains on the first line the $2$ numbers: $N$ and $Q$. The next $N$ lines contain the coordinates of the $N$ initial points. The next $Q$ lines describe an operation. These operations can be of two types:
- $1 \, X \, Y$ - a new point is inserted at coordinates $(X, Y)$. It is guaranteed that this point does not already exist.
- $2 \, X \, Y$ - a point is deleted from coordinates $(X, Y)$. It is guaranteed that this point already exists.

## Output data

The output file `triunghiuri.out` will contain $Q+1$ lines, the number of ways to choose $3$ points meeting the task conditions, both for the initial configuration and after each update.

## Constraints and clarifications

$1 \leq N \leq 10000$

$0 \leq Q \leq 10000$

$-10^9 \leq x, y \leq 10^9$

All coordinates are integers.

For $50\%$ of the tests, it is guaranteed that $n \leq 100$

$q = 0$

A degenerate triangle (with area $0$) is considered an integer.

A previous modification is preserved for subsequent modifications.

## Example

`triunghiuri.in`

$5 \; 0$

$5 \; 8$

$9 \; 2$

$9 \; 9$

$-6 \; 10$

$-5 \; 7$

`triunghiuri.out`

$5$