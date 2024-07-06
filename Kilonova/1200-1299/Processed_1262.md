Returning from school on the day he learned how to multiply numbers, Gigel heard the following statement on television: "To make a fortune, you don't need to add money in life, but rather multiply it."

All this made him ponder, so he decided to invent his own "coding system" for real numbers greater than $0$ that has the following properties:

* Each number will be encoded as a sequence of integer values (positive and/or negative)
* If a real number $x$ has the code $c_x$ and a real number $y$ has the code $c_y$, then the real number resulting from multiplying $x$ and $y$ must have the code obtained by "adding" the codes $c_x$ and $c_y$
* If a real number $x$ can be written as a product of numbers $y_1, y_2, \ldots , y_k$, then the code of $x$ is obtained by "adding" the codes of the numbers $y_1, y_2, \ldots , y_k$
* Considering a code $c_1$ formed of $n_1$ values $a_{n_1} \ldots a_1$ and a code $c_2$ formed of $n_2$ values $b_{n_2} \ldots b_1$, then the code $c_3$ obtained by **"adding"** the codes $c_1$ and $c_2$ will have $n_3$ values $d_{n_3} \ldots d_1$, with the following properties:
   * $n_3$ is the maximum between $n_1$ and $n_2$
   * $d_i = \begin{cases}
   a_i + b_i, &\text{for } i = 1, \ldots, \min(n_1,n_2) \\
   a_i, &\text{for } i = \min(n_1,n_2) + 1, \ldots n_1, &\text{if } \min(n_1, n_2)=n_2\\
   b_i, &\text{for } i = \min(n_1,n_2) + 1, \ldots n_2, &\text{if } \min(n_1, n_2)=n_1
   \end{cases}$

# Task

Given $N$ real numbers strictly greater than $0$, write their encoding in the system invented by Gigel.

# Input data

The input file `coduri.in` will contain:

* The first line of the file will contain the number $N$ of real numbers
* The next $N$ lines contain the $N$ real numbers, each on a separate line

# Output data

The output file `coduri.out` will contain $N$ lines:

The $i^{th}$ line ($i$ between $1$ and $N$) must contain: the number of values used to encode the number with index $i$ from the input file, followed by a space and then the values that make up the code of the number, separated two by two by a single space.

# Constraints and clarifications

* $2 \leq N \leq 18$
* The separator between the integer part and the decimal part is a comma
* Any number has at most $5$ digits after the comma
* The values in the codes of the numbers from the test files must be in the range $[-10^6, 10^6]$
* The integer part of each real number is a value less than or equal to $20\ 000$
* All numbers in the test files are strictly positive and distinct two by two
* The maximum number of values used to encode a number is $2\ 500$
* If there are multiple valid encodings, only one should be displayed
* There should not be two different numbers with the same encoding
* $40\%$ of the tests will contain only integers, $30\%$ of tests will contain integers and non-repeating real numbers, and $30\%$ of tests will contain both integers and real numbers with or without repeating patterns

# Example

`coduri.in`
```
8
10
2
5
0,3
7
2,1
1,(7)
1,2(34)
```

`coduri.out`
```
2 1 1
3 -1 0 1
3 1 1 0
3 2 1 0
3 -1 2 1
3 1 3 1
2 1 11
2 1 2
```

# Explanation

$10=2 \cdot 5$, and the sum of the codes for $2$ and $5$ determines the code for $10$

$2,1=7 \cdot 0,3$, and the sum of the codes for $7$ and $0,3$ determines the code for $2,1$