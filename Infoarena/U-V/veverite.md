## Task

Because Phineas and Ferb decided to bring winter to the town of Danville, the squirrels finally decided to leave Candace alone and want to stock up on acorns. Initially, the squirrels have a number $X$ of acorns. The squirrels will collect acorns over the course of $N$ days; on the $i^{th}$ day, the tree in the Flynn-Fletcher family's yard will have $A_i$ acorns. The squirrels have an interesting way of collecting acorns. They are happy if, each day, their number of acorns is greater than or equal to the number of acorns in the tree on that day. At the end of each day, they can add all the acorns that were in the tree that day to their collection. (First, they must meet the condition, then they can collect the acorns.) Because the squirrels know how often Phineas and Ferb notice the disappearance of Perry the platypus, they don't want to risk these two noticing the missing acorns from the tree either. Therefore, they want to minimize the number of days they steal the acorns from the tree. For $Q$ possible scenarios given the initial number of acorns that the squirrels have, you need to find the minimum number of days the squirrels need to steal the acorns from the tree to meet the conditions, or state that this is not possible.

## Input data

The input file `veverite.in` will contain on the first line two numbers $N$ (the number of days) and $Q$ (the number of test scenarios). The second line of the file contains $N$ numbers separated by spaces representing the number of acorns each day. The third line contains $Q$ numbers separated by spaces representing the initial number of acorns.

## Output data

In the output file `veverite.out` there will be $Q$ numbers separated by spaces, representing the answers for each scenario. If a scenario is not feasible, display $-1$ for that scenario.

## Constraints

1 $\leq$ $N$, $Q$ $\leq$ $10^5$

1 $\leq$ $A_i$ $\leq$ $10^9$

$A_i \leq A_{i+1}$ for 1 $\leq$ $i$ $\leq$ $N$ - 1

### Subtasks

Subtask 1 (20 points): $N,Q \leq 2000$

Subtask 2 (20 points): $A_i \leq 100$, for 1 $\leq$ $i$ $\leq$ $N$, $N,Q \leq 10^5$

Subtask 3 (60 points): initial constraints

## Example

`veverite.in`

```
10 4
2 3 3 6 6 7 7 10 18 23
5 1 7 23
```

`veverite.out`

```
3 -1 2 0
```

## Explanation

For the first scenario, there are multiple ways to obtain the minimum. One possible way is to take the acorns on days 2, 7, and 8. The number of acorns over the course of the $N$ days will be: 5 8 8 8 8 8 15 25 25 25. For the second scenario, the initial number of acorns is less than the number of acorns in the tree on the first day, so there is no solution.