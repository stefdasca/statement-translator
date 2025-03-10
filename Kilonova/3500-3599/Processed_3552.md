
# Task

You are given an array of natural numbers. We have several operations of two types:
* Update: The element at a certain position $p$ receives a given value $x$.
* Query: Given two indices $st$ and $dr$, determine the length of the longest increasing subsequence for the subarray that starts at position $st$ and ends at position $dr$.

# Input data

The first line of the file `qscmax.in` contains the number of elements in the given array, denoted by $n$. The second line contains $n$ numbers, separated by space, representing the elements of the given array, in order of positions, numbered from $1$ to $n$. The third line contains the number of operations, denoted by $m$. Each of the next $m$ lines contains the description of one operation. If we have an update, the line will contain the values $1$, $p$, $x$. If we have a query, the line will contain the values $2$, $st$, $dr$.

# Output data

The output file `qscmax.out` will contain the result for each query, in the order they appear in the input file. The values are printed on one line, separated by space.

# Constraints and clarifications

* $1 \leq n \leq 100 \ 000$;
* At any moment, the values in the array are $0$, $1$, $2$, or $3$;
* $1 \leq m \leq 100 \ 000$;
* There is at least one â€œqueryâ€ operation;
* $1 \leq p \leq n$;
* $1 \leq st \leq dr \leq n$.

# Example

`qscmax.in`
```
9
0 1 3 0 1 2 1 2 0
3
2 1 9
1 3 0
2 1 3
```

`qscmax.out`
```
5 2
```

## Explanation

For the first query, the length of the longest increasing subsequence in the entire given array is requested. This is $5$. For the second query, the length of the longest increasing subsequence for the elements at positions from $1$ to $3$ is requested. This is $2$ (the element at position $3$ has meanwhile become $0$).
