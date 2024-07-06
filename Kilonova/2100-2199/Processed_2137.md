In a distant world at the edge of a dark forest lies a mystical land known as the "Land of Wizards". There, amidst giant trees and ancient stones, lived magical and mysterious beings said to possess unimaginable powers.

This land, renowned for its magic, can be traversed according to strict rules. The land is divided into counties, each county being led by a magical being. Each magical being has an inherent power that we will henceforth call the $X$ factor. A being can pass through a county only if it meets strict rules related to their $X$ factor and the $X$ factor of the county's leader.

The map of such a land is represented as a matrix with $N$ rows and $N$ columns where each cell represents a county, and $a_{i,j}$ represents the $X$ factor of the magical being leading the county at coordinates $(i, j)$. Movement on the map is done in the directions given by the 4 cardinal points (N, E, S, W).

A young brave man wants to traverse the land starting from cell $(1, 1)$ and reaching cell $(N, N)$, but he does not know if he can do this and needs your help.

# Task

Knowing the $X$ factor of the young man and the fact that to be able to pass through a county, his $X$ factor must have at least as many divisors as the $X$ factor of the county's leader:

1. Determine the length of a path through which he can traverse the land according to the mentioned rules so that this length is minimal;
2. Determine the minimum cost of traversing the land, considering that the young man has to pay a sum of money equal to the difference between the number of divisors of his $X$ factor and the number of divisors of the county leader's $X$ factor.

Knowing that to traverse a county, the young man's $X$ factor must be strictly greater than that of the leader:

3. Find the minimum $X$ factor the young man can have so that he can traverse the land safely.

# Input data

The first line contains a number $C$ representing the task to be solved.

The second line contains a number $T$ representing the number of distinct cases that need to be solved.

Then $T$ groups of the following form will be read:
- For tasks 1 and 2, the first line will contain a number representing the $X$ factor of the young man.
- The next line contains a number $N$ with the above meaning.
- The next $N$ lines will contain the elements of the matrix.

# Output data

The output file will contain $T$ lines. Each line contains the answer for the corresponding test case.

# Constraints and clarifications

* If there is no path that respects the given rules, $-1$ will be displayed.
* It is guaranteed that the young man will always be able to enter cell $(1, 1)$.
* $C \in \{1, 2, 3\}$
* For $C = 1$ and $C = 2$, $a_{i,j} \geq 1$.
* $1 \leq T \leq 10$
* $1 \leq X \leq 10^{12}$
* $1 \leq N \leq 500$
* $0 \leq a_{i,j} \leq 10^{12}$
* For tests worth $10$ points, $C = 1$ and $1 \leq a_{i,j}, X \leq 10^{6}$.
* For other tests worth $23$ points, $C = 1$.
* For other tests worth $10$ points, $C = 2$ and $1 \leq a_{i,j}, X \leq 10^{6}$.
* For other tests worth $24$ points, $C = 2$.
* For other tests worth $10$ points, $C = 3$ and $1 \leq N \leq 300$, $0 \leq a_{i,j} \leq 10^{4}$.
* For other tests worth $23$ points, $C = 3$.

# Example 1
`tinut.in`
```
1
2
16
6
1 36 79 85 87 82
26 46 55 39 74 19
89 73 65 31 36 18
99 39 8 17 47 58
6 44 80 29 73 90
54 40 79 57 19 11
16
6
1 36 79 85 87 82
26 46 55 39 74 19
89 73 65 31 36 18
99 39 8 12 47 58
6 44 80 29 73 90
54 40 79 57 19 11
```

`tinut.out`
```
11
-1
```

## Explanation
For the first example, in the first case, we will consider a matrix where we mark with $0$ the places we can pass and with $\\textcolor{blue}{1}$ the places we cannot pass, the number of divisors of the young man's $X$ factor being $5$.

$$
\\textcolor{red}{0}\\ \\textcolor{blue}{1}\\ 0\\ 0\\ 0\\ 0 \\\\
\\textcolor{red}{0}\\ 0\\ 0\\ 0\\ 0\\ 0 \\\\
\\textcolor{red}{0}\\ \\textcolor{red}{0}\\ \\textcolor{red}{0}\\ \\textcolor{red}{0}\\ \\textcolor{blue}{1}\\ \\textcolor{blue}{1} \\\\
\\textcolor{blue}{1}\\ 0\\ 0\\ \\textcolor{red}{0}\\ 0\\ 0 \\\\
0\\ \\textcolor{blue}{1}\\ \\textcolor{blue}{1}\\ \\textcolor{red}{0}\\ 0\\ \\textcolor{blue}{1} \\\\
\\textcolor{blue}{1}\\ \\textcolor{blue}{1}\\ 0\\ \\textcolor{red}{0}\\ \\textcolor{red}{0}\\ \\textcolor{red}{0} \\\\
$$

In the second case, it can be observed that there is no path from $(1, 1)$ to $(N, N)$ that meets the conditions.

$$
0\\ \\textcolor{blue}{1}\\ 0\\ 0\\ 0\\ 0 \\\\
0\\ 0\\ 0\\ 0\\ 0\\ 0 \\\\
0\\ 0\\ 0\\ 0\\ \\textcolor{blue}{1}\\ \\textcolor{blue}{1} \\\\
\\textcolor{blue}{1}\\ 0\\ 0\\ \\textcolor{blue}{1}\\ 0\\ 0 \\\\
0\\ \\textcolor{blue}{1}\\ \\textcolor{blue}{1}\\ 0\\ 0\\ \\textcolor{blue}{1} \\\\
\\textcolor{blue}{1}\\ \\textcolor{blue}{1}\\ 0\\ 0\\ 0\\ 0 \\\\
$$

# Example 2
`tinut.in`
```
2
1
16
6
3 36 79 85 87 82
26 46 55 39 74 19
89 73 65 31 36 18
99 39 8 17 47 58
6 44 80 29 73 90
54 40 79 57 19 11
```

`tinut.out`
```
21
```

## Explanation
For the second example, the map looks like this, where the value in each cell represents either the fact that the county cannot be passed ($\\textcolor{blue}{\\text{x}}$), or the cost of passing through that county. The path followed to obtain the minimum cost can be observed.

$$
\\textcolor{red}{3}\\ \\textcolor{blue}{\\text{x}}\\ 3\\ 1\\ 1\\ 1 \\\\
\\textcolor{red}{1}\\ \\textcolor{red}{1}\\ \\textcolor{red}{1}\\ 1\\ 1\\ 3 \\\\
3\\ 3\\ \\textcolor{red}{1}\\ 3\\ \\textcolor{blue}{\\text{x}}\\ \\textcolor{blue}{\\text{x}} \\\\
\\textcolor{blue}{\\text{x}}\\ 1\\ \\textcolor{red}{1}\\ \\textcolor{red}{3}\\ 3\\ 1 \\\\
1\\ \\textcolor{blue}{\\text{x}}\\ \\textcolor{blue}{\\text{x}}\\ \\textcolor{red}{3}\\ 3\\ \\textcolor{blue}{\\text{x}} \\\\
\\textcolor{blue}{\\text{x}}\\ \\textcolor{blue}{\\text{x}}\\ 3\\ \\textcolor{red}{1}\\ \\textcolor{red}{3}\\ \\textcolor{red}{3} \\\\
$$

# Example 3
`tinut.in`
```
3
1
6
0 36 79 85 87 82
26 46 55 39 74 19
89 73 65 31 36 18
99 39 8 17 47 58
6 44 80 29 73 90
54 40 79 57 19 11
```

`tinut.out`
```
58
```

## Explanation
For the third example, there are multiple ways to traverse the land by a young man with an $X$ factor of 58, but there is none where the land can be traversed with a smaller factor. One such path is:

$$
\\textcolor{red}{3}\\ 36\\ 79\\ 85\\ 87\\ 82 \\\\
\\textcolor{red}{26}\\ \\textcolor{red}{46}\\ \\textcolor{red}{55}\\ \\textcolor{red}{39}\\ 74\\ 19 \\\\
89\\ 73\\ 65\\ \\textcolor{red}{31}\\ 36\\ 18 \\\\
99\\ 39\\ 8\\ \\textcolor{red}{17}\\ 47\\ 58 \\\\
6\\ 44\\ 80\\ \\textcolor{red}{29}\\ 73\\ 90 \\\\
54\\ 40\\ 79\\ \\textcolor{red}{57}\\ \\textcolor{red}{19}\\ \\textcolor{red}{11} \\\\
$$