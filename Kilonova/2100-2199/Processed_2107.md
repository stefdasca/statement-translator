```markdown
# Task

Given $N$, an **0-indexed** array $v$ containing $N$ numbers, $Q$ and $Q$ queries of the form:
* $1 \\ p$: What is the largest $i$, $i < p$ for which $v_i > v_p$? If none, display $-1$.
* $2 \\ p$: What is the largest $i$, $i < p$ for which $v_i < v_p$? If none, display $-1$.
* $3 \\ p$: What is the smallest $i$, $i > p$ for which $v_i > v_p$? If none, display $n$.
* $4 \\ p$: What is the smallest $i$, $i > p$ for which $v_i < v_p$? If none, display $n$.

# Input data

The first line contains $N$. The second line contains the array $v$. The third line contains $Q$. The following $Q$ lines contain the queries.

Due to the size of the input data, it is recommended to add these lines of code at the beginning of the `main()` function:
```cpp
ios_base::sync_with_stdio(false);
cin.tie(nullptr);
cout.tie(nullptr);
```

# Output data

The first $Q$ lines will contain the answers to the queries, one line per answer.

# Constraints and clarifications

* $1 \\leq N \\leq 2 \\cdot 10 ^ 5$
* $1 \\leq Q \\leq 4 \\cdot N$
* $1 \\leq v_i \\leq 10 ^ 9$
* $0 \\leq p < N$

|#|Points|Constraints|
|-|-|-|
|0|0|Example|
|1|40|$N \\leq 2 \\cdot 10 ^ 3$|
|2|60|No additional constraints|

# Example

`stdin`
```
10
1 2 3 6 4 5 3 2 1 10
12
1 5
2 2
3 9
4 4
1 3
2 4
3 3
4 8
1 9
2 8
3 6
4 7
```

`stdout`
```
3
1
10
6
-1
2
9
10
-1
-1
9
8
```
```