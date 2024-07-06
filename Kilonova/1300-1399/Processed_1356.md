```markdown
On his birthday, Gigel received a rectangular cake adorned with a grid that divides the cake into $m \cdot n$ squares, with each square containing either a cherry or a strawberry.

The fruit grid is represented by a matrix with $0$ and $1$, where $0$ means cherry and $1$ means strawberry. The birthday boy is allowed to cut $k$ slices of cake. A slice can be made by cutting along the grid lines, from one end to the other, with a width equal to $1$, from any side of the cake, coded as $N, E, S, W$. Being a big strawberry fan, Gigel wants to cut the $k$ slices in such a way that the number of strawberries in these slices is as large as possible.

For example, if the initial cake is represented as a matrix with $6 \cdot 6$ rows and columns, after $3$ cuts $N, E, W$ the remaining piece and the obtained slices will be as shown in the adjacent figure.

$$
\begin{array}{|c|c|c|c|c|c|}
\hline
0 &1 &1 &1 &0 &1\\
\hline
1 &0 &0 &0 &0 &1\\
\hline
0 &0 &0 &1 &0 &0\\
\hline
0 &1 &0 &1 &0 &1\\
\hline
1 &0 &0 &0 &0 &0\\
\hline
1 &1 &1 &0 &0 &1\\
\hline
\end{array}

\ \ \ \ 
\implies

\begin{array}{}

\text{N \ } \\

\begin{array}{|c|c|c|c|c|c|}
\hline
0 &1 &1 &1 &0 &1 \\
\hline
\end{array}
\ \\ \\

\begin{array}{}
\text{ V \  }
\begin{array}{|c|}
\hline
1 \\
\hline
0 \\
\hline
0 \\
\hline
1 \\
\hline
1 \\
\hline
\end{array}
\end{array}
\ \\ \\ \\

\begin{array}{|c|c|c|c|}
\hline
0 &0 &0 &0\\
\hline
0 &0 &1 &0\\
\hline
1 &0 &1 &0\\
\hline
0 &0 &0 &0\\
\hline
1 &1 &0 &0\\
\hline
\end{array}

\ \\ \\ \\

\begin{array}{|c|}
\hline
1 \\
\hline
0 \\
\hline
1 \\
\hline
0 \\
\hline
1 \\
\hline
\end{array}
\text{ \ E \ }

\end{array}
$$

# Task

Write a program to determine the number of possible ways to cut the $k$ slices of cake in order to obtain a maximum number of strawberries. Two variations that differ only in the order of cutting but leave the same piece of cake are not considered distinct. For example, if the maximum number of strawberries can be obtained by one of the variations: $WNSEE$ or $WSSEE$, they are not considered distinct.

# Input data

The first line of the input file `tort.in` contains the dimensions of the cake, $m$ and $n$ and the number $k$ of slices cut by Gigel, separated by a space. The following $m$ lines describe the fruit grid by a matrix with values of $0$ and $1$.

# Output data

The first line of the output file `tort.out` will contain the maximum number of strawberries that can be obtained from the $k$ slices of cake. The second line will contain the number of distinct ways to obtain the maximum number of strawberries.

# Constraints and clarifications

* $2 \leq m, n \leq 500$
* $1 \leq k < min(m, n)$

# Example

`tort.in`
```
6 6 3
0 1 1 1 0 1
1 0 0 0 0 1
0 0 0 1 0 0
0 1 0 1 0 1
1 0 0 0 0 0
1 1 1 0 0 1
```

`tort.out`
```
10
5
```

# Explanation

The cake is made up of a grid with $m=6$ rows and $n=6$ columns and $k=3$ slices can be cut. A maximum of $10$ strawberries can be obtained.

The $5$ ways to cut the $3$ slices are:
$NNS, NSE, NSW, EVW$ and $NEW$
```