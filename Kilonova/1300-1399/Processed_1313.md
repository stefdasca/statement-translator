We have rectangular cards inscribed with natural numbers and a given value $x$. Starting from a number $N$ of such cards, placed side by side and considered to form the base level (noted with $1$), the following $N - 1$ levels are formed according to the following rules (see also the figure in the example for clarification):

- the number of cards on any level is exactly $1$ less than the number of cards on the immediately lower level
- the number inscribed on any card is obtained as the sum of the numbers on the cards over which it is "placed", cards located on the immediately lower level.

On each level, the sum of the numbers on all the cards is calculated. Thus, $N$ sums will be formed, and each of them is represented in base $2$.

**Example**:
~[cartonas.png|align=center]

# Task

1. Display the number inscribed on the card on the last level.
2. Specify the level number containing the given value $x$
3. Display the level numbers in descending order of the number of digits equal to $1$ in the binary representation of the sum of each level. If there are two levels with sums having the same number of digits equal to $1$, the level with the smaller number will be displayed first.

# Input data

In the file `cartonas.in`:

- The first line contains a natural number $N$ representing the number of cards that form level $1$ (the base level)
- The second line contains a natural number $x$ representing the sought value
- The third line contains the $N$ numbers on level $1$ (the base level), separated by spaces

# Output data

In the file `cartonas.out`:

- The first line will contain the number inscribed on the card on the last level
- The second line will contain the level containing the sought value $x$
- The third line will contain the level numbers in the required order, separated by spaces

# Constraints and clarifications

* $1 \leq N \leq 100$
* $x$ is a natural number of at most $7$ digits
* The values on the cards are natural numbers of at most $7$ digits
* It is known that there are enough cards with any required number inscribed. The numbers on the base level do not lead to numbers on other levels that exceed $7$ digits, and the sums on each level have at most $9$ digits.
* Partial scores are awarded: $30\%$ of the score for Task 1, $30\%$ of the score for Task 2, and $40\%$ of the score for Task 3

# Example

`cartonas.in`
```
4
8
1 2 3 2
```

`cartonas.out`
```
18
3
2 3 4 1
```

## Explanation

On the last level, the value $18$ will be found, and the value $8$ is found on the third level, according to the drawing and the task requirements.
On the first level $S = 1 + 2 + 3 + 2 = 8 = 1000_{(2)}$, meaning it has $1$ digit equal to $1$
On the second level $S = 3 + 5 + 5 = 13 = 1101_{(2)}$, meaning it has $3$ digits equal to $1$
On the third level $S = 8 + 10 = 18 = 10010_{(2)}$, meaning it has $2$ digits equal to $1$
On the fourth level $S = 18 = 10010_{(2)}$, meaning it has $2$ digits equal to $1$