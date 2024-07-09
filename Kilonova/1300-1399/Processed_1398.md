For a matrix $A$ with $n$ rows and $m$ columns, containing natural numbers, **the median of matrix $A$** is defined as the value situated at the midpoint of the sorted sequence formed by all elements of matrix $A$, if the number of elements in this sequence is odd, or the smallest value of the two middle values if the number of elements in this sequence is even. 

Three types of operations that can be applied to matrix $A$ are defined:

* operation type $1$, denoted $L \\ x$, which consists of deleting the row with index $x$ from the matrix;
* operation type $2$, denoted $C \\ y$, which consists of deleting the column with index $y$ from the matrix;
* operation type $3$, denoted $Q$, which results in determining the median value of the matrix.

Ami is passionate about mathematics and needs to solve the following problem: for a matrix $A$ on which a sequence of such operations is applied, determine the answers to all operations of type $3$.

# Task

Write a program that determines the values obtained after performing the operations of type $3$ from the sequence of operations applied to matrix $A$.

# Input data

The input file `amedie.in` contains on the first line three natural numbers $n,m$ and $q$ separated by spaces, representing, in order, the number of rows in matrix $A$, the number of columns in matrix $A$, and the number of operations applied to matrix $A$. Each of the next $n$ lines of the file contains $m$ natural numbers, separated by spaces, representing, in order, the elements on the rows of matrix $A$. Each of the next $q$ lines of the file contains a string representing an operation to be applied to matrix $A$.

# Output data

The output file `amedie.out` will contain the values obtained, in order, from all $Q$ operations in the sequence of operations applied to matrix $A$. Each of the obtained values will be printed on a separate line in the file, in the order established by the sequence of operations.

# Constraints and clarifications

* $2 \\leq n, m \\leq 800$
* $0 < q \\leq 2\ 000$
* the elements of matrix $A$ are non-zero natural numbers, strictly less than $100\ 001$
* row and column indices in the matrix are noted starting with $1$
* operations of types $1$ and $2$ are applied using the row and column indices from the initial matrix $A$
* it is guaranteed that any operation in the input file can be performed

# Example

`amedie.in`
```
4 4 4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
L 2
Q
C 1
Q
```

`amedie.out`
```
10
11
```

# Explanation

$$
\begin{CD}

\begin{array}{|c|c|c|c|}
\hline
1 &2 &3 &4\\
\hline
5 &6 &7 &8\\
\hline
9 &10 &11 &12\\
\hline
13 &14 &15 &16\\
\hline
\end{array}


@>L \\ 2>>

\begin{array}{|c|c|c|c|}
\hline
1 &2 &3 &4\\
\hline
\color{red}\sout{5} &\color{red}\sout{6} &\color{red}\sout{7} &\color{red}\sout{8}\\
\hline
9 &10 &11 &12\\
\hline
13 &14 &15 &16\\
\hline
\end{array}

@>Q>> 

\begin{array}{} \\ \color{aqua}{10} \\
\begin{array}{|c|c|c|c|}
\hline
1_1 &2_2 &3_3 &4_4\\
\hline
\color{red}\sout{5} &\color{red}\sout{6} &\color{red}\sout{7} &\color{red}\sout{8}\\
\hline
9_5 &10_{\color{aqua}{6}} &11_7 &12_8\\
\hline
13_9 &14_{10} &15_{11} &16_{12}\\
\hline
\end{array}
\end{array}

\end{CD}

\\\\ \\\\ \\\\ \\\\

\begin{CD}

\begin{array}{|c|c|c|c|}
\hline
1 &2 &3 &4\\
\hline
\color{red}\sout{5} &\color{red}\sout{6} &\color{red}\sout{7} &\color{red}\sout{8}\\
\hline
9 &10 &11 &12\\
\hline
13 &14 &15 &16\\
\hline
\end{array}

@>C \\ 1>>

\begin{array}{|c|c|c|c|}
\hline
\color{red}\sout{1} &2 &3 &4\\
\hline
\color{red}\sout{5} &\color{red}\sout{6} &\color{red}\sout{7} &\color{red}\sout{8}\\
\hline
\color{red}\sout{9} &10 &11 &12\\
\hline
\color{red}\sout{13} &14 &15 &16\\
\hline
\end{array}

@>Q>>
\begin{array}{} \color{aqua}{11} \\
\begin{array}{|c|c|c|c|}
\hline
\color{red}\sout{1} &2_1 &3_2 &4_3\\
\hline
\color{red}\sout{5} &\color{red}\sout{6} &\color{red}\sout{7} &\color{red}\sout{8}\\
\hline
\color{red}\sout{9} &10_4 &11_{\color{aqua}{5}} &12_6\\
\hline
\color{red}\sout{13} &14_7 &15_8 &16_9\\
\hline
\end{array}
\end{array}

\end{CD}
$$