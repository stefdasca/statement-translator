# Task

Little Julius received an advent calendar for his birthday, which can be represented as a matrix with $n$ rows and $m$ columns. Behind each box, there is a chocolate. Being impatient, he ate a large part of the chocolates by opening the respective boxes.
To prevent his parents from noticing, he thought of sticking all the boxes from which he ate the chocolates with tape. He can use a strip of tape to stick a sequence of opened boxes (the tape can only cover opened boxes). In addition, all boxes must be adjacent vertically or horizontally. Once a tape strip is applied, those boxes are considered closed.
Since he does not want to use too much tape, he wonders what is the minimum number of strips he needs to use to close all the boxes from which he ate the chocolate.

# Input data

The file `scotch.in` contains:

- The first line contains two integers, $n$ and $m$, representing the number of rows and columns of the advent calendar, respectively.
- Each of the next $n$ lines contains $m$ characters `.` and `#`, which encode the calendar. The character `.` represents a closed cell, and the character `#` represents an opened cell.

# Output data

The file `scotch.out` should contain:

- A single integer representing the minimum number of tape strips required to stick all the opened boxes back.

# Constraints and clarifications

* $1 \leq n \leq 1 \ 000 $
* $1 \leq m \leq 10 $

| **#**       | **Points**  | **Constraints** 
| ----------- | ----------- | ----------
| 1      | 35       |  Each closed cell is adjacent to at most 2 other closed cells.
| 2      | 25        |  $1 \leq n \leq 10$
| 3      | 40       |  No additional constraints.

# Example 1

`scotch.in`
```
2 3
#.#
###
```

`scotch.out`
```
3
```

## Explanation

One possible solution is to use one strip for the first column, one strip for the third column, and one strip for the box at row $2$ and column $2$.

# Example 2

`scotch.in`
```
4 3 
.#.
###
.##
.#.
```

`scotch.out`
```
3
```

# Example 3

`scotch.in`
```
4 4 
####
#.#.
#.##
####
```

`scotch.out`
```
5
