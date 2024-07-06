You are given an array $a$ of length $n$. You need to process $q$ queries. Each query is one of the following two types:

1. $x$ - What is the value of $a_x$ modulo $10^9+7$?
2. $x \\ y \\ b \\ c$ - For every $i$ in the range [$x, y$], $a_i$ becomes max($a_i, b \\cdot i^c$)

# Input

The first line of input contains the integer $n$, the length of the array.

The second line of the input contains $n$ integers, the $i$-th being $a_i$

The third line of the input contains an integer $q$, the number of queries.

Each of the following $q$ lines contains a query of one of two aforementioned types.

# Output

The output will contain the answers to queries of type $1$ in the order they appear in the input.

# Constraints

* $1 \leq x, y \leq n \leq 10^5$
* $1 \leq a_i, b, c \leq 10^5$
* $1 \leq q \leq 2 \cdot 10^5$
* For tests worth $5$ points, every number in the input is smaller than or equal to $10$, except for $q$ 
* For tests worth $25$ more points, $n \leq 10^3$; $q \leq 10^5$
* For tests worth $30$ more points, $n \leq 5 \cdot 10^4$; $q \leq 10^5$
* The scores obtained now may be different compared to the ones from the original contest

# Example

`stdin`
```
10
5 3 7 8 3 9 10 10 1 2
15
1 7
2 1 5 3 3
1 5
1 4
1 1
2 6 10 2 2
1 6
1 7
1 10
2 1 10 10 10
1 1
1 2
1 10
1 7
1 3
```

`stdout`
```
10
375
192
5
72
98
200
10
10240
999999307
824752476
590490
```
