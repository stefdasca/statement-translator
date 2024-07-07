
Two natural numbers `N` and `M` are given. Consider an array of numbers of length `N` indexed from `0` to which values must be assigned such that it adheres to `M` constraints of the form:

`0 i val1 val2` - element $i$ can only have the value $val_1$ or $val_2$
`1 i j val` - exactly one of the elements at positions $i$ and $j$ must have the value $val$
`2 i j` - the elements at positions $i$ and $j$ must have different values
`3 i j` - the elements at positions $i$ and $j$ must have the same value

# Task
Determine an assignment of values to the array such that it adheres to the `M` constraints.

# Input data
The first line in the file `valori.in` contains the two natural numbers `N` and `M`.
The second line in the input file contains the `M` constraints.
The first `N` constraints (`N + 1` lines) represent constraints of type `0`.
The next `M – N` lines are constraints of type `1, 2`, or `3`.

# Output data
The output file `valori.out` will contain the values assigned to each element of the array of length `N`.

# Constraints and clarifications
* `1 \leq N \leq 10\ 000`
* `1 \leq M \leq 40\ 000`
* All values in the input will fit within `32` bits.
* Any correct solution can be displayed.
* It is guaranteed that there is at least one solution.

# Example
`valori.in`
```
6 10
0 0 1 2
0 1 1 0
0 2 3 2
0 3 2 3
0 4 1 0
0 5 1 3
1 2 3 2
2 0 4
3 1 0
3 5 1
```
`valori.out`
```
1 1 3 2 0 1
```
