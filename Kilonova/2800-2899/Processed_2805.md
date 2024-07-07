
To relax, Dan takes a walk through a virtual forest made up of $N \times N$ trees, arranged in the form of a square matrix with $N$ rows and $N$ columns. On each tree, a digit in base $10$ is written.
Dan's walk begins at an unknown coordinate position and consists of a sequence of steps. At each step, Dan will move to one of the neighboring trees. Two trees are neighbors if they are on the same row in consecutive columns, or they are in the same column, in consecutive rows. During the walk, Dan memorizes in a sequence $S$ the digits written on the trees located at the positions he passed through. However, being very tired, it is possible that at some point he memorized the digits incorrectly in the sequence $S$.

# Task

Given the matrix representing the virtual forest, as well as the sequence $S$ in which the digits from the trees located at the positions visited by Dan during the walk were memorized, determine the maximum number of visited positions during the walk, until the first incorrectly memorized digit in the sequence $S$.

# Input data

The input file `copaci.in` contains on the first line the natural number $N$. The next $N$ lines contain $N$ digits each, representing the digits written on the trees in the virtual forest, in the order of the rows, and for the trees on the same row, in the order of the columns. The last line contains the digits memorized in the sequence $S$. There are no spaces in the input file.

# Output data

The output file `copaci.out` will contain a single line which will contain a single natural number, representing the answer to the given task.

# Constraints and clarifications

* $1 \leq N \leq 100$
* $1 \leq |S| \leq 10^5$

|#|Score|Constraints|
|-|-|-|
|1|20|$N \leq 10$ and $\| S \| \leq 100$|
|2|80|No additional constraints.|

# Example 1

`copaci.in`
```
3
769
617
502
97205562
```

`copaci.out`
```
5
```

## Explanation

The maximum number of positions traversed until the first incorrectly memorized digit in $S$ is $5$. A possible walk is:
$\\textcolor{white}{7 \\ 6} \\ \\textcolor{blue}{9}$
$\\textcolor{white}{6 \\ 1} \\ \\textcolor{blue}{7}$
$\\textcolor{blue}{5 \\ 0 \\ 2}$

# Example 2

`copaci.in`
```
3
125
452
803
32541
```

`copaci.out`
```
5
```

## Explanation

The sequence $S$ is entirely correct. A possible walk is:
$\\textcolor{blue}{1} \\ \\textcolor{white}{2 \\ 5}$
$\\textcolor{blue}{4 \\ 5 \\ 2}$
$\\textcolor{white}{8 \\ 0} \\ \\textcolor{blue}{3}$

# Example 3

`copaci.in`
```
5
36231
92928
08044
51868
43301
6281864292913
```

`copaci.out`
```
11
```

## Explanation

The maximum number of positions traversed until the first incorrectly memorized digit in $S$ is $11$. A possible walk is:
$\\textcolor{white}{3} \\ \\textcolor{blue}{6} \\ \\textcolor{white}{2 \\ 3 \\ 1}$
$\\textcolor{blue}{9} \\ \\textcolor{purple}{2} \\ \\textcolor{blue}{9 \\ 2 \\ 8}$
$\\textcolor{white}{0} \\ \\textcolor{blue}{8} \\ \\textcolor{white}{0} \\ \\textcolor{blue}{4} \\ \\textcolor{white}{4}$
$\\textcolor{white}{5} \\ \\textcolor{blue}{1 \\ 8 \\ 6} \\ \\textcolor{white}{8}$
$\\textcolor{white}{4 \\ 3 \\ 3 \\ 0 \\ 1}$
Notice that during the walk, Dan might pass through the same position multiple times.

# Example 4

`copaci.in`
```
2
30
47
121
```

`copaci.out`
```
0
```

## Explanation

The maximum number of positions traversed until the first incorrectly memorized digit in $S$ is $0$, because there is no tree on which digit $1$ is written.
