
We define a ***square-free number*** as a natural number that does not have any perfect square greater than $1$ as a divisor. By convention, $1$ is considered *square-free*.

Thus, the sequence of *square-free* numbers is: $1, 2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, \dots$

Consider a sequence of $N$ natural numbers $X_i$, $1 \leq i \leq N$, where $N$ is a natural number.

We define a ***bisubsequence*** as a non-empty subsequence obtained by removing a number from a sequence that is not at the beginning or at the end of the sequence.

# Task
1) Determine how many *square-free* numbers the given sequence contains.
2) Determine the longest *bisubsequence* in the sequence formed from *square-free* numbers, obtained by removing a number that **is not** *square-free*.

# Input data
The input file `oneout.in` contains on the first line a natural number $C$, which can be only $1$ or $2$, representing the task. The second line contains the natural number $N$ and the third line contains $N$ natural numbers, separated by a space, as described above.

# Output data
If $C$ is equal to $1$, the output file `oneout.out` will contain the number of *square-free* numbers in the sequence.

If $C$ is equal to $2$:
- The first line of the output file `oneout.out` will contain two numbers $L$ and $K$ separated by a space, where $L$ represents the maximum length of a *bisubsequence* with the required properties, and $K$ represents the number of *bisubsequences* of maximum length existing in the sequence.
- On the next $K$ lines, the start and end indices of each *bisubsequence* of maximum length found will be written, in increasing order of the start index, separated by a space.
- If the sequence does not contain any *bisubsequence* with the required properties, `-1` will be written in the output file.

# Constraints and clarifications
- $3 \leq N \leq 10^6$
- $2 \leq X_i \leq 10^6$, $1 \leq i \leq N$
- The length of a *bisubsequence* represents the number of numbers in it.
- For tests worth 37 points $C = 1$, out of which for tests worth 24 points $3 \leq N \leq 25$.
- For tests worth 63 points $C = 2$, out of which for tests worth 23 points $3 \leq N \leq 101$.

# Example 1
`oneout.in`
```
1
6
10 2 12 7 8 15
```
`oneout.out`
```
4
```
$C = 1$, $N = 6$, $X_{1−6} = \{10, 2, 12, 7, 8, 15\}$. The first task is solved.
There are $4$ *square-free* numbers in the sequence $X_{1−6}$, namely $10$, $2$, $7$, and $15$.

# Example 2
`oneout.in`
```
2
6
10 2 12 7 8 15
```
`oneout.out`
```
3 1
1 4
```
$C = 2$, $N = 6$, $X_{1−6} = \{10, 2, 12, 7, 8, 15\}$. The second task is solved.
If $12$ is removed, the *bisubsequence* $\{10, 2, 7\}$ of length $3$ is obtained. If $8$ is removed, the *bisubsequence* $\{7, 15\}$ of length $2$ is obtained. So there is a single *bisubsequence* of maximum length $= 3$, which starts at position $1$ and ends at position $4$.

# Example 3
`oneout.in`
```
2
7
5 28 17 24 15 20 18
```
`oneout.out`
```
2 2
1 3
3 5
```
$C = 2$, $N = 7$, $X_{1−7} = \{5, 28, 17, 24, 15, 20, 18\}$. The second task is solved.
If $28$ is removed, the *bisubsequence* $\{5, 17\}$ of length $2$ is obtained. If $24$ is removed, the *bisubsequence* $\{17, 15\}$ also of length $2$ is obtained. Thus, there are two *bisubsequences* of maximum length $= 2$. The first starts at position $1$ and ends at position $3$. The second starts at position $3$ and ends at position $5$.

# Example 4
`oneout.in`
```
2
9
3 10 5 8 9 11 4 15 21
```
`oneout.out`
```
3 1
6 9
```
$C = 2$, $N = 9$, $X_{1−9} = \{3, 10, 5, 8, 9, 11, 4, 15, 21\}$. The second task is solved.
$8$ cannot be removed as it is at the end of a *bisubsequence* and $9$ cannot be removed as it would be the start of a *bisubsequence*.
The only number that is not *square-free* and can be removed is $4$ and the *bisubsequence* $\{11, 15, 21\}$ of length $3$ is obtained, starting at position $6$ and ending at position $9$.
