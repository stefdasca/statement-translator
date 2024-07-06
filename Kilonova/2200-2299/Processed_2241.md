Teo is an accountant at UNSTPB, but today he had a rough day. While entering data into his program, he mixed up the rows with the columns.

# Task

To rearrange the data correctly, Teo considered it faster to create a program that transposes the matrix he entered. However, he encountered a problem during execution. Help Teo identify the error so that he can complete the faculty expense table on time. You can find his program [here](wrongdata.cpp) or in the "Attachments" section on the side.

# Input data

The input consists of two natural numbers $n$ and $m$, followed by $n \times m$ numbers, representing the elements of the matrix.

# Output data

The output will contain the resulting matrix: $n$ elements separated by spaces, on $m$ lines.

# Constraints and clarifications

- $1 \le n, m \le 100$
- The elements of the matrix are integers between $0$ and $100$.

# Example 1

`stdin`
```
3 3
1 2 3
4 5 6
7 8 9
```

`stdout`
```
1 4 7
2 5 8
3 6 9
```

## Explanation

After reading the input data, the matrix is transposed and printed on the screen.

# Example 2

`stdin`
```
4 3
8 5 0
7 2 1
5 8 3
4 2 2
```

`stdout`
```
8 7 5 4
5 2 8 2
0 1 3 2
```
