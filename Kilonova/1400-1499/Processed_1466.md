```markdown
Ben has a piece of land with a forest of secular trees. He wants to build a cabin there, but being an ecologist, he does not want to cut down any trees. Instead, he wants to find the largest rectangular area without trees. He is looking for a rectangular area guarded only at the corners by trees and with sides parallel to the coordinate axes. Ben knows the coordinates of all the trees in the forest and asks you to help him find the area of the rectangle with the maximum surface area that has trees only at the four corners.

~[img.png|width=55em]

# Task
Knowing the number of trees in the forest and their coordinates, you are tasked with determining the area of the rectangle with the maximum surface area with trees only at the four corners, where Ben intends to build his cabin.

# Input data
The input file `cabana.in` contains on the first line a natural number $n$, representing the number of trees in the forest. Each of the next $n$ lines contains two integers, separated by a space, representing the abscissa and the ordinate of a tree.

# Output data
The output file `cabana.out` contains on the first line the natural number $a$, representing the area of the rectangle with the maximum surface area.

# Constraints and clarifications
- For $10\\%$ of the tests: $1 \\leq n \\leq 10$ and $-10^3 \\leq x, y \\leq 10^3$.
- For $30\\%$ of the tests: $1 \\leq n \\leq 500$ and $-10^3 \\leq x, y \\leq 10^3$.
- For $50\\%$ of the tests: $1 \\leq n \\leq 500$ and $-10^6 \\leq x, y \\leq 10^6$.
- For $70\\%$ of the tests: $1 \\leq n \\leq 3\ 000$ and $-10^9 \\leq x, y \\leq 10^9$.
- For $100\\%$ of the tests: $1 \\leq n \\leq 50\ 000$ and $-10^9 \\leq x, y \\leq 10^9$.
- There are no two trees positioned at the same coordinates.

# Example
`cabana.in`
```
22
6 25
25 22
15 5
23 23
6 7
11 16
11 20
10 22
6 16
12 6
7 19
10 19
10 14
7 14
7 7
18 14
18 7
10 7
19 19
29 19
29 4
19 4
```
`cabana.out`
```
150
```

## Explanation
The coordinates of the rectangle with the maximum area with sides parallel to the coordinate axes and containing trees only at the corners are $(19,19)$, $(29,19)$, $(29,4)$, $(19,4)$, so the maximum area is $150$.
```