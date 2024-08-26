# Seqval

For a sequence $S = s_1, \dots, s_k$ of distinct natural numbers, let $i$ be the position of the maximum element, and $j$ be the position of the minimum element. We define $v(S) = v(s_1, \dots, s_k) = i - j$. Given a permutation $A = a_1, \dots, a_N$ of the set $\{1, \dots, N\}$, determine the value of the sum:

## Input data

The first line of the input file `seqval.in` contains the natural number $N$.

The second line contains the elements of permutation $A$ in order.

## Output data

The output file `seqval.out` will contain the answer on a single line.

Subtasks:
- Subtask 1 (20 points) $N \leq 200$ 
- Subtask 2 (20 points) $N \leq 2\ 000$ 
- Subtask 3 (40 points) $N \leq 200\ 000$ 
- Subtask 4 (20 points) $N \leq 500\ 000$ 

## Example

`seqval.in`
```
5
1 2 3 4 5
```
`seqval.out`
```
20
```
`3`
```
2 3 1
```
`1000000006`

## Explanation

We observe that in the first example the required sum is:
$v(1,2) + \dots + v(4,5) + v(1,2,3) + \dots + v(3,4,5) + v(1,2,3,4) + v(2,3,4,5) + v(1,2,3,4,5) = 4 \times 1 + 3 \times 2 + 2 \times 3 + 1 \times 4 = 20$

We observe that in the second example the required sum is $v(2,3) + v(3,1) + v(2,3,1) = (2 - 1) + (1 - 2) + (2 - 3) = -1$, and $-1 \mod 10^9 + 7 = 10^9 + 6$.