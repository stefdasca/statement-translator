## Task

The king from the planet Ghiocel asks you to transform a diamond into an elegant diamond. An elegant diamond is a two-dimensional object that contains digits and is symmetric relative to both the horizontal and vertical axes.

A diamond of size $k$ extends over $2k-1$ lines, being formed with numbers separated by spaces, organized in the following way:
- Line $i \ (1 < i < k)$ contains $k-i$ spaces, then $i$ digits separated by a space.
- Line $i \ (k \leq i \leq 2k)$ contains $i-k$ spaces and then $2k-i$ digits separated by a space.

A diamond is improved if:
- $0$ or more digits are added
- it is of size $\geq k$
- the original diamond is part of the improved diamond

The cost of an improvement is given by the difference between the number of digits in the improved diamond and the number of digits in the original diamond.

The king gives you a diamond of size $k$ and asks you to improve it to become an elegant diamond, such that the cost of improvement is minimized.

## Input data

The input file `diamante.in` contains $k$ – the size of the diamond on the first line, and on the following $2k-1$ lines, the diamond, as described above.

## Output data

The output file `diamante.out` will contain on the first line the minimum cost required to improve the diamond.

## Constraints and clarifications

1 \leq k \leq 250

## Example

`diamante.in`
```
3 
1 
6 3 
9 5 5 
6 3 
1 
```

`diamante.out`
```
7 
```

## Explanation