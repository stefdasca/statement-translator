Here's the translated text:

---

On a horizontal table, there is an ultra-flexible strip made up of $2^n$ squares with a side length of $1$ cm. The thickness of the strip is $1$ mm. The squares are numbered from left to right from $1$ to $2^n$. This strip can be folded in half, overlapping one part over the other (left over right or vice versa). Thus, certain positions overlap, resulting in double thickness and a length of $2^{n-1}$ cm. The obtained strip can be further folded in half. This process is repeated $n$ times until a thickness of $2^n$ mm and a length of $1$ cm is achieved (i.e., all squares will overlap, forming a single column).

Using a pin, we will fix square $k$ of the strip to the table and apply the folding process described above, thus obtaining a column whose base is square $k$. In this column, we will number the positions of the squares from bottom to top from $1$ to $2^n$.

There are two types of possible queries:

1. Given a square (let's call it the _special_ square), determine its final position (in the column).
2. Given the final position of the special square, determine its number.

For example, for $n=3$ and $k=5$, we will obtain.

~[image.png|align=left]

# Task

Given the values $n$ and $k$, write a program that answers one of the queries of type $1$ or type $2$.

# Input data

The file `banda.in` contains $4$ lines. The first line contains the natural number $n$. The second line contains the natural number $k$, representing the position of the fixed square. The third line contains a digit $c$ that can be $1$ or $2$, indicating the type of query. If the digit $c$ is $1$, the fourth line contains the natural number $s$ representing the number of the special square. If the digit $c$ is $2$, the fourth line contains a natural number $f$ representing the final position of the special square.

# Output data

The file `banda.out` will contain a single line that will contain a natural number representing the result of the query.

# Constraints and clarifications

* $2 \leq n \leq 30$
* $1 \leq k, s, f \leq 2^n$
* For $30\%$ of tests $n \leq 7$. For $50\%$ of tests $c=1$

# Example 1

`banda.in`
```
3
5
1
2
```

`banda.out`
```
6
```

## Explanation

In the example, the strip with a length of $2^3=8$ cm is fixed to the table at position $5$.
In the first example, we need to find the final position of square $2$ (which is $6$).

# Example 2

`banda.in`
```
3
5
2
4
```

`banda.out`
```
8
```

## Explanation

In the second example, the final position $4$ is known, and we need to find the number of the special square ($8$).