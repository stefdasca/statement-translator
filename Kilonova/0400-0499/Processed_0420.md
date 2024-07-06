In Gheorgheni, there are `N` children who are passionate about football, numbered from `1` to `N`. They want to form $T_1$ teams, where $T_1$ cannot exceed a maximum value `K`, such that each team plays one match against each of the other $T_1-1$ teams. Thus, in this stage, there are $\\frac{T_1(T_1-1)}{2}$ matches.
After all these matches are finished, the children can decide to re-divide into $T_2$ teams ($T_2 \\leq K$) and play a new stage of matches.
The final goal is that after completing all the stages, each child has had at least once as an opponent each of the other children.

# Task
Determine the minimum number of stages that need to be played so that each child has faced each of the other children at least once as an opponent. Additionally, display a way of forming the teams in each of these stages.

# Input data
The file `copii.in` contains on the first line `N` and `K`, representing the number of children and the maximum number of teams that can be formed in one round.

# Output data
The first line of the file `copii.out` will contain the minimum number of rounds, `R`. For each round `i (1 \\leq i \\leq R)` the file will contain: on the first line the number of teams $T_i$ and on the next $T_i$ lines, the composition of the teams. The `j`-th of these lines $(1 \\le j \\le T_i)$ will have the following format:
$ K_j \\ C_j[1] \\ C_j[2] \\ ... \\ C_j[K]$
where `K` represents the number of children in team `j`, and $C_j[1], C_j[2], ..., C_j[K]$ represent the numbers associated with the children in team `j`.

# Constraints and clarifications
* `2 \\leq N \\leq 100\ 000`
* `1 < K \\leq N`
* A child cannot be part of two teams in the same stage.
* It is not mandatory that the teams formed in a stage have the same number of children.
* Two children are opponents if they are part of different teams.
* For `5%` of the tests `K = N`
* For `30%` of the tests `K = 2`
* For the correct display of the number of rounds, `20%` of the score is awarded.
* In a certain round there may be children who do not belong to any team.

# Example
`copii.in`
```
5 3
```
`copii.out`
```
2
3
2 1 2
2 3 5
1 4
2
2 1 5
2 3 2
```
Explanation
---
There are `5` children who can form a maximum of `3` teams in one stage.
In the first stage, the children form three teams: one made up of children numbered `1` and `2`, the second made up of children with numbers `3` and `5`, and the third made up of a single child – the one numbered `4`.
In the second stage, they form two teams: one made up of children numbered `1` and `5` and the other of two children – those numbered `2` and `3`.