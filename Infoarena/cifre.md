Cifre

Eugenia often asks Zaharel difficult questions, not because she doesn't know the answer, but because she wants to see how insightful Zaharel is. Sometimes she exaggerates and her questions are very tough, even for Zaharel; that's when he will ask for your help! Today, Eugenia asked Zaharel the following question: "I am thinking of an integer in the range $[A \dots B]$, what is the probability that the number I am thinking of contains at least $K$ digits of value $C$"?

##  Task

Help Zaharel answer the question as quickly as possible.

##  Input data

The first line of the input file contains the integers $A$, $B$, $C$, and $K$ (in this order).

##  Output data

The first line of the output file will contain the probability, a real number with four decimal places, that the number in the interval $[A \dots B]$ Eugenia is thinking of has at least $K$ digits of value $C$.

##  Constraints

$0 \leq A \leq B < 1\ 000\ 000\ 000$

$0 \leq C, K \leq 9$

For at least 50% of the tests $B-A \leq 1\ 000\ 000$

##  Example

`cifre.in` 
```
1 13 1 1
```

`cifre.out`
```
0.3846
```

##  Explanation

In the interval $[1 \dots 13]$ there are 5 numbers that contain at least one digit of value $1$: $1$, $10$, $11$, $12$, $13$.

Thus, the probability is $\frac{5}{13} = 0.(384615)$