~[tinta.png|align=right]
Alex has a passion for shooting at targets. Playing with numbers, he dreams of a new board for his passion. The dreamed board is square-shaped with $n$ rows and $n$ columns, and the numbers, from $1$ to $n \cdot n$, are positioned in the target, as in the adjacent image.
Alex, being a very good marksman, never hits the squares on the contour. When he hits an inner square, he gets a score equal to the sum of the values in the eight neighboring squares.

# Task

Given $n$ the number of rows and columns of the target:

1. Help Alex build the dreamed target.
2. How many distinct scores can Alex achieve if he has only one arrow?
3. Display the distinct scores found.

# Input data

The input file `tinta.in` contains on the first line the natural number $n$, indicating the number of rows and columns of the target.

# Output data

The output file `tinta.out` will contain on the first $n$ lines $n$ natural numbers each, separated by a space, representing the numbers on the $n$ rows of the target. On the $n + 1$ line, it will contain a single number $p$ representing the number of distinct scores. On the $n + 2$ line, it will contain $p$ natural numbers separated by a space and strictly increasing, representing the distinct scores.

# Constraints and clarifications

* $3 \leq n \leq 1 \ 000$
* Correctly displayed output for the first task will be awarded $40\%$ of the score, and correct outputs for the first two tasks will be awarded $60\%$ of the score.

# Example 1

`tinta.in`
```
3
```

`tinta.out`
```
1 2 6
3 5 7
4 8 9
1
40
```

## Explanation

Alex can only aim at the inner square (the one with $5$), thus he gets only one score, and the sum is $40$.

# Example 2

`tinta.in`
```
4
```

`tinta.out`
```
1 2 6 7
3 5 8 13
4 9 12 14
10 11 15 16
3
45 68 91
```

## Explanation

Alex can only aim at the squares $5$, $8$, $9$, or $12$.