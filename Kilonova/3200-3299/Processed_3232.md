
# Task

Chimmy has an array of $N$ integers and $Q$ queries of the form $a \ b$, where for each query Chimmy wants to find out, while traversing the array from position $a$ to position $b$, how many times the maximum changes. Chimmy, not knowing how to program, asks you to help for $100$ points!

# Input data

The program reads from the keyboard the numbers $N$ and $Q$, after which it will read $N$ numbers, representing the array. The following $Q$ lines will contain two numbers $a$ and $b$, with the meaning from the statement.

# Output data

The output should contain on each line the answer to each query.

# Constraints and clarifications

* It is recommended to use [fastio](https://www.geeksforgeeks.org/fast-io-for-competitive-programming/).
* $1 \leq N \leq 1 \ 000 \ 000$
* $1 \leq Q \leq 1 \ 000 \ 000$
* $1 \leq a, b \leq N$
* The numbers in the array can be represented on 32 signed bits.
* Traversals from $a$ to $b$ will not always be from left to right. For example, if $a = 5$ and $b = 3$, the indices will be traversed in the order $5, 4, 3$.

# Example

`stdin`
```
7 5
4 6 1 3 5 2 8
3 7
4 6
1 7
6 1
5 5
```

`stdout`
```
4
2
3
3
1
```

## Explanation

In the subarray $[1, 3, 5, 2, 8]$, the maximum changes $4$ times ($1$, $3$, $5$, $8$).

In the subarray $[3, 5, 2]$, the maximum changes $2$ times ($3$, $5$).

In the subarray $[4, 6, 1, 3, 5, 2, 8]$, the maximum changes $3$ times ($4$, $6$, $8$).

In the subarray $[2, 5, 3, 1, 6, 4]$, the maximum changes $3$ times ($2$, $5$, $6$) (the subarray $[6, 1]$ was traversed in reverse).

In the subarray $[5]$, the maximum changes $1$ time ($5$).
```
