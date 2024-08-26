# Pair Sequence

Given two sequences $A$ and $B$ of natural numbers, each containing $N$ elements: $A = [a_1, a_2, a_3, a_4 \dots a_N]$ $B = [b_1, b_2, b_3, b_4 \dots b_N]$. Find integers $x$ and $y$ such that for every $i$ from $1$ to $N – 1$ the relationship is true: $x * a_i + y * b_i < x * a_{i+1} + y * b_{i+1}$.

## Task

Given the two sequences $A$ and $B$, determine $x$ and $y$ that satisfy the previous relationship.

## Input data

The first line of the file `sdp.in` will contain the number $N$. The second line will contain $N$ numbers, separated by spaces, representing array $A$. The third line will contain $N$ numbers, separated by spaces, representing array $B$.

## Output data

In the file `sdp.out`, print on the first line the numbers $x$ and $y$ separated by a space. The printed numbers must be in the range $[-10^{18}, 10^{18}]$.

## Constraints and clarifications

1 $\leq$ $a_i$, $b_i$ $\leq$ $10^9$ 

For 15% of the score:
2 $\leq$ $N$ $\leq$ 100 and there exists a solution with 0 $\leq$ $|x|$, $|y|$ $\leq$ 100 

For 30% of the score:
2 $\leq$ $N$ $\leq$ $10^6$ and there exists a solution with 0 $\leq$ $|x|$, $|y|$ $\leq$ 1000 

For 70% of the score:
2 $\leq$ $N$ $\leq$ $10^6$ and there exists a solution with 0 $\leq$ $|x|$, $|y|$ $\leq$ $10^6$

For 100% of the score:
2 $\leq$ $N$ $\leq$ $10^6$ and there exists a solution with 0 $\leq$ $|x|$, $|y|$ $\leq$ $10^{18}$

## Example

`sdp.in`
3
2 5 7
1 2 3

`sdp.out`
2 1

## Explanation

$2 * 2 + 1 * 1 < 2 * 5 + 1 * 2$

$2 * 5 + 1 * 2 < 2 * 7 + 1 * 3$

Thus, $x = 2$ $y = 1$ is a valid solution.