# Task

After failing for the twentieth time in a row *due to a WA on test 69*, Ștefan decided to start participating in virtual competitions.

It is known that a competition has $6$ problems, and each problem is worth $500 \cdot$ the problem number in points. It is also known that for each incorrect solution, Ștefan will lose $50$ points.

Ștefan will participate in $n$ virtual competitions, and he wants to know in how many of the competitions he obtained a satisfactory score. A score is satisfactory if it is greater than or equal to one-third of the maximum possible score.

The maximum possible score is equal to the score obtained by correctly solving all $6$ problems $(500 + 1000 + 1500 + 2000 + 2500 + 3000) = 10500$ points, without any incorrect solution submitted.

# Input data

The first line contains a number $n$ representing the number of competitions Ștefan participated in.

The following $n$ lines contain two numbers, $x$ representing the encoding of problems solved by Ștefan, and $q$ representing the number of incorrect solutions submitted by Ștefan.

It is guaranteed that $x$ is a valid and non-zero encoding of the number of problems solved by Ștefan.

# Output data

The first line contains the number of satisfactory competitions Ștefan participated in.

# Constraints and clarifications

* $1 \leq n \leq 10^5$
* $1 \leq q \leq 953$

# Example

`stdin`
```
4
123456 5
3 0
123 2
56 20
```

`stdout`
```
2
```

## Explanation

The scores obtained are $10250$, $1500$, $2900$ and $4500$. Of these, two of them are satisfactory.