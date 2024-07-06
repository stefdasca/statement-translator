~[fibosnek.png|align=right|width=25%]

It is considered a matrix with $n$ rows and $m$ columns that contains non-zero natural numbers.

A ***snek*** traversal of the matrix is defined as a sequence of values obtained as follows: traverse the matrix elements column by column, from the first to the last column, and within each column, from top to bottom, from the element on the first row to the element on the last row, as in the example.

The Fibonacci sequence is defined below where $\\text{fib}[k]$ represents the $k$-th Fibonacci number:
* $fib[1] = 1, fib[2] = 1$;
* $fib[k] = fib[k - 1] + fib[k - 2]$, for any $k \\gt 2$;

A sequence is called ***fibosnek*** if it consists of one or more consecutive terms in the *snek* traversal, where each of them is a Fibonacci number. Similarly, a sequence is called ***non-fibosnek*** if it consists of one or more consecutive terms in the *snek* traversal, where none of them is a Fibonacci number. The length of the sequence is equal to the number of its terms. The sum of the sequence is equal to the sum of its terms.

A *non-fibosnek* sequence can be transformed into a *fibosnek* sequence by replacing each number in the sequence with the closest Fibonacci number. If there are two Fibonacci numbers equally close to the given number, the smallest one will always be chosen. For example, the sequence ($4$) transforms into the sequence ($3$), and the sequence ($9, 11$) transforms into the sequence ($8, 13$).

# Task

Given the elements of an $n$-row and $m$-column matrix, determine:
1. The number of Fibonacci numbers in the given initial matrix;
2. The sum of the longest *fibosnek* sequence that can be obtained, knowing that **at most one non-fibosnek sequence** can be transformed into a *fibosnek* sequence using the method explained above. If several such sequences of maximum length can be obtained, the first encountered one in the *snek* traversal of the matrix will be chosen.

# Input data
The input file `fibosnek.in` contains:
- On the first line, the natural numbers $c$, $n$, and $m$, where $c$ represents the task that needs to be solved ($1$ or $2$), and $n$ and $m$ have the significance given in the statement.
- On the next $n$ lines, it contains the matrix elements, traversed in order, line by line, and within each line, from left to right. The values on the same line of the file are separated by a space.

# Output data
The output file `fibosnek.out` contains either:
- Only the number determined for task $1$ (if $c = 1$),
- Or only the sum determined for task $2$ (if $c = 2$).

# Constraints and clarifications
* $c \\in \\{1, 2\\}$;
* $1 \\leq n, m \\leq 1 \ 500$;
* The elements of the matrix have values in the range $[1, 2^{31}-1]$;
* For $21$ points, $c = 1$ and $n, m \\leq 1 \ 000$;
* For $20$ points, $c = 2$ and $n, m \\leq 100$;
* For $44$ points, $c = 2$ and $n, m \\leq 1 \ 000$;
* For $15$ points, $c = 2$ with no further restrictions.

# Example 1

`fibosnek.in`
```
1 3 4
1 5 3 11
2 8 1 13
4 2 9 8
```

`fibosnek.out`
```
9
```

## Explanation

$c = 1, n = 3, m = 4$, and the matrix corresponds to the one in Fig. 1. There are $9$ Fibonacci numbers in the matrix: $1, 5, 3, 2, 8, 1, 13, 2, 8$.

# Example 2

`fibosnek.in`
```
2 3 4
1 5 3 11
2 8 1 13
4 2 9 8
```

`fibosnek.out`
```
61
```

## Explanation

$c = 2, n = 3, m = 4$, and the matrix corresponds to the one in Fig. 1. If the *non-fibosnek* sequence ($9, 11$) is transformed into the *fibosnek* sequence ($8, 13$), then the longest *fibosnek* sequence is ($5, 8, 2, 3, 1, 8, 13, 13, 8$), of length $9$ and sum $61$.

# Example 3

`fibosnek.in`
```
2 4 4
2 4 7 1
3 3 6 7
5 5 8 4
11 8 13 6
```

`fibosnek.out`
```
42
```

## Explanation

The *non-fibosnek* sequence ($11, 4$) is transformed into the *fibosnek* sequence ($13, 3$) and the *fibosnek* sequence ($2, 3, 5, 13, 3, 3, 5, 8$) is obtained with length $8$ and sum $42$. Although there is another *fibosnek* sequence of length $8$ that can be obtained by transforming the *non-fibosnek* sequence ($7, 6$), it was not chosen because it is not the first sequence that can be obtained.