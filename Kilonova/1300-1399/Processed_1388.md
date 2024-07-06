```markdown
For a given number with $k$ digits $\overline{c_1 \ c_2 ... \ c_k}$, the right circular shift algorithm from an initial digit $c_i$ to a final digit $c_j$, shifts the digit $c_i$ to the right $c_i$ times $(1 \leq i, j \leq k)$. If during the shift the digit $c_k$ is reached, the right circular shift continues with the digit $c_1$.
A number with $k$ digits is called a "circular" number if it meets the following two requirements:

* All digits are non-zero.
* Starting from digit $c_1$, applying the right circular shift algorithm exactly $k$ times brings you back to $c_1$, with each digit of the number being exactly once an initial digit.

For example, the number $2 \ 396$ is a "circular" number because it has only non-zero digits and the right circular shift algorithm is applied as follows:

1. Start from the initial digit $2 (2 \ 3 \ 9 \ 6)$ and count two digits to the right, reaching the final digit $9$: $2 \ 3 \ 9 \ 6$.
2. Start from the initial digit $9$ and count nine digits to the right, reaching the final digit $6$: $2 \ 3 \ 9 \ 6$.
3. Start from the initial digit $6$ and count six digits to the right, reaching the final digit $3$: $2 \ 3 \ 9 \  6$.
4. Start from the initial digit $3$ and count three digits to the right, reaching the final digit $2$: $2 \ 3 \ 9 \ 6$.

Thus, we return to the first digit of the number, which is $2$, after exactly $4$ applications of the algorithm, and each digit of the number is exactly once an initial digit.

# Task

Write a program that reads the non-zero natural number $n$, then the natural numbers $x_1, x_2, ..., x_n$, and determines:
1. The largest number in the sequence that contains at least one digit appearing at least twice. If no such number exists in the sequence, the largest number in the sequence is displayed.
2. An array $a_1, a_2, ..., a_n$ of $n$ natural numbers for which an element $a_i (1 \leq i \leq n)$ is calculated as follows:
* It is equal to $x_i$ if $x_i$ is a circular number.
* It is the closest number to $x_i$ (either greater or smaller than $x_i$) with the property that it is a circular number if for a number in the sequence a circular number $y$, $y > x_i$ and a circular number $z$, $z < x_i$ are identified such that $y - x_i = x_i - z$, then the number $y$ is chosen.

# Input data

The input file `numar.in` contains on the first line the number $n$, and on the next $n$ lines the natural numbers $x_1, x_2, ..., x_n$.

# Output data

The output file `numar.out` will contain on the first line a natural number determined according to requirement $a)$, and on the next $n$ lines the array of numbers determined according to requirement $b)$, each number on a separate line.

# Constraints and clarifications

* $0 \lt n \lt 100$
* $9 \lt x_i \lt 999\ 589$, $1 \leq i \leq n$
* For correctly solving the first requirement, $30\%$ of the score is obtained, and for correctly solving the second requirement, $70\%$ of the score is obtained.

# Example

`numar.in`
```
5
15
123
1972
222
515
```

`numar.out`
```
515
15
117
1959
222
522
```

## Explanation

$1. \ 515$ is the largest number among the five numbers read, containing a digit that appears at least twice.

$2.$ For $15$: starting from the initial digit $1$, count one digit to the final digit $5$, then starting from digit $5$ as the initial digit, count five digits and reach the final digit $1$. Thus, the digits $1$, $5$ are exactly once initial digits and after two applications of the shift algorithm, the first digit is reached, so 15 is a circular number.

For $123$: starting from the initial digit $1$, count one digit to the final digit $2`, then starting from digit $2$ as the initial digit, count two digits and reach the final digit $1$. Thus, the first digit is reached again, but the shift algorithm was applied only twice and not three times, and digit $3$ was not an initial digit. As a result, $123$ is not a circular number. The two circular numbers are determined, $y = 141$ and $z = 117$, the closest to $123$ being $117$. The same method applies to the other numbers.
```