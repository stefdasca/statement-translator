Natural numbers $N$ and $K$ and distinct non-zero digits $c_1, c_2, \dots, c_N$ are given.

# Task

Determine how many $K$-digit numbers formed only with the digits $c_1, c_2, \dots, c_N$ are divisible by $3$. Because this number can be very large, the result will be determined $\text{mod }4\ 001$.

# Input data

The file `div3.in` contains the natural numbers $N$ and $K$ separated by a space on the first line, and on the second line the $N$ distinct digits $c_1, c_2, \dots, c_N$ separated by a space

# Output data

The file `div3.out` will contain a single line with a single natural number, representing the number $\text{mod }4\ 001$ of $K$-digit numbers formed only with the digits $c_1, c_2, \dots, c_N$ and divisible by $3$.

# Constraints and clarifications

* $1 \leq N \leq 9$
* $2 \leq K \leq 1\ 000$
* $1 \leq c_1, c_2, \dots, c_N \leq 9$
* We define $x\text{ mod }4\ 001$ as the remainder of the integer division of $x$ by $4\ 001$. For example, $4\ 002$ modulo $4\ 001$ is $1$.
* Properties:
	* $(a + b)\text{ mod }4\ 001 = (a\text{ mod }4\ 001 + b\text{ mod }4\ 001)\text{ mod }4\ 001$.
	* $(a * b)\text{ mod }4\ 001 = (a\text{ mod }4\ 001 * b\text{ mod }4\ 001)\text{ mod }4\ 001$.

# Example

`div3.in`
```
3 2
1 3 2
```

`div3.out`
```
3
```
	
## Explanation

You need to determine the number of $K = 2$ digit numbers formed only from the digits $1$, $2$ and $3$ that are divisible by $3$. There are $3$ such numbers, namely: $12$, $21$, $33$. The result of $3$ divided by $4\ 001$ gives a remainder of $3$.