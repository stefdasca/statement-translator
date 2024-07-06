> — Fă, eu fac cartă du-te drecu. Tu mă înjuri pe mine mă? Tu știai că vine lupu?
— Bă Bahoi, ai dreptate să moară familia mea, te rog să mă ierți. Uite acuma, mă voi plesni, mă voi băga în [penitență](https://dexonline.ro/definitie/penitenta/definitii), Bahoi, ca să-mi cer scuze, că tu ești artistul artistilor, da?

Vadim is a very talented and passionate young programmer. Filled with the Christmas spirit, he decides to spend his winter vacation by participating in as many competitions as possible on his favorite platform, $\\text{Kiloforces}$. There, the scoring system is a bit different. If the contest has $K$ problems, where the $i$-th problem is worth $p_i$ points, then when he solves the $j$-th problem, $p_j$ points are added to the total score, and from the scores of the unsolved problems, $t_j$ points are subtracted. The platform rules allow for problems with negative scores at any time (which Vadim will have to resolve).

# Task

Vadim receives $N$ problems, knowing the values $p_i$ and $t_i$ for each. In the next $Q$ days, he chooses an interval $[l, r]$ and asks himself what is the maximum score he can achieve if he participates in a contest composed of the problems $l, l+1, l+2, \ldots, r-1, r$. Help Vadim answer these $Q$ questions, or you will end up on [Santa's naughty list](https://www.youtube.com/watch?v=BbeeuzU5Qc8).

# Input data

The first line contains $N$ and $Q$. The next 2 lines contain $N$ values each ($p_i$ and $t_i$, respectively), and the last $Q$ lines contain the questions posed by Vadim.

# Output data

Each of the next $Q$ lines must contain the answers to Vadim's questions.

# Constraints and clarifications

* $1 \leq N,Q, t_i \leq 10^5$
* This [link](https://www.youtube.com/watch?v=vXYVfk7agqU) might be useful for solving the problem.
* $1 \leq p_i \leq 10^9$
* The values in the array $t$ are pairwise distinct!!

| # | Points | Constraints | 
| - | ----- | ------------ |
| 1 | 11 | $1 \leq N \leq 100$ |
| 2 | 9  | $1 \leq N \leq 1 \ 000$|
| 3 | 12 | $1 \leq N \leq 10 \ 000$ |
| 4 | 10 | For each question, the optimal order in which Vadim solves the problems is given, in other words, he starts with problem $l$ and ends with $r$. |
| 5 | 20 | $1 \leq N \leq 50 \ 000$|
| 6 | 38 | Without additional constraints|

# Example 1

`stdin`
```
4 3
12 5 4 10
6 7 1 2
1 3
2 4
3 4
```

`stdout`
```
13
15
13
```

# Example 2

`stdin`
```
5 5
2 4 6 5 9 
4 9 5 2 8 
2 5
1 2
2 3
2 2
3 3
```

`stdout`
```
0
2
5
4
6
```