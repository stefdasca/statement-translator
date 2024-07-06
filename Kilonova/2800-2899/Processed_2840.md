# New York Stock Exchange

On the New York Stock Exchange, also known as NYSE, there is only one type of stock that can be traded. The daily price of such a stock is known for a period of $N$ consecutive days: $p_i$ represents the price of a stock on day $i \\ (1 \\leq i \\leq N )$, expressed in dollars.

William follows what happens on the stock exchange, and every day $i$ he can trade at most $L_i$ stocks in total. Therefore, if on day $i$ he sells $S$ stocks (at the price of $p_i$ dollars each) and buys $B$ stocks (at the price of $p_i$ dollars each), the inequalities must be respected: $0 \\leq S$, $0 \\leq B$ and $0 \\leq S + B \\leq L_i$. Additionally, the numbers $S$ and $B$ must be natural numbers. **Attention: William does not need to own at least one stock to be able to sell one**. For example, it is possible that the first trade William makes is to sell one (or more) stock(s).

For any $i$, we say that by the end of day $i$, William has closed his positions if the number of stocks bought in the first $i$ days is equal to the number of stocks sold in the first $i$ days (including any transactions made on day $i$). Following a series of transactions, the profit is equal to the difference between the total amount of dollars obtained from selling stocks and the total amount of dollars used for buying stocks. William needs to answer, in order, $Q$ questions in the form: considering a natural value $x$, determine the minimum index of a day $j \\ ($where $1 \\leq j \\leq N )$, such that after a series of transactions on days $1$, $2$, ..., $j$, the profit obtained is at least $x$ dollars, and he has closed his positions by the end of day $j$.

If there is no such index $j$, then it is considered that $j = -1$. William knows from the beginning of the first day the prices for the whole period of $N$ days, so he can optimally plan his trades, depending on each question received.

# Task

Write a program that, knowing $N$, the daily price of a stock for the $N$ days, as well as the daily trading limits, correctly answers $Q$ questions of the described form. The $Q$ questions are independent of each other, meaning that for each question, a different series of transactions can be chosen to result in the smallest value of $j$, if it exists (when $j \\neq -1$).

# Input data

The input file `nyse.in` contains on the first line the natural number $N$. The next line contains $N$ natural numbers, representing, in order: $p_1$, $p_2$, ..., $p_N$. The next line contains $N$ natural numbers, representing, in order: $L_1$, $L_2$, ..., $L_N$. The next line contains the natural number $Q$. The following $Q$ lines contain the questions, one question per line. A line representing a question contains a single natural number $x$, as described above. The numbers on the same line of the input file are separated by a space.

# Output data

The output file `nyse.out` contains $Q$ lines. On the $k$-th line is the answer to the $k$-th question described in the input file (where $1 \\leq k \\leq Q$).

# Constraints and clarifications

* $1 \\leq N \\leq 900\,000$ and $1 \\leq Q \\leq 100\,000$.
* $1 \\leq p_i \\leq 1\,000\,000\,000$ and $0 \\leq L_i \\leq 1\,000$, for each $i$: $1 \\leq i \\leq N$.
* $0 \\leq x \\leq 10^{18}$, for each of the $Q$ questions.
* Each day, William also has the option of not making any trades.

| # | Score | Constraints |
| - | - | - |
| 1 | 4 | $p_1 = p_2 = ... = p_N$ |
| 2 | 12 | $N \\leq 1\,000$ and $L_1 = L_2 = ... = L_N = 1$ |
| 3 | 17 | $N \\leq 1\,000$ |
| 4 | 11 | max$(p_1, p_2, ..., p_N)$ $-$ min$(p_1, p_2, ..., p_N) \\leq 25$ |
| 5 | 18 | $99\,000 \\leq N \\leq 100\,000$ |
| 6 | 14 | $N > 100\,000$ and $L_1 = L_2 = ... = L_N = 1$ |
| 7 | 24 | No additional constraints |

# Example 1

`nyse.in`
```
2
10 5
3 3
1
14
```

`nyse.out`
```
2
```

## Explanation

The price of the stock is known for a period of two consecutive days $(N = 2)$. On the first day, a stock is worth $p_1 = 10$ dollars, and on the second day, a stock is worth $p_2 = 5$ dollars. Both on the first day and on the second, at most three stocks $(L_1 = L_2 = 3)$ can be traded.
We have to answer a single question $(Q = 1)$, for which $x = 14$.
In the question, William chooses to sell three stocks (at the price of $10$ dollars each) on the first day and then buy three stocks (at the price of $5$ dollars each) on the second day. Thus, at the end of the second day, the number of stocks bought is equal to the number of stocks sold, namely three, so William has closed his positions.
The maximum profit obtained after the first two days is: $3 \cdot 10 - 3 \cdot 5 = 15$ dollars.

# Example 2

`nyse.in`
```
5
10 1 20 21 25
1 1 1 1 1
1
20
```

`nyse.out`
```
4
```

## Explanation

The maximum profit that can be obtained at the end of the fifth day is $35$ dollars.

# Example 3

`nyse.in`
```
5
10 12 5 113 343
1 2 3 2 1
4
0
1000
345
21
```

`nyse.out`
```
1
-1
5
4
```

## Explanation

The maximum profit that can be obtained at the end of the fifth day is $556$ dollars.