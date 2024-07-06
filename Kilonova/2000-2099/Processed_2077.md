# Task

The magic divisor $d(x)$ of a nonzero natural number $x$ is equal to:

$$
d(x) = 
\begin{cases}
\text{the largest divisor of } x \text{ strictly less than } x,  & \text{if } x > 1 \\
1, & \text{if } x = 1
\end{cases}
$$

For example, $d(1)=1$, $d(3)=1$, $d(28)=14$, and $d(125)=25$.

You are given an array $a_1,a_2,\ldots,a_n$ on which you have to perform $q$ operations of the following type:

- `l r`: For each $l \le i \le r$, $a_i$ will be replaced with $d(a_i)$.

Display the array $a$ after $q$ operations.

# Input data

The input file `divop.in` will contain two natural numbers $n$ and $q$ on the first line - the length of the array $a$ and the number of operations, respectively.

The second line will contain $n$ numbers $a_1,a_2,\ldots,a_n$ - the elements of the array $a$.

Each of the following $q$ lines will contain two numbers $l$ and $r$ - the endpoints of the operations.

# Output data

The output file `divop.out` will contain $n$ numbers, the elements of the array $a$ after performing the $q$ operations.

# Constraints and clarifications

- $1 \le n,q \le 3 \cdot 10^5$;
- $1 \le a_i \le 10^7$;
- $1 \le l \le r \le n$;
- For 10 points, $n,q,a_i \le 300$;
- For another 10 points, $n,q,a_i \le 1\,000$;
- For another 10 points, $n,q,a_i \le 5\,000$;
- For another 10 points, $n,q \le 5\,000$ and $a_i \le 10^5$;
- For another 10 points, $n,q \le 5\,000$;
- For another 10 points, $l = r$;
- For another 20 points, $n,a_i \le 10^5$;
- For another 10 points, $a_i \le 10^5$;
- For the remaining 10 points, no additional constraints are imposed.

# Example

`divop.in`
```
9 4
16 9 7 20 4 1 5 12 30
1 9
4 4
8 9
1 1
```

`divop.out`
```
4 3 1 5 2 1 1 3 5
```

## Explanation

After the first operation, the array $a$ will become $[8, 3, 1, 10, 2, 1, 1, 6, 15]$.

After the second operation, the array $a$ will become $[8, 3, 1, 5, 2, 1, 1, 6, 15]$.

After the third operation, the array $a$ will become $[8, 3, 1, 5, 2, 1, 1, 3, 5]$.

After the fourth operation, the array $a$ will become $[4, 3, 1, 5, 2, 1, 1, 3, 5]$.