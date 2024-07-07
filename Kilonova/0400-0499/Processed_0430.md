
A labyrinth is given in the form of a square array with `n \times n` elements `0` and `1`, with the following meaning: `0` represents a free position, and `1` represents an occupied position. A robot located in the labyrinth, on row `L1` and column `C1`, needs to reach a final position on row `L2` and column `C2`. The robot can move horizontally and vertically only.

# Task
Write a program that determines:
1) the minimum number of direction changes for the robot to move from position `(L1, C1)` to position `(L2, C2)`.
2) the minimum number of direction changes for the robot to move from position `(L1, C1)` to position `(L2, C2)`, considering we can transform one occupied position into a free position.
3) the number of obstacles with the property that eliminating any one of them results in the minimum number of direction changes from task 2).

# Input data
The first line of the file `robot.in` contains the natural number `n`.
The next `n` lines each contain `n` values `0` or `1` separated by a space, representing the elements of the labyrinth.
On line `n + 2`, there are the numbers `L1 C1 L2 C2`.

# Output data
The first line of the file `robot.out` contains three natural numbers, separated by a space, representing the answers to the three tasks.

# Constraints and clarifications
* `1 \leq n \leq 1\ 000`
* It is guaranteed that the robot can reach from position `(L1, C1)` to position `(L2, C2)`.
* For `30%` of the cases `n \leq 100`.
* Row and column numbering starts from `1`.
* Correctly solving the first task awards `20%` of the test score. Correctly solving the first two tasks awards `50%` of the test score. Correctly solving all three tasks awards `100%` of the test score.

# Example

`robot.in`
```
5
0 1 1 0 0
0 0 0 1 0
1 0 1 1 0
0 0 0 1 0
0 0 0 0 0
1 1 1 5
```
`robot.out`
```
4 2 2
```
Explanation
---
The obstacles that can be eliminated are those from `2, 4` and `3, 1`.
