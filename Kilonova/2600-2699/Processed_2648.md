
Andra has a package with $n$ types of chocolate balls, each type $i$ having $c_i$ balls. The number of $c_i$ depends on four factors, denoted by $x$, $y$, $z$, $t$, and is calculated as follows:

* $c_1 = x$
* $c_i = (c_{i-1} \cdot y)\\ \%\\ t + z$, $\forall i$, $2 \leq i \leq n$

where $a\\ \%\\ b$ denotes the remainder of the natural number $a$ when divided by the nonzero natural number $b$.

Andra wants to use all the balls to build pyramids, each consisting of one or more rows, numbered starting from $1$. For each pyramid, in row $i$, there are $2^{i-1}$ balls. For example, in row $8$ of a pyramid, there are $2^7 = 128$ chocolate balls. Each row of a pyramid contains one or more types of balls, and the same type of balls can be used in multiple rows. Among the pyramids that can be formed, the *serious* ones contain only one type of balls per row.

# Task

Using all the balls, help Andra determine:
1) The minimum number of chocolate pyramids she can form.
2) The minimum number of *serious* chocolate pyramids she can form, such that all obtained pyramids are of this kind.

# Input data

The input file `mandms.in` contains on the first line the number $p$, which can either be $1$ or $2$.

The second line of the file contains the natural number $n$, with the significance described in the statement.

The third line contains the natural numbers $x$, $y$, $z$, $t$, in this order, with the significance described in the statement.

# Output data

If $p = 1$, the output file `mandms.out` contains a natural number, representing the value specified in Task 1.

If $p = 2$, the output file `mandms.out` contains a natural number, representing the value specified in Task 2.

# Constraints and clarifications

* $1 \leq n \leq 2\ 000\ 000$
* $1 \leq x, y, t < 2^{64}$
* $0 \leq z < 2^{64}$
* $1 \leq c_i < 2^{64}$
* $0 \leq c_i \cdot y < 2^{64}$, $\forall i$, $2 \leq i \leq n$

| #  | Points | Constraints |
|----|--------|-------------|
| 1  | 30     | $p = 1$, $n \leq 1\ 500\ 000$, the total number of balls is strictly less than $2^{64}$ |
| 2  | 10     | $p = 1$, $n \leq 1\ 500\ 000$ |
| 3  | 40     | $p = 2$, $n \leq 100\ 000$ |
| 4  | 20     | $p = 2$ |

# Example 1

`mandms.in`
```
1
8
3 15 18 17
```

`mandms.out`
```
5
```

## Explanation

$x = 3$, $y = 15$, $z = 18$, $t = 17$

The number of balls of the $8$ types are calculated as follows:
* $c_1 = x = 3$
* $c_2 = (3 \cdot 15)\\ \%\\ 17 + 18 = 29$
* $c_3 = (29 \cdot 15)\\ \%\\ 17 + 18 = 28$
* $c_4 = (28 \cdot 15)\\ \%\\ 17 + 18 = 30$
* $c_5 = (30 \cdot 15)\\ \%\\ 17 + 18 = 26$
* $c_6 = (26 \cdot 15)\\ \%\\ 17 + 18 = 34$
* $c_7 = (34 \cdot 15)\\ \%\\ 17 + 18 = 18$
* $c_8 = (18 \cdot 15)\\ \%\\ 17 + 18 = 33$

The minimum number of pyramids that can be formed is $5$.

A possible configuration of the pyramid is the following:
~[mms1.png|width=85em]

In this configuration, we have one pyramid with $7$ rows, one with $6$ rows, one with $3$ rows, one with $2$ rows, and one with a single row.

# Example 2

`mandms.in`
```
2
8
3 15 18 17
```

`mandms.out`
```
7
```

## Explanation

$x = 3$, $y = 15$, $z = 18$, $t = 17$

The number of balls of the $8$ types are calculated as follows:
* $c_1 = x = 3$
* $c_2 = (3 \cdot 15)\\ \%\\ 17 + 18 = 29$
* $c_3 = (29 \cdot 15)\\ \%\\ 17 + 18 = 28$
* $c_4 = (28 \cdot 15)\\ \%\\ 17 + 18 = 30$
* $c_5 = (30 \cdot 15)\\ \%\\ 17 + 18 = 26$
* $c_6 = (26 \cdot 15)\\ \%\\ 17 + 18 = 34$
* $c_7 = (34 \cdot 15)\\ \%\\ 17 + 18 = 18$
* $c_8 = (18 \cdot 15)\\ \%\\ 17 + 18 = 33$

The minimum number of *serious* pyramids that can be formed, such that all the obtained pyramids are *serious*, is $7$.

A possible configuration of the pyramid is the following:
~[mms2.png|width=70em]

In this configuration, we have two pyramids with $6$ rows, two with $5$ rows, one with $3$ rows, and two with $2$ rows.
