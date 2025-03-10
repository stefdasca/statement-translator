Given a sequence of $N$ numbers and $Q$ operations of the type:

- `0 a b val`: add the value $val$ to all numbers in the interval $[a,b]$.
- `1 a b`: display the minimum even element and the maximum odd element in the interval $[a,b]$; if one of these numbers does not exist, display $-1$ in its place.

# Task

Respond correctly to all type 1 operations.

# Input data

The first line contains the number $N$. The second line contains $N$ numbers representing the elements of the sequence. The third line contains the number $Q$, and the following $Q$ lines contain $Q$ operations as described in the statement.

# Output data

Print the responses to the type 1 operations, one per line.

# Constraints and clarifications

* $N, Q \leq 200\,000$
* Numbers in the array are between $1$ and $2\,000\,000\,000$.
* Values $val$ from type 0 operations are between $1$ and $2\,000\,000\,000$.
* **ATTENTION! If one of the two responses to a type $1$ operation cannot be calculated, display $-1$ in its place!**

| # | Score | Constraints |
| --- | ---- | ----------- |
| 1 | 30 | $N, Q \leq 5\,000$ |
| 2 | 30 | There are no type 0 operations. |
| 3 | 40 | No additional constraints |

# Example

`stdin`
```
7
5 6 3 1 9 8 5
10
1 2 5
0 2 3 2
1 2 4
0 2 7 3
1 2 4
1 4 7
0 5 7 1
1 1 6
1 1 2
1 3 4
```

`stdout`
```
6 9
8 5
4 11
4 11
4 13
-1 11
4 -1
```

## Explanation

The initial sequence is: $5\,6\,3\,1\,9\,8\,5$.

Operation `1 2 5`: The two required values are displayed on the interval $[2, 5]$.

Operation `0 2 3 2`: The new sequence will be $5\,8\,5\,1\,9\,8\,5$.

Operation `1 2 4`: The two required values are displayed on the interval $[2, 4]$.

Operation `0 2 7 3`: The new sequence will be $5\,11\,8\,4\,12\,11\,8$.

Operation `1 2 4`: The two required values are displayed on the interval $[2, 4]$.

Operation `1 4 7`: The two required values are displayed on the interval $[4, 7]$.

Operation `0 5 7 1`: The new sequence will be $5\,11\,8\,4\,13\,12\,9$.

Operation `1 1 6`: The two required values are displayed on the interval $[1, 6]$.

Operation `1 1 2`: The two required values are displayed on the interval $[1, 2]$.

Operation `1 3 4`: The two required values are displayed on the interval $[3, 4]$.