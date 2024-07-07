
Farmer Ion wants to expand his business by investing in the oil field. On a field, there is a sequence of $N$ oil wells numbered from $1$ to $N$, where the well numbered $i$ has a profit equal to $P_i$ dollars per month. For reasons we cannot deduce at this time, for each subarray of wells of odd length $[l, r]$, with the property that $(r - l + 1) \geq K$, he considers the well with the median profit in this subarray as a \textit{special well}. Ion is interested in knowing the profits of the \textit{special wells}, in increasing order.

The median profit of a subarray of wells is equal to the profit of the well that would be in position $\displaystyle \frac{r + l}{2}$ if the subarray were sorted.

# Input data
The first line contains the number of wells $N$ and $K$. The second line contains $N$ distinct integers, the $i$-th representing the profit $P_i$ of the well numbered $i$.

# Output data
The first line will contain a number $M$, representing the number of \textit{special wells}. The next line will contain $M$ distinct values, ordered increasingly, representing the profits of the \textit{special wells}.

# Constraints and clarifications
* $1 \leq N \leq 100\ 000$
* $K \leq N$
* $1 \leq N \cdot K \leq 50\ 000\ 000$
* $-10^9 \leq P_i \leq 10^9$

## Subtask 1 (11 points)
* $1 \leq N \leq 100$
## Subtask 2 (23 points)
* $1 \leq N \leq 5\ 000$
## Subtask 3 (42 points)
* $1 \leq N \cdot K \leq 2\ 500\ 000$
## Subtask 4 (24 points)
* No additional constraints

# Examples
`stdin`
```
10 6
2 8 3 9 7 10 5 6 4 1
```
`stdout`
```
2
6 7
```
Explanations
---
The subarray 9 7 10 5 6 4 1 has a median profit of 6, and the subarray 8 3 9 7 10 5 6 has a median profit of 7.

`stdin`
```
10 3
2 8 3 9 7 10 5 6 4 1
```
`stdout`
```
7
3 4 5 6 7 8 9
```
