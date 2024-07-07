
Mihai created a square matrix $A$ of size $N$ with values in the set ${0,1}$. He prefers those matrices that have all identical elements and thus calculated for matrix $A$ the number $K$ of submatrices that have all identical elements. Now, Mihai wants to transform matrix $A$ into a matrix with all identical elements. For this, he selected a non-zero natural number $D$, and defines the ZET operation which consists of selecting a square submatrix of size $D$ from the previous matrix and swapping all the elements $0$ to $1$ and vice versa. He wants to apply the ZET operation initially to matrix $A$, then repeat the operation on the resulting matrix from the previous step, a minimum number of times, denoted $R$, until the resulting matrix has all identical elements, or if it is not possible, $R$ will have the value $-1$.

# Task

Mihai asks you to calculate the values $K$ and $R$. To specify the type of task, Mihai uses a code $T$ which if it has the value $1$, then it requests the calculation of the value $K$, and if $T$ has the value $2$, then it requests the calculation of the value $R$.

# Input data

The first line of the file `identice.in` contains the natural numbers $T, N$ and $D$, with the above meanings, separated by a space. The next $N$ lines contain $N$ values of $0$ and $1$, the elements of the rows of matrix $A$, without spaces between them.

# Output data

The first line of the file `identice.out` contains a natural number, namely the value $K$ for $T = 1$ or the value $R$ for $T = 2$.

# Constraints and clarifications

* $ 1 < D < N \leq 1 \ 000;$
* For calculating the value $K$, submatrices can be square or rectangular, with different sizes (including $1$), with identical elements$;$
* $40\%$ of the total points are awarded for correctly determining $K$ and $60\%$ for correctly determining $R$.

# Example 1

`identice.in`
```
1 4 2
0011
0011
1100
1100
```

`identice.out`
```
36
```

## Explanation

$T = 1$, so $K = 36$ is calculated. There are $18$ submatrices with all elements $0$ and $18$ with all elements $1$.

# Example 2

`identice.in`
```
2 4 2
0011
0011
1100
1100
```

`identice.out`
```
2
```

## Explanation

$T = 2$, so $R = 2$ is calculated because $2$ applications of the ZET operation are required.
