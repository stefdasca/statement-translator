## Task

A group of students is going on vacation to the island of Tenerife. They want to have fun but also spend as little money as possible. The island of Tenerife consists of $N$ clubs and $M$ unidirectional roads. Each road is given by $X$, $Y$, and $C$, meaning you can travel from club $X$ to club $Y$ with a cost of $C$, but not vice versa. Since the island is built in such a way that people do not get bored, you cannot return to the starting club by traveling on the roads. A trip consists of multiple clubs $X_1$, $X_2$, $\dots$, $X_p$, $p \geq 2$, such that there is a road from $X_1$ to $X_2$, from $X_2$ to $X_3$, $\dots$, from $X_{p-1}$ to $X_p$, and the cost of such a trip is the greatest common divisor of $(K, \text{cost of the road from } X_1 \text{ to } X_2, \text{cost of the road from } X_2 \text{ to } X_3, \dots, \text{cost of the road from } X_{p-1} \text{ to } X_p)$. Since the students do not have a lot of money, they want to take trips with a cost equal to $1$. Help the students and calculate the number of different trips that have a cost equal to $1$. Since this number can be very large, you should output it modulo $1000000007$.

## Input data

The input file `tenerife.in` contains on the first line $N$, $M$, and $K$. The next $M$ lines each contain 3 numbers, $X$, $Y$, and $C$, indicating that there is a directed edge from club $X$ to club $Y$ with a cost of $C$.

## Output data

The output file `tenerife.out` will print the number of different trips that have a cost equal to $1$ modulo $1000000007$.

## Constraints and clarifications

$1 \leq N \leq 50000$

$1 \leq M \leq 100000$

$1 \leq C, K \leq 10^9$

A trip must have at least $2$ clubs

For $10\%$ of the score $N \leq 1000$ and the graph will be in the form of a directed chain in one direction.

For another $10\%$ of the score $K = 1$.

For another $10\%$ of the score $K$ is a prime number.

For another $20\%$ of the score $K \leq 5000$.

For another $50\%$ of the score, the initial constraints.

## Example

tenerife.in
```
7 7 66
1 3 2
2 3 3
3 4 6
3 5 5
5 6 7
4 6 35
7 5 15
```

tenerife.out
```
12
```

## Explanation

For the first example: The trips that have a cost equal to $1$ are:

1) $3 \to 5$

2) $5 \to 6$

3) $4 \to 6$

4) $1 \to 3 \to 5$

5) $2 \to 3 \to 5$

6) $3 \to 5 \to 6$

7) $3 \to 4 \to 6$

8) $7 \to 5 \to 6$

9) $1 \to 3 \to 4 \to 6$

10) $1 \to 3 \to 5 \to 6$

11) $2 \to 3 \to 5 \to 6$

12) $2 \to 3 \to 4 \to 6$