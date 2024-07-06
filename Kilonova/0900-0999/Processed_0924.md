Mr. Wind has placed $N$ wind turbines along the edge of a road, some of which generate electricity, while others still consume energy. He labeled the turbines with distinct natural numbers from $1$ to $N$, in the order of their positioning along the road. Each wind turbine has a screen displaying an integer, representing the amount of energy it produces (if the number is positive) or consumes (if the number is negative).

To **properly build $k$ cities** along this road, an architect must consider that:
- Each city will be assigned a group of neighboring wind turbines on the road, all groups having the same number of turbines;
- The amount of energy allocated to a city is equal to the sum of the numbers displayed on the screens of the wind turbines in the assigned group; sometimes it is possible that the obtained sum is negative;
- Each of the $N$ wind turbines must be assigned to a city;
- The imbalance factor, denoted by $P(k)$, is the maximum value of the difference between the energies allocated to any two different cities, out of the $k$.

# Task
Write a program that reads the number $N$, the values displayed on the $N$ screens of the wind turbines and solves the following two tasks:
1. Display the number $M$ of ways in which the $N$ turbines can be grouped for the proper construction of cities;
2. Display the **maximum number** $X$ of cities that can be properly built, **from those with the minimum imbalance factor**, as well as the label $E$ of the first turbine assigned to the city with the highest amount of allocated energy, among the $X$ cities; if there are more such cities, consider the one assigned turbines labeled with higher numbers.

# Input data
The input file `wind.in` contains:
- The first line contains a natural number $C$ representing the task to be solved ($1$ or $2$).
- The second line of the file contains a natural number $N$, as described in the statement.
- The third line of the file contains $N$ integers, separated by a space, representing the values displayed on the $N$ screens of the wind turbines, in the order of their positioning along the road.

# Output data
The output file `wind.out` will contain on the first line:
- if $C=1$, the natural number $M$ representing the answer to task 1;
- if $C=2$, the two natural numbers $X$ and $E$, in this order, separated by a single space, representing the answer to task 2.

# Constraints and clarifications
- $2 \leq N \leq 100\ 000$, $N$ natural number;
- The numbers displayed on the screens of the turbines are integers with at most 9 digits;
- At least 2 cities will be constructed;
- Solving task 1 will earn 20 points.
- Solving task 2 will earn 70 points. For each test of this task, you will receive $50\\ \%$ of the test score for the correct value $X$ and $50\\ \%$ of the test score for the correct value $E$. This task requires that **exactly 2 numbers appear in the output file**.

# Example 1
`wind.in`
```
1
12
2 4 -5 12 3 5 -6 4 5 7 -8 2
```
`wind.out`
```
5
```
## Explanation
The task is 1.
The wind turbines can be grouped into 1, 2, 3, 4, or 6.

# Example 2
`wind.in`
```
2
12
2 4 -5 12 3 5 -6 4 5 7 -8 2
```
`wind.out`
```
3 1
```
## Explanation
The task is 2.
Possible groupings:
- Into **a turbine/city**:
  - The sums are $2, 4, -5, \ldots, 2$;
  - $P(12) = 20 = 12-(-8)$;
- Into **2 turbines/city**:
  - The sums are $6, 7, 8, -2, 12, -6$;
  - $P(6) = 18 = 12-(-6)$;
- Into **3 turbines/city**:
  - The sums are $1, 20, 3, 1$;
  - $P(4) = 19 = 20-1$;
- Into **4 turbines/city**:
  - The sums are $13, 6, 6$;
  - $P(3) = 7 = 13-6$;
- Into **6 turbines/city**:
  - The sums are $21, 4$;
  - $P(2) = 17 = 21-4$.

Thus, the minimum imbalance factor is $P(3) = 7$, so $X=3$. For this grouping of turbines, the city with the maximum energy amount ($13$) corresponds to the first group, which starts with the turbine labeled $E=1$.