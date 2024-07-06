There are $N$ participants numbered from $0$ to $N - 1$ competing in a padel competition, which takes place over $M$ days. Each day, one match is played. There are $M$ medals awarded in the competition, one new medal for each match. On the match held on day $i \ (0 \leq i \leq M - 1)$, the participants numbered $x$ and $y$ play. During a match, the following happens:

* Participant $x_i$ wins against participant $y_i$.
* A new medal is given to the winner $x_i$.
* All medals of the loser are given to the winner.

On day $M$ (the day after the last match), the award ceremony is organized. At the ceremony, the medals are collected and each is handed to the participant who was in possession of it for the longest period. Formally, medal $i$ is handed to the participant who held the medal for the most nights (not necessarily consecutive), until day $M$. If two or more participants held the medal for the same number of nights, the medal is given to the participant with the smallest index.

The goal is to determine for each participant the number of medals they receive at the award ceremony.

# Input data

The first line contains the integers $N$ and $M$, representing the number of participants and the number of matches.

Then there are $M$ lines. Each line $i$ contains two integers $x_i$ and $y_i$, representing the participants from day $i$, where $x_i$ defeats $y_i$.

# Output data

Print on a single line $N$ integers, where the $k$-th number represents the number of medals received by participant $k$ after the award ceremony.

# Constraints and clarifications

* $2 \leq N \leq 200\ 000$
* $1 \leq M \leq 200\ 000$
* $0 \leq x_i, y_i \leq N - 1$ and $x_i \neq y_i \ (for\ any\ 0 \leq i \leq M - 1)$.

Your solution will be tested on multiple groups of tests, each group having a number of points associated with it. Each group of tests can contain multiple tests. To obtain the score of a test group, the solution must pass all the tests in that group.

| # | Points | Constraints          |
| - | ------- | ------------------- |
| 1 | 12      | $N = 2$|
| 2 | 16      | $N, M \leq 2\ 000$      |
| 3 | 15      | The winner of match $i$ participates in match $i + 1$, for any $i$ such that $0 \leq i \leq M - 2$ |
| 4 | 20      | At the time of match $i$ , $x_i$ has at least as many medals as $y_i$, for any $i$ such that $0 \leq i \leq M - 1$.      |
| 5 | 22      | Once a participant loses, they will no longer participate in any match, on any day. |
| 6 | 15      | Without additional constraints.      |

# Example 1

`stdin`
```
3 4
0 1
2 1
1 0
2 1
```

`stdout`
```
1 1 2
```

## Explanation

For the first example, the drawing below shows who was in possession of which medals throughout the competition. When participant $1$ loses on the third day, all medals are given to participant $2$.

~[sample-small-1.png]

# Example 2

`stdin`
```
3 7
0 1
0 2
2 0
0 1
1 0
2 0
0 2
```

`stdout`
```
2 2 3
```

## Explanation

The second example can be observed below.

~[sample_illustration-1.png]

After the award ceremony, participant $0$ has medals $5$ and $6$, participant $1$ has medals $3$ and $4$, and participant $2$ has medals $0, 1$ and $2$.

# Example 3

`stdin`
```
6 10
2 5
3 0
4 2
0 1
4 3
2 4
0 3
0 2
5 2
5 0
```

`stdout`
```
5 0 1 1 1 2
```

