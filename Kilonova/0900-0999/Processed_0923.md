```markdown
A black and white photograph captured the image of lightning in the dark sky during an electrical storm. Enlarged, the photograph looks like a grid made up of small identical squares, white or black, arranged next to each other in $N$ rows and $M$ columns, $M$ per row. **The white squares** form the lightning in the photograph, while **the black squares** represent the sky. In the photograph, no two white squares are situated next to each other in the same row. **A lightning** is formed by white squares situated on consecutive rows that meet the following conditions:
- the white squares situated on two consecutive rows have a common corner or a common edge;
- a lightning can have only one white square per row.

In the photograph, the lightnings are **distinct**, they do not have white squares with common edges or corners. **The height of a lightning** is given by the number of white squares of that lightning.

~[foto.png|align=right|width=30em]
For it to be analyzed by programmers, the photograph is encoded with a two-dimensional array with $N$ rows and $M$ columns, whose elements are $0$ and $1$. The value $0$ is the encoding of the black square, and the value $1$ is the encoding of the white square.

Given the encoding, programmers must find the maximum number $P$ of black squares situated next to each other in the same row, the number of lightnings $F$, as well as the maximum height $H$ of a lightning in the photograph. For example, the adjacent photograph is encoded by the array $T$ next to the photograph.

# Task
Write a program that reads the numbers $N$ and $M$, the $N \cdot M$ elements of the array $T$ that encode the photograph, and solves the following tasks:
1) display the maximum number $P$ of black squares situated next to each other in a row in the photograph;
2) display the number $F$ of lightnings and the maximum height $H$ of a lightning in the photograph.

# Input data
The input file `foto.in` contains on the first line a natural number $C$ representing the task that needs to be solved ($1$ or $2$). The second line contains the two natural numbers $N$ and $M$, separated by a space, with the significance from the statement. On each of the following $N$ lines, there are $M$ values $0$ or $1$, separated by a space, representing the elements of the array that encode the photograph, in the order of their traversal in rows, from top to bottom, and from left to right within a row.

# Output data
The output file `foto.out` will contain, on a single line:
- if $C=1$, the number $P$, representing the answer to task $1$;
- if $C=2$, the two numbers $F$ and $H$, in this order, separated by a single space, representing the answer to task $2$.

# Constraints and clarifications
- $N$ is a natural number, $4 \leq N \leq 100$.
- $M$ is a natural number, $4 \leq M \leq 100$.
- For solving task 1:
\t- 20 points are awarded.
\t- Each test is worth 2 points.
- For solving task 2:
\t- 70 points are awarded.
\t- Each test for this task is worth 7 points:
\t\t- 3 points for the correct value of $F$;
\t\t- 4 points for the correct value of $H$.
\t- This task requires that **the output file contains exactly 2 numbers**.

# Example 1
`foto.in`
```
1
6 7
0 1 0 0 1 0 0
1 0 0 0 1 0 0
0 0 1 0 0 0 1
0 1 0 0 0 1 0
0 1 0 0 1 0 0
0 0 1 0 1 0 1
```
`foto.out`
```
3
```

## Explanation
Task **1** is solved. $N=6$, $M=7$. There are a maximum of $P=3$ black squares situated next to each other in rows $2$, $3$ and $4$ (see the photograph in the statement).

# Example 2
`foto.in`
```
2
6 7
0 1 0 0 1 0 0
1 0 0 0 1 0 0
0 0 1 0 0 0 1
0 1 0 0 0 1 0
0 1 0 0 1 0 0
0 0 1 0 1 0 1
```
`foto.out`
```
5 4
```

## Explanation
Task **2** is solved. $N=6$, $M=7$. There are $F=5$ lightnings and the maximum height of a lightning is $H=4$ (see the photograph in the statement).
```