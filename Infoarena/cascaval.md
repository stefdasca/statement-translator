## Task

A cheese-producing company (and other dairy products) wants to plan its production for the next $N$ months. For each month $i$, the company knows the cheese demand $D_i$, expressed in kilograms. It is also known that the cost to produce $Q$ $(Q > 0)$ kilograms of cheese in month $i$ is equal to $F_i + C_i \cdot Q$ ($F_i$ represents fixed costs, and $C_i$ represents variable costs). The cost to produce $0$ kilograms of cheese is $0$. The company can store part of the cheese produced in a certain month to use it for fulfilling the demand in a subsequent month. The cost of storing one kilogram of cheese in each month $i$ (until the beginning of the next month) is $S_i$. The company wants to fully meet the demand every month, paying the lowest possible total cost. The total cost is equal to the sum of production costs and storage costs for each of the $N$ months.

## Input data

The first line of the input file `cascaval.in` contains the natural number $N$, representing the number of months. The $i$-th of the following $N$ lines contains 4 integers, $F_i$, $C_i$, $S_i$, and $D_i$, separated by a space, having the meanings specified in the statement.

## Output data

In the output file `cascaval.out` you will print the minimum total cost that the company must pay to fully meet the cheese demand for each month.

## Constraints and clarifications

$1 \leq N \leq 100\,000$

$0 \leq F_i \leq 1\,000\,000\,000$

$0 \leq C_i \leq 1\,000\,000$

$0 \leq S_i \leq 100$

$0 \leq D_i \leq 1000$

Cheese can be stored for any number of months (it does not spoil).

## Example

`cascaval.in`
```
4
4 3 2 1
3 2 1 4
2 1 4 3
1 4 3 2
```

`cascaval.out`
```
32
```