Lensu finished the 9th grade with an average of 9.49 in mathematics and computer science. He was very eager to achieve an average of 10, because otherwise, he would not get a scholarship next year, so he proposed the following to his math and computer science teacher, Marlena:
``` - If you give me an average of 10 for the year 2022-2023, I will solve any problem you want during the summer vacation!```
The teacher responds by telling him that, in case he doesn't succeed, she will give him a grade of 2 next year. Lensu, being ambitious, accepts the condition.

# Task

The teacher's problem is the following:
Consider the following expression:

# $E(x) = \frac{x^4 - 3x^3 - 2x^2 + 5}{1000} + 10$

and $Q$ numbers $K$.

For how many natural numbers $x$, $4 \leq x \leq 10\ 000$, does the inequality $E(x) \leq K$ hold?

Help Lensu solve this problem and you will be rewarded with 100 points and 100 IQ.

# Input data

The first line contains the number $Q$ and the next $Q$ lines contain one natural number $K$ each.

# Output data

Print $Q$ natural numbers, one per line, representing the answer for each number $K$ in order.

# Constraints and clarifications

* It is guaranteed that there is at least one natural number x that satisfies the relationship;
* $K$ can be represented on 64 signed bits.
* $4 \leq x \leq 10\ 000$;
* $1 \leq Q \leq 100\ 000$;
* For 30 points, $4 \leq x \leq 100$.

# Example

`stdin`
```
3
12 
100
11
```

`stdout`
```
4
15
3
```

## Explanation

For the first number $K = 12$, there are 4 numbers $4 \leq x$ that satisfy the inequality $E(x) \leq  K$.