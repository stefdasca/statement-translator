
We consider a matrix with an infinite number of rows and columns indexed starting from `0`. On the first row, the matrix contains the sequence of natural numbers `(0, 1, 2, 3…)`.

On each row starting from the second row, at position `j`, the matrix contains the XOR sum of elements located on the previous row from position `0` to position `j`.

# Task
You are required to answer `q` questions of the form: “For given `i` and `j`, determine the number located at row `i` column `j` of the matrix.� To generate these `q` questions, the following values will be known: $i_1, j_1, a, b, m$. 
$i_1, j_1$ represents the values for the first question. The following questions $i_k, j_k$ will be generated one from another using the following rule: 
$i_k=(a \cdot i_{k-1} + b) \mod m$
$j_k=(a \cdot j_{k-1} + b) \mod m$

# Input data
The input file `xor.in` contains on the first line the natural numbers $q, i_1, j_1, a, b, m$ separated by a space.

# Output data
The output file `xor.out` will contain `q` lines. Each line `k` will print the element located at row $i_k$ column $j_k$ of the matrix.

# Constraints and clarifications
* For `10%` of the tests, `1 \leq q \leq 100, 1 \leq m \leq 100`
* For another `10%` of the tests, `1 \leq q \leq 100000, 1 \leq m \leq 1000`
* For another `30%` of the tests, `1 \leq q \leq 50, 1 \leq m \leq 30000`
* For another `50%` of the tests, `1 \leq q \leq 100000`, $1 \leq m \leq 10^8$
* $0 \leq i_1, j_1 < m$
* `1 \leq a, b \leq 9`

# Example

`xor.in`
```
4 2 3 1 1 5
```

`xor.out`
```
2
7
0
1
```

Explanation
---

We have `q=4` questions.
For $i_1=2, j_1=3, a=1, b=1, m=5$ the questions obtained are: `(2, 3), (3, 4), (4, 0), (0, 1)`

The matrix is:
0 **1** 2 3 4 5 6 …
0 1 3 0 4 1 7 …
0 1 2 **2** 6 7 0 …
0 1 3 1 **7** 0 0 …
**0** 1 2 3 4 4 4 …
…

It can be observed that at the positions corresponding to the questions we have the values `2, 7, 0` and `1`
