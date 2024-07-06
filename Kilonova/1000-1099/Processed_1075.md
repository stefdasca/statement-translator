A Latin square of order $N$ is a matrix with $N$ rows and $N$ columns that contains $N$ distinct symbols, such that every row and every column contains all $N$ symbols. The term Latin square originates from the works of mathematician Leonhard Euler, who used Latin alphabet letters as symbols.

Consider a Latin square of order $N$ that contains natural numbers from $1$ to $N$. It can in itself contain Latin subarrays. An $L$-order subarray ($1 < L < N$) is formed from elements located at the intersection of $L$ consecutive rows and $L$ consecutive columns in the given square. The $L$-order subarray is considered a Latin subarray if it contains only the natural numbers from $1$ to $L$, such that each row and each column in the subarray contains all $L$ numbers.

# Task

Given a Latin square, determine all Latin subarrays contained within it.

# Input data

The input file `latin.in` contains on the first line the natural number $N$. The next $N$ lines contain $N$ distinct natural numbers ranging from $1$ to $N$, separated by spaces, representing the elements of a Latin square of order $N$.

# Output data

The output file `latin.out` will contain on the first line a natural number $Nr$, representing the number of Latin subarrays contained in the given Latin square. On the following $Nr$ lines, the determined Latin subarrays will be described, one subarray per line. A line describing a subarray will contain $3$ natural numbers separated by spaces: $ls\\ cs\\ o$, where $ls$ and $cs$ represent the row and column of the upper-left corner of the subarray, and $o$ represents its order. The subarrays will be written in increasing order of the row of the upper-left corner; if there are multiple subarrays with the upper-left corner on the same row, they will be displayed in ascending order of their order.

# Constraints and clarifications

* $2 \\leq N \\leq 500$
* Rows and columns are numbered from $1$ to $N$.

# Example 1

`latin.in`
```
3
2 3 1
1 2 3
3 1 2
```

`latin.out`
```
0
```

# Example 2

`latin.in`
```
8
5 6 7 8 1 2 3 4
6 7 8 5 2 1 4 3
7 8 5 6 3 4 2 1
8 5 6 7 4 3 1 2
1 4 2 3 5 6 7 8
2 1 3 4 6 7 8 5
3 2 4 1 7 8 5 6
4 3 1 2 8 5 6 7
```

`latin.out`
```
4
1 5 2
1 5 4
3 7 2
5 1 4
```
