## Leaves

Let $n$ and $p$ be two positive natural numbers. A tree labeled with $n$ vertices is a connected and acyclic graph in which the vertices are numbered 1, 2, $\dots$, $n$. A vertex in the tree is called a terminal vertex (or leaf) if it has degree 1.

## Task

Write a program that determines the number of labeled trees with $n$ vertices, of which $p$ are terminal vertices.

## Input data

The input file `frunze.in` contains on the first line two natural numbers $n$ and $p$, separated by a space, as described above.

## Output data

The output file `frunze.out` contains on the first line a natural number representing the remainder of the division between the number of labeled trees with $n$ vertices, of which $p$ are terminal vertices, and 29989.

## Constraints

$3 \leq n \leq 50$

$2 \leq p < n$

## Example

`frunze.in`
```
4 2 
```

`frunze.out`
```
12 
```

`frunze.in`
```
3 2 
```

`frunze.out`
```
3 
```

