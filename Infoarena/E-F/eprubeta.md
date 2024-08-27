## Task

Bubu is in chemistry class and has in front of him a square support for $N$x$N$ test tubes. The test tube located at column $x$ and row $y$ contains a fixed volume of liquid $a_{x,y}$. Being a nerd, Bubu invents a single-player game. First, he fixes two numbers $i \leq j$, and on the square with the top-left corner $(i, i)$ and bottom-right corner $(j, j)$ he performs operations that can be of the following two types:
1. rotate the square $180$ degrees
2. calculate how much liquid is in the test tubes within the delimited square

You are asked to write a program which, given the size of the support and the initial amount of liquid in each test tube, simulates $M$ given operations. In the end, it will determine how much liquid is in each test tube.

## Input data

The input file `eprubeta.in` has the following format:
The first line will contain five numbers $N$, $M$, $Z$, $A$, and $B$. $N$ is described in the statement, and $M$ is the number of operations. To prevent having an excessively large input file, the volumes of liquid in each test tube will be generated using the formula: $a_{x, y} = \left(\frac{(y + A) * (x + B)}{4}\right) \% Z$ .

The next $M$ lines will contain three numbers describing the operation code ( $1$ or $2$, as above), $i$, and $j$, where $i$ and $j$ have the meanings described in the task.

## Output data

The output file `eprubeta.out` will have the following format:
For each operation of type $2$, it will print a number representing the total volume of liquid found in the square described in the operation.

To avoid a large output file, the last line will contain a number $T$. $T$ will be equal to the sum over line $u$ $(0 \leq u < N)$ of $(sum of elements in line u) 2 * (u + 1)$. $T$ will be written modulo $2^{32}$.

## Constraints

$0 < N \leq 2000$

$0 < M \leq 2000$

$0 \leq x, y < N$

$0 < A, B \leq 30000$

$0 < Z \leq 100000$

$0 \leq a_{x, y} < Z$

It is guaranteed that the sum of the volumes of liquid in all test tubes is strictly less than $2^{31}$

To prevent any explosion, the content of the test tubes will not be altered.

Rows and columns are indexed from 0.

If the result of each type 2 operation is correct, $60\%$ of the test score will be awarded.

If you choose not to calculate the intermediate sums, then for each type 2 operation you should print $0$.

If the number $T$ is correct, $40\%$ of the test score will be awarded.

For $20\%$ of the tests, $N \leq 400$.

To avoid exceeding the memory limit, avoid dynamically allocating many objects of the same kind by using a statically allocated array.

## Example

`eprubeta.in`
```
5 4 11 5 7
1 0 0
2 1 3
2 1 1
1 1 2
```

`eprubeta.out`
```
41
1
7489
```

## Explanation

The resulting square is

```
8 10 0 1 2
10 1 2 4 5
1 3 4 6 8
3 5 7 9 0
4 7 9 0 2
```

For the first operation, $(1\ 0\ 0)$, you need to rotate the top-left corner. It doesn't affect the square.

For the second operation, $(2\ 1\ 3)$, the correct value is: $1 + 2 + 4 + 3 + 4 + 6 + 5 + 7 + 9 = 41$

For the third operation, $(2\ 1\ 1)$, the correct value is $1$

The last operation, $(1\ 1\ 2)$, transforms the initial square into:

```
8 10 0 1 2
10 4 3 4 5
1 2 1 6 8
3 5 7 9 0
4 7 9 0 2
```

The value of $T$ is $21\ * 1 + 26\ * 2 + 18\ * 3 + 24\ * 4 + 22\ * 5 = (41, 52, 54, 96, 110) = 7489$