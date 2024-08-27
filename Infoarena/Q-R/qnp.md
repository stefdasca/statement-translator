## Task

Taking a break from cleaning, Harry stumbled upon the problem of a certain little robot who is always offline... He found the technical part ready, but the statement was missing. So he created what you see here... In Dexter's laboratory, there are all sorts of things - among the troublesome ones is Dee Dee, the little genius's sister. Recently, Dexter password-protected the library entrance as follows: the computer at the library displays 11 numbers: $a_0$, $a_1$, $\dots$, $a_9$, and $K$. The person who wants to enter the laboratory must enter the $K$-th number in ascending order formed by exactly $a_0$ digits of $0$, $a_1$ digits of $1$ $\dots$ $a_9$ digits of $9$, modulo $10^9 + 7$. Dexter thinks that only he can quickly calculate the answer to $M$ such queries. Show him he is wrong by creating a program that Dee Dee will upload to her password-cracking robot, previously borrowed from the lab!

## Input data

The input file `qnp.in` will contain on the first line a natural number $M$ representing the number of queries. The next $M$ lines will contain 11 natural numbers, representing the values $a_0$, $a_1$, $\dots$, $a_9$, and $K$.

## Output data

In the output file `qnp.out`, you will print $M$ lines, each line containing a natural number representing the answer to the $i$-th query.

## Constraints and clarifications

$1 \leq M \leq 5000$

$1 \leq a_0 + a_1 + \dots + a_9 \leq 70000$

$1 \leq K \leq 10^{12}$

For tests worth 20 points,

$M \leq 50$

$a_0 + a_1 + \dots + a_9 \leq 30$

$K \leq 25000$

For tests worth an additional 20 points,

$M \leq 4000$

$a_0 + a_1 + \dots + a_9 \leq 2500$

Numbers can start with the digit $0$. It is guaranteed that a solution exists.

## Example

`qnp.in`

```
6
1 1 0 0 0 0 0 0 0 0 1
1 1 0 0 0 0 0 0 0 0 2
1 1 1 0 0 0 0 0 0 0 1
1 1 1 0 0 0 0 0 0 0 2
1 2 0 0 0 0 0 0 0 0 2
1 10 12 21 201 101
```

`qnp.out`

```
12
21
201
101
```