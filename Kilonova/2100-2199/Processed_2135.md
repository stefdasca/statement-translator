## Grigore Moisil Intercounty Contest

The Grigore Moisil Intercounty Contest this year has concluded, and two contestants achieved the highest score. Because their result is significantly better than the rest of the competitors, they must receive prizes with the highest possible total value. Since their scores are equal, the sum of the values of the prizes they receive must also be equal.

# Task

Knowing the value of the $n$ prizes offered by the sponsors, determine a way of distributing the prizes so that the above requirements are met.

# Input data

The first line of the input file contains the number $n$ of the prizes. The next $n$ lines each contain the value of a prize.

# Output data

The first line of the output file should contain the sum of the prizes awarded to the other competitors, excluding the first two.

On the second line, print the number $k_1$ of prizes received by the first contestant. On the third line, print the indices numbered from $1$ representing the prizes received by the first contestant, considering the order in the input file.

On the fourth line, print the number $k_2$ of prizes received by the second contestant. On the fifth line, print the indices numbered from $1$ representing the prizes received by the second contestant, considering the order in the input file.

# Constraints and clarifications

* $1 \leq n \leq 1\ 000$
* The prize values are positive natural numbers.
* The sum of all prizes is at most $50\ 000$.
* If there are multiple solutions, any of them can be displayed.
* For $20\%$ of the score, $1 \leq n \leq 20$.
* For another $30\%$ of the score, $1 \leq n \leq 100$ and the total sum of the prizes does not exceed $5\ 000$.
* For the remaining $50\%$ of the score, there are no additional restrictions.

# Example

`premii.in`
```
5
13
21
8
4
8
```

`premii.out`
```
12
2
1 3
1
2
```

## Explanation

The first contestant receives the prizes with indices $1$ and $3$ with a total value of $13 + 8 = 21$.

The second contestant receives the prize with index $2$ with a value of $21$. Thus, both contestants receive prizes with an equal total value of $42$, which is the highest possible value for this example.

The two could have received the prizes with indices $3$ and $5$, but the total value of those would be only $16$, which is less than $42$.

If the first contestant had received the prizes with indices $1, 3$, and $5$ with a total value of $13 + 8 + 8 = 29$, and the second contestant prizes with indices $2$ and $4$ with a total value of $21 + 4 = 25$, the total sum would be $29 + 25 = 54$, but the two contestants would not have received prizes with an equal total value.