Nargy and Fumeanu are playing the following game: Nargy writes on a piece of paper the sequence of natural numbers from $1$ to $N$ in ascending order. Then, he performs $M$ operations of the form: two indices $i$ and $j$ are taken, and the segment between positions $i$ and $j$ in the sequence is reversed. After each operation, Nargy asks Fumeanu which number is at position $k$.

# Task

Write a program that helps Fumeanu answer Nargy's questions.

# Input data

The input file `rev.in` contains on the first line two natural numbers $N$ and $M$. The following $M$ lines will contain three natural numbers $i \\ j \\ k$ with the above-mentioned significance. The numbers on the same line are separated by a space.

# Output data

The output file `rev.out` will contain $M$ lines, one line for each operation in the input file. On line $i$, it will contain the number that is at position $k$ in the sequence after the first $i$ operations.

# Constraints and clarifications

* $1 \leq N \leq 100 \ 000$
* $1 \leq M \leq 20 \ 000$
* For $20\\%$ of the tests $N \leq 2 \ 000$ and $M \leq 1 \ 000$
* For $40\\%$ of the tests $M \leq 5 \ 000$

# Example

`rev.in`
```
7 3
1 3 2
4 6 5
2 5 3
```

`rev.out`
```
2
5
6
```

## Explanation

* $\\underline{1 \\ 2 \\ 3} \\ 4 \\ 5 \\ 6 \\ 7$
* $3 \\ 2 \\ 1 \\ \\underline{4 \\ 5 \\ 6} \\ 7$
* $3 \\ \\underline{2 \\ 1 \\ 6 \\ 5} \\ 4 \\ 7$
* $3 \\ 5 \\ 6 \\ 1 \\ 2 \\ 4 \\ 7$