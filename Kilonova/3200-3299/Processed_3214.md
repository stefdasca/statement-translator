# One, two, three, get me out of debt! Two, three, four and with you I marry! (ASG once said this to binary search)

~[frame.png|align=center|width=20%]

After playing Fortnite a lot, ASG dreamed about several islands from all the seasons. Being filled with nostalgia, he wishes to dream about them again in the following nights, but he is restricted to only a certain period of the dream. 

We know that the dream can be represented as a matrix with $N$ rows and $M$ columns, where there are $K$ islands that ASG has dreamed about. In the following $Q$ nights, he decides to dream about a submatrix of the dream matrix. An island is composed of one or more cells in the matrix, which are adjacent in the 4 directions: North, South, West, and East. We can have islands that overlap.

ASG will seek help to find out how many islands he will dream about in the night $i$.

# Input data

The first line contains four integers, $N$, $M$, $K$, and $Q$.
For each of the $K$ islands, the data will be found on two consecutive lines. On the first line of each island is the starting coordinate that ASG knows, followed by $X$ directions that ASG must follow to discover the whole island.
The second line describes a sequence of length $X$ containing the movement directions, formed of the letters:
* $N$ for North
* $S$ for South
* $V$ for West
* $E$ for East

After all the islands are described, there are $Q$ lines, each containing four integers that represent the coordinates of a submatrix that ASG desires to dream about on that particular night. The first two numbers represent the top-left corner of the submatrix, and the last two numbers represent the bottom-right corner of it.

Your task is to find out how many complete islands will be dreamed about during each of the $Q$ nights, considering that an island is made up of adjacent cells in the 4 directions (North, South, West, East), and can be considered complete only if it is entirely included in the selected submatrix for the night.

# Output data

Finally, $Q$ lines will be displayed, each line representing the number of complete islands dreamed about each night.

# Constraints and clarifications

* $N \cdot M \leq 500 \ 000$
* $Q \leq 2 \cdot 10 ^ 5$
* $K \leq 100$
* An island is considered dreamed only if it is fully contained within the selected submatrix for the dream on that night. If the island is not completely included in the submatrix, ASG will forget it when he wakes up.

# Example 1

`stdin`
```
4 4 1 2
2 2 4
SENE
2 2 3 4
2 2 3 3
```

`stdout`
```
1
0
```
$$
\begin{array}{|c|c|c|c|}
\hline
0 &0 &0 &0 \\
\hline
0 &1 &1 &1 \\
\hline
0 &1 &1 &0 \\
\hline
0 &0 &0 &0 \\
\hline
\end{array}
$$