```markdown
# Task

Given a string $S$, consisting of lowercase English letters, indexed from $1$. You need to answer $Q$ queries of the form $x, y$ - counting how many inversions are in the interval $[x, y]$. An inversion is a pair of indices $(i, j)$, $1 \leq i < j \leq N$, for which the relation $S_i > S_j$ holds.

# Input data

The first line contains a natural number $N$ representing the length of the string. The second line contains the character string $S$. The third line contains $Q$, representing the number of queries, and on the following $Q$ lines there are two natural numbers, separated by a space, which represent a query.

# Output data

Print, on different lines, $Q$ natural numbers representing the answers for each query.

# Constraints and clarifications

* $1 \leq N \leq 200\ 000$;
* $1 \leq Q \leq 400\ 000$.
* Subtask $1$ ($10\%$): $N \leq 100$;
* Subtask $2$ ($20\%$): $N \leq 1\ 000$;
* Subtask $3$ ($40\%$): $N \leq 10\ 000$;
* Subtask $4$ ($30\%$): No other restrictions.

# Example 1

`stdin`
```
7
yjiknyy
6
5 7
1 5
2 6
1 6
6 7
1 5
```

`stdout`
```
0
5
1
5
0
5
```

# Example 2

`stdin`
```
10
dvoeikwnuw
10
1 7
5 7
1 2
3 8
4 6
1 6
2 7
3 3
2 3
6 9
```

`stdout`
```
7
0
0
5
0
7
7
0
1
2
```
```