**ATTENTION:** This problem is worth $150$ points. In the "submissions," the maximum score is rescaled to $100$ points, but the actual score will be visible on the *[leaderboard](https://kilonova.ro/contests/179/leaderboard)*.

The digital pesticide management system in Chert And heavily relies on the following hash function for handling data traffic:

```cpp
long long hashFunction(long long x) {
  long long Hash = x;
  Hash += (Hash << 10);
  Hash ^= (Hash >> 6);
  Hash += (Hash << 3);
  Hash ^= (Hash >> 11);
  Hash += (Hash << 15);

  return Hash & ((1ll << 42) - 1);
}
```
*The function is written in C++ and uses the bitwise operations [xor](https://en.wikipedia.org/wiki/Exclusive_or) and [bit shifts right/left](https://en.wikipedia.org/wiki/Bitwise_operation#Bit_shifts).*

Find as many values $y$ (with the condition $y \le 2 \ 000 \ 000$) that are the hash of more than two values $x$ from the interval $1...36987 \cdot 10^7$. Formally, find as many values $y$ such that the set $\\{x | hashFunction(x) = y, 0 \le y \le 2 \ 000 \ 000, 1 \le x \le 36987 \cdot 10^7\\}$ has a cardinality of at least $2$.

# Task

This problem is *output only*.

On the first line, your submission must contain the number **$k$** of numbers you report.

On the next line, your submission must contain **$k$** **distinct values** that meet the condition stated in the problem.

Below is an example submission:
```
3
1590155 872696 560605
```

# Score

We define: $\\text{accuracy} = \\frac{\\text{reported}}{\\text{total}}$, where $reported$ is the number of **distinct** numbers you report, and $total$ is the total number of $y$ that meet the condition.

Then, the score you will receive for the problem will be: $accuracy \cdot 150$. Additionally:

- If $\\text{p} \ge 0.2$, you will receive a batch of coordinates for the **META-TASK**.
- If $\\text{p} \ge 0.5$, you will receive two batches of coordinates for the **META-TASK**.
- If $\\text{p} \ge 0.95$, you will receive three batches of coordinates for the **META-TASK**.

**ATTENTION:** Batches are received as a link to the *attachment* in the evaluation test's verdict.
**ATTENTION: If you report a $y$ that does not meet the condition, your score will be null.**