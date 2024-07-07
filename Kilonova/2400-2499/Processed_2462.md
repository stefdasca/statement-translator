# Task

Gigel is participating in a contest. To tell you what kind of contest it is, you need to solve the following problem:
You are given $2$ intervals of integer numbers $a, a + 1, ..., b$ and $c, c + 1, ..., d$. Determine if the product $c \cdot ( c + 1 ) \cdot ... \cdot d$ is divisible by the product $a \cdot ( a + 1 ) \cdot ... \cdot b$.

# Input data

The first line of the input file `concurs.in` contains an integer $t$, representing the number of independent tests.
Each of the next $t$ lines contains $4$ natural numbers $a_i$, $b_i$, $c_i$, $d_i$.

# Output data

You need to print $t$ lines, one for each test. On the $i^{th}$ line of the output file `concurs.out`, print `YES` if $c_i \cdot ( c_i + 1 ) \cdot ... \cdot d_i$ is divisible by $a_i \cdot ( a_i + 1 ) \cdot ... \cdot b_i$, otherwise print `NO`.

# Constraints and clarifications

* $1 \leq t \leq 10$
* $1 \leq a_i, b_i, c_i, d_i \leq 10\ 000\ 000$
* $a_i \le b_i$ and $c_i \le d_i$
* For tests worth $10$ points, the numbers are at most $50$.
* For tests worth another $20$ points, the numbers are at most $1\ 000$.
* For tests worth another $10$ points, $a_i$ = 1.

# Example 1

`concurs.in`
```
2 
9 10 3 6 
2 5 7 9
```

`concurs.out`
```
YES
NO
```

## Explanation

We have $9 \cdot 10 = 90$ and $3 \cdot 4 \cdot 5 \cdot 6 = 360$. The answer is *YES* because $90$ divides $360$.
In the second test, $2 \cdot 3 \cdot 4 \cdot 5 = 120$, which does not divide $7 \cdot 8 \cdot 9 = 504$, so the second answer is *NO*.

# Example 2

`concurs.in`
```
6
1 2 3 4 
1 4 2 3 
2 3 1 4 
1 3 2 4 
19 22 55 57 
55 57 19 22
```

`concurs.out`
```
YES 
NO 
YES
YES
YES
YES
