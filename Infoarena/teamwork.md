## Task

The company Robin Hood, famous for its charitable acts of stealing from the poor and giving to the rich, wants to initiate a new project to help rich children in Great Britain. For this project, you need to select a team of the best possible people. The company will provide a list with $N$ subordinates. For each subordinate $x$, their productivity $P_x$ is known (productivity can also be negative if they save endangered animals, help the needy elderly, or even maintain the ecological environment). The team must consist of a set of people in consecutive positions. You need to find the interval of people that produces maximum teamwork. A team's teamwork is calculated as follows: The productivity of the leader $\times$ The sum of the team's productivity. The leader is considered to be the member with the maximum productivity. More specifically, the teamwork of a team (or an interval $[a,b]$) is $\max(P_x)$ $\times$ $\sum(P_x)$ , for any $x$ team member (any $x$, $a \leq x \leq b$).

## Input data

The input file `teamwork.in` will contain on the first line a natural number $N$. The second line will contain $N$ integers representing the productivity of the employees.

## Output data

The output file `teamwork.out` will contain a single natural number representing the maximum teamwork of a team.

## Constraints and clarifications

$1 \leq N \leq 1\ 000\ 000$

$-1\ 000\ 000 \leq P_x \leq 1\ 000\ 000$

## Example

`teamwork.in` 
`teamwork.out` 
$12$
$7 -4 8 -5 -5 5 -5 -5 9 -3 1 1$ 
$88$ 

`8`
`7 -4 8 -20 9 -3 1 1` 
$400$

For the first example, the cost of the subarray $[1,3]$ is $\max(7, -4, 8)$ $\times$ $(7 - 4 + 8) = 8 \times 11 = 88$.

For the second example, the cost of the subarray $[4,4]$ is $-20 \times -20 = 400$ (a weak leader with a weak team can be very productive).