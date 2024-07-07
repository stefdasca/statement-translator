Passionate about computer science and puzzles, Dorel constructed a matrix $ A $ of size $ N \times M $ by gluing several rectangular pieces of different sizes. Each piece is composed of $ 1 \times 1 $ elements and holds the same value (see examples). The resulting matrix has no empty spaces, and the pieces it is composed of do not overlap. There are no two pieces with the same value.
Although initially it seemed like this design was unique, it did not take long before Dorel got bored. Thus, now he wants to "upgrade" the constructed matrix. Dorel selects a submatrix delimited by the coordinates $(x1,y1)$ - top left corner, $(x2,y2)$ - bottom right corner ($1 \le x1 \le x2 \le N$, $1 \le y1 \le y2 \le M$), where he increases all the values of the elements of the submatrix by the value $ V $.

Dorel performs **in order** $ Q $ upgrade operations, numbered from 1 to $ Q $. Upon the completion of the $ Q $ upgrade operations, all the elements in the matrix have a value greater than or equal to $ K $. After an upgrade operation, the initial structure of the matrix changes.

# Task
Given Dorel's legendary skill, you must help him solve the following problems:
1. Determine the coordinates of the piece with the maximum number of elements before Dorel performs the upgrade operations.
2. Determine the minimum number of upgrade operations after which all the elements in the matrix have a value greater than or equal to $ K $.

# Input data
The input data is read from the file `amat.in`, which has the following structure:
- The first line contains the natural number $ C $, which can be equal to 1 or 2, depending on the task to be solved;
- The next line contains the two natural numbers $ N $ and $ M $ with the meaning given in the statement;
- On the following $ N $ lines are the elements of the matrix $ A $.
- If $ C = 2 $, then the input file additionally contains:
  - On line $ N+2 $, the natural numbers $ Q $ and $ K $ with the meanings given in the statement;
  - On the next $ Q $ lines, the description of the submatrices on which upgrade operations are performed in the form: $ x1 \ y1 \ x2 \ y2 \ V $.

# Output data
The output data will be written to the file `amat.out`, as follows:

If $ C = 1 $, four non-zero natural numbers $ x1 \ y1 \ x2 \ y2 $ separated by space, representing the coordinates of the top left corner and the bottom right corner where the piece with the maximum number of elements is placed before the upgrade. If there are several such pieces, then the coordinates of the piece for which the top-left corner has the highest row value, and at equal rows, the piece with the highest column coordinate will be written.

If $ C = 2 $, a non-zero natural number $ NR $ representing the minimum number of upgrade operations after which all the elements in the matrix have a value greater than or equal to $ K $ will be written.

# Constraints and clarifications
- $ 2 \le N, M \le 1 \ 000 $; $ 1 \le Q \le 100 \ 000 $; $ 1 \le V \le 1 \ 000 $;
- $ -1 \ 000 \le $ elements of the matrix $ A $ before the upgrade $ \le 1 \ 000 $;
- The upgrade operations are performed in the order of reading;
- For tests worth 30 points, $ C = 1 $;
- For tests worth 30 points, $ C = 2 $ and $ N, M, Q \le 2 \ 500 $;
- For tests worth 50 points, $ C = 2 $ and $ Q \le 4 \ 000 $;
- For tests worth 70 points, $ C = 2 $.

# Example 1
`amat.in`
```
1
4 6
1 1 1 3 2 2
1 1 1 3 2 2
6 4 4 4 2 2
6 4 4 4 5 7
```
`amat.out`
```
3 2 4 4
```

## Explanation
Solving task 1. The initial matrix constructed by Dorel is:

~[amat.jpg]

There are 3 pieces with the maximum number of equal values, but the piece that meets the requirements has coordinates: $ 3 \ 2 \ 4 \ 4 $.

# Example 2
`amat.in`
```
2
4 6
1 1 1 3 2 2
1 1 1 3 2 2
6 4 4 4 2 2
6 4 4 4 5 7
3 6
1 1 3 3 5
1 2 4 6 5
4 1 4 3 1
```
`amat.out`
```
2
```

## Explanation
Solving task 2. The initial matrix constructed is as presented above. Dorel performs 3 upgrade operations.

The matrix obtained after the first upgrade:

\[
\begin{bmatrix} 
\textcolor{lime}{6} & \textcolor{lime}{6} & \textcolor{lime}{6} & 3 & 2 & 2 \\
\textcolor{lime}{6} & \textcolor{lime}{6} & \textcolor{lime}{6} & 3 & 2 & 2 \\
\textcolor{lime}{11} & \textcolor{lime}{9} & \textcolor{lime}{9} & 4 & 2 & 2 \\
6 & 4 & 4 & 4 & 5 & 7 
\end{bmatrix}
\]

The matrix obtained after the second upgrade:

\[
\begin{bmatrix} 
6 & \textcolor{lime}{11} & \textcolor{lime}{11} & \textcolor{lime}{8} & \textcolor{lime}{7} & \textcolor{lime}{7} \\
6 & \textcolor{lime}{11} & \textcolor{lime}{11} & \textcolor{lime}{8} & \textcolor{lime}{7} & \textcolor{lime}{7} \\
11 & \textcolor{lime}{14} & \textcolor{lime}{14} & \textcolor{lime}{9} & \textcolor{lime}{7} & \textcolor{lime}{7} \\
6 & \textcolor{lime}{9} & \textcolor{lime}{9} & \textcolor{lime}{9} & \textcolor{lime}{10} & \textcolor{lime}{12} 
\end{bmatrix}
\]

The matrix obtained after the third upgrade:

\[
\begin{bmatrix} 
6 & 11 & 11 & 8 & 7 & 7 \\
6 & 11 & 11 & 8 & 7 & 7 \\
11 & 14 & 14 & 9 & 7 & 7 \\
\textcolor{lime}{7} & \textcolor{lime}{10} & \textcolor{lime}{10} & 9 & 10 & 12 
\end{bmatrix}
\]

At the end of all upgrade operations, the matrix has all values greater than or equal to 6. It is observed that the first two upgrade operations are sufficient for all elements of the matrix to be greater than or equal to 6.