
Let $M$ be a two-dimensional array (matrix) of size $N$ by $N$, with elements from the set $\{0, 1\}$. The rows and columns of this array are numbered from $1$ to $N$. A path of length $K$ in this array is a sequence of pairs $(x_i, y_i)$, for $i$ from $1$ to $K$, with the following properties:

* $x_i$ and $y_i$ are natural numbers in the interval $[1, N]$, for $i$ from $1$ to $K$;
* $(|x_i - x_{i+1}|=1$ and $y_i = y_{i+1})$ **or** $(|y_i - y_{i+1}|= 1$ and $x_i = x_{i+1})$, for $i$ from $1$ to $K-1$.

In other words, a path is a sequence of positions in the array such that two consecutive positions are adjacent either top-bottom or left-right. We call **value of a path** the sequence of values $M[x_i][y_i]$, for $i$ from $1$ to $K$.

By **anagram** of a sequence of values, we understand any rearrangement of its elements. For example, if the initial sequence contains the elements $(1, 0, 0, 1)$, then the sequences $(1, 0, 0, 1)$, $(1, 0, 1, 0)$, $(1, 1, 0, 0)$, $(0, 1, 1, 0)$ are anagrams of it.

# Task

Given the dimension $N$ of the array, the elements of the array $M$, and a sequence $S$ composed of $K$ elements from the set $\{0, 1\}$, determine a path in the array $M$ having as value an **anagram** of $S$, if this path exists.

# Input data

The input data is read from the file `siruri.in`, which has the following structure:

* The first line contains two natural numbers $N$ and $K$, separated by a single space, representing the dimension of the array and the length of the sequence $S$, respectively;
* Each of the next $N$ lines contains $N$ values from the set $\{0, 1\}$, separated by a single space, representing the values of the array $M$;
* On line $N+2$ contains $K$ numbers from the set $\{0, 1\}$, separated by a single space, representing the values of the sequence $S$.

# Output data

The output data will be written to the file `siruri.out`, as follows:

* If there is no path that satisfies the task, then the value $-1$ will be written;
* If such a path exists, then $K$ pairs of values $x_i \\ y_i$, from the set $\{1,2, \dots, N\}$, separated by a single space, will be written on separate lines, representing the determined path.

# Constraints and clarifications

* $1 \leq N \leq 100$
* $1 \leq K \leq 100\ 000$
* The elements of the array $M$ and of the sequence $S$ are elements from the set $\{0, 1\}$
* For tests worth $20$ points, the sequence $S$ is found on a row or column of the matrix, as given in the input file or in reverse order;
* The solution is not unique, any solution is acceptable.

# Example 1

`siruri.in`
```
3 10
0 0 0
0 1 1
1 0 1
1 1 1 0 1 1 1 0 1 1
```

`siruri.out`
```
2 2
2 3
2 2
2 1
2 2
2 3
2 2
2 3
3 3
3 2
```

## Explanation

The value obtained for the path in the output file is $(1, 1, 1, 0, 1, 1, 1, 1, 1, 0)$ and represents an anagram of the given sequence.

# Example 2

`siruri.in`
```
4 3
1 0 0 0
0 0 1 0
1 0 0 0
1 0 0 0
1 1 0
```

`siruri.out`
```
4 1
3 1
2 1
```

## Explanation

The sequence $S$ is found on column $1$ of the matrix.

# Example 3

`siruri.in`
```
2 4
0 0
0 0
1 0 1 0
```

`siruri.out`
```
-1
```

## Explanation

In the array, there is no value $1$, so it is not possible to obtain a path whose value contains $1$.
