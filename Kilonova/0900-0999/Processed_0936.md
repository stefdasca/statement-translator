Farmer Feder cultivates potatoes on a rectangular field of width $N$ meters and length $M$ meters, divided into $N \times M$ identical square zones of length $1$ meter, placed side by side, with $N$ along the width (on $N$ rows, numbered from $1$ to $N$) and $M$ along the length (on $M$ columns, numbered from $1$ to $M$).

In each square zone, there is one potato plant. Traversing the field from the first row to the last, each odd-numbered row is traversed from column $1$ to column $M$, and each even-numbered row is traversed from column $M$ to column $1$. The farmer (fond of mathematics) wrote down the numbers of potatoes produced by each plant, in traversal order, and found that he obtained the sequence of the unit digits of the first $N \cdot M$ terms of the Fibonacci sequence (see Figure $1$ where $N = 3$ and $M = 6$).

~[cartofi.png]

# Task

Write a program that reads the numbers $N$ and $M$ (as described in the statement), and then determines:

1. the number of plants in the field that did not produce any potatoes;
2. the maximum number of potatoes that can be produced by the plants in a square area of the farmer's field;
3. for each of the $Q$ pairs of numbers ($A, B$) read, the number of potatoes produced by the plants located in the square zones between columns $A$ and $B$, inclusive.

# Input data

The input file `cartofi.in` contains on the first line a natural number $C$ representing the task number to be solved ($1$, $2$, or $3$). The second line of the file contains the two natural numbers $N$ and $M$, separated by a space, as described in the statement. If $C = 3$, then the file will also contain on the third line the natural number $Q$, and on each of the following $Q$ lines, two natural numbers separated by a space representing a pair of numbers ($A, B$) among those $Q$.

# Output data

The output file `cartofi.out` will contain:

If $C = 1$, the first line will contain a natural number representing the answer to task $1$.  
If $C = 2$, the first line will contain a natural number representing the answer to task $2$.  
If $C = 3$, $Q$ lines, one line for each pair ($A, B$) among the $Q$. The line corresponding to each pair ($A, B$) will contain a natural number representing the number of potatoes produced by the plants located in the square zones between columns $A$ and $B$, including these values, representing the answer to task $3$.

# Constraints and clarifications

* $2 \leq N \leq 500\ 000\ 000$;
* $3 \leq M \leq 1\ 000\ 000\ 000$;
* $N \leq M$;
* $Q \leq 100\ 000$;
* $1 \leq A \leq B \leq M$;
* $20$ points are awarded for task $1$, and $40$ points are awarded for each of tasks $2$ and $3$.
* The Fibonacci sequence is defined as follows: $f(1) = 1$, $f(2) = 1$ and $f(n) = f(n-1) + f(n-2)$ for $n \geq 3$ (where $n$ is a non-zero natural number).
* A square area of the field consists of $K \times K$ adjacent square zones arranged $K$ per row and $K$ per column, for any $1 \leq K \leq min(N, M)$;

# Example 1

`cartofi.in`
```
1
3 6
```

`cartofi.out`
```
1
```

## Explanation

Task $1$ is solved. $N = 3$, $M = 6$. The first $N \times M = 18$ terms of the Fibonacci sequence are: $1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584$. Thus, the potato numbers produced by each plant in the field are those in Figure $1$. There is one plant in the field that did not produce any potatoes (the one in row $3$, column $3$).

# Example 2

`cartofi.in`
```
2
3 6
```

`cartofi.out`
```
42
```

## Explanation

Task $2$ is solved. $N = 3$, $M = 6$. The potato numbers produced by each plant in the field are those in the table in Figure $1$. The plants in the yellow square area in the table in Figure $2$ have produced the largest number of potatoes.

# Example 3

`cartofi.in`
```
3
5 6
3
1 2
4 6
2 3
```

`cartofi.out`
```
48
64
43
```

## Explanation

Task $3$ is solved. $N = 5$, $M = 6$, $Q = 3$. The table in Figure $3$ contains the potato numbers produced by each plant in the field as shown in Figure $3$. The sum of the elements between columns ($1, 2$), including $1$ and $2$, is $48$. The sum of the elements between columns ($4, 6$), including $4$ and $6$, is $64$. The sum of the elements between columns ($2, 3$), including $2$ and $3$, is $43$.