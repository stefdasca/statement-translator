# Task

Given a text stored in a matrix $M$, defined by the coordinates of the top-left corner $(x_1,y_1)$ and the coordinates of the bottom-right corner $(x_2,y_2)$.

By applying a compression algorithm, the matrix $M$ is associated with a string of characters, denoted $C_M$.

The character string $C_M$ is constructed by applying the following rules:

a) If the matrix $M$ has a single row and a single column then $C_M$ contains only the character stored in the matrix

b) If all the elements of the matrix are identical then the entire matrix $M$ is compressed and $C_M$ is the string $k + c$, where $k$ represents the number of characters in the matrix, and $c$ is the stored character

c) If the matrix is composed of different characters and has at least two rows and two columns then:
   - the matrix is divided into $4$ submatrices $A$, $B$, $C$, $D$ as illustrated in the adjacent figure, where the coordinates of the top-left corner of submatrix $A$ are $(x_1,y_1)$, and the coordinates of the bottom-right corner are $(\lfloor \frac{x_2+x_1}{2} \rfloor, \lfloor \frac{y_2+y_1}{2} \rfloor)$
   - $C_M$ is the string `*` $+ C_A + C_B + C_C + C_D$, where $C_A$, $C_B$, $C_C$, $C_D$ are the character strings obtained, in order, by compressing the matrices $A$, $B$, $C$, $D$ using the same algorithm

~[2e2e22e2e.png]

d) If the matrix is composed of different characters and has a single row and multiple columns then $C_M$ is the string `*` $+ C_A + C_B$, where $A$, $B$, $C_A$, $C_B$ have the meanings described in point c).

e) If the matrix is composed of different characters and has multiple rows and a single column then $C_M$ is the string `*` $+ C_A + C_C$ where $A$, $C$, $C_A$, $C_C$ have the meanings described in point c).

# Task

Given the character string $C_M$ obtained by applying the compression algorithm to an $N \times N$ matrix $M$, determine:

a) the number of divisions that were necessary to obtain the compressed text

b) the initial matrix from which the compressed text originates.

# Input data

The input file `compresie.in` contains:

* the first line contains a string of characters representing the compressed text.

# Output data

The output file `compresie.out` contains:

* the first line will contain a natural number representing the number $nr$ of divisions that were necessary to obtain the compressed text
* the following $N$ lines will contain $N$ characters, lowercase letters of the English alphabet, not separated by spaces, representing, in order, the lines of the initial matrix.

# Constraints and clarifications

* $2 \leq N \leq 1000$
* $0 \leq nr \leq 1\ 000\ 000$
* $2 \leq$ the length of the compressed string $\leq 1\ 000\ 000$
* The text initially stored in the matrix $M$ contains only characters from the set of lowercase letters $\\{$`a`$, `b`, \dots, `z`$\\}$.
* For correctly solving task a) 20\% of the score is awarded, and for correctly solving both tasks the full score is awarded.

# Example 1

`compresie.in`
```
*4b*bbab4a*abbb 
```

`compresie.out`
```
3 
bbbb
bbab
aaab
aabb
```

## Explanation

There were $3$ divisions:

1. $M = *\begin{pmatrix}b & b\\b & b\end{pmatrix}\begin{pmatrix}b & b\\a & b\end{pmatrix}\begin{pmatrix}a & a\\a & a\end{pmatrix}\begin{pmatrix}a & b\\b & b\end{pmatrix}$
2. $\begin{pmatrix}b & b\\a & b\end{pmatrix} = *(b)(b)(a)(b)$
3. $\begin{pmatrix}a & b\\b & b\end{pmatrix} = *(a)(b)(b)(b)$

# Example 2

`compresie.in`
```
*4a*ab*aba
```

`compresie.out`
```
3 
aaa
aab
aba
```

## Explanation

There were $3$ divisions:

1. $M = *\begin{pmatrix}a & a\\a & a\end{pmatrix}\begin{pmatrix}a\\b\end{pmatrix}\begin{pmatrix}a & b\end{pmatrix}\begin{pmatrix}a\end{pmatrix}$
2. $\begin{pmatrix}a\\b\end{pmatrix} = *(a)(b)$
3. $\begin{pmatrix}a & b\end{pmatrix} = *(a)(b)$