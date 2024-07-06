> "Are you thinking about Maricica again?"

Maricica is a diligent and extremely beautiful girl, but despite her efforts in math, she cannot get a good grade. Recently, her math teacher taught a new chapter entitled divisibility, more precisely, the greatest common divisor of some given numbers, previously teaching them the sum of the numbers, and promises that he can give them a test from both chapters to change her grade. However, she is already overwhelmed with studying other subjects, such as Romanian, so she asks you to help her solve the test. If you help her, she will reward you with one hundred points.

# Task
The test has two exercises:
1. Given $N$ and $N$ natural numbers, find the greatest common divisor of the given $N$ numbers.
2. Given $N$, $Q$, then $N$ natural numbers $a_1, a_2, a_3, \ldots, a_N$, and $Q$ questions in the form $[l, r]$ where $1 \le l \le r \le N$, find the sum of the numbers $a_l$, $a_{l+1}$, $a_{l+2}$, \ldots, $a_r$ for each question.

# Input data
The input file will contain $C$ representing the number of the exercise on the first line.

If $C = 1$, then the second line will contain a number $N$ and the third line will contain $N$ natural numbers.

In case $C = 2$, then the second line will contain a number $N$, the third line will contain $N$ natural numbers followed by the next line with $Q$ representing the number of questions followed by $Q$ more lines in the form $[l,r]$ where $1 \le l \le r \le N$.

# Output data
If $C = 1$, then the output file will contain a single number on the first line, the greatest common divisor of the given $N$ numbers. If $C = 2$, then print, on separate lines, the answer to the $Q$ questions.

# Constraints and clarifications
- $1 \le N \le 100\ 000$
- $0 \le a_i \le 10^9$
- $1 \le Q \le 10\ 000$
- The first task is worth $30$ points.
- The second task is worth $70$ points.
- For tests worth $5$ points, $0 \le a_i \le 10^5$ and $C = 1$.
- For tests worth $20$ points, $1 \le N \le 1\ 000$ and $C = 2$.
- For tests worth $70$ points, $0 \le a_i \le 10^5$ and $C = 2$.

# Example 1
`maricica.in`
```
1
5
2 4 10 6 8
```
`maricica.out`
```
2
```

# Example 2
`maricica.in`
```
2
5
2 4 10 6 8
3
2 4
1 5
3 5
```
`maricica.out`
```
20
30
24
```
