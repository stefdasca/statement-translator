Laura has received a square matrix of dimensions `NxN` of integers for her birthday. Not knowing what to do with it, she began asking herself various questions. She considers that a path from `(x1, y1)` to `(x2, y2)` is a sequence of cells that starts at the cell `(x1, y1)`, ends at `(x2, y2)` and any two consecutive cells share a common side (movement can be made to the north, east, south, or west). Laura defines the cost of a path as the minimum value of a cell on that path. Then, she started asking herself `Q` questions in the form: *What is the maximum cost that a path from `(x1, y1)` to `(x2, y2)` can have?* The questions became difficult for her and she asks for your help.

# Task
Find the answer for each of the `Q` questions.

# Input data
The first line of the input file `matrix.in` contains `2` integers `N` and `Q` with the meaning described above. The next `N` lines contain `N` integers each, representing the matrix received by Laura. Each of the next `Q` lines contains four integers `x1 y1 x2 y2` describing a question.

# Output data
The output file `matrix.out` contains the answer to the `Q` questions, each on a new line, in the same order they appear in the input file.

# Constraints and clarifications
* `1 \leq N \leq 300`
* `1 \leq Q \leq 20 000`
* The elements of the matrix are integers ranging between `1` and `1 000 000`.
* For `15\%` of the tests `N \leq 50, Q \leq 10` and the matrix values are between `1` and `250`.
* For another `20\%` of the tests `N \leq 100, Q \leq 100`.
* There is no question for which the pair `(x1, y1)` coincides with the pair `(x2, y2)`.

# Example

`matrix.in`
```
5 3
9 5 9 8 7
2 1 1 3 8
1 3 9 4 6
4 1 8 6 7
2 4 5 5 6
1 1 3 3
5 5 1 5
2 2 4 3
```

`matrix.out`
```
5
6
1
```

Explanation
---

For the first question, the answer is given by the following path:
**9 5 9 8 7**
2 1 1 3 **8**
1 3 **9** 4 **6**
4 1 **8** 6 **7**
2 4 **5** **5** **6**

