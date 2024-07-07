> *Colegiul Național “Frații Buzești�* ~[logos.png|align=right|width=20rem]
> *Centrul de Pregătire pentru Performanță în Informatică*
> **InfoCNFB** - Edition II, Seniors
> December 9, 2023

# Task

The map of the Rectangular Country is encoded by a matrix with $0$s and $1$s. The $1$s delimit the counties, marking their borders. Two neighboring $1$s on the same row, column, or diagonal are considered neighbors and thus part of the border.

We need to answer two types of questions:
- Question type $1$: How many counties are there?
- Question type $2$: A rectangular area (submatrix) where a forest needs to be established is given. We need to determine how many counties have a part of the forest within their territory.

# Input data

The first line of the file `padure.in` contains two numbers, $n$ and $m$, separated by space, representing the number of rows and the number of columns of the matrix.
The next $n$ lines contain $m$ elements each, which can be $0$ or $1$, not separated by spaces.
The next line contains a number $Q$. This can be $1$ or $2$, depending on the type of question we need to answer.
If the value is $2$, the next line contains another $4$ numbers, separated by space, $L_1$, $C_1$, $L_2$, $C_2$ representing the row and column of the top-left corner, respectively the row and column of the bottom-right corner.

# Output data

The file `padure.out` will contain a single number, representing the answer to the question given in the input file.

# Constraints and clarifications

* $1 \leq n, m \leq 1\ 000$;
* $1 \leq L_1 \leq L_2 \leq n$;
* $1 \leq C_1 \leq C_2 \leq n$;
* The $1$s on the borders do not belong to any county;
* For $31$ points, $n$ and $m$ are at most $50$ and $Q=1$;
* For the remaining points, we have $Q=2$.

# Example 1

`padure.in`
```
6 10
0001000010
0000111100
0001000000
1110011111
0000011000
0000010000
1
```

`padure.out`
```
4
```

## Explanation

There are 4 counties:

$\textcolor{green}{000}\textcolor{red}{1}\textcolor{blue}{0000}\textcolor{red}{1}\textcolor{yellow}{0}$
$\textcolor{green}{0000}\textcolor{red}{1111}\textcolor{yellow}{00}$
$\textcolor{green}{000}\textcolor{red}{1}\textcolor{yellow}{000000}$
$\textcolor{red}{111}\textcolor{yellow}{00}\textcolor{red}{11111}$
$\textcolor{yellow}{00000}\textcolor{red}{11}\textcolor{blue}{000}$
$\textcolor{yellow}{00000}\textcolor{red}{1}\textcolor{blue}{0000}$

# Example 2

`padure.in`
```
6 10
0001000010
0000111100
0001000000
1110011111
0000011000
0000010000
2
1 8 4 10
```

`padure.out`
```
2
```

## Explanation

If the rectangle with the top-left corner $1, 8$ and the bottom-right corner $4, 10$ is given, the answer is $2$ (there are $0$s corresponding to two counties):

$\textcolor{green}{000}\textcolor{red}{1}\textcolor{blue}{000}\colorbox{DarkGray}{\textcolor{blue}{0}\textcolor{red}{1}\textcolor{yellow}{0}}$
$\textcolor{green}{0000}\textcolor{red}{111}\colorbox{DarkGray}{\textcolor{red}{1}\textcolor{yellow}{00}}$
$\textcolor{green}{000}\textcolor{red}{1}\textcolor{yellow}{000}\colorbox{DarkGray}{\textcolor{yellow}{000}}$
$\textcolor{red}{111}\textcolor{yellow}{00}\textcolor{red}{11}\colorbox{DarkGray}{\textcolor{red}{111}}$
$\textcolor{yellow}{00000}\textcolor{red}{11}\textcolor{blue}{000}$
$\textcolor{yellow}{00000}\textcolor{red}{1}\textcolor{blue}{0000}$