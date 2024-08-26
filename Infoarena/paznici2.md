# Paznici2

In a city in full reconstruction, there are $N$ tourist attractions that need to be guarded overnight. The city administration has contracted a security company that provided $N$ guards. However, there is a strange aspect related to this transaction: each guard negotiates their salary individually, depending on the tourist attraction they have to guard. Knowing the salary demands of each guard, Algorel - the IT manager at the city hall - must distribute the $N$ guards such that:

* each tourist attraction is guarded by at least one guard
* the total sum of the salaries is as small as possible

Since Algorel knew how to solve such problems quickly since high school, he began to ponder other aspects related to the distribution of guards. Thus, for each attraction, he wondered which guards could be assigned to guard it in optimal distributions (with the minimum sum of salaries). In other words, for each pair (guard $X$, attraction $Y$), Algorel wants to know if there is an optimal distribution in which guard $X$ guards attraction $Y$. The problem proved interesting and Algorel proposed it in this contest.

## Input data

The input file `paznici2.in` contains on the first line the natural number $N$, representing the number of guards and the number of attractions. The next $N$ lines contain $N$ numbers each: number $j$ on line $i+1$ represents the salary of guard number $i$ if they guard attraction number $j$ (both the attractions and the guards are numbered from 1 to $N$).

## Output data

The first line of the output file `paznici2.out` will contain the sum of the guards' salaries in an optimal distribution. The next $N$ lines contain information about the guards that can guard each attraction: the first number will represent the number of guards and then the ordinal numbers of these guards in ascending order. Line $i+1$ will contain information about attraction number $i$.

## Constraints and clarifications

* The guards' salaries are natural numbers in the interval $[1, 1000]$

In the table below you can find information about the 10 tests used for testing:

Test | $N$
------- | -----
1 | 7
2 | 15
3 | 19
4 | 25
5 | 30
6 | 50
7 | 80
8 | 150
9 | 170
10 | 200

## Example

`paznici2.in` 
```
3
1 1 1
1 1 1
10 10 1
```

`paznici2.out`
```
3
2 1 2
2 1 2
1 3
```

## Explanation

The optimal distributions are: $\{(1, 1), (2, 2), (3, 3)\}$ and $\{(1, 2), (2, 1), (3, 3)\}$.