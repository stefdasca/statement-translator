```markdown
# Task

You are given a tree with $N$ nodes. Each edge has a weight $w_i$. The difference of two nodes $u$ and $v$ is the binary XOR of the weights on the simple path that connects them. More formally, if the simple path between $u$ and $v$ consists of the edges $e_1, e_2, \dots, e_l$, then their difference is defined as $w_{e_1} \oplus w_{e_2} \oplus \dots \oplus w_{e_l}$.

Let $I$ be the set of interesting nodes ($I$ is initially empty). You have to perform $Q$ operations on this set: in one operation, a node is either added or removed from $I$. After each operation, you have to print the maximum difference between two distinct interesting nodes (if $|I| \leq 1$, you must print $0$).

# Input data

The first line contains two integers, $N$ ($1 \le N \le 50000$) and $Q$ ($1 \le Q \le 50000$). The $i$-th of the following $N-1$ lines contains three integers $u_i$, $v_i$ ($1 \le u_i, v_i \le N$ for each $i=1\ldots N-1$) and $w_i$ ($0 \le w_i \le 10^9$ for each $i=1\ldots N-1$), corresponding to an edge of weight $w_i$ between nodes $u_i$ and $v_i$.

Each of the next $Q$ lines contains a single integer $p_i$ ($1 \le p_i \le N$ for each $i=1\ldots Q$). If $p_i \not \in I$, then node $p_i$ gets added to $I$, otherwise it gets deleted from $I$.

For tests worth $11$: $N, Q \leq 100$.

For tests worth $13$: $w_i \in \{0, 1\}$ for each $i = 1 \ldots N-1$.

For tests worth $17$: $N, Q \leq 1000$.

For tests worth $59$: No additional limitations.

# Output data

You need to print $Q$ lines. The $i$-th line must contain a single integer, the maximum difference between two interesting nodes after the $i$-th operation.

`stdin`
```
3 4
1 2 1
1 3 2
1
2
3
2
```

`stdout`
```
0
1
3
2
```

`stdin`
```
5 5
1 2 3
1 3 1
3 4 4
3 5 1
3
1
4
3
2
```

`stdout`
```
0
1
5
5
6
```

# Notes

In the **first sample case**, the set of interesting nodes and the interesting pair with the maximum difference after each operation:

| No. of operation | Set of interesting nodes | Pair with maximum difference|
|------------------|--------------------------|-----------------------------|
|1 | $\{1\}$ | No pairs |
|2 | $\{1, 2\}$ | $(1, 2)$ |
|3 | $\{1, 2, 3\}$ | $(2, 3)$ |
|4 | $\{1, 3\}$ | $(1, 3)$ |

~[sample1.png]

In the **second sample case**, the set of interesting nodes and the interesting pair with the maximum difference after each operation:

| No. of operation | Set of interesting nodes | Pair with maximum difference|
|------------------|--------------------------|-----------------------------|
|1 | $\{1\}$ | No pairs |
|2 | $\{1, 3\}$ | $(1, 3)$ |
|3 | $\{1, 3, 4\}$ | $(1, 4)$ |
|4 | $\{1, 4\}$ | $(1, 4)$ |
|5 | $\{1, 2, 4\}$ | $(2, 4)$ |

~[sample2.png]
```