```markdown
# Task

Let the set $M= \{1, 2, 3, \dots , n \}$. We will define a *bipermutation of order $n$* as a matrix $a$ with two rows and $n$ columns, in which each number $k$ of the set $M$ appears in the matrix **in two distinct columns** (figures $1$, $2$, $3$ and $4$ each contain a bipermutation, while the matrix in figure $0$ is not a bipermutation). 
In a bipermutation we can perform the following operations:
1. swap two elements in the same column (figure $1 \rightarrow$ figure $2$)
2. swap two columns (figure $1 \rightarrow$ figure $3$)
3. swap two distinct values $x$ and $y$ in the bipermutation (figure $1 \rightarrow$ figure $4$)

~[echival.png]

Two bipermutations are equivalent if there exists a sequence of operations through which the first bipermutation can be transformed into the second. In the figures above, all four bipermutations are equivalent.
If two bipermutations are equivalent, then they belong to the same *equivalence class*.

Given a bipermutation of order $n$, check its equivalence with $10$ other bipermutations of order $n$.

# Input data

The input file `echival1.in` contains on the first line the natural number $n$, with the above significance. The next $2$ lines contain $n$ numbers separated by space and describe the bipermutation to be checked, the next $20$ lines describe analogously the $10$ bipermutations of the set, each on two lines.

# Output data

The output file `echival1.out` will contain $10$ consecutive lines, in the order the bipermutations are read from the input file, each with a natural number as follows: $1$, if the current bipermutation is equivalent to the first bipermutation read, and $0$ otherwise.

# Constraints and clarifications

* $3 \leq n \leq 100\ 000$;
* The problem is worth $50$ points in the contest

# Example 1

`echival1.in`
```
5
5 3 4 1 2
2 4 1 3 5
5 2 4 4 1
3 1 5 3 2
1 1 2 3 4
2 4 5 5 3
1 1 5 3 4
4 3 2 2 5
2 1 3 4 4
1 5 2 3 5
3 2 4 1 1
5 3 2 4 5
3 4 5 5 1
4 2 3 1 2
1 3 2 3 4
4 1 5 5 2
5 2 5 1 1
3 4 2 4 3
4 4 5 2 1
1 2 3 3 5
3 5 3 2 2
1 1 5 4 4
```

`echival1.out`
```
1
0
0
0
0
0
0
0
0
1
```

## Explanation

The first bipermutation is 

$$
\begin{pmatrix}
5 & 3 & 4 & 1 & 2 \\
2 & 4 & 1 & 3 & 5
\end{pmatrix}
$$

Among the following $10$ bipermutations, only the first and the last are equivalent to this bipermutation.

The bipermutation 

$$
\begin{pmatrix}
5 & 3 & 4 & 1 & 2 \\
2 & 4 & 1 & 3 & 5
\end{pmatrix}
$$

is equivalent to the bipermutation

$$
\begin{pmatrix}
5 & 2 & 4 & 4 & 1 \\
3 & 1 & 5 & 3 & 2
\end{pmatrix}
$$

$$
\begin{pmatrix}
5 & 3 & 4 & 1 & 2 \\
2 & 4 & 1 & 3 & 5
\end{pmatrix} \xrightarrow{2} \begin{pmatrix}
3 & 5 & 4 & 1 & 2 \\
4 & 2 & 1 & 3 & 5
\end{pmatrix} \xrightarrow{3} \begin{pmatrix}
5 & 3 & 4 & 1 & 2 \\
4 & 2 & 1 & 5 & 3
\end{pmatrix} \xrightarrow{3} \begin{pmatrix}
5 & 4 & 3 & 1 & 2 \\
3 & 2 & 1 & 5 & 4
\end{pmatrix} \xrightarrow{3} \begin{pmatrix}
5 & 2 & 3 & 1 & 4 \\
3 & 4 & 1 & 5 & 2
\end{pmatrix} \xrightarrow{1} \begin{pmatrix}
5 & 2 & 3 & 4 & 1 \\
3 & 1 & 4 & 5 & 2
\end{pmatrix} \xrightarrow{2} \begin{pmatrix}
5 & 2 & 4 & 4 & 1 \\
3 & 1 & 5 & 3 & 2
\end{pmatrix}
$$

The bipermutations

$$
\begin{pmatrix}
5 & 3 & 4 & 1 & 2 \\
2 & 4 & 1 & 3 & 5
\end{pmatrix}
$$

and

$$
\begin{pmatrix}
1 & 1 & 2 & 3 & 4 \\
2 & 4 & 5 & 5 & 3
\end{pmatrix}
$$

are not equivalent.
```
