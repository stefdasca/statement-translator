Zvon

## Task

The manager of a branch of a large company has heard a rumor that the company's president has decided to close that branch and lay off all employees of the branch (including the manager). Being on good terms with his employees, the manager decided to inform his employees as quickly as possible so they can find another job as soon as possible. The branch employees are organized in a hierarchical tree structure. At the top of the hierarchy is the manager, who has several direct subordinates. These, in turn, have other direct subordinates, and so on, down to the lowest employee, who has no subordinates. The rumor of the layoff propagates from the top of the hierarchy to its base. One minute after hearing the rumor, the manager can call and inform one of his subordinates. After another minute, the manager can inform another subordinate, until all his subordinates are informed. In turn, each subordinate, immediately after hearing the rumor, waits a minute before informing one of their own subordinates, then another minute before informing another subordinate, and so on. Employees who have no subordinates do not inform anyone. It is clear that the order of informing subordinates influences the duration of time after which all employees hear the rumor. Determine the minimum duration of time from the moment the manager hears the rumor until all employees can hear the rumor.

## Input data

The first line of the input file `zvon.in` contains the integer $T$, representing the number of tests. Next, the description of the $T$ tests follows. The first line of each test case contains the integer $N$, representing the number of employees. The next $N-1$ lines contain two different integers $a$ and $b$, meaning that $b$ is a direct subordinate of $a$.

## Output data

For each test, print to the output file `zvon.out` a line containing the minimum duration of time after which all employees can hear the rumor.

## Constraints and clarifications

$1 \leq T \leq 57$

$1 \leq N \leq 100\,000$

Employees are numbered from 1 (the manager) to $N$.

## Example

`zvon.in`
```
3
1
3
1 2
1 3
5
1 2
1 3
3 4
3 5
```

`zvon.out`
```
0
2
3
```