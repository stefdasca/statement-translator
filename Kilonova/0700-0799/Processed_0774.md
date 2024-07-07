# Task

In a two-dimensional array of given dimensions $m$ (number of rows) and $n$ (number of columns), each cell contains a value 0 or 1. A tower consists only of neighboring 1-values in the same column, where the number of these equal 1-values represents the height of the tower. It is assumed that there are no other 1-values in a column apart from those that are part of a tower.

Each column can contain exactly one tower. If a column has only 0-values, it is still considered to contain a tower with height 0. If a column has one or more 1-values, then one of them is necessarily placed on the last row.

Considering all pairs of 2 towers on neighboring columns, the following reconfiguration operation is possible: from 2 non-zero height towers on 2 neighboring columns, a new tower can be formed with a height equal to the sum of the two. We aim to finally obtain the maximum number of towers with the maximum height. However, there are two conditions that must be met:
- The height of the newly formed tower cannot exceed the value of $m$ (the number of rows in the array);
- Any tower that contributed to the formation of a maximum height tower cannot contribute to the formation of another maximum height tower.

The reconfiguration operation is performed only once.

# Task

Given a two-dimensional array with $m$ rows and $n$ columns with 0 and 1 values, it is required:

1. To display the heights of the towers in the initial configuration, mentioning the towers with height 0, starting with the leftmost tower.
2. To display the maximum height of the towers resulting from the reconfiguration operation.
3. To display the maximum number of towers with maximum height resulting from the reconfiguration operation.

# Input data

The input file `turnuri.in` will contain:

- the first line of the file contains the natural number $m$ representing the number of rows and the natural number $n$ representing the number of columns, values separated by a space.
- the next $m$ lines contain $n$ values 0 or 1, each value separated by a space.

# Output data

The output file `turnuri.out` will contain three lines:

- the first line contains the initial heights of the towers, values separated by a space.
- the second line contains the maximum height of the towers resulting from the reconfiguration operation.
- the third line contains the maximum number of towers with maximum height resulting from the reconfiguration operation.

# Constraints and clarifications

* $2 \leq m, n \leq 1\ 000$;
* Tests and constraints have been updated to the standards of the year 2023.
* Partial scores are awarded: task a) 40% of the points, task b) 40% of the points, task c) 20%.
* All towers start on the last row of the matrix.

# Example 1

`turnuri.in`
```
6 6
0 0 0 0 0 0
1 0 0 0 0 0
1 0 1 0 0 0
1 0 1 1 0 1
1 0 1 1 1 1
1 0 1 1 1 1
```

`turnuri.out`
```
5 0 4 3 2 3
5
2
```

## Explanation

~[turnuri.png|width=38em]

We have 6 towers: the first, the leftmost, has a height of 5, the next 0, the next 4, the next 3, the next 2, and the last 3.

The maximum height is 5 and is obtained from the initial height of tower 1, as well as from combining the last tower with the penultimate or the penultimate tower with the third-last one.

Observation: the tower on column 5 (penultimate) contributes to the formation of only one maximum height tower, either with the tower from column 4 (third-last) or with the one from column 6 (last), but not with both simultaneously. Thus, the number of maximum height towers is 2 (one initial and one formed from the last two towers (or from the penultimate and third-last)). Also, if the third tower were combined with the fourth, a tower with height 7 would result, which is greater than the number of rows in the array (6), meaning an illegal operation.

# Example 2

`turnuri.in`
```
4 4
0 0 0 0
0 0 0 0
1 0 1 0
1 1 1 1
```

`turnuri.out`
```
2 1 2 1
3
2
```

## Explanation

We have 4 towers with initial heights: 2, 1, 2, 1. The maximum height is 3 and is obtained from combining towers 1 and 2, respectively 3 and 4.