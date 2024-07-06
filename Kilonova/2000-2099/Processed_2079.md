# Task

You are given a matrix $a$ with $n$ rows and $m$ columns consisting of lowercase English letters.

On this matrix, perform $q$ operations of the following types:

- `1 i j` - exchange rows $i$ and $j$ of the matrix.
- `2 i j` - exchange columns $i$ and $j$ of the matrix.
- `3 i j` - display the letter located at row $i$ and column $j$ of the matrix.

# Input data

The first line of the input file `lineswap.in` will contain three numbers $n$, $m$, and $q$.

The next $n$ lines contain the elements of matrix $a$, with $m$ lowercase letters on each line.

Each of the next $q$ lines contains 3 numbers $t$, $i$, and $j$, representing the descriptions of the operations.

# Output data

For each operation of type $3$, print to the output file `lineswap.out` the letter located at row $i$ and column $j$ of the matrix.

# Constraints and clarifications
- $2 \le n,m \le 5\ 000$;
- $1 \le q \le 3 \cdot 10^5$;
- $1 \le t \le 3$;
- If $t=1$, then $1 \le i < j \le n$;
- If $t=2$, then $1 \le i < j \le m$;
- If $t=3$, then $1 \le i \le n$ and $1 \le j \le m$;
- For 30 points, $1 \le q \le 3\ 000$;
- For 25 points, there are no operations of type $2$;
- For 15 points, $n \le 10$;
- For the remaining 30 points, there are no additional constraints.

# Example

`lineswap.in`
```
3 3 9
abc
def
ghi
3 1 1
1 1 3
3 3 3
1 2 3
3 2 2
2 1 2
3 2 1
2 2 3
3 3 1
```

`lineswap.out`
```
a
c
b
b
e
```

## Explanation
The letters displayed for the operations of type $3$ are indicated below:

$$
\begin{pmatrix} 
\text{{\color{green}{\underline{\textbf{a}}}}} b c \\ 
\text{d e f} \\ 
\text{g h i} 
\end{pmatrix} \rightarrow
\begin{pmatrix} 
\text{g h i} \\
\text{d e f} \\
\text{a b {\color{green}{\underline{\textbf{c}}}}}
\end{pmatrix} \rightarrow
\begin{pmatrix} 
\text{g h i} \\
\text{a {\color{green}{\underline{\textbf{b}}}} c} \\
\text{d e f}
\end{pmatrix} \rightarrow
\begin{pmatrix} 
\text{h g i} \\
\text{{\color{green}{\underline{\textbf{b}}}} a c} \\
\text{e d f}
\end{pmatrix} \rightarrow
\begin{pmatrix} 
\text{h i g} \\
\text{b c a} \\
\text{{\color{Green}{\underline{\textbf{e}}}}} f d
\end{pmatrix}
$$