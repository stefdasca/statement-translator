# Euclid1

After eating at Deadpool's restaurant and escaping from the Matrix, you are now asked to return to the ancient world, specifically to the moment of inventing the greatest common divisor. In the wonderful city of Alexandria, a vicious king reigned. His kingdom was made up of $N$ cities lined up in a straight line and numbered from $1$ to $N$, and each city had to pay taxes (city $i$ initially has to pay $V_i$ coins). From time to time, the king wanted to increase certain taxes or ask Euclid what the greatest number that divides all the taxes in a range of cities is.

## Task

Given the initial array $V$, where $V_i$ represents the number of coins that city $i$ has to pay to the king. You are asked to perform $Q$ operations on this array, operations that can be divided into two categories:
- query($a$, $b$) - you are asked to help Euclid calculate the greatest common divisor of the values $V_a$, $V_{a+1}$, $V_{a+2}$, $\dots$, $V_b$
- update($a$, $b$, $k$) - the king increases the taxes as follows:
  - $V_a += k$
  - $V_{a+1} += 2 \times k$
  - $V_{a+2} += 3 \times k$
  - $\dots$
  - $V_b += (b - a + 1) \times k$

## Input data

The input file `euclid1.in` contains on the first line two integers $N$ and $Q$, representing the number of cities and the number of the king's questions, respectively. The second line contains $N$ integers, the array $V$. The following $Q$ lines contain an operation, each described as follows:
- if the operation is query($a$, $b$), then the line will contain three integers: $0 \; a \; b$
- if the operation is update($a$, $b$, $k$), then the line will contain four integers: $1 \; a \; b \; k$

## Output data

The output file `euclid1.out` must contain the answer for each query type question, in the order in which they are given, separating each answer by a new line.

## Constraints and clarifications

$1 \leq N \leq 100\,000$

$1 \leq Q \leq 100\,000$

$1 \leq a \leq b \leq N$ for all operations.

$1 \leq k \leq 200\,000\,000$ for all update operations.

$1 \leq V_i \leq 200\,000\,000 \; (\forall) \; 1 \leq i \leq N$

For $20\%$ of the tests $N, Q \leq 1\,000$

For another $40\%$ of the tests $N, Q \leq 70\,000$

## Example

`euclid1.in`
```
8 3
2 8 12 24 66 33 21 7
0 2 4
1 1 4 2
0 2 4
```

`euclid1.out`
```
4
2
```

## Explanation

For the first operation: the greatest common divisor is calculated as $\text{gcd}(8, 12, 24) = 4$

As a result of the second operation, the array becomes: $(4, 12, 18, 32, 66, 33, 21, 7)$

The third operation: $\text{gcd}(12, 18, 32) = 2$