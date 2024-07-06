# Task

You became fond of the problem Interval XOR from the third round, so we decided to give you a more challenging version.

You are given an array of length $n$, which has positive integers, and $q$ queries.

For each query, we will give the values $l$ and $r$ and we are required to solve the problem Interval XOR for the values in the range [$l, r$] in the array. In other words, you will need to find the maximum XOR we can get by removing exactly one value from that interval.

# Input data

The first line of the input will contain $n$ and $q$ ($1 \le n, q \le 2 * 10^5$), the number of values in the array and the number of query operations your program will have to perform.

The next line of the array will contain $n$ values, the starting values of the array ($0 \le v_i < 2^{30}$).

The next $q$ lines of the array will contain $2$ values each, respecting the format given earlier in the statement ($1 \le l, r \le n$).

For tests worth $14$ points, $1 \le n, q \le 2 * 10^3$.

For tests worth $24$ more points, $l = 1$ for all the queries. 

# Output data

The output will contain a line for each operation given in the input. 

# Example 1

`stdin`
```
5 4
4 5 2 6 7
1 4
1 3
3 5
1 5
```

`stdout`
```
7
7
5
7
```