```markdown
A real estate construction company recently purchased a rectangular plot of dimensions $N \times M$. The land is divided into plots of size 1x1. Trees are planted on some of these $N \times M$ plots. The company wants to build a grandiose commercial complex and needs to clear the entire land. For this purpose, robots are used, each robot having a base of a square with side $L$. The area cleared by each robot at any given moment is precisely its coverage area, $L \times L$. Each robot enters through the top-left corner at coordinates $(1, 1)$, can only move to the right and down, and can exit only through the bottom-right corner at coordinates $(N, M)$.

# Task
Knowing the dimensions $N$, $M$ of the land and the coordinates of the plots with planted trees, determine:
1. The minimum number of robots needed to clear the entire land.
2. Answer $Q$ queries of the form $k$, where $k$ is a natural number. For each query of this form, determine the minimum side length of a robot required so that at most $k$ robots are needed for clearing.

# Input data

The input file `roboti.in` contains:
* The first line contains a natural number $p$ representing the variant of the task to be solved. For all input tests, the number $p$ can only have the value 1 or the value 2.
* The second line contains 3 natural numbers $N$, $M$, $T$ separated by a space, representing the number of rows, the number of columns of the rectangular land, and the number of planted trees, respectively.
* The next $T$ lines each contain two natural numbers $x, y$ separated by a space, representing the row and column of the plot where a tree is planted.
* In the case of task 2, the penultimate line will contain a natural number $Q$, and the last line will contain $Q$ natural numbers $k_1, k_2, ..., k_Q$ separated by a space, representing the maximum number of robots that can be used in each of the $Q$ queries.

# Output data

* If the value of $p$ is 1, only task 1 will be solved. In this case, the output file `roboti.out` will contain a single natural number $n_1$, representing the minimum number of robots used.
* If the value of $p$ is 2, only task 2 will be solved. In this case, the output file `roboti.out` will contain $Q$ lines. Each line $i$ will contain one natural number $n_i$, representing the minimum side length of a robot such that at most $k_i$ robots are used for clearing.

# Constraints and clarifications

* $2 \leq N, M, L \leq 150$;
* $1 \leq Q \leq 150$;
* $1 \leq k_i \leq 150, 1 \leq i \leq Q$;
* $1 \leq T \leq 1 \ 000$;
* The side length of the robot cannot be greater than the dimensions of the land;
* Throughout its movement, each robot will be within the boundaries of the land;
* At any moment, there will be at most one robot inside the land.

# Example 1

`roboti.in`
```
1
6 8 8
4 1
5 3
3 5
2 6
5 5
4 7
3 8
6 8
4
```

`roboti.out`
```
1
```

## Explanation

$p = 1$. If the robots have a side length of 4, only one robot is needed to clear the entire land. **Attention! Only task 1 is solved for this test.**

# Example 2

`roboti.in`
```
2
6 8 8
4 1
5 3
3 5
2 6
5 5
4 7
3 8
6 8
2
1 3
```

`roboti.out`
```
4
1
```

## Explanation

$p = 2$. The first value in the output file represents the minimum side length of the robots such that only one robot is needed for clearing the entire land according to the first query. The second value in the output file represents the minimum side length of the robots such that at most three robots are needed for clearing the entire land according to the second query. **Attention! Only task 2 is solved for this test.**
```