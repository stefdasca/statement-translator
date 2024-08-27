## Task

Pig Costel is playing pinball. After many hours of studying the game by repeatedly hitting the pinball table with his beak, Pig Costel believes he understands how it works. There are $N$ springs on the pinball table, which are meant to launch the ball further. Imagining a "top-down" view of the table, the spring $i$ is the $i$-th spring from left to right, i.e., horizontally. Now, the springs are also characterized by their vertical position. Specifically, the $i$-th spring has a vertical coordinate $y_i$. If the ball hits a spring $i$, it launches it towards another spring $j,\ j > i$. In this case, we say that the ball bounces from spring $i$ to spring $j$. There are two possibilities:
- bounce upwards: $y_j > y_i$, only if the last bounce was downwards.
- bounce downwards: $y_j < y_i$, only if the last bounce was upwards. 

The first bounce has no restrictions: Pig Costel launches the ball towards the first spring, and from there it bounces either upwards or downwards. The score obtained by Pig Costel for a launch is the number of springs the ball bounces off. Once it has passed the last spring, the turn is over. Pig Costel spent a lot of time calculating the maximum score he could achieve by launching the ball correctly. However, what he does not know is that hitting the table from time to time causes some springs to change their vertical coordinate. Help Pig Costel calculate the maximum score he can achieve at each moment.

## Input data

The input file `pinball.in` will contain the number $N$. The second line will contain a sequence of integers $y_1, y_2, \dots, y_N$. The third line will contain the number $Q$ and the following $Q$ lines will contain two numbers $i$ and $y$ representing an update as follows: spring $i$ acquires the vertical coordinate $y_i = y$

## Output data

The output file `pinball.out` will contain $Q + 1$ lines. The first line contains the answer for the initial state of the array. Then, we have $Q$ lines with the answer after each of the $Q$ updates.

## Constraints and clarifications

$1 \leq N \leq 10^5$

$1 \leq y_i \leq 10^9$

$1 \leq Q \leq 10^5$

$1 \leq i \leq N$

$1 \leq y \leq 10^9$

It is guaranteed that there will be no $i$ and $y_i$ such that $y_i$ appears both in the initial array and during the $Q$ operations.

## Example

`pinball.in`
```
10
1 10 2 5 6 3 4 8 9 7 
3
1 11 
7 17 
8 12
```

`pinball.out`
```
6
4
4
4
```