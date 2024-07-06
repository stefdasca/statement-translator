Here is the translated and adjusted problem statement:

---

The plumber Mario has set out in search of Princess Peach. Before reaching Bowser's Castle, where the princess was held prisoner, Mario collected $N$ magic coins. Each coin, numbered from $1$ to $N$, has a certain value, with the $i$-th coin having a value of $m_i$ ($1 \leq i \leq N$).

Upon reaching the Castle, Mario met Bowser, who proudly possessed an impressive collection of coins, numbered from $1$ to $M$, with the $i$-th coin having a value of $b_i$ ($1 \leq i \leq M$).

In the final confrontation, Bowser offers Mario the chance to save Peach only if he manages to make the necessary exchanges between their coins, such that the smallest $N$ coins are in Mario's possession and the largest $M$ values are in Bowser's possession. **The number of exchanges must be minimal.**

# Task

Write a program that allows Mario to save Peach.

# Input data

The input file `mario.in` contains the following:
- The first line contains the number $N$, representing the number of coins found by Mario.
- The next line contains the $N$ values of the coins found by Mario, separated by a space.
- The third line contains the number $M$, the number of coins Bowser has.
- The last line contains the $M$ values of Bowser's coins, separated by a space.

# Output data

The first line of the output file `mario.out` will contain the number $k$ of exchanges between the two sets of coins. The following $k$ lines contain the exchanges, with each line containing two natural values $m\ b$ meaning "the coin with order number $m$ among Mario's coins will be exchanged with the coin with order number $b$ among Bowser's coins."

# Constraints and clarifications

* $1 \leq N, M \leq 1\ 000$
* The values in each box are $\leq 10\ 000$.
* The solution is not unique.
* Correctly determining $k$ gives $40\%$ of the score, while correctly determining the exchanges gives $60\%$.

# Example

`mario.in`
```
6
3 1 7 4 6 2
2
4 5
```

`mario.out`
```
2
3 1
5 2
```

## Explanation

There will be two coin exchanges, specifically the coin with order number $3$ among Mario's coins will be exchanged with the coin with order number $1$ among Bowser's coins, then the $5$-th coin will be exchanged with the $2$-th coin.

It is observed that the following solution is also correct:
```
2
3 2
5 1
```

---