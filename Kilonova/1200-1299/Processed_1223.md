```markdown
Consider a lidorian matrix with $x$ rows and $y$ columns. The rows of the matrix are numbered from bottom to top, with numbers from $0$ to $x-1$. The columns of the matrix are numbered from right to left, with numbers from $0$ to $y-1$. The lidorian matrix is composed only of $1$s and $0$s. 

~[joc.png]

For each row $i$, $sl_i$ is calculated as the sum of all products between $a(i,j)$ and $2^j$. For each column $k$, $sc_k$ is calculated as the sum of all products between $a(i,k)$ and $2^i$.

~[joc2.png]

Let $S_1$ be the sum of all sums calculated over the rows and let $S_2$ be the sum of all sums calculated over the columns. $S_1$ = $Sl_0$ + $Sl_1$ + $Sl_2$; $S_2$ = $Sc_0$ + $Sc_1$ + $Sc_2$ + $Sc_3$. We define $t$ = $S_1$ + $S_2$. "Move" is understood as an interchange between any two values $1$ and $0$ in the matrix. The lidorian game involves performing the minimum number of moves such that the value of $t$ is minimized.

# Task 

Write a program that allows the calculation of the minimum value of $t$. For this value of $t$, determine the minimum number of moves required.

# Input data

The input file `joc.in` contains, in order, by lines:

* $x$, $y$ number of rows, number of columns separated by a space.
* $a_{x-1,y-1}$; $a_{x-1,y-2}$; $\ldots$; $a_{x-1,0}$ elements of row $x-1$, without spaces between them.
* $a_{x-2,y-1}$; $a_{x-2,y-2}$; $\ldots$; $a_{x-2,0}$ elements of row $x-2$, without spaces between them.
* $\ldots$
* $a_{0,y-1}$; $a_{0,y-2}$; $\ldots$; $a_{0,0}$ elements of row $0$, without spaces between them.

# Output data

The file `joc.out` contains, in order, the first line containing the value of $t$, then the minimum number of moves, with a single space between them. 

# Constraints and clarifications

* $2 \leq x, y \leq 12$;
* the matrix contains at least one digit of $1$ 

# Example

`joc.in`
```
5 6 
100010
010000
000001
000010
011000 
```

`joc.out`
```
28 5
```

## Explanation

~[joc3.png]
```