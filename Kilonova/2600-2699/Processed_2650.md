~[fig1.png|align=right]

Roman the Commissioner is facing an explosive device consisting of a pyramid with $N$ levels numbered from $1$ to $N$. Each level $i$ contains $i$ bombs numbered from $1$ to $i$. We denote the bomb $j$ on level $i$ as $B_{i,j}$. For each bomb $B_{i,j}$, the time in seconds $T_{i,j}$ from the initial moment after which it explodes is known. Roman must defuse the device according to the following rules:

1. Defusing a bomb takes one second.
2. To defuse bomb $B_{i,j}$, you must first defuse the two bombs it is placed on top of, namely $B_{i+1,j}$ and $B_{i+1,j+1}$. The bombs on level $N$ have no bombs underneath and thus are not subject to this rule.

The device is considered defused once all bombs have been defused. Roman does not want to rush, so he wants to know the maximum number of seconds $X$ such that, if he were to start the defusing operation with an initial delay of $X$ seconds, the device could still be successfully defused. In other words, the task is to find the largest number $X$ such that defusal would still be possible if we replaced the numbers $T_{i,j}$ with $T_{i,j} \minus X$ for $1 \leq j \leq i \leq N$. $X$ could also be negative if Roman arrived too late at the device. For example, if defusing is impossible under the given conditions but would have been possible if he arrived at the scene one second earlier, then $X = \minus1$. If not even one second earlier was sufficient, but two seconds earlier would have been, then $X = \minus2$, and so on.

# Task

For $Q$ tests, given $N$ and the values $T_{i,j}$ for $1 \leq j \leq i \leq N$, the task is to find the number $X$.

# Input Data

The input file `detonator.in` contains the following:

The first line contains $Q$, representing the number of tests. The descriptions of the $Q$ tests follow, each test being described as follows. The first line contains the integer number $N$. The next $N$ lines, numbered within the test from $1$ to $N$, contain integers such that the $j$-th number on line $i$ is $T_{i,j}$. Note that line $i$ contains $i$ numbers.

# Output Data

The output file `detonator.out` should contain $Q$ lines, representing the number $X$ for each given test.

# Constraints and Clarifications

* $1 \leq Q \leq 5$
* $1 \leq N \leq 1\ 000$
* $1 \leq T_{i,j} \leq 10^9$ for $1 \leq j \leq i \leq N$.

| #  | Points  | Constraints                                   |
| -- | ------- | --------------------------------------------- |
| 1  | 7       | The values $T_{i,j}$ for $1 \leq j \leq i \leq N$ are equal (all bombs are scheduled to explode at the same time). |
| 2  | 13      | $N \leq 5$, $|X| \leq 10$                      |
| 3  | 9       | $N \leq 5$                                     |
| 4  | 14      | $N \leq 50$, $|X| \leq 10$ and $T_{i,j} \ge max(T_{i+1,j}, T_{i+1,j+1})$ for $1 \leq j \leq i < N$ |
| 5  | 13      | $N \leq 50$, $|X| \leq 10$                     |
| 6  | 2       | $N \leq 50$                                    |
| 7  | 9       | $N \leq 200$, $|X| \leq 10$                    |
| 8  | 2       | $N \leq 200$                                   |
| 9  | 19      | $N \leq 500$                                   |
| 10 | 12      | No additional constraints                       |

# Example

`detonator.in`
```
4
2
10
10 10
4
10
7 9
4 6 8
1 3 2 5
3
9
9 9
1 1 1
3
6
5 3
4 4 4
```

`detonator.out`
```
7
0
-2
0
```

## Explanation

* The first test has $N = 2$, and the $N \cdot (N + 1)/2 = 3$ bombs all explode after $10$ seconds. Thus, Roman can wait up to $7$ seconds before starting the process, defusing the three bombs after $8, 9,$ and $10$ seconds.
* The second test is illustrated in _Figure 1_. In this case, Roman must start defusing immediately, as the bomb $B_{4,1}$ would explode after one second. The only valid defusal order is given by the values of $B_{i,j}$ in the order $1, 2, \dots, 10$.
* The third test has three bombs that explode immediately, so Roman would have needed to arrive $2$ seconds earlier at the device.