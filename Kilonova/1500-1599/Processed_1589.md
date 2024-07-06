~[culori.png|align=right]

On a sheet of a math notebook, there are $N$ rows of boxes that Andrei numbered from top to bottom with values from $1$ to $N$. On each row, Andrei colors one or more boxes using a set of $9$ pencils of different colors, colors that are coded with distinct values from $1$ to $9$. For each row of the notebook, Andrei decides on a number of adjacent boxes that he will color and proceeds as follows: he chooses a pencil with which he colors the first box (the one on the left of his sheet), then proceeds similarly for the second box and so on until he finishes coloring the number of boxes he decided for that row (there can be two or more boxes colored the same). The length of a row is thus determined by the number of all the colored boxes on that row.

# Task

Given the number $N$ of rows with boxes, the number of colored boxes on each row, and the color of each box, write a program that determines:
1. $Lmax$ and $Kmax$, two natural numbers, where $Lmax$ represents the maximum length of a row that has the property that any two adjacent boxes have different colors, and $Kmax$ represents how many such rows are on the sheet.
2. The largest natural number that can be formed by concatenating all the digits corresponding to the colors of the same row, traversed from left to right.

# Input data

The input file `culori.in` contains on the first line two natural numbers $C$ and $N$, where $C$ represents the task number and can have the values $1$ or $2$, and $N$ represents the number of colored rows in Andrei's notebook. On each of the next $N$ lines, natural numbers separated by a space. Each line corresponds to a row of the notebook sheet, in the order of numbering the rows. The first number on each line represents the number of colored boxes on that row, and then the following values represent the color codes used for coloring the boxes on that row, each corresponding to one box, in order, starting with the first on that row (the one on the left), to the last on that row (the one on the right).

# Output data

The output file `culori.out` will contain on the first line:
* for task $1$, two natural numbers $Lmax$ and $Kmax$, in that order and separated by a space;
* for task $2$, a single natural number determined according to the task.

# Constraints and clarifications

* $1 \leq N \leq 10 \ 000$;
* $1 \leq$ number of colored boxes on each row $ \leq 500$;
* for the correct solving of the first task, $27$ points are awarded, and for the correct solving of the second task, $73$ points are awarded;
* for test scenarios worth $10$ points and $C = 2$, the notebook does not contain two rows with the same number of colored boxes;
* for test scenarios worth $23$ points and $C = 2$, the number of boxes on each row is less than or equal to $19$.

# Example 1

`culori.in`
```
1 7
6 4 2 3 1 1 1
5 7 2 3 9 3
2 4 4
6 2 2 7 1 7 7
1 3
4 9 9 9 9
5 7 2 7 2 7
```

`culori.out`
```
5 2
```

## Explanation

The example corresponds to the above image. Task $1$ will be solved. Rows $2$, $5$ and $7$ have the property from the task. The length of row $2$ is $5$, the length of row $5$ is $1$, and the length of row $7$ is $5$. Thus, the maximum length of a row is $5$ and there are $2$ rows of this length. $Lmax=5$ and $Kmax=2$.

# Example 2

`culori.in`
```
2 7
6 4 2 3 1 1 1
5 7 2 3 9 3
2 4 4
6 2 2 7 1 7 7
1 3
4 9 9 9 9
5 7 2 7 2 7
```

`culori.out`
```
423111
```

## Explanation

Task $2$ will be solved. The natural numbers constructed from the digits of each row are: $423111$, $72393$, $44$, $227177$, $3$, $9999$, and $72727$. The largest among them is $423111$.