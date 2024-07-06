In graph theory, a planar graph is a graph that can be embedded in a plane, meaning it can be drawn on the plane in such a way that its edges intersect only at nodes. In other words, it can be drawn such that any two edges do not intersect. Florin is studying computer science between 2023-2029. Passionate about prime numbers, he found out that the number $20232029$ is a prime number. He is preparing a paper on the chapter of graphs and needs your help.

Given $NR = 2 \cdot N$ fixed nodes (similar to a classic clock) in the xOy plane and $N$ edges, Florin wants to determine the number of distinct planar graphs where each node will have degree $1$.

For example:
- For $NR = 6$, this is a representation variant: ~[img1.png|width=16em]
- For $NR = 4$, there are 2 solutions:
    - In the first case, the edges are vertical: ~[img21.png|width=16em]
    - In the second case, the edges are horizontal: ~[img22.png|width=16em]

# Task

Write a program that determines the number of graphs obtained by Florin:
- Task 1: The number of graphs will be displayed modulo $20232029$
- Task 2: The number of graphs will be displayed in its entirety.

# Input data

The input file `planar.in` contains on the first line two natural numbers $C$ and $NR$ representing the task and the even number of nodes of the graph.

# Output data

The output file `planar.out` will contain a single line that will contain the computed result.

# Constraints and clarifications

* $1 \leq NR \leq 10^4$
* $1 \leq C \leq 2$
* For $30$ points, $C = 1$.
* For another $24$ points, $C = 2$ and $NR \leq 20$.
* For the remaining $36$ points, $C = 2$.

# Example 1

`planar.in`
```
1 4
```

`planar.out`
```
2
```

# Example 2

`planar.in`
`````
1 50
```

`planar.out`
```
7744491
```

## Explanation

$4 \ 861 \ 946 \ 401 \ 452\\ \% \\ 20232029 = 7 \ 744 \ 491$

# Example 3

`planar.in`
```
2 50
```

`planar.out`
```
4861946401452
```
