
**ATTENTION:** This problem is worth $150$ points. In "submissions," the maximum score is rescaled to $100$ points, but the real score will be visible on the *[leaderboard](https://kilonova.ro/contests/179/leaderboard)*. 

The environmental guard has determined that water cells between which one can move in two different ways have special properties that can help uncover the mystery!

# Problem

You are given two water cells. You must determine if it is possible to move between the two cells in two different ways.

A movement between two cells is a succession of cells such that any two consecutive cells share at least one side or one corner. In a movement, we cannot pass through the same cell more than once. Two movements between two cells are considered different if the intersection of the set of cells (excluding the first and last cell) of both movements is empty.

# Output only

This problem is of type output only. You (the participants) will need to run $Q$ tests locally (which can be downloaded [here](algo1task3.zip) or on the right side of the page under *â€œAttachmentsâ€*), then submit the answers to the committee through the platform.

## Input data

The first line of a test will contain two numbers $N$ and $M$, which represent the length and the width of the matrix, respectively.

On the next $N$ rows, there will be $M$ values, separated by a space, representing the archipelago coding. A cell with value $0$ represents a water cell, and a cell with value $1$ represents a land cell.

On line $N+2$ of the input, there will be $4$ numbers, $a, b, c$, and $d$, which represent the cells for which we want to find out if there are two distinct movements between the cells $(a, b)$ and $(c, d)$.

## Output data

If there are two distinct movements between the cells $(a, b)$ and $(c, d)$, you will transmit `YES`; otherwise, you will transmit `NO`.

The answers to the $Q$ tests can be submitted either through a file or uploaded below in the attachment area of the code. The answers to each test will be on a separate line; on the $i$-th line of the output will be the answer to the $i$-th question.

# Constraints and clarifications

* $Q = 10$
* $N = M = 250$
* The values in the matrix are either $0$ or $1$.
* It is guaranteed that the cells $(a, b)$ and $(c, d)$ are water cells.
* Rows and columns are indexed starting from $1$.
* A movement is not valid if it exits the matrix.
* For correct solving of the task, you will receive a batch of coordinates for **META-TASK**.
* The link to the batch will be found in the verdict of the evaluation test.

**Note:** For simplicity, the examples will strictly analyze two smaller tests, which will not be used for evaluation.

# Examples

`0.txt`
```
7 7
1 0 1 1 1 0 1
0 1 0 1 1 1 1
0 0 0 1 0 1 1
0 1 1 1 1 1 0
0 0 0 0 0 0 0
1 1 1 1 0 1 1
0 0 0 0 0 0 0
3 1 1 2
```

`output`
```
YES
```

`input`
```
7 7
1 0 1 1 1 0 1
0 1 0 1 1 1 1
0 0 0 1 0 1 1
0 1 1 1 1 1 0
0 0 0 0 0 0 0
1 1 1 1 0 1 1
0 0 0 0 0 0 0
3 1 4 7
```

`output`
```
NO
```

## Explanation

~[task13.png]

Between the cells $(3, 1)$ and $(1, 2)$, two distinct paths can be made (the orange path and the yellow path).

Between the cells $(3, 1)$ and $(4, 7)$, two distinct paths cannot be made.

# Good luck!
