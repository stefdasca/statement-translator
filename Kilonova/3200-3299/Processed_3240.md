
# Task

Tudor and Luca are two young programmers. They have just completed an advanced algorithm course in C and are trying to solve problems as efficiently as possible. One of the problems they are contemplating is the following:

- there is a matrix $N \times N$ with values between $0$ and $1$;
- a snowflake formation is defined as a group of bits that are $1$ and start from a cell in all directions (`N`, `N-E`, `E`, `S-E`, `S`, `S-W`, `W`, `N-W`);
- a perfect snowflake formation is a shape that meets the snowflake condition and also has "arms" of the same length;
- find the longest snowflake.

`Perfect snowflake of length 3`
```
1 0 1 0 1
0 1 1 1 0
1 1 1 1 1
0 1 1 1 0
1 0 1 0 1
```

`Perfect snowflake of length 2`
```
0 0 0 0 0
0 1 1 1 0
0 1 1 1 0
0 1 1 1 0
0 0 0 0 0
```

`Perfect snowflake of length 1`
```
1 0 1 0 1
0 1 1 0 0
1 1 1 1 1
0 1 1 1 0
1 0 1 0 1
```

Since Tudor has found the optimal solution again, Luca pays you to solve the problem for him to avoid falling behind his friend. He asks you to be very careful due to tight limits, the less efficient, the less money!!!

# Input data

The first line of the input file `algoritmul.in` contains a number $N$ followed by a matrix of $N \times N$: $a_{11}$, $a_{12}$, $\\dots$, $a_{nn}$ representing the value at positions $a_{ij}$ in the matrix.

# Output data

On line $i$ of the output file `algoritmul.out`, there will be $3$ values, the size of the largest perfect snowflake, and on the next line the coordinates $(x, y)$ of its center.

# Constraints and clarifications
* $1 \leq N \leq 1 \ 000$;
* 30 points are awarded for $1 \leq N \leq 300$;
* 50 points are awarded for $1 \leq N \leq 500$;
* 80 points are awarded for $1 \leq N \leq 800$;
* If there are multiple largest snowflakes, display the one with the smallest $x$ coordinate. If there are several that also meet this condition, display the one with the smallest $y$ coordinate.

# Example

`lumtirogla.in`
```
7
0 1 1 1 0 0 0
0 1 1 1 0 0 0
0 1 1 1 0 1 0
0 0 1 1 1 0 0
0 1 1 1 1 1 0
0 0 1 1 1 0 0
0 1 0 1 0 1 0
```

`lumtirogla.out`
```
3
5 4
```

## Explanation

As can be seen, there are only $2$ snowflakes that have a length greater than $2$. The first has its center at $(2, 3)$ and has a size of $2$. The second has its center at $(5, 4)$ and has a size of $3$, so it is the one we need.
