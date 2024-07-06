# Task

We have a sequence of $N$ numbers. We all know that a subarray of the sequence is of the form: $(s_i, s_{i+1}, . . . , s_j )$ with $1 \\leq i \\leq j \\leq N$.
The score of a subarray is given by the sum of the elements in that subsequence.
A K-**Supersequence** is a sequence formed by $K$ contiguous subarrays of the initial sequence. The score of such a K-Supersequence is given by the sum of the scores of the subarrays from which it is composed.
For example, for the sequence $1, 2, 3$, we have the following 2-Supersequences:
* $\\fbox 1 \\ \\fbox 2$ (with score 3)
* $\\fbox 1 \\ \\fbox {2 3}$ (with score 6)
* $\\fbox {1 2} \\ \\fbox 3$ (with score 6)
* $\\fbox 2 \\ \\fbox 3$ (with score 5)

Two K-Supersequences are considered distinct if they differ by at least one of the subarrays from which they are composed.
Given a sequence of numbers, a number $K$, and a number $X$, you need to determine how many distinct K-Supersequences with score $X$ exist in the sequence. Since this task would be too easy otherwise, each of these K-Supersequences must be composed of subarrays of length at least a given number $Z$.

# Input data

The input file will contain on the first line an integer $N$, representing the number of elements in the sequence.
The second line contains the sequence of numbers.
The third line contains three numbers, $K$, $X$, and $Z$, which have the meaning described in the task.

# Output data

The output file will contain on the first line a single integer, representing the number of distinct K-Supersequences with score $X$ that exist in the given sequence, composed only of subarrays of at least $Z$ elements, modulo $999 \\ 983$.

# Constraints and clarifications
* $1 \\leq K \\leq N \\leq 1 \\ 000 \\ 000$
* $1 \\leq X \\leq 1 000 \\ 000 \\ 000$

# Scoring
* For tests worth $5$ points, $K = 1, N \\leq 1 \\ 000$ and $Z = 1$.
* For other tests worth $5$ points, $K = 1$ and $Z = 1$.
* For other tests worth $5$ points, $N, K \\leq 15$ and $Z = 1$.
* For other tests worth $15$ points, $N \\leq 1 \\ 000$ and $Z = 1$.
* For other tests worth $50$ points, $Z = 1$.
* For other tests worth $20$ points, there are no additional constraints.

# Example 1

`supersecv.in`
```
5
1 1 1 2 1
2 3 1
```

`supersecv.out`
```
4
```

# Example 2

`supersecv.in`
```
5
1 2 3 2 1
2 8 1
```

`supersecv.out`
```
6
```

# Example 3

`supersecv.in`
```
5
1 2 3 2 1
2 8 2
```

`supersecv.out`
```
2
```

# Explanations

In the first example, the possible supersequences are:
$\\fbox 1 \\ \\fbox {1 1}$ 
$\\fbox {1 1} \\ \\fbox 1$
$\\fbox 1 \\ \\fbox 2$
$\\fbox 2 \\ \\fbox 1$
In the second example, the possible supersequences are:
$\\fbox 1 \\ \\fbox {2 3 2}$
$\\fbox {1 2} \\ \\fbox {3 2}$
$\\fbox {1 2 3} \\ \\fbox 2$
$\\fbox 2 \\ \\fbox {3 2 1}$
$\\fbox {2 3} \\ \\fbox {2 1}$
$\\fbox {2 3 2} \\ \\fbox 1$
In the third example, the possible supersequences are:
$\\fbox {1 2} \\ \\fbox {3 2}$
$\\fbox {2 3} \\ \\fbox {2 1}$