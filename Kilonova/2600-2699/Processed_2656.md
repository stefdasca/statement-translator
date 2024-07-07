
Two sequences, $A$ and $B$, are given with values from the set $\{0, 1\}$.

# Task

1. Determine the number of distinct subarrays in $B$ that are subsequences in $A$.
2. Determine, for a subarray $B_{p \dots q}$, the number of subsequences in $A$ equal to it.
3. Determine the number of subsequences in $A$ that are subarrays in $B$.

# Input data

The first line of the file `seqstr.in` contains $n$ representing the length of sequence $A$. The second line contains the $n$ elements of sequence $A$ separated by a space. The third line contains the number $m$ representing the length of sequence $B$. The fourth line contains the $m$ elements of sequence $B$ separated by a space. The fifth line contains the number $C$ representing the task $1$, $2$, or $3$.

If $C$ is $2$, the sixth line contains two numbers $p$ and $q$ separated by a space.

# Output data

The file `seqstr.out` will contain a single line which contains the required number as per the task.

# Constraints and clarifications

* The required results will be calculated and displayed modulo $10^9 + 7$.
* By a subsequence $T$ of length $p$ of $A$, we understand a sequence $A_{t_1}, A_{t_2}, A_{t_3}, \dots, A_{t_p}$ determined by the positions $1 \leq t_1 < t_2 < t_3 < \dots < t_p \leq n$.
* Any subarray of $B$ is determined by two positions $1 \leq p \leq q \leq m$ and is equal to the sequence $B_p, B_{p+1}, \dots, B_q$. The length of the sequence is equal to $q - p + 1$.
* Two subarrays of $B$, determined respectively by the pairs of positions $(p_1, q_1)$ and $(p_2, q_2)$ are **distinct** if they have different lengths or if they have equal lengths and there exists $k$ such that $p_1 \leq p_1 + k \leq q_1$ and $p_2 \leq p_2 + k \leq q_2$ and $B_{p_1 + k} \neq B_{p_2 + k}$.
* $1 \leq m \leq n$

|#| Points |        Constraints                                    | 
|-|-------|------------------------------------------------------|
|1|    7  | $C = 1$ and $n \leq 20$                               |
|2|    9  | $C = 1$ and $21 \leq n \leq 500$                      |
|3|   19  | $C = 1$ and $501 \leq n \leq 5000$                    |
|4|    3  | $C = 2$ and $n \leq 20$                               |
|5|    9  | $C = 2$ and $21 \leq n \leq 100$                      |
|6|   15  | $C = 2$ and $101 \leq n \leq 5000$                    |
|7|    9  | $C = 3$ and $n \leq 20$                               |
|8|    9  | $C = 3$ and $21 \leq n \leq 100$                      |
|9|   20  | $C = 3$ and $101 \leq n \leq 500$                     |


# Example 1

`seqstr.in`
```
5
1 1 0 0 1
3
0 1 1
1
```

`seqstr.out`
```
4
```

## Explanation

We need to solve task $1$. The distinct subarrays in sequence $B$ for which there exists a subsequence in $A$ are: $(0)$, $(1)$, $(0, 1)$, and $(1, 1)$. For the subarray $(0, 1, 1)$ in $B$, there is no subsequence in $A$.


# Example 2

`seqstr.in`
```
5
1 1 0 0 1
3
0 1 1
2
2 3
```

`seqstr.out`
```
3
```

## Explanation

We need to solve task $2$. The subsequences in $A$ equal to the subarray $(1, 1)$ in $B$ are those determined by the subsequences of positions: $(1, 2)$, $(1, 5)$, and $(2, 5)$.

# Example 3

`seqstr.in`
```
5
1 1 0 0 1
3
0 1 1
3
```

`seqstr.out`
```
10
```

## Explanation

We need to solve task $3$. Only subsequences of length $1$, $2$, or $3$ will be analyzed. We do not have any subsequences of length $3$ in $A$ equal to subarrays in $B$, and from the lengths of $1$ or $2$ we count those equal to $(0)$, $(1)$, $(0, 1)$, and $(1, 1)$.
