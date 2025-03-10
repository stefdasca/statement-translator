
# Task

We have a text consisting of $n$ characters. These are numbered from left to right starting with position $1$. A highlight operation can be applied to this text. Such an operation is specified by a triplet in the form `st dr c` meaning: Characters between positions $st$ and $dr$ inclusive are colored using color $c$ (regardless of whether they were previously colored or not). If $c = 0$, it is considered that the highlight is removed from the area between positions $st$ and $dr$ ($0$ is not a color).

From time to time, we are interested in finding out, for a given color $c$, how many zones are highlighted with it. A maximal sequence of consecutive characters having the color $c$ is counted only once.

# Input data

The first line of the file `highlight.in` contains $n$ (the length of the text) and $m$ (the number of operations). Each of the next $m$ lines contains the description of one operation in one of the following two modes:
* `1 st dr c` (this represents a highlight operation as described above);
* `2 c` (this represents a query operation as described above).

# Output data

The file `highlight.out` contains the same number of lines as the number of operations of type $2$ in the input file. For each operation, in the order of their appearance, print a number with the meaning described earlier.

# Constraints and clarifications

* $1 \leq n \leq 100 \ 000$;
* $1 \leq m \leq 100 \ 000$;
* $0 \leq c \leq 100 \ 000$ (for operations of type $1$);
* $1 \leq c \leq 100 \ 000$ (for operations of type $2$);
* For each operation of type $1$, the values $st$ and $dr$ are between $1$ and $n$ inclusive and $st \leq dr$;
* For $27$ points, $1 \leq n, m \leq 2 \ 000$;
* For another $30$ points, $c \leq 1$ (for operations of type $1$ and $2$).

# Example

`highlight.in`
```
9 10
1 3 3 1
1 2 4 1
1 5 6 1
2 1
2 2
1 4 5 2
2 1
1 3 5 0
2 1
2 2
```

`highlight.out`
```
1
0
2
2
0
```

## Explanation

Let's consider color $1$ as red and color $2$ as blue.
* `1 3 3 1`: $XX\textcolor{red}{X}XXXXXX$
* `1 2 4 1`: $X\textcolor{red}{XXX}XXXXX$
* `1 5 6 1`: $X\textcolor{red}{XXXXX}XXX$
* `2 1`: Color $1$ appears once.
* `2 2`: Color $2$ appears zero times.
* `1 4 5 2`: $X\textcolor{red}{XX}\textcolor{blue}{XX}\textcolor{red}{X}XXX$
* `2 1`: Color $1$ appears twice.
* `1 3 5 0`: $X\textcolor{red}{X}XXX\textcolor{red}{X}XX$
* `2 1`: Color $1$ appears twice.
* `2 2`: Color $2$ does not appear.
```
