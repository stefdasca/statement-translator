```markdown
Consider a matrix $A$ of dimensions $2^N$ x $2^N$ given. This is constructed as follows:
It starts with a matrix of dimension $2$ x $2$ having small letters of the English alphabet as elements. The matrix $B$ of dimension $2^k$ x $2^k$ is formed from four submatrices of dimension $2^{k-1}$ x $2^{k-1}$ and is obtained from the matrix $C$ of dimension $2^{k-1}$ x $2^{k-1}$, as follows:

* The submatrix from the top left will be $C$
* The submatrix from the top right will be formed from $C$, by increasing each element by $3$ (`a` becomes `d`, `b` becomes `e`, `z` becomes `c`)
* The submatrix from the bottom left will be formed from $C$, by decreasing each element by $4$ (`a` becomes `v`, `b` becomes `x`, \dots, `z` becomes `u`)
* The submatrix from the bottom right is $C$ rotated $180$ degrees
* For example, if $C$ of dimension $2$ x $2$ has the value:

For example, if $C$ of dimension $2$ x $2$ has the value:

~[image.png|align=left]

Then the matrix $B$ of dimension $2^2$ x $2^2$ has the value:

~[image2.png|align=left]

# Task

Given $Q$ triplets $(i, j, L)$, with the meaning: at position $A_{i,j}$ is the letter $L$. What is the maximum number of triplets that can be selected so that all are true?

Example:
$N = 2, Q = 7$
***(1, 2, b)***
***(2, 3, f)***
(2, 1, d)
(1, 2, z)
***(4, 1, y)***
***(4, 4, a)***
***(3, 3, d)***

The answer is $5$ (the first, the second, and the last three). For example, if the initial matrix is:
- $ \\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}  $

Then the matrix $A$ will be:
- $ \\begin{pmatrix} a & b & d & e \\\\ c & d & f & g \\\\ v & x & d & c \\\\ y & z & b & a \\end{pmatrix}  $

# Input data

The input file `expandmat.in` contains on the first line the numbers $N$ and $Q$, separated by a space, with the significance above, and on each of the following $Q$ lines there will be a triplet of numbers $i, j, L$ with the meanings from the statement.

# Output data

The output file `expandmat.out` will contain on the first line the maximum number of triplets that can be selected so that all are true.

# Constraints and clarifications

* $1 \leq N \leq 60$
* $1 \leq Q \leq 100\ 000$
* The matrix is indexed from $1$.

|#|Points|Constraints|
|-|-|--------|
|1|21|the initial matrix contains only the letters `a`,`b`,`c`,`d` and $N \leq 8, Q \leq 100$|
|2|19|the initial matrix contains only the letters `a`,`b`,`c`,`d` and $N \leq 60, Q \leq 300$|
|3|13|the letters of the initial matrix are equal|
|4|21|in the initial matrix, the letters on the same line are equal|
|5|9|it is guaranteed that the answer is at least $Q/2$|
|6|17|Without additional constraints|

# Example 1

`expandmat.in`
```
2 7
1 2 b
2 3 f
2 1 d
1 2 z
4 1 y
4 4 a
3 3 d
```

`expandmat.out`
```
5
```

## Explanation

***N = 2*** and ***Q = 7***.
The 5 triplets that can be chosen are:
***(1, 2, b)***
***(2, 3, f)***
***(4, 1, y)***
***(4, 4, a)***
***(3, 3, d)***

If the initial matrix is:
- $ \\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}  $

Then the final matrix is:
- $ \\begin{pmatrix} a & b & d & e \\\\ c & d & f & g \\\\ v & x & d & c \\\\ y & z & b & a \\end{pmatrix}  $

This matrix satisfies all the 5 triplets.
```