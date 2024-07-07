
The $N$ children from the elementary school want to form a soccer team composed of $K$ students, out of which at least one must be left-footed and at least one must be right-footed. For each child $i$ (from $0$ to $N-1$), the time interval during which they are available to be part of the team is known as a pair, $[start_{i}, end_{i}]$, as well as whether they are left-footed or right-footed. $K$ children can play in the same team if their availability intervals overlap at least at one point (moment in time).

# Task

Determine the number of ways to form a team with $K$ of the $N$ students; since this number can be very large, it will be displayed modulo $10^9+9$.

# Input data

The first line of the file `fotbal.in` contains the numbers $N$ and $K$. The next $N$ lines contain 3 natural numbers each, $start_{i}$, $end_{i}$, $f_{i}$, where $[start_{i}, end_{i}]$ represents the time interval during which the $i$-th child is available to be part of the team, and $f_{i}$ represents the foot with which the $i$-th child plays, $f_{i}=1$ if the $i$-th child is right-footed and $f_{i}=0$ if the $i$-th child is left-footed.

# Output data

The file `fotbal.out` will contain only the required number of ways, in the form specified in the task.

# Constraints and clarifications

* $2 \leq K \leq N \leq 100 \ 000$;
* $0 \leq start_{i} \leq end_{i} \leq 1 \ 000 \ 000 \ 000$, for any $i$ from $0$ to $N-1$;
* $f_{i} \in \{0, 1\}$, for any $i$ from $0$ to $N-1$;
* For $25$ points, $K = 2$ and $2 \le N \le 1 \ 000$;
* For $17$ points, $K = 2$ and there are at most $5$ children who are left-footed;
* For $33$ points, $2 \leq K \leq N \leq 1 \ 000$;
* For $25$ points, there are no additional constraints.

# Example

`fotbal.in`
```
5 2
1 8 0
2 5 1
3 7 0
0 9 1
6 12 0
```

`fotbal.out`
```
5
```

## Explanation

Possible teams are $(0, 1)$, $(0, 3)$, $(1, 2)$, $(2, 3)$, $(3, 4)$. We cannot form, for example, the team $(2, 4)$ because both children are left-footed. Also, we cannot form the team $(1, 4)$ because the time intervals during which the two children are available do not overlap at any point.
