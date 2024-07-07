
Matrix $T$ with $n$ rows (numbered from $1$ to $n$) and $m$ columns (numbered from $1$ to $m$) containing integers is considered.

A submatrix of matrix $T$ is defined by the top-left corner row and column $(x_1,y_1)$, and the bottom-right corner row and column $(x_2,y_2)$, with $1 \leq x_1 \leq x_2 \leq n$ and $1 \leq y_1 \leq y_2 \leq m$ and contains all the elements at positions $(x,y)$ of the matrix for which $x_1 \leq x \leq x_2$ and $y_1 \leq y \leq y_2$. Specifically, the submatrix with the top-left corner at $(1,1)$ and the bottom-right corner at $(n,m)$ is identical to the matrix $T$.

For each row of a given submatrix, the row sum is calculated by adding the elements on that row. The sums obtained for each of the rows of this submatrix form the sequence $S$ of row sums. We say that a submatrix is *aprogressive* if $x_1 < x_2$ and $y_1 < y_2$ and the sequence $S$ of row sums can be rearranged to form an arithmetic progression with a **non-zero** difference $r$.

~[matrice4x4.png|align=right|width=20%]

The compressed form of a submatrix $R$ with the top-left corner $(x_1,y_1)$ and the bottom-right corner $(x_2,y_2)$ is denoted as $\mathbb{C}(R)$ and is defined as follows:
* if $x_1 = x_2$ (it is a row submatrix) or if $y_1 = y_2$ (it is a column submatrix) then its compressed form is $\mathbb{C}(R)$= $(x_1,y_1,x_2,y_2,0)$. Otherwise,
* if $R$ is *aprogressive*, its compressed form is $\mathbb{C}(R)$= $(x_1,y_1,x_2,y_2,r)$. Otherwise,
* $R$ is divided into $4$ submatrices $A$, $B$, $C$, $D$ with disjoint sets of elements as illustrated in the adjacent figure, where submatrix $A$ has the top-left corner at $(x_1,y_1)$ and the bottom-right corner at $(\left[\frac{x_1+x_2}{2}\right], \left[\frac{y_1+y_2}{2}\right])$, $[x]$ representing the integer part of the real number $x$. The compressed form of submatrix $R$ is defined recursively as $\mathbb{C}(R)$ =$(\mathbb{C}(A), \mathbb{C}(B), \mathbb{C}(C), \mathbb{C}(D))$.

For example, the matrix $T$ in the adjacent figure has $n=5$, $m=5$, $x_1=1$, $y_1=1$, $x_2=5$, $y_2=5$ is compressed according to the reasoning below.

~[matrice-originala.png|align=right|width=20%]

Because it is neither a row matrix nor a column matrix, the sequence $S$ of row sums for the matrix $T$ is determined, namely: $9,19,14,8,10$. Since it is not an *aprogressive* matrix, it will be divided into submatrices:
* $A$  – with top-left and bottom-right corners $(1,1) – (3,3)$;
* $B$  – with top-left and bottom-right corners $(1,4) – (3,5)$;
* $C$  – with top-left and bottom-right corners $(4,1) – (5,3)$;
* $D$  – with top-left and bottom-right corners $(4,4) – (5,5)$;

For submatrix $A$ the sequence $S$ of row sums is: $4,10,7$, which, when rearranged, forms an arithmetic progression with a difference $r=3$. The compressed form of submatrix $A$ is $\mathbb{C}(A)$ = $(1,1,3,3,3)$.

For submatrix $B$ the sequence $S$ of row sums is: $5,9,7$, which, when rearranged, forms an arithmetic progression with a difference $r=2$. The compressed form of submatrix $B$ is $\mathbb{C}(B)$ = $(1,4,3,5,2)$.

For submatrix $C$ the sequence $S$ of row sums is: $5,5$, which, when rearranged, forms an arithmetic progression but with a difference $r=0$. For this submatrix, the subdivision process is resumed. The compressed form of submatrix $C$ is $\mathbb{C}(C)$ = $((4,1,4,2,0)(4,3,4,3,0)(5,1,5,2,0)(5,3,5,3,0))$.

For submatrix $D$ the sequence $S$ of row sums is: $3,5$, which, when rearranged, forms an arithmetic progression with a difference $r=2$. The compressed form of submatrix $D$ is $\mathbb{C}(D)$ = $(4,4,5,5,2)$.

Thus, the compressed form of matrix $T$ is: $\mathbb{C}(T)$ = `((1,1,3,3,3)(1,4,3,5,2)((4,1,4,2,0)(4,3,4,3,0)(5,1,5,2,0)(5,3,5,3,0))(4,4,5,5,2))`.

# Task

Given the dimensions and elements of matrix $T$ determine:

* The row indices of matrix $T$ for which the sum of the elements on each of these rows is maximal.
* The row indices of matrix $T$ for which the elements can be rearranged such that they form on that row, a non-zero difference arithmetic progression.
* The compressed form of matrix $T$.

# Input data

The input file `aprogressive.in` contains on the first line the number $c$ representing the task that needs to be solved. 
The second line contains the natural numbers $n$ and $m$ with the meaning from the statement. 
Each of the next $n$ lines contains $m$ integers representing the elements of matrix $T$. 
The numbers on the same line of the input file are separated by a space.

# Output data

The output file `aprogressive.out` will contain either the answer for task $1$ (if $c=1$), the answer for task $2$ (if $c=2$), or the answer for task $3$ (if $c=3$).

For task $1$ the indices determined for task $1$ will be printed, each on a separate line, in **strictly increasing order**.

For task $2$ the indices determined for task $2$ will be printed, each on a separate line, in **strictly increasing order**, and if there are no rows that meet the requirement, $0$ will be printed.

For task $3$ the compressed form of matrix $T$ will be printed, on a single line, without spaces, with the values separated by commas, properly enclosed in parentheses.

# Constraints and clarifications

* $c \in \{1, 2, 3\}$;
* $1 \leq n, m \leq 1 \ 024$;
* The elements of matrix $T$ belong to the interval [$-10^9, 10^{9}$].

|# | Score | Constraints|
| - | - | ------------|
|1|20|$c = 1$|
|2|25|$c = 2$|
|3|25|$c = 3$ and $n, m \leq 512$|
|4|30|$c = 3$|

# Example 1

`aprogressive.in`
```
1
3 4
6 3 7 4
3 1 4 2
2 6 4 8
```

`aprogressive.out`
```
1
3
```

## Explanation

$c=1$, $n=3$, $m=4$. Task $1$ is solved.
The sum on row $1$ is equal to $20$. The sum on row $2$ is equal to $10$. The sum on row $3$ is equal to $20$.
The indices of rows $1$ and $3$ are printed, in this order, because on these rows the sum is maximal.

# Example 2


`aprogressive.in`
```
2
3 4
6 3 7 4
3 1 4 2
2 6 4 8
```

`aprogressive.out`
```
2
3
```

## Explanation

$c=2$, $n=3$, $m=4$. Task $2$ is solved.
The elements of row $2$ can be rearranged such that they form an arithmetic progression with a difference $r=1$: $1, 2, 3, 4$.
The elements of row $3$ can be rearranged such that they form an arithmetic progression with a difference $r=2$: $2, 4, 6, 8$.
The indices of rows $2$ and $3$ are printed, in this order.

# Example 3


`aprogressive.in`
```
3
5 5
2 1 1 3 2
3 2 5 4 5
1 4 2 1 6
2 2 1 2 1
1 3 1 2 3
```

`aprogressive.out`
```
((1,1,3,3,3)(1,4,3,5,2)((4,1,4,2,0)(4,3,4,3,0)(5,1,5,2,0)(5,3,5,3,0))(4,4,5,5,2))
```

## Explanation

$c=3$, $n=5$, $m=5$. Task $3$ is solved.
The answer to this task is printed on a single line in the output file.
The steps to obtain the answer are explained in the statement.

