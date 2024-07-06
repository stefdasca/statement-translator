A rabbit is found in a garden full of surprises.

The map of the garden can be represented as a rectangular board with $m$ rows, numbered from $1$ to $m$ from top to bottom, and $n$ columns, numbered from $1$ to $n$ from left to right.

In each cell of this garden, there can be at most one of the following surprises: arrow, tree, wall, trap, carrot, bomb.

An __arrow__ points in one of the directions north, south, east, west. Once the rabbit enters a cell containing such an arrow, it will continue moving in the direction indicated by the arrow, and the arrow disappears.

In a cell containing a __tree__ or a __wall__, the rabbit cannot enter, but if it "bumps" into a tree, it maintains its direction but changes the direction it is facing (if it was moving north, it will change to south, if it was moving east, it will change to west, etc.).

If the rabbit enters a cell containing a __trap__, all the walls on the terrain disappear and new walls will appear in specified positions. If the rabbit passes again through a cell containing a trap, the newly built walls disappear and the initial walls reappear. More precisely, there are two sets of walls that switch each time the rabbit passes through a cell containing a trap.

If the rabbit passes __twice__ through the vicinity of a cell containing a __bomb__ (i.e., through the cells adjacent to the south, north, east, or west of the cell containing the bomb), the bomb will explode and the rabbit will instantly turn into an angel. Also, if the rabbit enters a cell containing a bomb, it immediately turns into an angel.

The rabbit will chew all the carrots that come its way. Obviously, if it passes a second time through the same cell, it will not find a carrot on the second pass.

The surprises in the garden are coded as follows: $1$ for arrow pointing north, $2$ for arrow pointing west, $3$ for arrow pointing south, $4$ for arrow pointing east, $5$ for tree, $6$ for bomb, $7$ for carrot, $8$ for wall, $9$ for trap. The empty cells on the garden map are coded as $0$.

Initially, the position and the direction of the rabbit are known. Its expedition ends in one of the following situations:

* upon the explosion of a bomb, in which case it turns into an angel
* upon exiting the garden (i.e., leaving the given rectangular area), in which case it becomes lost
* when it manages to chew all the carrots, in which case it is happy

# Task

Given the garden map, determine the final state of the rabbit (angel, lost, or happy), the number of carrots chewed until the expedition ends, and the number of steps the rabbit takes until this moment.

# Input data

The first line of the input file `iepuras.in` contains two integers $m$ and $n$, separated by a space, representing the number of rows and the number of columns of the map.

The second line of the file contains three natural numbers, separated by spaces, representing the row and column of the initial position of the rabbit on the map and the direction it is facing. The direction is coded as follows: $1$ for north, $2$ for west, $3$ for south, $4$ for east.

The next $m$ lines contain $n$ integers separated by spaces, representing the coding of the garden map, as specified above.

The next line contains a single natural number $t$ representing the number of cells that will contain walls after the first passage through a cell containing a trap. The next $t$ lines contain two natural numbers $i$ and $j$, separated by a space, representing the coordinates of a cell that will contain a wall after the first passage through a cell containing a trap.

# Output data

The output file `iepuras.out` will contain on its first line one of the words __ANGEL__, __LOST__, or __HAPPY__, corresponding to the final state of the rabbit. The second line of the file will contain two integers separated by a space, representing the row and column of the rabbit's last position on the field, that is, the position where it died, or where it became happy, or its last position on the field before becoming lost.

The third line of the file will contain two integers separated by a space, representing the number of carrots collected until the expedition ended, and the number of steps the rabbit took to reach the final state.

# Constraints and clarifications

* the initial position of the rabbit is valid, that is, it is a free cell within the terrain
* for the test data, it is ensured that the rabbit will make a finite number of steps before ending its expedition
* $1 \leq m, n \leq 200$
* $0 \leq t \leq 20$
* the maximum number of walls present at any given time is at most $50$, and it is possible that at some point there are no walls on the field
* it is guaranteed that for the input data, the rabbit cannot simultaneously reach two of the three states
* trees and traps are objects that remain permanently on the terrain, in their initial positions
* at any given time, there can be only one surprise (tree, wall, trap, carrot, arrow, bomb) in a garden cell

# Example 1

`iepuras.in`
```
10 15
7 1 4
0 0 6 0 5 5 0 7 0 0 0 0 0 0 0
0 0 0 0 5 5 0 0 4 0 0 0 0 0 3
0 5 5 0 5 5 0 0 0 0 0 0 0 0 0
0 5 5 0 5 5 0 1 7 0 0 7 0 0 2
0 0 0 0 5 5 0 0 0 0 0 0 0 0 0
0 0 0 0 0 5 0 0 0 0 0 0 0 0 0
0 3 0 0 0 5 6 0 0 5 5 5 0 0 0
0 7 0 0 0 0 0 0 0 0 0 0 0 5 0
0 4 0 0 0 7 0 0 3 5 0 0 0 5 0
0 6 0 0 0 0 0 0 1 5 0 0 0 5 0
0
```

`iepuras.out`
```
HAPPY
1 8
5 37
```

# Explanation

$\[
0 \ 0 \ 6 \ 0 \ 5 \ 5 \ 0 \ \textcolor{#228B22}{7} \ 0 \ 0 \ 0 \ 0 \ 0 \ 0 \ 0 \\
0 \ 0 \ 0 \ 0 \ 5 \ 5 \ 0 \ \textcolor{#228B22}{0} \ \textcolor{#228B22}{4} \ 0 \ 0 \ 0 \ 0 \ 0 \ 3 \\
0 \ 5 \ 5 \ 0 \ 5 \ 5 \ 0 \ \textcolor{#228B22}{0} \ \textcolor{#228B22}{0} \ 0 \ 0 \ 0 \ 0 \ 0 \ \textcolor{#228B22}{0} \\
0 \ 5 \ 5 \ 0 \ 5 \ 5 \ 0 \ \textcolor{#228B22}{1} \ \textcolor{#228B22}{7} \ 0 \ 0 \ 7 \ 0 \ 0 \ 2 \\
0 \ 0 \ 0 \ 0 \ 5 \ 5 \ 0 \ \textcolor{#228B22}{0} \ 0 \ 0 \ 0 \ 0 \ 0 \ 0 \\
0 \ 0 \ 0 \ 0 \ 0 \ 5 \ 0 \ \textcolor{#228B22}{0} \ 0 \ 0 \ 0 \ 0 \ 0 \ 0 \\
\textcolor{#8a42f5}{0} \ \textcolor{#8a42f5}{3} \ 0 \ 0 \ 0 \ 5 \ 6 \ \textcolor{#228B22}{0} \ 5 \ 5 \ 5 \ 0 \ 0 \ 0 \\
0 \ \textcolor{#8a42f5}{7} \ 0 \ 0 \ 0 \ 0 \ 0 \ \textcolor{#228B22}{0} \ 0 \ 0 \ 0 \ 0 \ 5 \ 0 \\
0 \ \textcolor{#8a42f5}{4} \ 0 \ 0 \ 0 \ 7 \ 0 \ \textcolor{#228B22}{0} \ 3 \ 5 \ 0 \ 0 \ 0 \ 5 \ 0 \\
0 \ 6 \ 0 \ 0 \ 0 \ 0 \ 0 \ \textcolor{#228B22}{1} \ 5 \ 0 \ 0 \ 0 \ 5 \ 0 \\
\]

# Example 2

`iepuras.in`
```
6 5
2 1 3
0 0 0 7 0
0 0 0 0 0
9 6 7 2 0
8 0 0 0 0
7 8 0 0 0
4 8 9 1 0
4
4 4
5 4
1 5
2 5
```

`iepuras.out`
```
ANGEL
3 3
2 11
```

# Explanation

$\[
0 \ 0 \ 0 \ 7 \ 0 \\
\textcolor{#228B22}{0} \ 0 \ 0 \ 0 \ 0 \\
\textcolor{#228B22}{9} \ 6 \ \textcolor{#228B22}{7} \ 2 \ 0 \\
\textcolor{#228B22}{8} \ 0 \ 0 \ \textcolor{#228B22}{0} \ 0 \\
\textcolor{#228B22}{7} \ 8 \ 0 \ \textcolor{#228B22}{0} \ 0 \\
\textcolor{#228B22}{4} \ 8 \ 9 \ 1 \ 0 \\
\]

# Example 3

`iepuras.in`
```
4 3
2 1 3
0 0 0
0 0 0
9 6 7
8 0 0
4
4 3
1 2
1 3
2 3
```

`iepuras.out`
```
LOST
4 1
0 3
```

# Explanation

$\[
2 \ 1 \ 3 \\
0 \ 0 \ 0 \\
\textcolor{#228B22}{0} \ 0 \ 0 \\
\textcolor{#228B22}{9} \ 6 \ 7 \\
\textcolor{#228B22}{8} \ 0 \ 0 \\
\]

# Example 4

`iepuras.in`
```
5 4
2 1 3
4 0 7 0
0 0 0 0
0 0 0 0
5 0 0 0
0 0 0 0
0
```

`iepuras.out`
```
HAPPY
1 3
1 5
```

# Explanation

$\[
\textcolor{#228B22}{4} \ 0 \ 7 \ 0 \\
\textcolor{#228B22}{0} \ 0 \ 0 \ 0 \\
\textcolor{#228B22}{0} \ 0 \ 0 \ 0 \\
5 \ 0 \ 0 \ 0 \\
0 \ 0 \ 0 \ 0 \\
\]