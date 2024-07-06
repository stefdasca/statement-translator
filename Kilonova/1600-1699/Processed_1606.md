_**Note** — This problem is a simplified version of the problem [uwu](https://kilonova.ro/contests/26/problems/1605). However, the solutions to the two problems are different._
\
Although school hasn't started for Ștefan for some time, a familiar sound has captured his thoughts: `uwuwuwuwuwu`.

Thus, he thought to use this opportunity to turn this sound into a good problem for RoAlgo Back to School!

# Task

Given a string $s$ indexed from $1$ that contains **only** the letters `u` and `w`, as well as $q$ queries of the form $L_i, R_i$, determine for each query how many *uwu* subsequences can be obtained in the interval $[L_i, R_i]$ if we conveniently arrange the characters within the interval $[L_i, R_i]$.

A subsequence defined by the chosen positions $i$, $j$ and $k$ (with $L_i \leq i < j < k \leq R_i$) is called *uwu* if $s_i =$ `u`, $s_j =$ `w`, $s_k =$ `u`.

Arrangements do not transfer from one query to another; in other words, all queries start from the initial string.

# Input data

The first line contains two integers, $n$ and $q$, representing the length of the string and the number of queries. The next line contains the string $s$ of length $n$. The following $q$ lines contain the queries, in the order they must be answered.
\
**Attention!** It is recommended to add the following line of code at the beginning of the `main()` function to speed up reading:
```cpp
cin.tie(0);ios::sync_with_stdio(0);
```

# Output data

Print $q$ lines, with the $i$-th line containing the answer for the $i$-th query.

# Constraints and clarifications

* $1 \leq n, q \leq 500\ 000$

|#|Score|Constraints|
|-|-|--------|
|0|0|Example|
|1|31|$N, Q \leq 2\ 000$|
|2|69|No additional constraints|

# Example

`stdin`
```
14 8
uuwuwuuuwwuuuu
1 14
5 10
8 13
3 9
4 12
2 11
4 6
1 9
```

`stdout`
```
100
6
8
12
27
36
1
27
```

## Explanation

For the fourth query, we can arrange the characters in the interval $[3, 9]$ as follows: `uuwwwuu`.

