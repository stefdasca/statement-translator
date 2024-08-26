# Rombulum

Given a matrix with $N$ rows and $N$ columns of integers, all initially set to $0$. A series of $Q$ updates defined by $x, y, lat, val$ are applied to this matrix with the meaning: The elements that lie inside the rhombus with the corners $(x - lat, y), (x, y + lat), (x + lat, y), (x, y - lat)$ are modified by adding the value $val$. For example, starting from an initial $7 \times 7$ matrix with all elements $0$, through an update $(4, 5, 2, 1)$ we get the matrix:
```
|1234567 
-+-------
1|0000000
2|0000100
3|0001110
4|0011111
5|0001110
6|0000100
7|0000000
```
To solve the problem, you need to determine the two largest values in the matrix after the updates, as well as the number of occurrences of these two values.

## Input data

The input file `rombulum.in` contains the number of tests $T$ on the first line. Each test is described on the first line with two numbers $N$ and $Q$, the number of rows and columns of the matrix and the number of updates. Each of the following $Q$ lines contains $4$ numbers $x \ y \ lat \ val$ which describe the update.

## Output data

The output file `rombulum.out` must contain for each test $4$ numbers $v1 \ f1 \ v2 \ f2$ with the meaning:
- $v1$ = the maximum value in the matrix
- $f1$ = the number of occurrences of $v1$
- $v2$ = the second highest value (there will be at least two distinct values)
- $f2$ = the number of occurrences of $v2$

## Constraints and clarifications

$T \leq 16$

$1 \leq N \leq 250$

$1 \leq Q \leq 50000$

$0 \leq val \leq 1000$ for any update

Any update contains all elements inside the matrix: $x - lat, x + lat, y - lat, y + lat$ will belong to the interval $[1, N]$.

## Example

`rombulum.in`
```
2
8 2
4 4 3 2
6 6 2 3
10 7
8 2 1 616
2 6 1 796
...
```

`rombulum.out`
```
5 4 2 2
1673 1 1418 2
```

## Explanation

For the first test, the generated matrix is as follows:
```
|12345678 
-+--------
1|00020000
2|00222000
3|02222200
4|22222520
5|02225530
6|00255333
7|00023330
8|00000300
```
The largest value is $5$ with $5$ occurrences, and the second largest value is $3$ with $8$ occurrences.