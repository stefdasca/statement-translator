
# Task

Given an array with $n$ natural numbers that are less than or equal to $10^9$, and $q$ queries of the following types:

* $1 \ x \ k$: The largest $x$ values in the array will become equal to their value modulo $k$. If we have multiple values equal to the $x$-th value, we will apply the operations from left to right. If a value was $15$ and we apply the operation with $k = 9$, that value will become $6$.
* $2 \ p \ x$: The value at position $p$ becomes $x$.
* $3$: Display the maximum value in the array.

Since the committee does not want to spend time chatting with you, you must solve the problem as fast as possible, or else they'll get upset with you.

# Input data

The first line of the input file `mod.in` contains two integers, $n$ and $q$.

The next line contains the initial array $v$, which has $n$ natural elements.

The next $q$ lines contain the queries, according to the description in the statement, being of type $1$, $2$, or $3$.

# Output data

The output file `mod.out` will contain as many numbers as there are type $3$ queries, printing the maximum value at that moment.

# Constraints and clarifications

* $1 \leq N, Q \leq 200 \ 000$;
* $1 \leq MAXVAL \leq 10^9$;

We will denote the maximum value in the array or from one of the updates with $MAXVAL$. Then we have the following subtasks:

| # | Points | Constraints | 
| - | ------- | ---------- |
| 1 | 16 | $N, Q, MAXVAL \leq 2 \ 000$ |
| 2 | 24 | $MAXVAL \leq 100$ |
| 3 | 23 | $N, Q, MAXVAL \leq 50 \ 000$ |
| 4 | 10 | $MAXVAL \leq 10^6$ |
| 5 | 27 | No other constraints |

# Example

`mod.in`
```
7 8
12 4 8 10 9 7 8
1 2 5
3
2 3 11
1 5 8
2 6 4
3
2 3 4
3
```

`mod.out`
```
9
4
4
```

## Explanation

After the first operation, the array will look like this: $[2, 4, 8, 0, 9, 7, 8]$. It can be observed that the first and the fourth values have been reduced (from $12$ became $2$ and $10$ became $0$).

After the third operation, the array will look like this: $[2, 4, 11, 0, 9, 7, 8]$.

After the fourth operation, the array will look like this: $[2, 4, 3, 0, 1, 7, 0]$.

After the fifth operation, the array will look like this: $[2, 4, 3, 0, 1, 4, 0]$.

After the seventh operation, the array will look like this: $[2, 4, 4, 0, 1, 4, 0]$.
