# Task <br>

According to some ancient texts (from November 2022), the points $A$, $B$ and $C$ are called *almost collinear* if $d(A,B)+d(B,C)=d(A,C)$, where $d(M,N)=|X_M-X_N|+|Y_M-Y_N|$ represents the Manhattan distance between points $M$ and $N$. <br>

The coordinates of $n$ points in the plane $P_1,P_2,\ldots,P_n$ are given. Find the number of triplets $(i,j,k)$ ($1 \le i,j,k \le n$, $i \neq j \neq k \neq i$) such that the points $P_i$, $P_j$ and $P_k$ are *almost collinear*. <br>

# Input data <br>

The first line of the input file **aproapecoliniare.in** will contain the number of points $n$ ($3 \le n \le 3 \cdot 10^5$). <br>

Each of the following $n$ lines will contain two numbers $x_i$ and $y_i$ ($1 \le x_i,y_i \le 10^9$) &mdash; the coordinates of the point $P_i$. <br>

It is guaranteed that all points in the input file are distinct. <br>

# Output data <br>

The output file **aproapecoliniare.out** will contain the number of triplets $(i,j,k)$ ($1 \le i,j,k \le n$, $i \neq j \neq k \neq i$) such that the points $P_i$, $P_j$ and $P_k$ are *almost collinear*. <br>

# Constraints and clarifications <br>

- For $8$ points, $n \le 300$
- For $12$ points, $n,x_i,y_i \le 800$
- For $10$ points, $n,x_i,y_i \le 3000$
- For $5$ points, $n \le 3000$
- For $20$ points, $n,x_i,y_i \le 50000$
- For $10$ points, $n \le 50000$
- For $20$ points, all $x$ coordinates and all $y$ coordinates are distinct.
- For $15$ points, no additional constraints.

# Examples <br>

## Example 1:

**aproapecoliniare.in**
```
5
1 1
2 2
3 1
3 2
3 3
```
**aproapecoliniare.out**
```
16
```

# Explanations

The $16$ triplets in the example are:

- $(1,2,4)$ and $(4,2,1)$
- $(1,2,5)$ and $(5,2,1)$
- $(3,4,5)$ and $(5,4,3)$
- $(2,4,3)$ and $(3,4,2)$
- $(2,4,5)$ and $(5,4,2)$
- $(1,3,4)$ and $(4,3,1)$
- $(1,3,5)$ and $(5,3,1)$
- $(1,4,5)$ and $(5,4,1)$
