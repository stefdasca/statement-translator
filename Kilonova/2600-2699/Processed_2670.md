# Task

There are $q$ questions of the type:

For given $l$, $r$, and $k$, are there two natural numbers **not necessarily distinct** $a$ and $b$ that satisfy the following conditions?

1. $l \le a,b \le r$
2. The greatest common divisor of the numbers $a$ and $b$ is equal to $k$.

# Input data

The first line of the input file `divizorus.in` will contain the number of questions $q$.

Each of the following $q$ lines contains three numbers $l$, $r$, and $k$.

# Output data

The output file `divizorus.out` will contain $q$ digits (`0`=`NO`, `1`=`YES`), the answers to the $q$ questions.

# Constraints and clarifications
- $1 \le q \le 2 \cdot 10^5$
- $1 \le l,r,k \le 10^9$, $l \le r$.

|#|Points|Constraints                            |
|-|-------|--------------------------------------|
|1| 30    | $1 \le q,l,r,k \le 100$              |
|2| 20    | $k \le 100$                          |
|3| 20    | $k \ge 2 \cdot 10^8$                 |
|4| 30    | No additional constraints            |

# Example 1

`divizorus.in`

```
4
1 5 2
50 100 1
50 100 40
50 100 50
```

`divizorus.out`
```
1 1 0 1
```

## Explanation 

- For the first question, we have $a=2$ and $b=4$ with the greatest common divisor equal to $2$.
- For the second question, we have, for example, $a=68$ and $b=69$ with the greatest common divisor equal to $1$.
- For the third question, there are no two numbers in the given range with the greatest common divisor equal to $40$.
- For the fourth question, we have $a=50$ and $b=100$ with the greatest common divisor equal to $50$.