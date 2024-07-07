
# Task

We define the cost of an array as follows:

For each position $i$, $1 \leq i < N$, we proceed as follows:

* If $a_i<a_{i+1}$, then the cost will increase by $i$
* If $a_i>a_{i+1}$, then the cost will decrease by $i$
* If $a_i=a_{i+1}$, then the cost becomes $0$

Given $N$ numbers, $a_1$, $a_2$, $a_3$, $\dots$, $a_N$ and $Q$ queries in the form:

What is the cost of the subarray $[st, dr]$?

$\bold{Attention!}$ The positions of the subarray $a_{st}$, $a_{st+1}$, $a_{st+2}$, $\dots$, $a_{dr-1}$, $a_{dr}$ do not have the same positions in the initial array compared to the subarray $[st, dr]$. For example:

Let $N=7$, and the array `1 3 3 4 2 1 9`, the subarray `3 4 2 1` has positions `3`, `4`, `5` and `6` in the initial array, but in subarray $[2, 6]$ they are in positions `2`, `3`, `4` and `5`.

# Input data

The first line of the input file `sircost.in` contains the natural number, $N$. The second line contains $N$ natural numbers, representing the array $a_1$, $a_2$, $\dots$, $a_N$. The third line contains the natural number $Q$. The following $Q$ lines contain two natural numbers $st_i$, $dr_i$, representing the ends of the $i$-th subarray.

# Output data

The first $Q$ lines of the output file `sircost.out` will contain the answers for the $Q$ queries.

# Constraints and clarifications

* $1 \leq N, Q \leq 2 \cdot 10^5$;
* $0 \leq a_i \leq 10^9$;

| # | Score  | Constraints                                    |
| - | ------ | ---------------------------------------------- |
| 1 | 13     | $a_1=a_2=a_3=...=a_N$                           |
| 2 | 14     | $a_i \not= a_{i+1}$, $1 \leq i < N$             |
| 3 | 12     | The elements of the array are pairwise distinct |
| 4 | 9      | $1 \leq N, Q \leq 200$                          |
| 5 | 15     | $200 < N, Q \leq 2000$                          |
| 6 | 37     | No other constraints                            |


# Example 1

`sircost.in`
```
7
1 3 3 4 2 1 9
2
1 4
3 7
```

`sircost.out`
```
3
0
```

## Explanation

For the subarray $[1, 4]$:

* $1<3$, the cost becomes $1$
* $3=3$, the cost becomes $0$
* $3<4$, the cost becomes $3$

For the subarray $[3, 7]$:

* $3<4$, the cost becomes $1$
* $4>2$, the cost becomes $-1$
* $2>1$, the cost becomes $-4$
* $1<9$, the cost becomes $0$
```
