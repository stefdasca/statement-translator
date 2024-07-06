### ATTENTION
This problem is worth $150$ points. In "submissions," the maximum score is rescaled to $100$ points, but the actual score will be visible on the *[leaderboard](https://kilonova.ro/contests/179/leaderboard)*.

**The only difference between Task 1 and Task 2 is the content of the `bursa.txt` and `queries.txt` files.**

It is evident that a gigantic company like Chert And is listed on the Bucharest Stock Exchange. The stock prices vary in a very interesting way, but they give market analysts immense headaches. These analysts have collected data on stock prices at certain points in time. Help them predict the price of stocks at other points in time. In return, you will receive insights about the disaster at the farm in Romania.

~[What-is-Green-trading.jpeg|align=center|width=15cm]

$$ 
\text{fig 1. Green Trading}
$$

# Problem

You are given $N$ pairs of values $x, y$. These represent that at time $x$, a stock costs $y$ RON.

You need to provide for $Q$ values $x$, representing other points of time, an approximation of the price, $y$.

# Input

The first line of the attached file (to the right of the page under "Attachments"), `bursa.txt`, will contain the number $N$.

The following $N$ lines will contain pairs of numbers $x,y$, with the meaning described in the statement.

The first line of the attached file (to the right of the page under "Attachments") `queries.txt`, will contain the number $Q$.

The next line will contain $Q$ values $x$, with the meaning described in the statement.

# Output

The problem is *output only*.

Your submission will be a text file and must contain $Q$ values, the answers in order to the questions in the file `queries.txt`.

```
value_1
value_2
...
value_Q
```
Please display the answer with at least $3$ decimal places.

# Constraints and Clarifications

- All given values, as well as those the committee expects to receive, are in the interval $-10^9 \dots 10^9$ and are of type *double* (real numbers).

# Scoring

We define $avgDeviation = \frac{\sum_{k = 1}^{Q} |g_i - v_i|}{Q}$, and $p = \frac{|10 - min(10, avgDeviation)|}{10}$. Intuitively, this formula means that if on average your answers to the queries differ from the real answers by more than 10, you will get 0 points. Otherwise, you will gradually earn points.

Thus, the score you will receive for the problem will be: $p \cdot 150$. Additionally:

- If $p \ge 0.3$, you will receive a batch of coordinates for **META-TASK**.
- If $p \ge 0.6$, you will receive two batches of coordinates for **META-TASK**.
- If $p \ge 0.9$, you will receive three batches of coordinates for **META-TASK**.

### ATTENTION
The batches are received as a link to *Google Drive* in the evaluation test's verdict.