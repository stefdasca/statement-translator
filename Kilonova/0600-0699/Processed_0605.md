```markdown
# Task
Consider a natural number $n$, a **strictly increasing** sequence of natural numbers $x_1, x_2, \dots, x_n$ and a closed interval with natural number endpoints. Verify if any natural number in the given interval can be written as a sum with the same minimum number of terms from the sequence in the following two ways:
1) necessarily using the term $x_n$ at least once;
2) using any of the values from the sequence.

Display the number of values in the interval that do not meet the condition, as well as the respective values.
**Note:** If a number cannot be decomposed in one of the two ways, the minimum number of terms in the decomposition is considered to be $0$.

# Input data
The input file `numere.in` has the following structure:
- The first line contains the number $n$ which signifies the number of elements in the sequence.
- The second line contains the numbers $a$ and $b$, separated by a space, which signify the endpoints of the interval.
- The third line contains the sequence $x_1, x_2, \dots, x_n$ of natural numbers.

**Note:** The input data is correct and does not require validation.

# Output data
The first line of the output file `numere.out` will contain the number of values in the interval that do not meet the condition, and if this is nonzero, the next line will print the respective values separated by a space.

# Constraints and clarifications
- $1 \leq n \leq 3\ 000$
- $2 \leq a < b \leq 10\ 000$
- $1 \leq x_1 < x_2 < \dots < x_n \leq a$

# Example 1
`numere.in`
```
3
7 13
1 4 5
```
`numere.out`
```
2
8 12
```
## Explanation
The interval is $[7, 13]$.\
The number $7$:
- According to the first method (necessitating the use of the last term along with other values from the sequence), it can be written as a sum of at least $3$ terms ($1+1+5$);
- According to the second method (using any values from the sequence), it can be written as a sum of at least $3$ terms ($1+1+5$).

The number $8$:
- According to the first method, it can be written as a sum of at least $4$ terms ($1+1+1+5$);
- According to the second method, it can be written as a sum of at least $2$ terms ($4+4$).

The number $9$:
- According to the first method, it can be written as a sum of at least $2$ terms ($4+5$);
- According to the second method, it can be written as a sum of at least $2$ terms ($4+5$).

The number $10$:
- According to the first method, it can be written as a sum of at least $2$ terms ($5+5$);
- According to the second method, it can be written as a sum of at least $2$ terms ($5+5$).

The number $11$:
- According to the first method, it can be written as a sum of at least $3$ terms ($1+5+5$);
- According to the second method, it can be written as a sum of at least $3$ terms ($1+5+5$).

The number $12$:
- According to the first method, it can be written as a sum of at least $4$ terms ($1+1+5+5$);
- According to the second method, it can be written as a sum of at least $3$ terms ($4+4+4$).

The number $13$:
- According to the first method, it can be written as a sum of at least $3$ terms ($4+4+5$);
- According to the second method, it can be written as a sum of at least $3$ terms ($4+4+5$).

# Example 2
`numere.in`
```
3
7 10
2 4 6
```
`numere.out`
```
0
```
## Explanation
All the numbers meet the required condition (for example, $7$ cannot be represented in either of the two ways, so both decompositions have $0$ terms, and $8$ is represented in both ways with the same minimum number of $2$ terms, etc.).
```