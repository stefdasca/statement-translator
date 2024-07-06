# Task

Tommaso would like to buy a new computer but unfortunately, he doesn't have enough money. So he decided to try his luck and buy some lottery tickets.

The lottery tickets are numbered, and one of his friends told him the secret to win the lottery: in a winning ticket the sum of the digits of the ticket number is exactly $N$ and the ticket number does not contain $3$ consecutive equal digits.

When Tommaso arrived at the lottery shop, he saw that some tickets were already sold. The current ticket number is $S$ and Tommaso must buy the tickets in order (first ticket number $S$, then ticket number $S+1$, then ticket number $S+2$, and so on).

He wants to buy some tickets until he finds a winning one. Note that it is possible that Tommaso is not able to buy a winning ticket.

What is the number of the winning ticket bought by Tommaso?

Help Tommaso to find the answer in $T$ different scenarios.

# Input data

The first line contains a single integer $T$ ($1 \le T \le 200$), denoting the number of test cases.

The following $T$ lines contain $2$ integers: $N$ and $S$ ($1 \le N \le 80\ 000$), ($1 \le |S| \le 10\ 000$).

For tests worth $30$ points, $N \le 32$ and the length of each $S$ does not exceed $4$.

For tests worth $30$ more points, $N \le 2\ 000$ and the length of each $S$ does not exceed $300$.

# Output data

You need to write $T$ lines with an integer: the number of the winning ticket bought by Tommaso, or $-1$ if he cannot buy one.

# Example 1

`stdin`
```
4
7 502
1 123
10 99
16 4440
```

`stdout`
```
502
-1
109
4453
```

# Explanation

In the **first sample case**:

In the first test, Tommaso can buy the first ticket since it is a winning ticket.

In the second test case, Tommaso cannot buy any winning ticket. Note that the ticket number $1000$ is not a winning ticket since it contains three consecutive $0$.