This year marks the first edition of the Interdisciplinary Olympiad for Centers of Excellence, *PluriCEX*. Each Center of Excellence in the country will send a team consisting of $k$ members (all participants at the Center of Excellence). The team will have to solve interdisciplinary problems, with the subjects being those from the Center of Excellence ($D$ subjects, numbered from $1$ to $D$).

The director of CEX Iași made a list of the top $n$ best students from the CEX, then numbered the students from $1$ to $n$ in the order of their appearance on the list. For each student, the director noted the subjects they participate in at the CEX.

# Task
Write a program to determine all the teams that can be formed from $k$ of the $n$ students on the director's list, provided that for each subject, there is at least one team member who studies that subject at the CEX.

# Input data
The input file `pluricex.in` contains on the first line three natural numbers $n$, $k$, and $D$ (as defined in the problem statement). The next $n$ lines describe the CEX participation of the $n$ students on the director's list. Specifically, on line $i+1$, the participation of student $i$ is described as: $nr$, $d_1$, $d_2$, $\\dots$, $d_{nr}$.

The first number on the line ($nr$) indicates the number of subjects student $i$ participates in. The following $nr$ numbers represent the subjects student $i$ participates in. The numbers written on the same line are separated by space.

# Output data
The output file `pluricex.out` will contain all the teams that can be formed respecting the conditions from the problem statement, one team per line. The members of a team should be written in ascending order, separated by a space. The teams should be written in lexicographic order.

# Constraints and clarifications
- $0 < n \leq 22$
- $0 < k \leq 8$
- $0 < D \leq 10$
- For the test data, the problem always admits a solution, with the number of solutions being $< 20\ 000$.
- We say that the array $(x_1, x_2, \\dots, x_n)$ precedes lexicographically the array $(y_1, y_2, \\dots, y_n)$ if there exists an index $i$ such that $x_j=y_j$ for any $1 \leq j < i$, and $x_i < y_i$.
- For $20\%$ of the tests, the solution is unique.

# Example
`pluricex.in`
```
6 3 5
1 2
2 1 4
3 2 4 3
1 5
2 3 1
1 3
```
`pluricex.out`
```
2 3 4
3 4 5
```

Please let me know if you need any further assistance.