## Task

In a company, there are $N$ people working. Each person belongs to one of the company's departments and holds a position of either a manager or a regular employee. Each manager within a department interacts with every employee in the same department (but not with other managers). The efficiency of a department is equal to the number of distinct interactions (manager, employee) that occur within that department. The overall efficiency characterizing the entire company is the sum of the efficiency levels of each department. The company director knows that his company's efficiency is equal to $E$. However, for this efficiency to be a relevant economic indicator, it must be achieved with a minimum number of people and, if it can be achieved in multiple ways with the same minimum number of people, with as few managers as possible (it is known that managers work much less than regular employees). Write a program that determines the minimum number of people needed, and for this number, the minimum number of managers, for the company's efficiency to be equal to $E$. Also, determine the structure of the company, by department.

## Input data

The file `comp2.in` contains a single integer: $E$.

## Output data

The first line of the `comp2.out` file will contain 3 integers: $N$ - the minimum number of people, $S$ - the total minimum number of managers among these $N$ people, and $K$ - the number of company departments. On the next $K$ lines, you will print 2 integers: $P_i$, representing the number of people working in department $i$, and $S_i$, representing the number of managers among these $P_i$ people $\left(P_i \geq S_i\right)$. If there are multiple solutions with the same minimal values of $N$ and $S$, you can print any of them.

## Constraints and clarifications

$1 \leq E \leq 2000$

The company must have at least one department.

$S_1 + S_2 + \dots + S_K = S$

$P_i \geq 1$

$1 \leq S_i \leq P_i$

## Example

`comp2.in`

```
7
```

`comp2.out`

```
7 3 2
2 2
5 2
```