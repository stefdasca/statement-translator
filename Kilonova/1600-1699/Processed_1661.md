Given two 2D arrays $a$ and $b$, each with $m$ rows and $n$ columns, we define the following operations:

1. The sum of arrays $a$ and $b$, as an array $c$ with $m$ rows and $n$ columns, where each element is equal to the sum of the elements in the same row and column from $a$ and $b$. In this case, we use the operator `+`, that is $c = a + b$.
2. The product of arrays $a$ and $b$, as an array $d$ with $m$ rows and $n$ columns, where each element is equal to the product of the elements in the same row and column from $a$ and $b$. In this case, we use the operator `$\cdot$`, that is $d = a \cdot b$.

If $a$ and $b$ are identical arrays (i.e., $a$ and $b$ have identical elements in the same positions), then for $d$, the notation $a^2$ or $b^2$ is also used.

Example:
For $m = 2$, $n = 3$ and the arrays:

~[operatii.png]

Given a 2D array $a$ with $m$ rows, $n$ columns, and natural number components, we want to determine a sequence of 2D arrays: $b_1$, $b_2$, $\dots$, $b_k$ with the minimum number of terms (minimum $k$), with the property that $a = b_1^2 + b_2^2 + \dots + b_k^2$.

# Task

Write a program that determines the 2D arrays $b_1$, $b_2$, $\dots$, $b_k$ with the property mentioned above.

# Input data

The input file `operatii.in` contains on the first line the natural numbers $m$ and $n$ separated by a space. The next $m$ lines contain the elements of the array $a$, with $n$ numbers on each line, and within a line, the numbers being separated by a space.

# Output data

The output file `operatii.out` contains on the first line a natural number representing the value $k$, then on the next $k \cdot m$ lines the elements of the $k$ arrays $b_1$, $b_2$, $\dots$, $b_k$. Each of these arrays will be written on $m$ consecutive lines, with $n` numbers separated by a space on each line.

# Constraints and clarifications

* $1 \leq m, n \leq 200$
* Components of the array a are natural numbers $\leq 10\ 000$.
* There may be multiple solutions, but the output file will contain one of them.
* $30\%$ of the tests have the components of the array $a$ less than or equal to $100$ and $m, n \leq 100$.
* $60\%$ of the tests have the components of the array $a$ less than or equal to $1\ 000$.

# Example

`operatii.in`
```
2 3
1 2 4
5 5 9
```

`operatii.out`
```
2
1 1 0
2 2 3
0 1 2
1 1 0
```

## Explanation

$a$ is: 

```
1 2 4
5 5 9
```

$b_1$ is: 

```
1 1 0
2 2 3
``` 

and $b_1^2$ is: 

```
1 1 0
4 4 9
```

$b_2$ is: 
```
0 1 2 
1 1 0
```
and $b_2^2$ is: 

```
0 1 4
1 1 0
```

It can be observed that $b_1^2 + b_2^2 = a$.