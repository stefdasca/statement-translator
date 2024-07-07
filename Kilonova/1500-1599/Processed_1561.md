
Viewed from space, the map of the island in our story has the shape of a square grid with $L$ rows and $L$ columns. The rows and columns are numbered from $1$ to $L$. In each of the $L \cdot L$ cells, there is a lighthouse. Initially, the one at position $1,1$ is lit, and all of them respect the rule: any lighthouse has neighboring lighthouses (on row and column, so at most $4$) in the opposite state to its own.

After a storm, strange things happened: lightning struck one after another and affected the state of some lighthouses. There are three types of lightning:
- Type $1$ lightning. For this type, the row it strikes is indicated, and it affects the state of the lighthouses on that row and on the rows with a higher order number. More precisely, all the lighthouses on these rows instantly change their state.
- Type $2$ lightning. For this type, a number representing the column it strikes is indicated, and it affects the state of the lighthouses on that column and on the columns with a higher order number. More precisely, all the lighthouses on these columns instantly change their state.
- Type $3$ lightning. For this type, the row and then the column of an element in the grid are indicated. All the lighthouses located on the same parallel with the secondary diagonal with the specified element and on the parallels with the secondary diagonal below it, change their state.

Changing the state of a lighthouse means that it lights up if it is off and turns off if it is lit.

# Task

Data about lightning is given, in the order they occur. The task is to indicate the state of certain lighthouses at the specified coordinates on the island at the end of the storm.

# Input data

The first line of the file `lumini.in` contains a natural number $L$, with the above-mentioned significance. The second line contains a natural number $F$, representing the number of lightning strikes.

On the following $F$ lines, data about each lightning occurs in the order they appear. The first number on each line is the type of lightning ($1$, $2$, or $3$). If this number is $1$ or $2$, there is another number on that line. This represents the row the lightning strikes (if the line in the file starts with $1$), respectively the column the lightning strikes (if the line starts with $2$). If it is about type $3$ lightning, there are two more numbers on that line, representing the row and column of the element on the island where the lightning strikes, separated by space.

The following line contains a number $Q$. On the next $Q$ lines, there are two numbers (separated by space) representing the row and column of a lighthouse on the island whose state after the storm is to be determined.

# Output data

The output file `lumini.out` should contain on a single line, separated by space, $Q$ numbers representing the results of the queries in the order they appear in the input file. If the corresponding lighthouse is lit, the value $1$ will be written, and if it is off, the value $0$ will be written.

# Constraints and clarifications

* $2 \leq L \leq 2 \ 000 \ 000 \ 000$;
* $1 \leq F \leq 1 \ 000$;
* It is guaranteed that for the lightning specification, the line starts with $1$, $2$, or $3$, and the other values on the respective lines are between $1$ and $L$ inclusive.
* $1 \leq Q \leq 100 \ 000$;
* It is guaranteed that for each lighthouse whose state needs to be determined, the row and column are between $1$ and $L$ inclusive.
* For $24$ points, $L \leq 100$, $F \leq 100$ and there are only type $1$ lightning;
* For another $18$ points, $L \leq 100$, $F \leq 100$;
* For another $12$ points, $L \leq 10 \ 000$ and there are only type $1$ lightning;
* For another $8$ points, $L \leq 10 \ 000$;
* For another $13$ points, $L \leq 1 \ 000 \ 000$;
* For the remaining $25$ points, there are no additional constraints.

# Example

`lumini.in`
```
4
3
1 2
3 3 1
2 3
5
1 1
2 4
3 2
4 2
4 4
```

`lumini.out`
```
1 0 0 1 0
```

## Explanation

Initially, the state of the lighthouses on the island can be represented as follows:
$
\begin{matrix}
    1 & 0 & 1 & 0 \\
    0 & 1 & 0 & 1 \\
    1 & 0 & 1 & 0 \\
    0 & 1 & 0 & 1
\end{matrix}
$

After applying the first lightning, the state of the lighthouses becomes:

$
\begin{matrix}
    1 & 0 & 1 & 0 \\
    \textbf{1} & \textbf{0} & \textbf{1} & \textbf{0} \\
    \textbf{0} & \textbf{1} & \textbf{0} & \textbf{1} \\
    \textbf{1} & \textbf{0} & \textbf{1} & \textbf{0}
\end{matrix}
$

After applying the second lightning, the state of the lighthouses becomes:

$
\begin{matrix}
    1 & 0 & \textbf{0} & \textbf{1} \\
    1 & \textbf{1} & \textbf{0} & \textbf{1} \\
    \textbf{1} & \textbf{0} & \textbf{1} & \textbf{0} \\
    \textbf{0} & \textbf{1} & \textbf{0} & \textbf{1}
\end{matrix}
$

After applying the third lightning, the state of the lighthouses becomes:

$
\begin{matrix}
    1 & 0 & \textbf{1} & \textbf{0} \\
    1 & 1 & \textbf{1} & \textbf{0} \\
    1 & 0 & \textbf{0} & \textbf{1} \\
    0 & 1 & \textbf{1} & \textbf{0}
\end{matrix}
$
