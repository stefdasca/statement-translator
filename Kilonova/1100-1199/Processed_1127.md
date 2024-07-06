```
# Task

Generate a two-dimensional array with the following properties:

* it contains $N$ rows and $N$ columns;
* its elements are nonzero natural numbers;
* the sum of the elements is equal to the nonzero natural number $S$;
* no two elements in any row or in any column are identical;
* the difference between the largest and smallest element in the array is minimized.

# Input data

The input file is `tablou.in`. It contains the nonzero natural numbers $N$ and $S$.

# Output data

The output file `tablou.out` contains $N$ rows, each with $N$ numbers, representing the elements of the generated array.

# Constraints and clarifications

* $1 < N \leq 100$
* $0 < S < 2^{31}$
* If the problem has no solution, the output file will contain the number $0$.
* If the problem has multiple solutions, only one will be provided in the file.

# Example

`tablou.in`
```
3 51
```

`tablou.out`
```
4 6 7
7 4 5
5 7 6
```
```