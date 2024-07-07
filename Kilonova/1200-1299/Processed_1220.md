
A group of children buy tickets to climb Postăvarul peak. At the cable car, they find a line formed by $n$ of their classmates and ask to be let in among them. To avoid any disagreements, a rule was established by which some of the newcomers are accepted. Thus, for each ticket (let $P$ be its series), the sum $S$ of the digits of the number $P$ is calculated. In front of each child in the initial line, for whom the numbers $P$ and $S$ are coprime, those children for whom the series on their tickets are prime numbers between $S$ and $P$ are placed.

# Task

Recompose the line of children, modified according to the described rule.

# Input data

The first line of the input file `prieteni.in` contains a number $n$ representing the number of children and then $n$ numbers separated by spaces representing the series of the tickets bought.

# Output data

The first line of the output file `prieteni.out` will contain the number of children in the final line and the second line will contain the series of the tickets of these children in their order in the line.

# Constraints and clarifications

* $1 \leq n \leq 100$
* The series of the tickets are distinct natural numbers less than $65\ 535$.
* If there is no ticket whose series meets the described conditions, the line remains unchanged.

# Example 1

`prieteni.in`
```
4
64 14 31 17
```

`prieteni.out`
```
11
64 5 7 11 13 14 19 23 29 31 17
```

## Explanation

$P = 14$ and $S = 1+4 = 5$ are coprime. In front of $14$, the prime numbers between $5$ and $14$ that are not in the line are inserted.

$P = 31$ and $S = 3+1 = 4$ are coprime. In front of $31$, the prime numbers between $4$ and $31$ that are not in the line are inserted.

$P = 17$ and $S = 1+7 = 8$ are coprime. No numbers are inserted in front of $17$.
