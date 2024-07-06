```markdown
On a rectangular shaped field with $L$ rows and $C$ columns, $M$ mines are planted. The rows are numbered from top to bottom with values from $1$ to $L$, and the columns are numbered from left to right with values from $1$ to $C$.

Since the war has ended, specialists want to clear the field of mines and make it available for public use. Moving a mine means transferring a mine from row $x_1$ and column $y_1$ to a free position given by row $x_2$ and column $y_2$, where $1 \leq x_1, x_2 \leq L$ and $1 \leq y_1, y_2 \leq C$.

Since moving a mine is dangerous, we need to determine the **minimum number of mines that need to be moved from their original positions** such that all mines on the field are arranged next to each other in a **compact rectangular area**, anywhere within the given field, so that they can all be detonated together later.

For example: if $L=4$, $C=5$, $M=8$ and the mines are initially positioned as shown in the figure below (the black-colored areas indicate the positions of the mines), the minimum number of mines that need to be moved to achieve a compact rectangular area is $3$.

~[0.png|align=center|width=40em]

# Task
Knowing the number of rows $L$ and columns $C$ of the mined field, the number of mines $M$, as well as the position of each mine, write a program that determines:
1. The row or rows that contain the most mines;
2. The minimum number of mines that need to be moved, so that all the mines on the field are arranged in a compact rectangular area.

# Input data
The input file is `deminare.in` and contains:
- The first line contains the natural number $V$ whose value can only be $1$ or $2$;
- The second line contains two natural numbers $L$ and $C$, as described;
- The third line contains the natural number $M$, as described;
- Each of the following $M$ lines contains a pair of values $x_i$ and $y_i$, $1 \leq i \leq M$, representing the row and column where a mine is located.

The numbers on the same line of the file are separated by a space.

# Output data
The output file is `deminare.out`.
\
If the value of $V$ is $1$, then the first line of the output file will contain the number of the row containing the most mines.
If there are two or more such rows, all their numbers will be printed in ascending order, separated by a space.

If the value of $V$ is $2$, then the output file will contain on the first line the minimum number of mines that need to be moved. If the mines cannot be arranged in a compact rectangular area, the value $-1$ will be written in the output file.

# Constraints and clarifications
- $1 \leq L, C \leq 500$
- $1 \leq M \leq L \cdot C$
- An area where mines are placed on consecutive columns in the same row or placed on consecutive rows in the same column is considered to form a compact rectangular area.
- A compact rectangular area can have the number of occupied rows equal to the number of occupied columns.
- For tests worth 20 points, we have $V=1$.
- For tests worth 70 points, we have $V=2$.
- For tests worth 20 points, we have $V=2$ and $L \cdot C \leq 10\ 000$.
- For tests worth 32 points, we have $V=2$ and $L \cdot C \leq 100\ 000$.

# Example 1
`deminare.in`
```
1
4 5
8
1 2
1 5
2 1
3 2
3 5
4 3
4 4
4 5
```
`deminare.out`
```
4
```
## Explanation
This example corresponds to the figure in the statement.
$V=1$, so only **Task 1** is solved. $L=4$, $C=5$, $M=8$.

Mines are placed at positions $(1,2)$, $(1,5)$, $(2,1)$, $(3,2)$, $(3,5)$, $(4,3)$, $(4,4)$, and $(4,5)$.
On row $1$ there are 2 mines;
On row $2$ there is 1 mine;
On row $3$ there are 2 mines;
On row $4$ there are 3 mines.

So, there is only one row with the maximum number of mines, which is row $4$.

# Example 2
`deminare.in`
```
2
4 5
8
1 2
1 5
2 1
3 2
3 5
4 3
4 4
4 5
```
`deminare.out`
```
3
```

## Explanation
This example corresponds to the figure in the statement.
$V=2$, so only **Task 2** is solved. $L=4$, $C=5$, $M=8$.

Mines are placed at positions $(1,2)$, $(1,5)$, $(2,1)$, $(3,2)$, $(3,5)$, $(4,3)$, $(4,4)$, and $(4,5)$.

To achieve a compact rectangular area, a minimum of 3 mines need to be moved. One possible arrangement is:
The mine from $(1,2)$ is moved to $(3,3)$;
The mine from $(1,5)$ is moved to $(3,4)$;
The mine from $(2,1)$ is moved to $(4,2)$.

This results in a compact rectangular area, with the top-left corner at position $(3,2)$ and the bottom-right corner at position $(4,5)$.
```