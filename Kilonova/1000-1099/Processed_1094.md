Here is the translated problem statement according to the specified instructions:

---

Iliuță, during a visit with his parents, receives a raffle ticket on which a natural number $S$ is written. To win a prize, Iliuță needs to find, starting from the number $S$, a winning number $X$. To help him guess the winning number, his mother tells Iliuță that the number $S$ on his ticket is the sum of the winning number $X$ and all the numbers obtained starting from the winning number $X$, by deleting the units digit of the number $X$, then, successively, by deleting the units digit of the number obtained in the previous step, until arriving at a single-digit number.

For example, if the number $X$ is $2019$, then from $X$, three numbers can be obtained according to the above rule: $201$, $20$, and $2$. The sum of all these numbers is $S$ = $2019$ + $201$ + $20$ + $2$ = $2242$. So, if a ticket holds the number $S = 2242$, then the winning number corresponding to $S$ is $X$ = $2019$.

Unfortunately, not all natural numbers allow the determination of a winning number. For example, for the number $21$, there is no natural number $X$ from which we can obtain $21$ following the rule described by Iliuță's mother.

With the help of a program, a sequence of $N$ numbers is generated automatically, numbered in the order of generation $S_1$, $S_2$, $\dots$, $S_N$. This program receives four natural numbers $A$, $B$, $C$, $D$, and the first number in the sequence $S_1$. The $i$-th generated number is obtained by the rule $S_i$ = (($S_{i-1} \% A$) $\cdot \ B + C$) $\% D$, where $1 < i \leq N$ and $a$ % $b$ represents the remainder of dividing $a$ by $b$ ($b \neq 0$).

# Task

Given the natural numbers $N$, $S_1$, $A$, $B$, $C$, $D$, write a program that solves the following tasks:

1. For each term of the sequence $S_1$, $S_2$, $\dots$, $S_N$, determine the largest natural number strictly less than that term for which a winning number exists; the program will display the remainder of the sum of the obtained numbers at $10^{18}$ + $31$.
2. For each term of the sequence $S_1$, $S_2$, $\dots$, $S_N$, determine how many natural numbers less than or equal to that term do NOT have a winning number; the program will display the remainder of the sum of the obtained results at $10^{18}$ + $31$.

# Input data

The input file `tombola.in` contains:

- The first line contains the natural number $p$, representing the task that needs to be solved ($1$ or $2$).
- The second line contains the natural numbers $N$, $S_1$, $A$, $B$, $C$, $D$, in this order, separated by a space.

# Output data

The output file `tombola.out` will contain a single natural number that represents the result of task $p$.

# Constraints and clarifications

* $1 \leq N \leq 500 \ 000$ 
* $1 < S_1, C, D \leq 10^{17}$ 
* $1 < A, B \leq 10^9$
* It is guaranteed that $S_i$ > $1$, for any $1 \leq i \leq N$
* For tests worth $50$ points, the task is $1$
* For $30\%$ of the total number of tests, $N \cdot D \leq 10^6$ and $N \cdot S_1 \leq 10^6$ ($50\%$ of these being for task $1$) 
* For $60\%$ of the total number of tests, $N \leq 30 \ 000$ ($50\%$ of these being for task $1$).

# Example 1

`tombola.in`
```
1
1 22 3 3 3 3
```

`tombola.out`
```
20
```

## Explanation

Task $1$ is solved. We have a single term in the sequence $S_1 = 22$. The number $20$ is the largest number strictly less than $22$ that allows a winning number ($X$ = $19$ because $20$ = $19$ + $1$).

# Example 2


`tombola.in`
```
2
1 22 3 3 3 3
```

`tombola.out`
```
2
```

## Explanation

Task $2$ is solved. We have a single term in the sequence $S_1 = 22$. There are two numbers less than or equal to $22$ that do NOT allow a winning number, $10$ and $21$.

# Example 3


`tombola.in`
```
1
3 12345678901234567 999999999 123456789 98765432109876543 1020304050607080
```

`tombola.out`
```
12805467424792840
```

# Example 4


`tombola.in`
```
2
3 98765432109876543 999999999 123456789 12345678901234567 1020304050607080
```

`tombola.out`
```
9912065223185559
```

---