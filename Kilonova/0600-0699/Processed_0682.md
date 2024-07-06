Anastasia and Zoe are playing on the board in the classroom. Zoe writes three rows of digits on the board:
$
1531 \\
0982 \\
2453 \\
$

From time to time, Anastasia changes a digit on the board (destroying Zoe's artistic work ☺). After each such change (and before all the changes), Anastasia asks Zoe: in how many ways can you delete columns so that the value from the first row, added to the value from the second row, equals the value from the third row? For example, we can delete the first three columns (which gives us $1 + 2 = 3$), the third column ($151 + 92 = 243$), the third and the last column ($15 + 9 = 24$), or all the columns ($0 + 0 = 0$), so the answer would be $4$.

Help Zoe answer Anastasia's questions!

# Task
On the first line of the input file, you will find the values $N$ and $Q$: the number of digits written by Zoe on each row initially, and the number of changes and questions made by Anastasia.

The next three lines contain $N$ decimal digits each, not separated by spaces. After this, you will find $Q$ lines. A line contains the numbers $i, j, c$: Anastasia changes the digit on row $i$ and column $j$ to $c$.

# Input data
The first line of the input file contains the values $N$ and $Q$: the number of digits written by Zoe on each row initially, and the number of changes and questions made by Anastasia.

The next three lines each contain $N$ decimal digits, not separated by spaces. After these, you will find $Q$ lines. A line contains the numbers $i, j, c$: Anastasia changes the digit on row $i$ and column $j$ to $c$.

# Output data
The output file will contain $Q + 1$ numbers, each on a new line. The first number will represent the answer to Anastasia's question, modulo $1 \\ 000 \\ 000 \\ 007$, before all the changes, and the following numbers will represent the answers after each change, also modulo $1 \\ 000 \\ 000 \\ 007$.

# Constraints
* $1 \\leq N \\leq 100 \\ 000$
* $1 \\leq Q \\leq 100 \\ 000$

## Subtask 1 (20 points)
* $N \\leq 20$
* $Q = 0$

## Subtask 2 (30 points)
* $N \\leq 1 \\ 000$
* $Q \\leq 1 \\ 000$
 
## Subtask (50 points)
* No additional constraints.

# Example

`stdin`
```
4 1
1531
0982
2453
1 1 2
```
`stdout`
```
4
4
```
