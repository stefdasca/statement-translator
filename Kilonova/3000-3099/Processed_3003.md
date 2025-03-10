Robot Vasile has been employed at a candy factory. He needs to package candies into boxes. All the candies are rectangular in shape. Two candies are of distinct types if they differ in at least one of their side dimensions. The robot measures the dimensions of the candies (expressed in millimeters) and needs to package the candies into boxes so that each box contains exactly one candy of each type.

# Task

Write a program that reads the dimensions of the candies and solves the following two tasks:
1. Determine the number of distinct types of candies.
2. Determine the maximum number of candy boxes that robot Vasile can obtain from the existing candies, respecting the conditions mentioned.

# Input data

The input file `robot.in` contains on the first line the task $c$ that needs to be solved ($1$ or $2$). The second line contains the natural number $n$, representing the number of candies. On the following $n$ lines, the dimensions of the candies are provided, one candy per line; a line describing a candy contains two natural numbers separated by a space $lg_1 \\ lg_2$, representing the lengths of the candy's sides.

# Output data

The output file `robot.out` will contain a single line on which a natural number is written, determined according to task $c$.

# Constraints and clarifications

* $2 \leq n \leq 500 \ 000$
* $0 < lg_1, lg_2 < 100$
* Candies can be rotated when being placed in boxes.
* Candies can also be square-shaped (where the two sides have equal lengths), a square being a particular rectangle.
* For tests worth $30$ points, the task is $1$.
* For tests worth $60$ points, the task is $2$.
* $10$ points are awarded for free.

# Example 1

`robot.in`
```
1
7
1 2
3 4
2 1
3 4
5 6
3 4
5 6
```

`robot.out`
```
3
```

# Example 2

`robot.in`
```
2
7
1 2
3 4
2 1
3 4
5 6
3 4
5 6
```

`robot.out`
```
2
```

## Explanations

The $3$ distinct types of candies have dimensions $1 \\ 2$, $3 \\ 4$, $5 \\ 6$. Only two boxes can be obtained, each containing one candy of each type.