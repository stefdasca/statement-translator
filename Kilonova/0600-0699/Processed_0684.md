At the computer science contest in Strehaia, participants received $n$ problems to solve. Since the committee wants the scores to be as diverse as possible, the contest organizers decided to calculate the number of distinct scores that can be obtained at the contest.

# Task

Given the number $n$ of problems and for each problem a number $m$ followed by $m$ natural numbers, representing the number of tests of problem $i$ ($1 \le i \le n$), respectively the score of each test, determine the number of distinct scores that can be obtained at the contest.

# Input data

The first line contains the number $n$ of problems in the contest.

The following $n$ lines each contain a number $m$ followed by $m$ numbers, representing the number of tests, respectively the score for each test.

# Output data

The first line will contain a single number, representing the number of distinct scores that can be obtained at the contest in Strehaia.

# Constraints and clarifications

* $1 \leq n \leq 10\ 000$
* $1 \leq$ score of a test $\leq 100$
* For each problem, the sum of the test scores will be $100$.
| # | Score | Constraints            |
| - | ----- | ----------             |
| 1 | 30    | $1 \leq n \leq 20$     |
| 2 | 30    | $1 \leq n \leq 1\ 000$ |
| 3 | 40    | No other constraints   |

# Example 1

`stdin`
```
2
2 30 70
2 10 90
```

`stdout`
```
15
```

## Explanation

Participants can obtain the following scores:

$0 + 0 = 0$

$0 + 10 = 10$

$30 + 0 = 30$

$30 + 10 = 40$

$70 + 0 = 70$

$70 + 10 = 80$

$0 + 90 = 90$

$100 + 0 = 100$

$100 + 10 = 110$

$30 + 90 = 120$

$30 + 100 = 130$

$70 + 90 = 160$

$70 + 100 = 170$

$100 + 90 = 190$

$100 + 100 = 200$

# Example 2

`stdin`
```
3
1 100
3 38 12 50
4 93 2 2 3
```

`stdout`
```
137
