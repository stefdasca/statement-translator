```markdown
*In a mysterious way, Gigelivs Valerivs Maximvs Olimpicvs, a computer scientist from ancient Rome, was transported through time to today. (What was a computer scientist in ancient Rome? An expert in using automatic calculation devices, such as the abacus.)*

Gigelivs is very surprised by everything that has happened, but what surprises him the most are today's computing problems. If in ancient times even dynamic allocation was considered a big deal, now people are not so easily impressed. However, Gigelivs, wanting to impress, presents the following problem.

A sequence $a_0, ... , a_{N-1}$ of `N` elements and a number `K` are given. On the sequence $Q_M$ modifications and $Q_I$ queries are made. These can be of the following types:
* A modification, determined by the values `pos, val`, through which the element $a_{pos}$ becomes `val`.
* A query. We define the function (where $\oplus$ denotes the xor operation on bits): $v(a) = (a_0 \oplus a_1) + (a_1 \oplus a_2) + ... + (a_{N-2} \oplus a_{N-1})$

We seek the minimum value of the function `v(a)` if you change the value of at most `K` elements from the sequence `a`.

*Note!* Within a query operation, the sequence `a` does *not* actually change, and these `K` value changes have nothing to do with the modification operation.

# Task
The contestant will implement the following functions:

```cpp
void initialize(int N, int K, std::vector <int > a);
void modify(int pos, int val);
long long calculate();
```

The interaction will proceed as follows:
1. The jury will call the `initialize` function exactly once, providing the numbers `N, K`, and the sequence `a`, indexed from `0`.
2. The jury will call the `modify` function exactly $Q_M$ times, providing through parameters the `pos, val` values mentioned in the statement.
3. The jury will call the `calculate` function exactly $Q_I$ times. The contestant must return the required answer for the current value of the sequence `a`.

# Local Interactor
If you want to test your source locally, then it is important to know the following:
The grader will read all the information from the input from the keyboard.
The input must have the following format:
* Line 1: `N`
* Line 2: $a_0, a_1,... , a_{N-1}$
* Line 3: `Q`

The following `Q` lines will be queries or modifications in the following format:
`0` – a query
`1 pos val` – a modification where the element at position `pos` becomes `val`

The interactor will display the answers to the queries on a single line: $ans_1, ans_2, ..., ans_{Q_I}$ 
$Q = Q_I + Q_M$, where $Q$ is the total number of queries or modifications, $Q_I$ is the number of queries, and $Q_M$ is the number of modifications

# Constraints
* `1 \leq N \leq 100 000`
* `1 \leq K \leq 20`
* `K \leq N`
* $1 \leq Q_I \leq 1000$
* $0 \leq Q_M \leq 50 000$
* $0 \leq a_i < 2^{31}$
* You must include "minimize.h"

## Subtask 1 (5 points)
* `N \leq 15`
* $Q_I \leq 1000$, $Q_M \leq 50 000$
## Subtask 2 (5 points)
* `N \leq 1 000`
* $Q_I = 1$, $Q_M = 0$
## Subtask 3 (10 points)
* `N \leq 100 000`
* $Q_I = 1$, $Q_M = 0$
## Subtask 4 (10 points)
* `N \leq 1 000`
* $Q_I \leq 1000$, $Q_M \leq 50 000$
## Subtask 5 (30 points)
* `N \leq 100 000`
* $Q_I \leq 1000$, $Q_M \leq 1 000`
## Subtask 6 (2 points)
* `K = 1`
## Subtask 7 (2 points)
* `K \leq 2`
## Subtask 8 (6 points)
* `K \leq 10`
## Subtask 9 (30 points)
* `N \leq 100 000`
* $Q_I \leq 1000$, $Q_M \leq 50 000$

# Examples
Consider the following call:

```cpp
void initialize(5, 2, [1, 9, 4, 6, 2])
```

This means that `N = 5, K = 2`, and `a = [1, 9, 4, 6, 2]`. The following call will occur:

```cpp
long long calculate()
```

We can modify the sequence `a` to `a = [4, 4, 4, 6, 2]` by changing the values at positions `0` and `1`. We get `v(a) = 6` which is the minimum value we can obtain, so the function should return the value `6`.

Next, there are two modifications to the sequence, defined by the following calls.

```cpp
long long modify(1, 3)
```

Thus `a` becomes `[1, 3, 4, 6, 2]`

```cpp
long long modify(2, 3)
```

Thus `a` becomes `[1, 3, 3, 6, 2]`

```cpp
long long calculate()
```

We can modify the sequence `a` to `a = [3, 3, 3, 3, 2]` by changing the values at positions `0` and `3`. We get `v(a) = 1` which is also the minimum value we can obtain, so the function should return the value `1`.
```