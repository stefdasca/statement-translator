Since it is the final competition, the committee can finally relax watching the real-time ranking of the competitors during the trial. However, evidently, that does not satisfy them enough, so they also want to know, after each score change of a competitor, how many times have the competitors been ordered in the respective order throughout the competition until that moment.

# Input data

The input file `clasament.in` contains on the first line the numbers $N$ and $M$, representing the number of competitors, respectively the number of ranking changes. The next line contains $N$ numbers, the scores of the $N$ competitors before the trial (since the rank differentiation was very well done, all scores are different). The next $M$ lines contain $M$ pairs of numbers $x$ and $y$ which describe in chronological order the score changes. The $i$-th pair represents the fact that the score of participant $x$ has become $y$. The score of a competitor at any point in time can be lower than at the start of the competition, but it is guaranteed not to be negative.

# Output data

In the output file `clasament.out` $M$ lines will be displayed, each line containing the required answer.

# Constraints and clarifications

* $1 \leq N \leq 50\ 000$
* $1 \leq M \leq 200\ 000$
* $1 \leq x \leq N$
* Both at the beginning of the competition and during it, the scores of the competitors will be integers from the range $[0, 1\ 000\ 000\ 000]$
* The ranking is in descending order of score.
* In the case where $2$ or more scores are equal at any moment, the competitors are ranked based on the time of the last score change, so that the competitor who achieved the score earlier is ranked higher.
* For $20\%$ of the tests $1 \leq N, M \leq 2\ 000$

# Example

`clasament.in`
```
3 6
10 12 8
1 13
2 15
3 10
1 17
2 20
1 20
```

`clasament.out`
```
0
1
2
1
3
4
```

## Explanation

Moment $0$: ranking: {$2, 1, 3$}, scores: {$10, 12, 8$}
Moment $1$: ranking: {$1, 2, 3$}, scores: {$13, 12, 8$}
Moment $2$: ranking: {$2, 1, 3$}, scores: {$13, 15, 8$} (same as at moment $0$)
Moment $3$: ranking: {$2, 1, 3$}, scores: {$13, 15, 10$} (same as at moments $0$ and $2$)
Moment $4$: ranking: {$1, 2, 3$}, scores: {$17, 15, 10$} (same as at moment $1$)
Moment $5$: ranking: {$2, 1, 3$}, scores: {$17, 20, 10$} (same as at moments $0$, $2$, and $3$)
Moment $6$: ranking: {$2, 1, 3$}, scores: {$20, 20, 10$} (same as at moments $0$, $2$, $3$, and $5$)

Since the final ranking is identical to the first, we can say the competition was somewhat in vain.