## Task

Infoarena has $N$ participants in the Algoritmiada competition and $M$ qualifying rounds. For each contestant, the evolution of their rating after each of the $M$ contests is known. Unfortunately, the rankings have been lost. Since the committee is cunning, it has decided to recreate the rankings as they see fit, provided that the participants' ratings do not cause an impossibility. Specifically, the only rule is: For any two participants $X$ and $Y$, if $X$ had a rating greater than or equal to $Y$ before a qualifying round and $X$ beat $Y$ in that round, after the rating adjustments, $X$ must still have a rating greater than or equal to $Y$. Otherwise, any other anomaly in the infoarena rating is allowed. Initially, all participants had a rating of $0$.

## Input data

The input file `rating.in` will contain on the first line 2 natural numbers $N$ and $M$, representing the number of participants and the number of contests. The next $N$ lines will contain $M$ natural numbers each. The element $j$ on line $i$ represents the rating of participant $i$ after the $j$-th contest.

## Output data

The output file `rating.out` will contain $M$ lines of $N$ natural numbers each. On line $i$ will be the ranking of contest $i$, represented by a permutation of length $N$ (at position $x$ will be the index of the contestant who finished in place $x$ in that contest).

## Constraints and clarifications

$N * M \leq 1\,000\,000$

Ratings are natural numbers in the range $[0\, 1\,000\,000\,000]$

If there are multiple solutions, you can display any

## Example

`rating.in`
3 2
100 200 1000
3 5 123

`rating.out`
2 1 3
3 1 2