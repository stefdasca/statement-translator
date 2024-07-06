Ricǎ is a 12th-grade student who aspires to pursue a degree in computer science at Politehnica Bucharest - University Center Pitești. To achieve this, he is preparing to take the baccalaureate exam in computer science. While revising the fundamental concepts of graph theory, he encountered two counting problems. Given $N$, the first problem requires determining the number of undirected graphs with $N$ nodes where node $1$ is a terminal, while the second problem requires determining the number of trees with node $1$ as a terminal node, and the degree of node $2$ being at least $2$. The nodes of the graphs and trees are labeled with $1, 2, \dots, N$.

# Task

Given $N$, determine:
1. the number of undirected graphs with $N$ nodes where node $1$ is terminal, modulo $7919$
2. the number of trees with node $1$ as a terminal node, with the degree of node $2$ being at least $2$, modulo $7919$

# Input data

The first line of the input file `numarare.in` contains $C$, the task number ($1$ or $2$), and the second line contains $N$.

# Output data

The first line of the output file `numarare.out` will contain a single natural number representing the number corresponding to the task to be solved.

# Constraints and clarifications

* $1 \leq N \leq 15\ 000$;
* $A$ modulo $k$ is $A \ \% \ k$;
* Correctly solving task $1$ will earn $20$ points.
* Correctly solving task $2$ will earn $80$ points.

# Example 1

`numarare.in`
```
1
3
```

`numarare.out`
```
4
```

## Explanation

The figure below shows the $4$ graphs.

~[numarare1.png|align=center|width=90]

# Example 2

`numarare.in`
```
2
4
```

`numarare.out`
```
5
```

## Explanation

The figure below shows the $5$ trees.

~[numarare2.png|align=center|width=90]