```markdown
A partition of a natural number `n` is defined as an ordered set of non-zero natural numbers $(p_1, p_2, \ldots, p_k)$ that contains at least two elements, fulfilling the condition: $p_1 + p_2 + \ldots + p_k = n$.

Let's consider all partitions of a natural number $n$ in lexicographic order.

For example, for the natural number `n=4`, there are `7` partitions. We write them in lexicographic order in a list we will refer to as the lexicographic table.

| Order Nr.    | Partition    |
|--------------|--------------|
| 1            | 1 1 1 1      |
| 2            | 1 1 2        |
| 3            | 1 2 1        |
| 4            | 1 3          |
| 5            | 2 1 1        |
| 6            | 2 2          |
| 7            | 3 1          |

# Task
Given the value of the natural number n:
1. For a given number `k`, print the partition at position `k` in the lexicographic table.
2. For a given partition, calculate its order number in the lexicographic table.

# Input data
The input file `partit.in` contains on the first line the number `c`, representing the task to solve. If `c=1`, task `1` will be solved, and if `c=2`, task `2` will be solved.
The second line contains the value of `n` – the number we need to partition.
On the third line, depending on the value of `c`, we can have:
- If `c=1`, the third line contains a natural number `k`, representing an order number,
- If `c=2`, the third line contains natural numbers separated by a space, representing a partition of the number `n`.

# Output data
The output file `partit.out` will have the following content depending on the value of `c`:
- If `c=1`, the first line will contain the partition with the number `k` in lexicographic order, with numbers separated by a space;
- If `c=2`, the first line will contain the order number `k` of the read partition.

# Constraints and clarifications
- `1 < n < 10000`
- $0 < k < 10^{17}$ (regardless of whether it is case `c=1` or `c=2`)
- for tests worth `18` points we have `n \leq 20`
- for other tests worth `36` points we have `n < 10000` and `k \leq 1000000`
- for other tests worth `18` points we have `k \leq 2000000000`
- for all tests in the input files, there is a solution
- `10` points are awarded by default.

# Examples

`partit.in`
```
1
4
5
```

`partit.out`
```
2 1 1
```

`partit.in`
```
2
21
1 2 3 4 5 6
```

`partit.out`
```
375776
```
```