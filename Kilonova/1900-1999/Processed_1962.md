```
Bossanip presents you with an $N \times N$ matrix initially filled with $0$. You can perform three types of operations on it:
* $1$ – Update $x \\ y \\ z$: Add integer value $z$ to the element at row $x$ and column $y$.
* $2$ – Query $x \\ y$: Request the sum of the elements in the submatrix determined by the top-left corner $(1,1)$ and the bottom-right corner $(x,y)$.
* $3$ – Undo $x$: Remove the last $x$ Update and Undo operations.

You are given $M$ such operations.
# Input data
The first line of the input file `undo.in` contains a natural number $N$ and a natural number $M$. The next $M$ lines contain the $M$ operations ($1 \\ x \\ y \\ z$ for Update; $2 \\ x \\ y$ for Query; $3 \\ x$ for Undo).
# Output data
The output file `undo.out` will contain the result of each Query operation, one per line.
# Constraints and clarifications
* $1 \\leq N \\leq 520$;
* $1 \\leq M \\leq 500 \ 000$;
* It is guaranteed that for Undo operations $x$, there have been at least $x$ Update and Undo operations prior.
* $1 \\leq z \\leq 2 \ 000$, for any operation of type $1$;
* Don't forget about Tassadar!

# Example

`undo.in`
```
5 11
1 1 1 2
1 2 3 1
2 1 3
1 3 2 4
1 2 2 10
2 3 2
3 2
1 1 1 3
2 5 5
3 3
2 4 4
```

`undo.out`
```
2
16
6
7
```
```