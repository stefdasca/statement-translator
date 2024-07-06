**ATTENTION:** This problem is worth $100$ points. In the "submissions" the maximum score is rescaled to $100$ points, but the true score will be visible on the *[leaderboard](https://kilonova.ro/contests/179/leaderboard)*.

**Note:** All restrictions imposed on the previous task also apply here.

The detectives investigating the Chert And corporation have concluded that a certain island might provide additional information for unraveling the disaster!

# Problem

You are given a land cell that belongs to an island. Since you believe clues might also be found in the water, you will want to determine the smallest area rectangle that completely encloses the island to which the land cell belongs. A rectangle completely encloses an island if all the cells that belong to that island are within the rectangle (and not on its boundary).

# Output only

This problem is of type "output only." You (the participants) will have to run locally $Q$ tests (which can be downloaded [here](algo1task2.zip) or on the right side of the page under "Attachments"), then submit the answers through the platform to the commission.

## Input data

The first line of a test will contain two numbers $N$ and $M$, which represent the length and width of the matrix, respectively.

In the next $N$ rows will be $M$ values, separated by a space, which represent the coding of the archipelago. A cell with the value $0$ represents a water cell, and a cell with the value $1$ represents a land cell.

On line $N + 2$ of the input will contain two numbers, $a$ and $b$, which represent the cell for which we want to find the rectangle that completely encloses the island to which the cell belongs.

## Output data

You will display two points: the top-left corner of the rectangle and the bottom-right corner of the rectangle. The coordinates will be separated by a space.

You can submit the answers to the $Q$ tests either by a file or upload them below in the code attachment area. The answers for each test will be on a separate row, with the $i$-th row in the output containing the answer to the $i$-th question.

# Constraints and clarifications

* $Q = 5$
* $N = M = 250$
* The values in the matrix are either $0$ or $1$.
* It is guaranteed that the cell $(a, b)$ is a land cell.
* Rows and columns are indexed from $1$.
* The cells on the boundary of the **matrix** (not the island) will all have values of $0$.
* For correct task resolution you will receive a batch of coordinates for **META-TASK**.
* The link to the batch can be found in the evaluation test's verdict.

**Note:** For simplicity, the example will strictly analyze a smaller test, which will not be used for evaluation.

# Example

`0.txt`
```
7 7
0 0 0 0 0 0 0
0 1 1 1 0 0 0
0 0 1 1 1 0 0
0 1 1 0 1 0 0
0 0 0 0 1 1 0
0 0 0 0 1 0 0
0 0 0 0 0 0 0
4 2
```

`output`
```
1 1 7 7
```

## Explanation

~[task12.png]

It can be observed that our island can be completely enclosed in the rectangle with corners $(1, 1)$ and $(7, 7)$. A rectangle with a smaller area than the one given in the example is impossible to find.

# Good luck!