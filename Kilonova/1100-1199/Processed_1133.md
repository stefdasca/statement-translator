```markdown
On each of the gates of the $n$ houses in a village, a number is written using stamps. Example: to write the number $3404$, the stamps with $3$ and $0$ will be applied once each and the stamp with $4$ twice.

# Task

$n$ natural numbers are read (those written on the gates), and the following are required:

1. Which stamp is used the least?
2. What is the order of the $10$ stamps (with the $10$ digits), starting with the most used and ending with the least used?
3. Which numbers used exactly two stamps?

# Input data

The input file `stampile.in` contains $n$, the number of houses in the village on the first line. On the second line, $n$ integers $x_i$ representing the number written on house $i$ are found.

# Output data

The first line of the output file `stampile.out` will contain a single integer, the digit used the least. If there are multiple such digits, the smallest digit will be displayed.
The second line will contain the required order as stated in the task. If there are multiple stamps used the same number of times, the smaller digit stamps will be displayed first.
The third line will contain the numbers with exactly two stamps, in the order they appeared in the input.

# Constraints and clarifications

* $1 \leq n \leq 100\ 000$;
* $1 \leq x_i < 10^9$;
* The tests and constraints have been redone.

# Example 1

`stampile.in`
```
7
1011 2924 3925 6748 2222 3434 9988
```

`stampile.out`
```
0
2 4 9 1 3 8 0 5 6 7 
1011 3434 9988 
```

## Explanation

Digits $0$, $5$, $6$, $7$ appear once, with $0$ being the smallest of them. It can be observed that $1011$, $3434$, $9988$ have only two different digits.
```
