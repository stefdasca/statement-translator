## Task

Some researchers have invented a way to encode a bitmap of dimensions $M \times N$ as a string of characters. The string is actually a representation of operations performed on the bitmap. The encoding algorithm is described below:

- If all the cells of the bitmap have the color $1$, then the encoding is "1"
- If all the cells of the bitmap have the color $0$, then the encoding is "0" 
- Otherwise, you need to choose one of the following ways to encode the bitmap: 
  - Encode($B$) = "A" + Encode($B_1$) + Encode($B_2$), where "+" represents the concatenation operation, $B_1$ is the bitmap obtained by keeping the first $M/2$ rows of the bitmap $B$ and all the columns, and $B_2$ is the bitmap obtained by keeping the last $M-M/2$ rows of the bitmap $B$ and all the columns (thus, $B_1$ will have $M/2$ rows and $N$ columns, and $B_2$ will have $M-M/2$ rows and $N$ columns). 
  - Encode($B$) = "B" + Encode($B_1$) + Encode($B_2$), where "+" represents the concatenation operation, $B_1$ is the bitmap obtained by keeping the first $N/2$ columns of the bitmap $B$ and all the rows, and $B_2$ is the bitmap obtained by keeping the last $N-N/2$ columns of the bitmap $B$ and all the rows (thus, $B_1$ will have $M$ rows and $N/2$ columns, and $B_2$ will have $M$ rows and $N-N/2$ columns). 
  - Encode($B$) = "C" + Encode($B_1$) + Encode($B_2$), where "+" represents the concatenation operation, $B_1$ is the bitmap obtained by keeping all the odd-numbered rows of the bitmap $B$ (rows are numbered starting from $1$) and all the columns, and $B_2$ is the bitmap obtained by keeping all the even-numbered rows of the bitmap $B$ and all the columns (thus, $B_1$ will have $M-M/2$ rows and $N$ columns, and $B_2$ will have $M/2$ rows and $N$ columns). 
  - Encode($B$) = "D" + Encode($B_1$) + Encode($B_2$), where "+" represents the concatenation operation, $B_1$ is the bitmap obtained by keeping all the odd-numbered columns of the bitmap $B$ (columns are numbered starting from $1$) and all the rows, and $B_2$ is the bitmap obtained by keeping all the even-numbered columns of the bitmap $B$ and all the rows (thus, $B_1$ will have $M$ rows and $N-N/2$ columns, and $B_2$ will have $M$ rows and $N/2$ columns). 

Given a bitmap, find the length of its shortest encoding.

## Input data

The first line of the input file `bitmap.in` contains the number of tests $T$. The following lines describe the $T$ tests. The first line of each test contains $2$ integers $M$ and $N$, representing the number of rows and columns of the bitmap. Each of the next $M$ lines contains a string of $N$ characters from the set $\{'0','1'\}$, representing a row of the bitmap.

## Output data

For each test, print to the output file `bitmap.out` a single line containing the minimum length of an encoding of the bitmap for that respective test.

## Constraints

$1 \leq T \leq 1105$

$1 \leq M, N \leq 11$

## Example

bitmap.in 
```
2
4 6
000000
111111
000000
111111
5 8
01011111
01011111
01011010
01011010
01011010
```

bitmap.out
```
3
9
```

## Explanation

A minimum length encoding for the first test is: $C01$

A minimum length encoding for the second test is: $BD01A1D10$