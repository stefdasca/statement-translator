There are $N$ candidates in the presidential elections. Each of the $N$ candidates knows exactly whom they will vote for. One person can vote for only one other person (they can also vote for themselves). Your goal is to create confusion among the candidates. To achieve this, you are allowed to prohibit at most $K$ candidates from participating. When a candidate is eliminated, all candidates who would have voted for them will vote for the person the eliminated candidate would have voted for (because they trust their decision). If the eliminated candidate would have voted for themselves or was **UNDECIDED**, all those who would have voted for them become **UNDECIDED**.

In short, if $A$ votes for $B$ and $B$ votes for $C$, after eliminating $B$, $A$ will vote for $C$. If $A$ votes for $B$ and $B$ votes for $B$, after eliminating $B$, $A$ will become **UNDECIDED**. Also, if $A$ votes for $B$ and $B$ is **UNDECIDED**, after eliminating $B$, $A$ will become **UNDECIDED**. A candidate is considered **DECIDED** if they are **NOT** eliminated and **NOT** **UNDECIDED**.

# Task

For each $K$ from $1$ to $N$, find the minimum number of **DECIDED** candidates we can have if we eliminate $K$ candidates.

# Input data

The first line of the input file `politic.in` will contain the natural number $N$, representing the number of candidates. There will be $N$ more lines. The $i + 1$ line will contain a natural number, representing the candidate whom the candidate with number $i$ votes for.

# Output data

The output file `politic.out` will contain $N$ lines. On line $i$, print a single natural number, representing the minimum number of decided candidates if we eliminate $i$ candidates.

# Constraints and clarifications

* $1 \leq N \leq 1 \\ 000$
* For tests worth $30$ points, $N \leq 200$.
* Candidates are indexed from $1$.

# Example

`politic.in`
```
6
2
6
2
5
5
5
```

`politic.out`
```
3
2
0
0
0
0
```

## Explanation

By eliminating candidate $5$, candidates $4$ and $6$ become undecided, so only $3$ decided candidates remain ($1$, $2$ and $3$). Further eliminating candidate $6$, candidate $2$ becomes undecided because $6$ was undecided. Thus, only $1$ and $3$ remain decided. By eliminating candidate $2$, no decided candidate remains.