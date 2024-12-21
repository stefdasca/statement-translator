
A two-dimensional array with $N$ rows and $N$ columns is given. There are $Q$ distinct positions, labeled with distinct natural numbers from 1 to $Q$, where in the array the value is 1, at all other positions in the array the value is 0. For any given position among the $Q$ provided, we call the "force" of that position the number of submatrices within the given matrix that contain only a single value 1, located at that position, with the rest of the elements in the subarrays being equal to 0.

# Task
For a sequence consisting of $P$ distinct labels, among those corresponding to the given $Q$ positions, it is required to calculate the sum of their "forces".

# Input data
The input file `f1.in` will contain on the first line the natural numbers $N$, $Q$, and $P$, separated by space. On the next $Q$ lines, there will be two natural numbers, separated by space, representing the row and column for each of the $Q$ positions where the value is 1, in the order of their labels. On the next $P$ lines, there is a natural number representing the $P$ labels of the positions for which the sum of the "forces" must be calculated.

# Output data
The output file `f1.out` will contain on the first line a natural number representing the required sum of the "forces".

# Constraints
- $1 \le P \le Q \le 1000$.
- $1 \le N \le 5000$
- The rows and columns of the array are numbered with $1, 2, 3, \cdots, N$.

## Subtask 1 (2 points)
- $Q = 1$

## Subtask 2 (18 points)
- $Q \le 5$

## Subtask 3 (7 points)
- The $Q \le 200$ positions where the value is 1 are strictly ordered in increasing order by rows and then by columns

## Subtask 4 (7 points)
- The $Q \le 200$ positions where the value is 1 are located on the same row

## Subtask 5 (7 points)
- $N \le 10$, $Q \le 200$

## Subtask 6 (12 points)
- $N \le 300$, $Q \le 200$

## Subtask 7 (23 points)
- $N \le 500$, $Q \le 200$

## Subtask 8 (8 points)
- $Q \le 200$

## Subtask 9 (16 points)
- There are no additional constraints

# Example 1
`f1.in`
```
4 1 1
2 2
1
```

`f1.out`
```
36
```

# Example 2
`f1.in`
```
4 3 2
2 2
3 4
4 1
3
1
```

`f1.out`
```
33
```

# Explanation of examples

In the first example, we have an array of size 4x4 and the value 1 at position (2,2). The subarrays containing the position (2,2) have the top-left corner in the area delimited by rows 1 and 2, respectively columns 1 and 2, and the bottom-right corner in the area delimited by rows 2 and 4, respectively columns 2 and 4. In total, 36 subarrays.

In the second example, we have an array of size 4x4 and the value 1 at positions (2,2), (3,4), and (4,1). We must calculate the forces of the positions with the labels 3 and 1, thus of the positions (4,1) and (2,2). The subarrays that contain only the position (4,1) are: those with the top-left corner in the positions (1,1) or (2,1) and the bottom-right corner at position (4,1); those with the top-left corner in (3,1) or (4,1) and the bottom-right corner at (4,1), (4,2) or (4,3); the one with the top-left corner at (4,1) and the bottom-right corner at (4,4). Thus the force of position (4,1) is 2+6+1=9. The subarrays that contain only the position (2,2) are: those with the top-left corner in positions (1,1), (1,2), (2,1) or (2,2) and the bottom-right corner in positions (2,2), (2,3), (2,4), (3,2) or (3,3); those with the top-left corner in (1,2) or (2,2) and the bottom-right corner at (4,2) or (4,3). The force of position (2,2) is equal to 20+4=24. The sum of the two forces is 33.
```
