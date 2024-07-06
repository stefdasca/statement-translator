~[tripas.png|align=right]

Consider the pyramid arrangement of numbers in the figure (also known as Pascal's triangle). At the top and on the lateral edges of the pyramid, the number $1$ is found. The rest of the numbers in this triangle are formed as the sum of the two numbers above them. We define a $tripas(r, c, L)$ as an equilateral triangle of numbers within Pascal's triangle, with the specified position $(r,c)$ of its vertex and $L$, the length of its side. ($r$ = row, $c$ = column, $L$ = side length).

$tripas(3, 1, 4)$ - represents the triangle of numbers with the vertex positioned on the third row, the first element, and a side length of $4$ elements, meaning the numbers ($1$), ($1$, $3$), ($1$, $4$, $6$), ($1$, $5$, $10$, $10$) – written from top to bottom and from left to right. In the above figure, $tripas(3, 1, 4)$ has the elements framed in rectangles.

We denote by $S$ the sum of the elements of a $tripas(r, c, L)$.

# Task

Write a program that determines the number $S$, knowing the numbers $r$, $c$, and $L$ that define a $tripas(r, c, L)$. Because it can be very large, $S$ will be calculated modulo $3 \ 000 \ 017$.

# Input data

The input file `tripas.in` contains the natural numbers $r$, $c$, and $L$ separated by spaces on the first line.

# Output data

The output file `tripas.out` will contain on the first line the remainder of the division of the number $S$ by $3 \ 000 \ 017$.

# Constraints and clarifications

* $1 \leq c \leq r \leq 10^6$
* $1 \leq L \leq 10^6$

# Example

`tripas.in`
```
3 1 4
```

`tripas.out`
```
42
```

## Explanation

The triangle with the vertex situated on the first element of the third row and with a side length of $4$ elements has the sum of elements $1$ + $1$ + $3$ + $1$ + $4$ + $6$ + $1$ + $5$ + $10$ + $10$ = $42$.