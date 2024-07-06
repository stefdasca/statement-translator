In the city $X$, elections were held with $K$ candidates participating. Each of the $N$ citizens attended the vote and wrote a permutation $p_1, p_2, ..., p_K$ on the ballot, representing the list of candidates in the order of the citizen's preferences. The winner of the election is the candidate who appears most often in position $1$ in the $N$ permutations submitted in the ballot box.

The Necromancer wishes for candidate number $1$, Charles, to win. To this end, he has managed to find, for each voter $i$ out of the $N$, a sequence $A_i$ that is a subsequence of the permutation $i$ submitted to the ballot box. The Necromancer can then create additional votes for candidate $1$ through means only he knows.

# Task
Knowing, for each permutation $i$ in the ballot box, a subsequence $A_i$ of it, determine the minimum number of additional votes that the Necromancer needs to create so that there exists at least one valid set of votes in which candidate $1$ wins, obviously aided by these additional votes. A set of votes is valid if, for each citizen $i$, a permutation is chosen that contains sequence $A_i$ as a subsequence.

# Input data
The file `necromancer.in` will contain on the first line two natural numbers $N$ and $K$ with their meanings from the statement. The following $N$ lines contain the subsequences of the $N$ permutations known by the Necromancer. Line $i + 1$ will contain an integer $L_i$, representing the length of the subsequence. Then, line $i + 1$ will also contain $L_i$ natural numbers representing the elements of the subsequence.

# Output data
The file `necromancer.out` will contain on the only line a natural number $V$ representing the minimum number of additional votes required for there to exist at least one valid set of votes in which candidate $1$ wins.

# Constraints and clarifications
* $1 \leq N, K \leq 1\ 000$
* For $30\%$ of the tests, $1 \leq N, K \leq 100$
* For $60\%$ of the tests, $1 \leq N, K \leq 500$
* Candidate $1$ must have strictly more votes than the next candidate to win.

# Example
`necromancer.in`
```
3 4
2 3 1
3 2 1 3
4 1 2 3 4
```
`necromancer.out`
```
1
```

Explanation
---
We can choose the permutations:
**3** 2 **1** 4
**2 1 3** 4
**1 2 3 4**
In this situation, candidates $1$, $2$, and $3$ each have $1$ vote. Thus, the Necromancer needs to add only one additional vote so that $1$ has two votes and wins.
We observe that we could also choose inconvenient permutations:
2 **3** 4 **1**
**2 1 3** 4
**1 2 3 4**
In this case, candidate $2$ would have $2$ votes and candidate $1$ just $1$. Thus, the Necromancer would need to add $2$ additional votes.