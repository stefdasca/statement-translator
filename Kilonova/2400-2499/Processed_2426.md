# Task

After helping the children form teams for IKPC (International Kindergarten Programming Contest), you now want to know which team won the competition!

You have received information from the teachers regarding the number of teams, $N$, the number of problems, $P$, and the total number of actions the teams have taken, $Q$.

During an action, you will know the team that took the action, $t_i$, the problem they submitted a solution for, $p_i$, and the verdict of the solution, $1$ if the solution was accepted and $0$ if the solution was rejected. If the team **has not previously submitted a correct** source for that problem, the team's penalty for that problem will increase by $i$, where $i$ represents the ordinal number of the action in the input. If a team submits multiple solutions for a problem, the total penalty will increase by the sum of the penalties accumulated up to the submission of the first correct submission, **including the penalty for the first correct solution**. However, if a team does not submit any correct submission for a particular problem, the accumulated penalties **WILL NOT** be added to the final penalty.

For example, if a team submits the following submissions for problem $1$, they will receive a penalty of $24$, because only the submissions at times $5$, $9$, $10$ are considered. Pay attention to the submission at time $15$ as it is not considered and the penalty is not added.
* one wrong submission at time $5$
* one wrong submission at time $9$
* one correct submission at time $10$
* one wrong submission at time $15$

To *simplify* the competition, each action takes place at a **different** moment in time, so the $i$-th action will take place in the $i$-th minute. The time moments are numbered from $1$.

The final ranking of the competition will be decided as follows:
* First, teams are ordered in descending order of the number of problems solved. **Note**, if a problem receives multiple correct solutions from the same team, only the first correct submission will be considered.
* If two or more teams are tied, they will be ordered in descending order of penalty points obtained. **Note**, to calculate the penalty points, only the penalty points accumulated within the **solved** problems will be considered, without taking into account the solutions submitted after solving the problem.
* If the teams are still tied, they will be ordered in descending order of the number of problems for which the respective team was the first team to solve the problem.
* If the teams are still tied, they will be ordered in ascending order of the number of the respective team (if two teams have the same results, the team with the smaller contest number will be first).

For example, if a team solved $10$ problems and has a total penalty of $190$, it will be ahead of teams that have solved $9$ or fewer problems, as well as ahead of any team that has solved $10$ problems but with a penalty greater than $190$, or in the situation where they have a penalty of $190$ and fewer problems for which they were the first to solve them or if here there is also a tie and the contest number is smaller.

# Input data

The first line will contain $N$, $P$ and $Q$, representing the number of teams, the number of problems and the number of actions made by the teams in total.

The next $Q$ lines contain three values, $t_i$, $p_i$ and $v_i$, where $t_i$ ($1 \leq t_i \leq N$) represents the number of the team that undertook that action, $p_i$ ($1 \leq p_i \leq P$) represents the problem number they submitted a solution for, and $v_i$ is the verdict they received ($0$ for a rejected solution and $1$ for an accepted solution).

# Output data

A single line will be printed, which will contain the teams in the order of the ranking, from the team in first place to the team in last place, according to the restrictions mentioned in the statement.

# Constraints and clarifications

* $1 \leq N, P \leq 100$
* $1 \leq Q \leq 10^{4}$

| # | Points | Constraints |
| - | ----- | ------------ |
| 1 | 30 | $1 \leq M, P \leq 50$ |
| 2 | 70 | No additional constraints. |

# Example

`stdin`
```
7 11 17
5 3 0
4 11 1
2 5 1
3 9 1
2 11 1
7 7 0
6 1 1
4 2 1
6 11 1
4 9 1
5 5 0
1 4 1
2 2 1
2 6 0
6 10 1
3 8 1
3 5 1
```

`stdout`
```
4 2 6 3 1 5 7
```

## Explanation

In the table below, you can find the list of solved problems, the total penalty points and the number of problems for which each team was the first to solve the problem.

| Team | Number of solved problems | Penalty | Number of problems first solved |
| - | ----- | ------------ |----|
| 4 | 3 | 20 | 2 |
| 2 | 3 | 21 | 1 |
| 6 | 3 | 31 | 2 |
| 3 | 3 | 37 | 2 |
| 1 | 1 | 12 | 1 |
| 5 | 0 | 0 | 0 |
| 7 | 0 | 0 | 0 |