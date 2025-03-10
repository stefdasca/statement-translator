
# Jancsi and the Tables

Jancsi has a table with $n$ elements, consisting of integer numbers, $a$, and a table with $m$ integer elements, $b$.

Jancsi considers a table $c$ of length $m$ to be **"good"** if the elements of the table $c$ can be rearranged so that at least $k$ of them match the elements of table $b$.

For example, if $b=[1, 2, 3, 4]$ and $k=3$, then:

* The tables $[4, 1, 2, 3]$ and $[2, 3, 4, 5]$ are good (because they can be rearranged as $[1, 2, 3, 4]$ and $[5, 2, 3, 4]$)
* The tables $[3, 4, 5, 6]$ and $[3, 4, 3, 4]$ are not good.

# Task

Jancsi selects each subarray of length $m$ from table $a$ as a possible table $c$. Help Jancsi count how many of these tables are **good**.

In other words, we need to determine the number of positions $l$ where $1 \leq l \leq n - m + 1$, and the elements $a_l$, $a_{l+1}$, ... , $a_{l+m-1}$ form a **good** table.

# Input data

* The first line of the input file `jancsi.in` contains an integer $t$ - the number of test cases.
* For each test, the first line contains three integers: $n$, $m$, and $k$ - the number of elements in arrays $a$ and $b$ and the corresponding number of elements that need to match.
* The second line contains $n$ integers: $a_1$, $a_2$, …, $a_n$ - the elements of table $a$.
* The third line contains $m$ integers: $b_1$, $b_2$, …, $b_m$ - the elements of table $b$.

# Output data

* For each test, print on a separate line in `jancsi.out` the number of good tables from array $a$.

# Constraints and clarifications

* $1 \leq t \leq 10^4$
* $1 \leq k \leq m \leq n \leq 2 \cdot 10^5$;
* $1 \leq a_i \leq 10^6$
* $1 \leq b_i \leq 10^6$
* The elements of table $a$ are not necessarily unique. The elements of table $b$ are not necessarily unique.

# Example

`jancsi.in`
```
5
7 4 2
4 1 2 3 4 5 6
1 2 3 4
7 4 3
4 1 2 3 4 5 6
1 2 3 4
7 4 4
4 1 2 3 4 5 6
1 2 3 4
11 5 3
9 9 2 2 10 9 7 6 3 6 3
6 9 7 8 10
4 1 1
4 1 5 6
6
```

`jancsi.out`
```
4
3
2
4
1
```

## Explanation

* In the first example, all subarrays are good.
* In the second example, the good subarrays start at positions 1, 2, and 3.
* In the third example, the good subarrays start at positions 1 and 2.
```
