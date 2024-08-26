Oo

Farmer Ion has a circular farm, where $N$ hens are raised. The farm is divided into $N$ sectors, numbered from $1$ to $N$, such that any two sectors with consecutive numbers are adjacent (they are next to each other). In addition, the first and the last sector are adjacent. In each sector, there is one hen, and this hen lays a certain number of eggs each day. After the hens lay the eggs, Farmer Ion wants to collect them to eat. Because the farmer is very greedy, each time he chooses two adjacent sectors from which he simultaneously collects the eggs. Unfortunately, due to his greed, the hens in the sectors neighboring the two chosen ones get scared and become violent, so the farmer can no longer collect eggs from these sectors. In the example from the problem, if the farmer collects the eggs simultaneously from sectors $1$ and $2$, he will no longer be able to collect the eggs from sectors $3$ and $10$.

## Task

Determine the maximum number of eggs that Farmer Ion can collect, following his greedy strategy.

## Input data

The input file `oo.in` contains:
- The first line contains the number of sectors into which the farm is divided (and, implicitly, the number of hens).
- The next line contains $N$ integers in the interval $[0,100]$, representing the number of eggs laid by each hen, in the order of the sectors they are in.

## Output data

In the output file `oo.out`, you will print the maximum number of eggs Farmer Ion can collect.

## Constraints and clarifications

$2 \leq N \leq 100\,000$

## Example

`oo.in`
```
10 
3  4  0  1  0  6  7  1  2  1
```

`oo.out`
```
20
```

## Explanation

The farmer can collect the eggs from sectors $2$ and $3$ $(4+0)$, $6$ and $7$ $(6+7)$, and $9$ and $10$ $(2+1)$.