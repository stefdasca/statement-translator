Here is the translated and formatted competitive programming problem statement:

```markdown
Considering two natural numbers $X$ and $Y$, we say that $X$ is a prefix for $Y$ if $X$ can be obtained from $Y$ by deleting $0$, $1$ or more digits from the end of $Y$.  
Examples:
* $1024$ is a prefix for $1024789056$
* $526$ is a prefix for $526$

We are given the natural numbers $Q$, $L$ and then a sequence of $Q$ queries of the following $3$ types:

|Query Type|Meaning|
|---|---|
|1 M|Determine the minimum $N$, $N \leq L$, such that $2^N$ has $M$ as a prefix (it is guaranteed that for the given queries there exists such a number).|
|2 M N|Check if $M$ is a prefix of $2^N$ (the answer is $1$ if true, otherwise $0$).|
|3 M A B|Determine the number of values $N \\ (A \\leq N \\leq B)$ such that $M$ is a prefix of $2^N$.|

where $M, N , A$ and $B$ are natural numbers.

# Task

Given $Q, L$ and a sequence of $Q$ queries, determine the answers to the given queries.

# Input data

The input file `p2.in` contains in the first line the natural numbers $Q$ and $L$, separated by a space.
The next $Q$ lines contain the $Q$ queries, one query per line, in the form described in the table.

# Output data

The output file `p2.out` will contain $Q$ lines.  
Each line $i$ will contain the answer for the $i$-th query from the input file.

# Constraints and clarifications

* $1 \leq Q \leq 100 000$
* $1 \leq L \leq 1 000 000$
* $0 \leq M \leq 999 999$
* $0 \leq N \leq L$
* $0 \leq A \leq B \leq L$

|#|Points|Constraints|
|-|-|-|
|1|24|The input file contains only queries of type $1$ and $1 \leq L, Q \leq 100 000$.|
|2|24|The input file contains only queries of type $2$ and $1 \leq L, Q \leq 100 000$.|
|3|24|The input file contains only queries of type $3$ and $1 \leq L, Q \leq 100 000$.|
|4|16|$1 \leq L, Q \leq 100 000$.|
|5|12|No additional constraints.|

# Example

`p2.in`
```
4 13
1 8
2 81 13
2 64 7
3 1 0 13
```

`p2.out`
```
3
1
0
4
```

## Explanation

The values for $2^0$, $2^1$, ..., $2^{13}$ are $1$, $2$, $4$, $8$, $16$, $32$, $64$, $128$, $256$, $512$, $1 \ 024$, $2 \ 048$, $4 \ 096$, $8 \ 192$.
For the first query, we have $M=8$, and the smallest $N \leq 13$ with a prefix equal to $8$ for $2^N$ is $3$, $2^3 = 8$.  
For the second query, we have $M=81$ and $N=13$ and since $2^{13} = 8 \ 192$, we have the result $1$.  
For the third query, we have $M=64$ and $N=7$ and since $2^7 = 128$, we have that the result is $0$.  
For the fourth query, we have $M=1$, $A=0$ and $B=13$, and the values of $N$ for which $1$ appears as a prefix in $2^N$ are $0$, $4$, $7$, $10$ so the answer is $4$.
```