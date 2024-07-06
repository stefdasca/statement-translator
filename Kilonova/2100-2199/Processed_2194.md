**ATTENTION:** This problem is worth $150$ points. In "submissions" the maximum score is rescaled to $100$ points, but the true score will be visible on the *[leaderboard](https://kilonova.ro/contests/179/leaderboard)*.

**The only difference between Task 1 and Task 2 is the content of the files `bursa.txt` and `queries.txt`.**

Obviously, a giant company like Chert And is listed on the Bucharest Stock Exchange. The stock prices vary in a very interesting way, giving market analysts enormous headaches. They have collected data about stock prices at certain moments in time. Help them predict the stock prices at other moments in time. In return, you will receive insights regarding the disaster at the farm in Romania.

~[What-is-Green-trading.jpeg|align=center|width=15cm]
$$
\text{fig 1. Green Trading}
$$

# Problem

There are $N$ pairs of values $x, y$. These represent that at moment $x$, a stock costs $y$ RON.

You need to respond for $Q$ values $x$, representing other moments in time, with an approximation of the price, $y$.

# Input data

The attached file (`bursa.txt`), found on the right side of the page under "Attachments", will contain on the first line the number $N$.

On the next $N$ lines you will find pairs of numbers $x, y$, with the significance described in the statement.

The attached file (`queries.txt`), found on the right side of the page under "Attachments", will contain on the first line the number $Q$.

On the next line, you will find $Q$ values $x$, with the significance described in the statement.

# Output data

The problem is *output only*.

Your submission will be a text file and must contain $Q$ values, the answers in order to the questions from the file `queries.txt`.

```
value_1
value_2
...
value_Q
```

Please display the answer with a precision of at least $3$ decimal places.

# Constraints and clarifications

- All given values, as well as those the commission expects to receive, are in the interval $-10^9 \dots 10^9$ and are of type *double* (real numbers).

# Score

We define $avgDeviation = \frac{\sum_{k = 1}^{Q} |g_i - v_i|}{Q}$, and $p = \frac{|10 - min(10, avgDeviation)|}{10}$. Intuitively, this formula means that if on average your answers to the queries differ from the real answers by more than 10, you will receive 0 points. Otherwise, you will receive points gradually.

Thus, the score you will receive for the problem will be: $p \cdot 150$. Additionally:

- If $p \ge 0.3$, you will receive a batch of coordinates for **META-TASK**.
- If $p \ge 0.6$, you will receive two batches of coordinates for **META-TASK**.
- If $p \ge 0.9$, you will receive three batches of coordinates for **META-TASK**.

**ATTENTION:** The batches are received in the form of a link to *Google Drive* in the evaluation test verdict.
