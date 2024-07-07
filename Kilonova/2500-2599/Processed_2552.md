
# Task

We have at our disposal a chessboard of $N \times M$.

Some cells are blocked, on the rest of the cells we can place knights. What is the maximum number of knights we can place such that they do not attack each other?

The knight moves as can be observed:
~[Screenshot 2024-03-26 144338.png]

# Input data

The first line contains the numbers $N$ and $M$.
Next, the chessboard follows in the form of a character matrix with `#` for occupied cell and `.` for free cell.

# Output data

Print the maximum number of knights.

# Constraints and clarifications

* $1 \leq N \times M \leq 5000$
* For 60 points $1 \leq N \times M \leq 300$
* $\textbf{All tests are grouped!}$

# Example

`stdin`
```
5 4
#...
.#..
###.
#..#
.###
```

`stdout`
```
6
```
