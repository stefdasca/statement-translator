```markdown
Gigel needs to buy $n$ medications, numbered from $1$ to $n$. The doctor gave him $m$ prescriptions of two types, coded with the numbers $1$, $2$ as follows:
* $1$ — non-subsidized prescription, meaning the price of the medications on the prescription is fully paid by the buyer;
* $2$ — 50\% subsidized prescription, meaning the price of the medications listed on the prescription is halved;

It is known that there are no other medications on the prescriptions other than those numbered from $1$ to $n$ and a prescription does not contain two identical medications.
If a prescription is used, then all the medications listed on it will be bought.

# Task

Write a program that determines the minimum sum of money required to buy exactly one of each of the $n$ medications, using the available prescriptions.

# Input data

The input file `reteta.in` has the following format:
- the first line contains the natural numbers $n$ and $m$;
- the next $m$ lines describe the $m$ prescriptions, one prescription per line. The line describing a prescription contains the type of the prescription ($1$ — non-subsidized, $2$ — subsidized), followed by a natural number $q$ representing the number of medications on the prescription, then $q$ distinct numbers from the set $\{1, 2, \dots, n\}$ representing the medications listed on that prescription;
- the last line of the input file contains $n$ natural numbers separated by a space, representing in order from $1$ to $n$, the price of the medications.

All numbers on the same line are separated by a space.

# Output data

The output file `reteta.out` will contain a single line that will print a real number with one decimal, representing the determined minimum sum.

# Constraints and clarifications

* $1 \leq N \leq 20$
* $1 \leq M \leq 15$
* $1 \leq$ price of any medication $\leq 200$
* For the test data, there is always a solution.

# Example

`reteta.in`
```
4 5
2 1 3
2 2 2 3
1 1 1
1 3 4 1 2
1 1 3
8 20 2 16
```

`reteta.out`
```
45.0
```

## Explanation

The solution was obtained by using the first and fourth prescriptions.
Another solution, but with a higher cost, would have been obtained if the fourth and fifth prescriptions were used.
```