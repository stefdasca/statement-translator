# Task

Mihnea is in some serious trouble! He forgot to turn in his homework which is **crucial** to his final grade.

He was tasked to find an array of **length** $N$, such that $L \le a_i \le R$ for every element $a_i$ ($0 \le i \le N-1$) in the array, and the *sum of all elements* in the array **modulo** $M$ is equal to $k$ ($0 \le k < M$).

After he bargains with the teacher, in order for him to pass he is now tasked to find *the number of different arrays* that satisfy this property. Since this value can be too **big**, print the answer **modulo** $10^9+7$.

Because of his laziness, he asked you to solve this problem for him.

# Input

The input contains a single line with five integers $N$ ($1 \le N \le 10^{18}$), $M$ ($1 \le M \le 1\,000$) $L, R$ ($1 \le L \le R \le 2 \cdot 10^9$), $k$ ($0 \le k < M$).

For tests worth $0$ points: Examples.

For tests worth $10$ points: $N \le 6$; $M \le 10$; $L, R \le M$.

For tests worth $10$ points: $N \le 10\,000$; $M \le 10$; $L, R \le M$.

For tests worth $7$ points: $N \le 10\,000$; $M \le 10$.

For tests worth $8$ points: $N, M \le 500$.

For tests worth $25$ points: $M \le 100$.

For tests worth $40$ points: No additional limitations.

# Output

Print a single line with an integer: the number of arrays that satisfy the initial task modulo $10^9+7$.

# Example 1

`stdin`
```
2 7 1 7 0
```

`stdout`
```
7
```

# Example 2

`stdin`
```
3 7 27 29 3
```

`stdout`
```
1
```

# Example 3

`stdin`
```
100 17 55 123 7
```

`stdout`
```
56460584
```

# Notes

In the **first sample case**, the possible arrays are:
$[1, 6]; [2, 5]; [3, 4]; [4, 3]; [5, 2]; [6, 1]; [7, 7]$.

In the **second sample case**, the only possible array is:
$[29, 29, 29]$.