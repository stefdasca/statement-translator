```markdown
Because Lili forgot to give her friend Georgiana a Christmas present, she decided to make up for it by giving her gifts for $N$ days. Thus, each day $i$ of the $N$ days, Lili will bring $cnt_i$ gifts, all of size $m_i$, in front of Georgiana's house. After $N$ days, Georgiana starts sorting the gift boxes in ascending order by size. Since there are so many gifts, Georgiana asks you to find the size of the $K$-th gift after sorting.

# Interaction Protocol

The contestant will implement the `solve` function, with the following signature:
```cpp
int solve(int N, long long K, int cnt[] , int m[])
```

The parameters of this function have the meaning described in the task above. The function will return the required result according to the problem. **The contestant must not implement the `main` function**.

# Constraints and clarifications

* The `solve` function will be called only once
* $1 \leq N \leq 5 \ 000 \ 000$
* $1 \leq K \leq \sum_{i=0}^{n-1} cnt_i$
* $1 \leq cnt_i, m_i \leq 10^9$, for any $i$ from $0$ to $N \minus 1$
* For the official tests, the arrays $cnt$ and $m$ are generated pseudo-randomly. Details are hidden from the contestants.
* Tests are grouped into subtasks. Points for a subtask are awarded only if the source passes all tests of that subtask.

|#|Points|Constraints|
|-|-|--------|
|1|9|$\\sum_{i=0}^{n-1} cnt_i \leq 5 \ 000 \ 000$|
|2|10|$N \leq 50 \ 000$|
|3|11|$K = 4$|
|4|12|$m_i \leq 3$|
|5|58|No additional constraints|

# Example

`cadouri.in`
```
5 7
3 2
4 3
2 1
2 2
1 1
```

`cadouri.out`
```
2
```

## Explanation

The sizes of the gifts, after sorting, are:
$1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3$
Therefore, the $7$-th gift's size is $2$
```
