The $N$ students from the 1st year of Computer Science at Politehnica University of Bucharest - Pitești University Center, coded as $1, 2, \dots, N$ need to participate in two competitions at different time periods. For the first competition, they need to send a team, and for the second competition, they need to send three teams. For the first competition, the team can have at least one student and at most $N$ students. For the second competition, the teams have names PBCUP1, PBCUP2, PBCUP3 and each contain at least one student. The order within the team does not matter, and a student can only participate in one of the teams in the second competition.

# Task

Given $N$ the number of students, determine:
1. In how many ways the team for the first competition can be chosen.
2. In how many ways the teams PBCUP1, PBCUP2, PBCUP3 for the second competition can be chosen. This number must be given modulo $7919$.

# Input data

The first line of the input file `concursuri.in` contains $C$, the number of the task that needs to be solved, and the second line contains the number of students $N$.

# Output data

The first line of the output file `concursuri.out` will contain a single natural number, which represents the value corresponding to the task $C$ from the input file.

# Constraints and clarifications

* $3 \leq N \leq 15\ 000$;
* $A$ modulo $k$ represents the remainder of the division of $A$ by $k$, i.e. $A \ \% \ k$;
* For the correct resolution of task $1$, $20$ points will be awarded.
* For the correct resolution of task $2$, $80$ points will be awarded.

# Example 1

`concursuri.in`
```
1
3
```

`concursuri.out`
```
7
```

## Explanation

In this case, task $C = 1$ is solved. The teams for the first competition can be $[1]$, $[2]$, $[3]$, $[1\ 2]$, $[1\ 3]$, $[2\ 3]$ and $[1\ 2\ 3]$.

# Example 2

`concursuri.in`
```
2
3
```

`concursuri.out`
```
6
```

## Explanation

In this case, task $C = 2$ is solved. The teams PBCUP1, PBCUP2, PBCUP3 for the first competition can be: $([1],[2],[3])$, $([1],[3],[2])$, $([2],[1],[3])$, $([2],[3],[1])$, $([3],[1],[2])$, $([3],[2],[1])$. Therefore, there are $6$ ways to participate in the second competition.