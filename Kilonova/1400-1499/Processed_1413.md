Bia and Ștefan are playing a new game. Bia asked Ștefan to think of a positive integer strictly smaller than $VMAX=2^n$. Then, she took a pen and paper and drew $n$ square matrices (briefly called squares), which she numbered from $1$ to $n$. She then filled the squares as follows: in the square numbered $i$ were written in ascending order all natural non-zero numbers less than $VMAX$ that, written in base $2$, have the digit corresponding to $2^{i-1}$ equal to $1$; the numbers were placed by traversing the columns from left to right and filling each column from top to bottom. Each square has the minimum side length necessary to contain all the numbers that need to be included. It is possible that the squares are not completely filled (in this case, the square will be completed with the value $0$).

After drawing the squares, Bia asked Ștefan in which of the squares the number he thought of is located. Then she performed a magic trick and guessed the number Ștefan was thinking of. Additionally, to impress Ștefan even more, Bia told him the row and column where this number is located in the first square mentioned by Ștefan.

# Task

Since you do not believe in magic, write a program that determines the number Ștefan thought of, as well as the position of this number in the first square mentioned by Ștefan.

# Input data

The input file `patrate.in` contains on the first line the natural numbers $n$ and $m$, separated by a space, representing the number of squares Bia will draw, respectively, in how many of the drawn squares the number Ștefan thought of is located. The second line contains, separated by spaces, $m$ natural numbers between $1$ and $n$, representing the $m$ squares in which the number Ștefan thought of is located.

# Output data

The output file `patrate.out` will contain:
- On the first line, the number Ștefan thought of
- On the second line, two natural numbers separated by a space $L$ and $C$, representing the row and column where this number is located in the first square mentioned by Ștefan.

# Constraints and clarifications

* $1 < m \leq n \leq 28$
* In each square matrix, the rows are numbered from top to bottom starting with $1$, and the columns from left to right starting with $1$.
* For tests worth $50\%$ of the total points, $n$ is $ \leq 14$.
* For correctly determining the number Ștefan thought of, $40\%$ of the test points are awarded. Full points are obtained for solving both tasks.

# Example

`patrate.in`
```
4 3
1 4 3
```

`patrate.out`
```
13
1 3
```

## Explanation

The number $13$ is the one Ștefan thought of because, written in base $2$, it is $1101$. The number $13$ is the only one that is found only in the squares indicated by Ștefan ($1, 4$, and $3$), because it has the digits corresponding to $2^0, 2^3, 2^2$ equal to $1$. The first square mentioned by Ștefan is $1$. The number $13$ is located in this square in row $1$ and column $3$.
Square $1$ is shown below:
$$ \begin{pmatrix} 1 & 7 & 13 \\ 3 & 9 & 15 \\ 5 & 11 & 0 \end{pmatrix}  $$