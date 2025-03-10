**Skittlez. Taste the rainbow, solve the rainbow.**

Mr. Rainbow McRainbows is the employee of the month in the Rainbow Packing department at the Skittlez factory (being the only one working in this department).

For those who are not familiar with them, a bag of Skittlez is filled with small, round, and colorful fruit-flavored candy pieces. If you've ever wondered how they are packed and why there are never enough greens in a bag, today is your lucky day, because Mr. McRainbows will exclusively provide you with information on how Skittlez bags are filled.

# Task

The Rainbow Packing department has two components: the _bag matrix_ and the _filling machine_. The bag matrix is divided into $N$ rows (numbered from $1$ to $N$) and $N$ columns (numbered from $1$ to $N$), where each cell contains a bag that needs to be filled with candies of different colors. The filling machine is used to pour candies into the bags in the matrix and can receive commands of the following form: $(x_1, y_1, x_2, y_2, c, k)$, which indicates that in each bag in a cell $(i, j)$ with $x_1 \leq i \leq x_2$ and $y_1 \leq j \leq y_2$, the machine will pour $k$ candies of color $c$.

Mr. McRainbows has a rather boring task, his sole responsibility is to control the filling machine. At the start of each day, all bags in the matrix are empty, and his supervisors provide him with a list of commands that must be executed by the filling machine. Therefore, he decided to write a program to do this for him so he could focus on much more intellectual activities, like playing Solitaire.

Unfortunately, his supervisors started to become suspicious when they saw how much his maximum score increased (like any respectable company, Skittlez has an internal Solitaire leaderboard). Thus, they asked him to compile a report at the end of each day specifying which of the packed bags contain an overpowering color. A color is overpowering for a bag if the number of candies of that color in the bag is strictly greater than those of other colors combined.

Because he doesn't quite know how to do this and doesn't want to spend a few days trying to figure it out, he asks you to write a program to prepare the report for him. Formally, you are given the size of the bag matrix $N$ and the list of commands the machine receives in a day, and you want to obtain a matrix $B$ with the same number of rows and columns as the bag matrix where:

$$
B_{i, j} = 
\begin{cases}
c, & \text{if the overpowering color in the bag in cell $(i, j)$ is $c$,} \\
-1, & \text{otherwise.}
\end{cases}
$$

# Input data

The first line of the input data contains two positive integers $N$, the size of the bag matrix, and $Q$, the number of commands received by the machine on that day.

Each of the following $Q$ lines contains six positive integers $x_1$, $y_1$, $x_2$, $y_2$, $c$, and $k$ that describe a command. The values on each line of the input are separated by spaces.

# Output data

Print $N$ lines, each containing $N$ integers separated, representing the matrix $B$ described above.

# Constraints and clarifications

* $1 \leq N \leq 1 \ 000$
* $1 \leq Q \leq 500 \ 000$
* $1 \leq x_1 \leq x_2 \leq N$
* $1 \leq y_1 \leq y_2 \leq N$
* $1 \leq c \leq Q$
* $1 \leq k \leq 10^9$
* **Attention!** The extra spaces in the example results have been added for better visibility; you should display only one space between two consecutive values.

| # | Points | Constraints          |
| - | ------- | ------------------- |
| 1 | 7      | $N, Q \leq 20$ and $k \leq 5$ |
| 2 | 21      | There are at most $20$ different colors of candies.      |
| 3 | 44      | $N \leq 300$ and $Q \leq 100 \ 000$     |
| 4 | 28      | No additional restrictions.      |

# Example 1

`stdin`
```
5 3
1 3 5 5 3 3
2 2 4 4 1 5
1 1 3 5 1 3
```

`stdout`
```
 1  1 -1 -1 -1
 1  1  1  1 -1
 1  1  1  1 -1
-1  1  1  1  3
-1 -1  3  3  3
```

# Example 2

`stdin`
```
10 10
1 6 6 10 2 4
5 4 9 8 2 5
2 7 6 9 2 3
6 3 10 9 6 4
1 2 2 10 1 3
5 1 7 6 1 3
9 1 9 2 2 4
4 6 8 7 2 3
2 5 3 7 2 4
1 8 6 10 2 3
```

`stdout`
```
-1  1  1  1  1  2  2  2  2  2
-1  1  1  1  2  2  2  2  2  2
-1 -1 -1 -1  2  2  2  2  2  2
-1 -1 -1 -1 -1  2  2  2  2  2
 1  1  1  2  2  2  2  2  2  2
 1  1  6 -1 -1  2  2  2  2  2
 1  1  6 -1 -1  2  2  2  6 -1
-1 -1  6  2  2  2  2  2  6 -1
 2  2  6  2  2  2  2  2  6 -1
-1 -1  6  6  6  6  6  6  6 -1
