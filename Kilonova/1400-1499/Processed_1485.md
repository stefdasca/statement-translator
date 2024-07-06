~[cristale1.png|align=right]
Precious stones have fascinated humanity since ancient times, and the most renowned among them, crystals, have become symbols of both hardness and eternity. As a result of a scientific study, different types of molecules, arranged in perfect geometry, can be observed on a rectangular sample with $M$ rows, each containing $N$ molecules aligned next to each other. A crystallizable formation consists of $3$ molecules of the same type, arranged in one of the four shapes shown in the adjacent image (fig. 1).

~[cristale2.png|align=right]
Each formation is surrounded all around, as in fig. 2, by a special shell also made of identical molecules, of a different type than those in the crystallizable formation it surrounds and isolates from the rest of the molecular formations. In this way, each molecule in the crystallizable formation is adjacent to the North, South, East, and West with a molecule from the same crystallizable formation or with a molecule from the special shell.

Each crystallizable formation is bombarded with X-rays, and in this way crystallization occurs, a process in which the special shell extends over the crystallizable formation it surrounds, forming a single structure from which the crystal will develop.

# Task

1. Determine the number of crystallizable formations that can be identified on the analyzed sample.
2. Display the sample result after crystallization.

# Input data

The input file `cristale.in` contains on the first line a natural number $c$ representing the task that needs to be solved ($1$ or $2$). The second line contains two natural numbers $M$ and $N$, separated by a space, having the meaning as described above. The following $M$ lines contain $N$ natural numbers each, separated by a space, representing the molecules in the analyzed sample.

# Output data

If the value of $c$ is $1$, then only task $1$ will be solved, in which case the first line of the output file `cristale.out` will contain a natural number representing the number of crystallizable formations identified in the analyzed sample.
If the value of $c$ is $2$, then only task $2$ will be solved. In this case, the output file `cristale.out` will contain on each of the first $M$ lines, $N$ natural numbers separated by a space, representing the molecules of the sample result after crystallization.

# Constraints and clarifications

* $4 \ \leq \ M, \ N \ \leq \ 800$ and the type of each molecule is expressed by a natural number in the interval $[1, 16]$;
* no crystallizable formations can be identified on the edge of the sample;
* there is at least one crystallizable formation on the analyzed sample;
* the sample does not contain crystallizable formations stuck (with neighboring cells in one of the four directions);
* for the correct solution of task $1$, $30\%$ of the points are given, and for the correct solution of task $2$, $70\%$ of the points are given.

# Example 1

`cristale.in`
```
1
6 8
5 6 6 1 5 2 6 5
6 9 9 6 1 7 1 2
6 6 9 6 3 4 1 6
2 2 6 3 4 7 4 2
8 8 2 4 7 7 4 6
8 2 7 2 4 4 2 5
```

`cristale.out`
```
2
```

## Explanation

Task $1$ of the problem will be solved.
The sample has $6$ rows with $8$ molecules each. On this sample, we observe a crystallizable formation with cells of type $9$, isolated by the special shell made of identical cells, all type $6$, and a crystallizable formation with cells of type $7$, isolated by the special shell made of identical cells, all type $4$. The formation of $3$ molecules of type $8$ is not a crystallizable formation because it is on the edge of the sample.
~[cristale3.png|width=20em]

# Example 2

`cristale.in`
```
2
6 8
5 6 6 1 5 2 6 5
6 9 9 6 1 7 1 2
6 6 9 6 3 4 1 6
2 2 6 3 4 7 4 2
8 8 2 4 7 7 4 6
8 2 7 2 4 4 2 5
```

`cristale.out`
```
5 6 6 1 5 2 6 5
6 6 6 6 1 7 1 2
6 6 6 6 3 4 1 6
2 2 6 3 4 4 4 2
8 8 2 4 4 4 4 6
8 2 7 2 4 4 2 5
```

## Explanation

Task $2$ of the problem will be solved.
After crystallization, the shell around each of the two crystallizable formations extends over them.
~[cristale4.png|width=20em]