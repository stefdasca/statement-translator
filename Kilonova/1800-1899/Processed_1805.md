Here's the translated statement:

---

Șimon learned yesterday at school about divisibility rules, and being a very smart student, Georgescu gave him an interesting problem that he had been pondering since his youth.

# Task

Given the set of digits $M = \\{ 1, 6, 8, 9 \\}$.

Answer $Q$ questions of the form:
How many $N$-digit numbers, formed only from the digits of the set $M$, have a remainder of $X$ when divided by $3$?

# Input data

The first line will contain the number $Q$, and the next $Q$ lines will each contain two natural numbers $N$ and $X$.

# Output data

$Q$ natural numbers will be displayed, each on a new line, representing the answer to each question, in order.

# Constraints and clarifications

* Since the answer can be very large, Șimon will only tell Georgescu the remainder of its division by $10^9 + 7$.
* $1 \\leq N \\leq 10^{18}$.
* $1 \\leq Q \\leq 100\ 000$.
* Clearly, $0 \\leq X \\leq 2$.

|#|Score|Constraints|
|-|-|--------|
|1|11|$1 \\leq N \\leq 6$|
|2|20|$X = 0$|
|3|41|$7 \\leq N \\leq 100\ 000$|
|4|28| No additional constraints |

# Example

`stdin`
```
3
2 0
3 1
5 2
```

`stdout`
```
6
21
341
```

## Explanation

For $N = 2$ and $X = 0$, the convenient numbers are: $18$, $81$, $66$, $99$, $69$, $96$.
There are $6$ numbers of $2$ digits formed from the digits of the set $M$ divisible by $3$.
The remainder of $6$ divided by $10^9 + 7$ is $6$.

---

The translated statement above preserves the original structure, format, and mathematical values, with improved grammar and syntax for clarity.