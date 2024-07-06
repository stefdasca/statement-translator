In the city $X$, a new edition of the $Y$ contest will take place, where three teams with the contest numbers $1$, $2$, and $3$ participate. The teams can have a different number of contestants.

The order in which participants enter the contest is random. Each contestant has to complete $9$ trials. In each trial, a contestant obtains a score represented by a natural number between $0$ and $10$, inclusive.

Shortly after a contestant has completed all $9$ trials, the contestant's performance is displayed in the form of two natural numbers, as follows:

* The first number can be $1$, $2$, or $3$ and represents the team the contestant belongs to.
* The second number is obtained by concatenating (joining) the **non-zero** scores obtained by the contestant in the $9$ trials. If a contestant has a score of $0$ in all trials, the second number is $0$.

The total score of a contestant is obtained by adding the scores obtained in the $9$ trials. The score of a team is obtained by adding the total scores of its members. For example, the display $2\\ 14102172$ means that this contestant is part of team $2$ and has non-zero scores $1$, $4$, $10$, $2$, $1$, $7$, and $2$ in $7$ out of the $9$ trials completed. In the other two trials, the score was $0$. Their total score is $27$, contributing $27$ points to team $2$.

The team with the highest score is declared the champion. If multiple teams achieve the highest score, all these teams are declared champions. However, if all teams have a total score of $0$, then no team is declared champion.

# Task

Knowing the number $N$ of contestants, the teams they belong to, and the scores obtained by each of them, determine:

1. The maximum score obtained by a contestant and the number of contestants who obtained this score.
2. The contest number(s) of the teams declared champions, in ascending order, and the score obtained by them. If all teams have the final score of $0$, the text `FARA CAMPION` will be displayed.

# Input data

The input file `concurs.in` contains:
- On the first line, a number $C$ (which can be $1$ or $2$), indicating the task to be solved.
- The second line contains a natural number $N$ representing the number of contestants, and on each of the following $N$ lines, there are two natural numbers, separated by a space, representing the team and the scores of each of the $N$ contestants, in the order of entry into the contest.

# Output data

1. If $C = 1$, the output file `concurs.out` will contain on a single line two natural numbers, separated by a space, representing the maximum score obtained by a contestant and the number of contestants who obtained that score.
2. If $C = 2$, the output file will contain on a single line the text `FARA CAMPION` if all teams have a final score of $0$. Otherwise, the line will contain two, three, or four natural numbers separated by a space, representing the contest number(s) of the teams declared champions, in ascending order, and then the score obtained by them.

# Constraints and clarifications

* $1 \leq N \leq 100\ 000$;
* For tests worth $35$ points, we have $C = 1$.
* For tests worth $65$ points, we have $C = 2$.

# Example 1

`concurs.in`
```
1
7
1 1111973
2 3101971
1 1999
2 1010101
3 1010101
3 0
3 1371910
```

`concurs.out`
```
31 4
```

## Explanation

The scores obtained by the contestants are: $23$, $31$, $28$, $31$, $31$, $0$, $31$ so the maximum score is $31$ and there are $4$ contestants with this score.

# Example 2

`concurs.in`
```
2
5
1 1111973
2 3101971
1 1999
3 1010101
3 1371910
```

`concurs.out`
```
3 62
```

## Explanation

There are $5$ contestants, the first contestant is from team $1$ and has a score of $23$, the second contestant is from team $2$ and has a score of $31$, the third is from team $1$ and has a score of $28$, the fourth is from team $3$ and has a score of $31$, and the fifth is from team $3$ and has a score of $31$. The total score of team $1$ is $51$, the total score of team $2$ is $31$, the total score of team $3$ is $62$. So team $3$ wins with $62$ points.

# Example 3

`concurs.in`
```
2
3
2 1111973
3 31019
1 1010111
```

`concurs.out`
```
1 2 3 23
```

## Explanation

There are $3$ contestants, the first contestant is from team $2$ and has a score of $23$, the second contestant is from team $3$ and has a score of $23$, the third is from team $1$ and has a score of $23$. So all $3$ teams have a maximum score of $23$.