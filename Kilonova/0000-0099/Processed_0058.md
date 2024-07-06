In front of the Fussy Princess's palace, there are $N$ suitors lined up, one behind the other. Each of them carries a number of precious stones under their cloak that they wish to offer the princess as a wedding gift. To avoid causing discord among them, the princess decided to eliminate $N-1$ of them peacefully, with the remaining suitor becoming the chosen one (regardless of the number of stones he possesses).

Two neighboring suitors in the line can come to an understanding as follows: the one with fewer precious stones leaves the line, receiving from the other a number of stones such that he goes home with double the number of stones he had. If two suitors have the same number of stones, one of them (it doesn't matter which) leaves, taking all the stones from his neighbor.

A suitor can come to an understanding at any moment with only one of his two neighbors. After a suitor leaves, everyone behind him moves up.

For example: for the adjacent configuration of $5$ suitors, a possible sequence of negotiations that leads to reducing the line to a single suitor is: suitors $4$ and $5$ come to an understanding, and $4$ leaves; then $1$ and $2$ come to an understanding, and $1$ leaves; then $3$ and $2$ come to an understanding, and $3$ leaves; $2$ and $5$ come to an understanding, and $5$ leaves. Thus, suitor $2$ wins the hand of the beautiful princess, offering her $0$ precious stones as a wedding gift.\
~[nunta.png]

# Task
Let $P$ be the number of precious stones that the suitor who will become the princess's chosen one has. Determine the distinct values of $P$ that can be achieved through all possible sequences of negotiations.

# Input data
The input file `nunta.in` contains:
- the first line contains the number of suitors: $n$ ($1 \leq n \leq 50$).
- the second line contains $n$ natural numbers in the range $[0, 20]$, representing the number of precious stones the suitors have, in the order they stand in line.

# Output data
The output file `nunta.out` will contain:
- the first line contains the number $m$ of distinct values that can be obtained.
- the second line contains the $m$ values in ascending order, representing the values that can be obtained.

# Example

`nunta.in`
```
4 
1 4 2 6
```

`nunta.out`
```
3
1 3 5
```