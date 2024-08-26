# Tabara2

Alexandra is spending her summer vacation at a camp, where participants have been divided into teams, and she has been chosen as the leader of one of them. The teams go through different trials during which they accumulate points, with the team having the most points winning the camp trophy. For the first trial, each team received a camp map marked with $N$ locations, numbered from $1$ to $N$, and a list of tasks numbered from $1$ to $S$, each task worth a certain number of points. The tasks will be performed based on the instructions received from the organizers throughout the trial. The instructions are of $2$ types: $1)$ Completing task $i$ allows the completion of task $j$ and vice versa (completing task $j$ allows completing task $i$). $2)$ At location $i$, task $j$ can be performed (after which tasks allowed by instruction $1$ can be performed).

## Task

Help Alexandra to determine for the given locations $i$ and $j$ the task with the maximum points that can be completed starting from any location in the interval $[i, j]$.

## Input data

The first line of the input file `tabara.in` contains $3$ numbers $N$, $S$, and $M$ representing the number of locations, the number of tasks, and the number of instructions and queries, respectively. The second line contains $S$ numbers representing the points of the tasks in order, from $1$ to $S$. The next $M$ lines will contain the instructions and queries. A line will have the form:
$1)$ $U$ $1$ $i$ $j$ $\rightarrow$ Completing task $i$ allows the completion of task $j$ and vice versa (completing task $j$ allows completing task $i$).
$2)$ $U$ $2$ $i$ $j$ $\rightarrow$ At location $i$, task $j$ can be performed (after which tasks allowed by instruction $1$ can be performed).
$3)$ $Q$ $i$ $j$ $\rightarrow$ Print in the output file the task with the maximum points that can be completed from a location $k$, $i \leq k \leq j$. 

## Output data

In the output file `tabara.out`, print the required number on a separate line for each `'Q'` query.

## Constraints

$1 \leq N, S, M \leq 50\ 000$

For $30\%$ of the tests $1 \leq N, S, M \leq 1\ 000$

Note! It is guaranteed that a task can only be accomplished from one location (directly or indirectly).

The points of a task are $\leq 1\ 000\ 000\ 000$.

## Example

`tabara2.in`
```
2
4
6
3
2
4
1
U 1 2 4
U 2 1 1
U 2 2 2
Q 1 2
U 1 3 4
Q 1 2
```

`tabara2.out`
```
3
4
```