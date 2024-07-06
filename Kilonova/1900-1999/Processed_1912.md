> "legit checkers are impossible for this"

Well, Traian needed more problems for the contest, so he thought to provide this one.

# Task

Traian thought of $t$ sequences of $n$ numbers each (for each sequence, the number $n$ is not necessarily the same) and also thought of a number $m$ for each sequence (again, $m$ is not necessarily the same everywhere). He wants you to tell him a number that is divisible by every number in the sequence and has exactly $m$ digits.

# Input data

The first line will contain the number $t$, representing the number of sequences. On the $2 \\cdot i$-th line will contain the numbers $n$ and $m$. On the $2 \\cdot i + 1$-th line will contain the $n$ numbers from the sequence.

# Constraints and clarifications

* $1 \\leq n \\leq 2 \\cdot 10 ^ 5$
* $1 \\leq m \\leq 10 ^ 5$
* The sum of the numbers $n$ does not exceed $2 \\cdot 10 ^ 5$
* The sum of the numbers $m$ does not exceed $10 ^ 5$
* The sought number exists for any of the $t$ sequences.
* We denote the sequence by $a$
* $1 \\leq a_i \\leq 10 ^ 9 \\ (1 \\leq i \\leq n)$
* $1 \\leq a_1 \\cdot a_2 \\cdot ... \\cdot a_n \\leq 10 ^ 9$

# Example 1

`stdin`
```
9
4 11
113 158 170 96 
5 10
22 18 6 30 6 
11 9
4 6 5 4 5 3 6 4 5 4 3 
6 11
28 9 9 25 6 17 
3 10
565 623 621 
11 9
2 4 2 3 3 5 4 3 4 4 6 
3 10
920 274 410 
10 11
3 1 5 7 1 3 5 2 4 7 
4 9
30 90 40 26 
```

`stdout`
```
10052516160
6000005880
100000020
80000272800
1092944475
900000180
3007566480
50000000400
100002240
```

## Explanation

I don’t know, check them!