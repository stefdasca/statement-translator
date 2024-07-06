![cursa.png|align=right]
An electric car race equipped with solar panels is taking place on a route that traverses $n$ towns, numbered in the order on the route from $1$ to $n$. The starting line is at kilometer zero and coincides with the beginning of the first town. The finish line is at the end of the last town. Any town, except for town $1$, starts at the end of the previous town. Therefore, for each town $i$, the distance $d_i$ from the starting line to the end of the town is known, expressed in $\text{km}$.
At the beginning of the competition, there is exactly one car from each town aligned at the starting line. The cars have the same characteristics, so they move at the same speed, except when crossing their own town where, due to the advantages of their own terrain (supporters equipped with mirrors, lamps, etc.), they instantly double their speed until they exit the town, then return to the initial speed.
Local televisions are also invited to the contest, and for the viewers, the highlights are the overtakes, so it is important to remember information about them to be able to rewatch them. An overtake is considered when a car catches up with another car and then moves ahead of it.

# Task

Given the towns on the route, write a program that prints the order of arrival of the cars at the finish line, as well as information about all overtakes made during the competition.

# Input Data

The input file `cursa.in` will contain on the first line the number of towns $n$. The next $n$ lines describe information about the $n$ towns. The $i + 1$ line of the file will contain two natural numbers $c$ and $d$, separated by space, meaning that the competition number of the car from town $i$ is $c$ and that town $i$ ends at $d$ kilometers from the starting line.

# Output Data

The output file `cursa.out` will contain on the first line the competition numbers of the cars in the order of their arrival, separated by a space. In case there are multiple cars that arrive simultaneously at the finish line, they will be displayed in ascending order of their competition numbers. The following lines describe the overtakes, in ascending order of the towns in which they occur. An overtake is described by a sequence of values in the form $L \\ c \\ k \\ m_1 \\ m_2 \\ \\dots \\ m_k$, meaning that in town $L$, the car with the competition number $c$ overtakes $k$ cars, the overtaken cars being, in the order they are overtaken, $m_1, m_2, \\dots, m_k$. If two or more cars are overtaken at the same time, they will be displayed in descending order of their competition numbers.

# Constraints and clarifications

* $2 < n \leq 500$
* The competition numbers of the cars are distinct non-zero natural numbers with a maximum of $3$ digits.
* The distance between the starting line and the finish line (end of the last town) $\leq 30 \ 000$
* If the first task is solved correctly, $40\%$ of the score for the test will be obtained. If the first task is solved correctly but the cars from a town are not displayed in the requested order, $70\%$ of the score for the test is awarded. Full score is obtained for the correct resolution of both tasks.

# Example

`cursa.in`
```
5
10 5
66 7
99 15
35 23
70 34
```

`cursa.out`
```
70 35 99 10 66
3 99 2 66 10
4 35 2 66 10
5 70 4 66 10 99 35
```

## Explanation

The first town starts at km $0$ and ends at km $5$ and has car number $10$. The second town is between km $5 - 7$ and has car number $66$. The third town is between km $7 - 15$ and has car number $99$. The fourth town is between km $15 - 23$ and has car number $35$ and the last town is between km $23 - 34$ and has car number $70$.
The **order of arrival** of the cars is: $70 \\ 35 \\ 99 \\ 10 \\ 66$. Cars $35$ and $99$ finish the race at the same time, they are listed in the ascending order of their numbers.
**Overtakes**:
Town $3$: car $99$ will overtake $2$ cars, in order car $66$ then $10$.
Town $4$: car $35$ overtakes $2$ cars, $66$ and $10$, and reaches $99$ without overtaking it.
Town $5$: car $70$ overtakes $4$ cars, in order $66$, $10$, then simultaneously $99$ and $35$ at the same time (listed in descending order).