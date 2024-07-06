~[img.png|align=right]

Gimi the pigeon has gotten into trouble again; he is visiting a tree-shaped city with $N$ intersections, connected by $N - 1$ bidirectional streets rooted at the intersection with index $1$. The intersections of the city are numbered from $1$ to $N$, and for each intersection $i$, $p_i$ (the parent intersection of $i$) and $d_i$ (the size of a monument at the intersection) are known.

# Task
As Gimi visits the city, he will make $Q$ flights starting from an intersection $x$ to an intersection $y$, visiting all intersections on the path from $x$ to $y$ in order. Since our pigeon is quite clumsy, he will bump into every monument that is greater than or equal to all monuments from the intersections visited up to that point on the path. Therefore, Gimi will also bump into the monument at the starting intersection $x$.

Gimi wants to know, for each of the $Q$ flights, how many monuments he will bump into.

# Input data
The first line of the input file contains two numbers $N$ and $Q$, representing the number of intersections and the number of flights Gimi will make, respectively. The second line contains $N$ numbers representing the array $d_1, d_2, \ldots, d_n$. The third line contains $N-1$ values representing the array $p_2, p_3, \dots, p_n$. Each of the following $Q$ lines contains two numbers $x_i$, $y_i$ describing the $i$-th query.

# Output data
The output file will contain $Q$ numbers, each on a new line. The $i$-th number represents the answer to the $i$-th query.

# Constraints and clarifications
- $1 \leq N \leq 200\ 000$
- $1 \leq Q \leq 200\ 000$
- $1 \leq  p_{i} \leq N$
- $1 \leq  d_{i} \leq N$
- Node $1$ has no parent.

|# | Score | Constraints|
| - | - | ------------|
|1|11|$N \leq 2\ 000$ and $Q \leq 2\ 000$|
|2|8|The tree is a path.|
|3|9|For each query, $y$ is an ancestor of $x$.|
|4|28|For each query, $x$ is an ancestor of $y$.|
|5|21|$N \leq 50\ 000$ and $Q \leq 50\ 000$|
|6|23|No additional constraints|

# Example
`impiedicat.in`
```
8 9
3 2 4 1 3 1 2 1
1 1 2 2 4 5 1
6 8
8 6
6 7
7 6
6 1
1 6
4 5
5 4
6 3
```
`impiedicat.out`
```
4
2
4
2
4
1
3
1
5
```

# Explanation
The sizes of the monuments visited for each flight are:

- $\\textcolor{red}{1} \\rightarrow \\textcolor{red}{1} \\rightarrow \\textcolor{red}{2} \\rightarrow \\textcolor{red}{3} \\rightarrow 1$
- $\\textcolor{red}{1} \\rightarrow \\textcolor{red}{3} \\rightarrow 2 \\rightarrow 1 \\rightarrow 1$
- $\\textcolor{red}{1} \\rightarrow \\textcolor{red}{1} \\rightarrow \\textcolor{red}{2} \\rightarrow \\textcolor{red}{3} \\rightarrow 2$
- $\\textcolor{red}{2} \\rightarrow \\textcolor{red}{3} \\rightarrow 2 \\rightarrow 1 \\rightarrow 1$ 
- $\\textcolor{red}{1} \\rightarrow \\textcolor{red}{1} \\rightarrow \\textcolor{red}{2} \\rightarrow \\textcolor{red}{3}$ 
- $\\textcolor{red}{3} \\rightarrow 2 \\rightarrow 1 \\rightarrow 1$
- $\\textcolor{red}{1} \\rightarrow \\textcolor{red}{2} \\rightarrow \\textcolor{red}{3}$
- $\\textcolor{red}{3} \\rightarrow 2 \\rightarrow 1$ 
- $\\textcolor{red}{1} \\rightarrow \\textcolor{red}{1} \\rightarrow \\textcolor{red}{2} \\rightarrow \\textcolor{red}{3} \\rightarrow \\textcolor{red}{4}$

With $\\textcolor{red}{red}$ marking the monuments Gimi bumps into during the flight.