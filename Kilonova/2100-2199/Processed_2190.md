**ATTENTION:** This problem is worth $100$ points. For "submissions," the maximum score is rescaled to $100$ points, but the true score will be visible on the *[leaderboard](https://kilonova.ro/contests/179/leaderboard)*.

The corporation Chert And is conducting suspicious activities on some islands in the Pacific Ocean. From experiments whose impact on the environment is unknown to illegitimate bank transactions, expose this activity by solving the following task, and the megacorporation will be obliged to reveal more data from the farm in Romania.

# Problem

Our archipelago can be represented as a matrix of size $N \times M$, where the $1 \times 1$ cells in the matrix can have two values:

* $0$ - a water cell
* $1$ - a land cell

We say that two cells are considered neighbors if they have at least one side in common. Multiple neighboring land cells form an island.

To get some clues about the illegal activities of the Chert And corporation, you need to answer several questions: Are the cells $(a, b)$ and $(c, d)$ on the same island?

# Output only

This problem is an output-only type. Participants will need to run $Q$ tests locally (which can be downloaded [here](algo1task1.zip) or on the right side of the page under *“Attachments”*), then submit the answers to the committee via the platform.

## Input data

The first line of a test will contain two numbers $N$ and $M$, which represent the length and width of the matrix, respectively.

In the next $N$ rows, there will be $M$ values each, representing the encoding of the archipelago. A cell with value $0$ represents a water cell, and a cell with value $1$ represents a land cell.

On the $N + 2$ line of the input, there will be $4$ numbers, $a, b, c,$ and $d$, which represent the cells $(a, b)$ and $(c, d)$ about which we want to know if they are on the same island.

## Output data

If the cells $(a, b)$ and $(c, d)$ are in the same cell, you will print `YES`, otherwise you will print `NO`.

You can submit the answers to the $Q$ tests either via a file or upload them below in the code attachment area. The answers to each test will be on a separate line, with the answer to the $i$-th question on the $i$-th line of the output.

# Constraints and clarifications

* $Q = 10$
* $N = M = 250$
* The values in the matrix are either $0$ or $1$.
* It is guaranteed that the cells $(a, b)$ and $(c, d)$ are land cells.
* Rows and columns are indexed starting from $1$.
* For the correct resolution of the task, you will receive a batch of coordinates for **META-TASK**.
* The link to the batch will be found in the evaluation test verdict.

**Note:** For simplicity, the examples will strictly analyze two smaller tests, which will not be used for evaluation.

# Examples

`0.txt`
```
7 7
1 0 0 0 0 1 0
0 0 0 0 1 1 0
1 1 1 1 1 0 0
0 0 0 1 0 0 0
1 0 0 0 0 0 0
1 1 0 0 1 1 1
1 0 0 0 1 0 0
3 1 2 6
```

`output`
```
YES
```

`input`
```
7 7
1 0 0 0 0 1 0
0 0 0 0 1 1 0
1 1 1 1 1 0 0
0 0 0 1 0 0 0
1 0 0 0 0 0 0
1 1 0 0 1 1 1
1 0 0 0 1 0 0
3 3 7 5
```

`output`
```
NO
```

## Explanation

~[task11.png]

It can be seen from the drawing that the cells $(3, 1)$ (red circle) and $(2, 6)$ (green circle) are on the same island. However, the cells $(3, 3)$ (blue circle) and $(7, 5)$ (black circle) are on different islands.

# Good luck!