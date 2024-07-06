Here is the translated competitive programming problem statement in English while preserving the required formatting, mathematical values, variable names, and structure:

---

Italag has been passionate about stock market speculations all his life, managing to accumulate a considerable fortune. Being an original person and passionate about mathematics, he wrote an unusual will. The will contains two natural numbers: $S$ representing the fortune that must be divided among heirs and $N$ representing his choice for distributing the fortune. Italag decides to divide **all the fortune**, and the amounts he grants to the heirs must be in **strictly decreasing order**.

For example, if the fortune were $7$ monetary units, it could be divided as follows:

* $4$ (units to the first heir) $3$ (units to the second heir), or
* $6$ (units to the first heir) $1$ (units to the second heir), or
* $7$ (to only the first heir), or
* $5$ (units to the first heir) $2$ (units to the second heir), or
* $4$ (units to the first heir) $2$ (units to the second heir) $1$ (units to the third heir).

Seeing that it is very difficult for him to check if he missed any variant of division, Italag wrote them in lexicographical order. For the above example: $4 \\ 2 \\ 1$; $4 \\ 3$; $5 \\ 2$; $6 \\ 1$; $7$. 

He decided that the money should be distributed according to the $N$-th possibility in lexicographical order.

# Task

Write a program that for the given numbers $S$, $N$ calculates and displays the total number of possible ways to divide the fortune, as well as the way this division is done according to the $N$-th possibility in lexicographical order.

# Input data

The input file `avere.in` contains a single line with two natural numbers separated by a single space:
- the first number ($S$) represents the total sum
- the second ($N$) represents the order number of the sought position

# Output data

The output file `avere.out` will contain two lines:
- the first line will contain the total number of ways to divide the fortune;
- the second line will contain the $N$-th possibility of dividing $S$ according to the task in lexicographical order. Its elements will be separated by a space.

# Constraints and clarifications

* $1 < S < 701$
* $0 < N <$ total number of possibilities with the sum $S$
* Partial scores are awarded for each test: $50\\%$ for correctly determining the number of ways to divide $S$ and $50\\%$ for correctly determining the $N$-th possibility in lexicographical order.
* The possibilities of dividing the fortune are numbered starting from $1$.
* Let $x = (x_1, x_2 \dots, x_m)$ and $y = (y_1, y_2, \dots, y_p)$ be two sequences. We say that $x$ precedes $y$ in lexicographical order if there exists $k \geq 1$, such that $x_i = y_i$, for any $i$ from $1$ to $k-1$ and $x_k < y_k$. Example: $4 \\ 2 \\ 1$ precedes the sequence $4 \\ 3$ because ($4=4, 2<3$), and $6 \\ 1$ precedes $7$ because $6 < 7$.

# Example 1

`avere.in`
```
7 2
```

`avere.out`
```
5
4 3
```

# Example 2

`avere.in`
```
12 5
```

`avere.out`
```
15
6 5 1 
```

# Example 3

`avere.in`
```
700 912345678912345678
```

`avere.out`
```
962056220379782044
175 68 63 58 54 45 40 36 34 32 20 18 17 14 11 9 3 2 1
```

---

Please review the translation for any potential grammatical or syntactical errors.