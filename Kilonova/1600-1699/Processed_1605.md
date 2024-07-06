Although school has not started for Ștefan for some time, a familiar sound has occupied his thoughts: `uwuwuwuwuwu`.

Thus, he thought to use this opportunity to transform this sound into a good problem for RoAlgo Back to School!

# Task

Given a string $s$ indexed from $1$ that contains **only** the letters `u` and `w`, and $q$ queries of the form $L_i, R_i$, find for each query how many *uwu* subsequences exist in the interval $[L_i, R_i]$.

A subsequence defined by the chosen positions $i$, $j$, and $k$ (with $L_i \leq i < j < k \leq R_i$) is called *uwu* if $s_i =$ `u`, $s_j =$ `w`, $s_k =$ `u`.

# Input data

The first line contains two integers, $n$ and $q$, representing the length of the string and the number of queries. The next line contains the string $s$ of length $n$. The following $q$ lines contain the queries, in the order in which they need to be answered.
\
**Attention!** It is recommended to add the following line of code at the beginning of the `main()` function to make reading faster:
```cpp
cin.tie(0);ios::sync_with_stdio(0);
```

# Output data

Print $q$ lines, on the $i$-th line containing the answer for the $i$-th query.

# Constraints and clarifications

* $1 \leq n, q \leq 500\ 000$

|#|Score|Constraints|
|-|-|--------|
|0|0|Example|
|1|21|$N, Q \leq 2\ 000$|
|2|17|There are at most $20$ characters equal to `w`|
|3|23|$N, Q \leq 100\ 000$|
|4|39|No additional constraints|

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
85
0
6
3
21
23
1
17
```

## Explanation

For the fourth query, the triplets that form *uwu* subsequences are $(4, 5, 6)$, $(4, 5, 7)$, $(4, 5, 8)$.