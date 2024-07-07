
In a room, there are $N$ urns. In each urn, there are $P$ balls numbered with integers. Amongst the $N \times P$ balls, there are no two balls with the same number.
For any natural number $X$ in the interval $[1, P^N]$, there exists a combination of balls, one extracted from each urn, such that the sum of the numbers on the balls equals $X$.

For example, if we have $2$ urns and in each urn $4$ balls, then the urns with contents $U1=\{6,7,10,11\}, U2=\{-5,-3,3,5\}$ allow obtaining all natural numbers in the interval $[1,16]$:
$1=6-5, 2=7-5, 3=6-3, 4=7-3, 5=10-5, 6=11-5, 7=10-3, 8=11-3, 9=6+3, 10=7+3, 11=6+5, 12=7+5, 13=10+3, 14=11+3, 15=10+5, 16=11+5$.

Another possible configuration of the urns is $\{-2,0,2,-4\}$ and $\{5,14,13,6\}$.
In the first presented solution, the maximum of the balls is $11$, whereas in the second solution, the maximum of the balls is $14$.
# Task
Given the values of $N$ and $P$, find a configuration of the urns in which **the maximum number inscribed on the balls is minimized**.

# Input data
**This problem is output-only**. You will receive $10$ files named `x-balls.in` with the values of $x$ from the set $\{0,1,2,3,4,5,6,7,8,9\}$. Each input file will contain on the first line the two natural numbers $N$ and $P$ separated by a space.

# Output data
For each input file `x-balls.in`, create the output file `x-balls.out`, which will contain $N$ lines, each line with $P$ integers separated by a space. Each line represents the content of an urn.

# Constraints and clarifications
* The numbers $N$ and $P$ are chosen such that the value $P^N$ does not exceed $1\ 000\ 000$.
* The numbers on the balls will be between $-1\ 000\ 000\ 000$ and $1\ 000\ 000\ 000$.
* The order of the urns, and respectively the order of the balls in the urns, does not matter.
* Each test is worth $10$ points.
* **Note: For each test, the corresponding `.out` file will be submitted as a separate source, selecting "Output Only" as the language**.
* A solution is worth $0$ points if the maximum value of the balls is greater than the maximum of the balls in the result of the committee.
* For each test where you find a solution better than the committee's (the maximum value of the balls being lower than that of the committee), you will be rewarded with an additional $10$ bonus points.

# Example
`x-balls.in`
```
2 4
```
`x-balls.out`
```
-6 2 -2 6
10 8 7 9
```
Explanation
---
We have $2$ urns, each containing $4$ balls.
The minimized maximum value is $10$.
If any of the examples from the task description were displayed, the test score would be $0$.
