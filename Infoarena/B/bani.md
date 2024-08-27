## Money

A serious guy wants to make a lot of $money$. So he goes to the $market$ with $N$ items for which he knows the value, the weight, and whether they can be partitioned or not. If an $item$ $i$ has the value $val[i]$ and the weight $greu[i]$ and it can be partitioned, then it can be partitioned into 2 distinct items such that: $val1[i] + val2[i] = val[i]$ and $greu1[i] + greu2[i] = greu[i]$ and $val1[i] / val[i] = greu1[i] / greu[i]$ where $greu1[i]$ and $val1[i]$ are the weight and value of the first of the two items obtained by partitioning, and $greu2[i]$ and $val2[i]$ are the weight and value of the second one. Knowing that he has a $backpack$ in which he can carry at most $G$ units, you need to calculate the maximum value the guy can gain.

## Input Data

The input file `bani.in` contains on the first line a number $T$, representing the number of tests. For each test, the first line contains two numbers $N$ and $G$, representing the number of items and respectively the maximum weight of the backpack. On the next $N$ lines, there are 3 numbers $val[i]$, $greu[i]$, and $part[i]$, representing the value of the item $i$, its weight, and whether it can be partitioned or not.

## Output Data

The output file `bani.out` will contain $T$ numbers, one on each line, each representing the answer for the $T$ tests.

## Constraints and Clarifications

$T = 10$

$1 \leq N \leq 750$

$1 \leq G \leq 1000$

$0 \leq greu[i] \leq 1000$ for $1 \leq i \leq N$

$1 \leq val[i] \leq 5000$ for $1 \leq i \leq N$

If an $item$ $i$ can be partitioned then $part[i] = 1$, otherwise $part[i] = 0$.

To receive points for this problem, the absolute difference between your solutions and those of the committee must be less than $10^{-6}$, and the committee suggests using 8 decimals for display.

## Example

`bani.in`
```
1
3 15
10 10 0
10 10 0
5 7 1
```

`bani.out`
```
13.57142857
```

## Explanation

Because we cannot take the first 2 items since they are too heavy, we will take one of them, and partition the third one into two items so that with one of the two we fill the backpack.