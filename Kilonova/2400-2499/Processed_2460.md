```markdown
Gregor lives by the saying _"One for all and all for one"_, so you can(not) imagine what he did when he received a sequence of $N$ numbers for his birthday! He created a new operation on the sequence: delete all elements of value $x$ and concatenate the remaining parts. For example, if the sequence contains the numbers $1, \\ 1, \\ 2, \\ 2, \\ 3, \\ 3, \\ 1, \\ 1, \\ 2, \\ 2, \\ 3, \\ 3,$ then performing the operation for $x = 1$ gives $2, \\ 2, \\ 3, \\ 3, \\ 2, \\ 2, \\ 3, \\ 3$.

Gregor wants you to perform this operation a number of times such that the resulting sequence has the following properties: First, the resulting sequence must be _increasing_ and, second, among all increasing sequences of this kind, it must have _maximum length_. We consider a sequence $a_1, \\dots , a_N$ to be increasing if $a_1 \\leq a_2 \\leq \\dots \\leq a_N$. Similarly, we consider it to be decreasing if $a_1 \geq a_2 \geq \\dots \geq a_N$.

# Task

More formally, given a sequence of $N$ integers, your task is to find the maximum length of a possible increasing sequence obtained by deleting all elements with certain chosen values.

Help Gregor in his adventure to find the answer!

# Input data

Each input file contains multiple test cases. The first line of the input file contains the number $T$, the number of test cases. The descriptions of the $T$ cases follow. Each case contains two lines. The first line of a case contains $N$, the length of the given sequence. The second line contains the given sequence.

# Output data

You must print $T$ lines. Line $i$ must contain the answer for case $i$.

# Constraints

* $1 \leq T \leq 20\ 000$
* Let $\\sum N$ be the sum of the values of $N$ for all test cases in an input file. $1 \leq \\sum N \leq 200\ 000$.
* Let $V$ be the largest value in the sequence. $1 \leq V \leq 10^9$

| # | Score  | Constraints          |
| - | ------ | -------------------- |
| 1 | 6      | The given sequence is increasing. |
| 2 | 6      | The given sequence is decreasing. |
| 3 | 7      | $V \leq 3$           |
| 4 | 19     | There are no two equal elements in the given sequence. |
| 5 | 23     | $\\sum N \leq 4\ 000$|
| 6 | 39     | No additional constraints. |

# Example

`stdin`
```
3
2
1 1
4
1 2 1 2
10
1 2 1 2 1 3 1 2 4 3
```

`stdout`
```
2
2
5
```

## Explanation

In the first test case, Gregor can keep all the values since the sequence is already increasing.

In the second test case, Gregor needs to delete at least one of the values to obtain an increasing sequence, so the answer is $2$.

In the third test case, it can be demonstrated that by deleting the values $2$ and $3$, Gregor will obtain an increasing sequence of maximum length.
```