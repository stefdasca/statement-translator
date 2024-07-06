Doc the Dwarf has secured his bank card's PIN in a way known only to him. The PIN is exactly $4$ digits long. Doc has a set of numerical information arranged on $R$ rows. Each digit of the bank card's PIN is a majority element on its row, meaning the number of occurrences of that digit is greater than $\\frac{n}{2}$, where $n$ represents the total number of digits on that row. Can you figure out Doc's PIN or do you think he made a mistake in securing it?

# Task

Given the number $R$ of rows and the numbers on each row, write a program to determine Doc's PIN.

# Input data

The input file `pin.in` contains on the first line the number $R$ which represents the number of rows. Each of the next $R$ lines contains a set of at most $2024$ natural numbers.

# Output data

The output file `pin.out` will contain a single line which will either print the message `CORRECT PIN` followed by the natural number representing Doc's PIN or the message `INCORRECT PIN` followed by a number representing Doc's mistake in securing the PIN.

# Constraints and clarifications

* $R$ is a natural number, $4 \leq R \leq 1\ 000$.
* The numbers on each row have at most $9$ digits and are separated by a single space.
* It is guaranteed that there is at least one majority digit.
* The PIN digits are chosen in the order of traversing the rows from row $1$ to $R$.

# Example 1

`pin.in`
```
5
17 111 4112 1019 1 23
45 3033 3 8 3033 48899
45 3033 3 8 3033
100 200 300
77777
```

`pin.out`
```
CORRECT PIN 1307
```

## Explanation

The first digit of the PIN is $1$ found from row $1$. The second digit of Doc's PIN is $3$ (row $2$). The third digit is $0$ found from row $3$. The last digit, the fourth, is deduced from row $4$. The PIN has EXACTLY $4$ digits, so it is correct.

# Example 2

`pin.in`
```
7
17 123 4112 4049 8 23 6788
45 3033 3 8 3033 48899
45 3033 3 8 3033
100 200 300
7890
1 2 3 4 5 6 7 8 9
0 0 0 9 9 9 888 666
```

`pin.out`
```
INCORRECT PIN 30
```

## Explanation

Doc made a mistake in securing the PIN because the PIN has only $2$ digits: the digit $3$ found from row $3$ and the digit $0$ found from row $4$.