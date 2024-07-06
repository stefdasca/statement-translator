Traversing the elements of a square matrix of size $n$ in a spiral manner, starting from the top-left corner, clockwise, from the edges towards the center, a strictly increasing sequence consisting of all values from $1$ to $n^2$ is obtained, as in the figure below. From the given sequence, two disjoint subsequences of equal length with the maximum number of terms are obtained. The first subsequence is formed from consecutive numbers in the first half of the sequence and must mandatorily contain the value $1$, while the second is formed from consecutive numbers in the second half of the sequence and must mandatorily contain the value $n^2$.
| 1| 2| 3| 4| 5|
|-|-|-|-|-|
|**16**|**17**|**18**|**19**|**6**|
|**15**|**24**|**25**|**20**|**7**|
|**14**|**23**|**22**|**21**|**8**|
|**13**|**12**|**11**|**10**|**9**|

# Task
Determine the position in the matrix of the largest term in the first subsequence and the smallest term in the second subsequence.

# Input data
The input file `spiralmatrix.in` contains the natural number $n$.

# Output data
In the output file `spiralmatrix.out` you will write:
- the first line contains two numbers, separated by a space, representing first the row and then the column where the largest term of the first subsequence is located in the matrix;
- the second line contains two other numbers, separated by a space, representing first the row and then the column where the smallest term of the second subsequence is located in the matrix.

# Constraints and clarifications
- $1 < n < 1\ 000\ 000\ 000$
- For tests worth 45 points, $n$ is odd.
- For tests worth 45 points, $n < 1\ 000$.
- For tests worth 75 points, $n < 1\ 000\ 000$.
- Rows are numbered from top to bottom starting with $1$, and columns are numbered from left to right starting with $1$.
- A score on a test is obtained only if all 4 values are correct.

# Example 1
`spiralmatrix.in`
```
5
```
`spiralmatrix.out`
```
5 2
4 1
```

## Explanation
The first subsequence is formed from values $1$ to $12$. The value $12$ is located on row $5$ and column $2$.
The second subsequence is formed from values $14$ to $25$. The value $14$ is located on row $4$ and column $1$.

# Example 2

`spiralmatrix.in`
```
4
```
`spiralmatrix.out`
```
4 3
4 2
```

## Explanation
The first subsequence is formed from values $1$ to $8$. The value $8$ is located on row $4$ and column $3$.
The second subsequence is formed from values $9$ to $16$. The value $9$ is located on row $4$ and column $2$.