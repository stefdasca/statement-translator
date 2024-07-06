**Romanians Got Talent!** Attracted by the grand prize offered by the organizers of the contest "Romanians Got Talent", many Romanians came to the auditions organized in Piatra Neamț to demonstrate that they have talent.
At registration, each participant received a contest number, represented by a non-zero natural number. Some of the participants may have a special status, being admitted directly to the semifinals, as a result of their outstanding results achieved in previous editions, the contest number received by them having the property that all its digits can be rearranged to form a palindrome.
Among the contest numbers received by participants with special status, there are numbers that have a maximum number of distinct digits in their decimal representation. The smallest of these numbers represents the contest number of the VIP participant.

# Task

Write a program that reads the natural number $n$ (representing the number of participants registered in the contest), $n$ natural numbers (representing the contest numbers of the $n$ participants) and determines:
1. the number $x$ of participants admitted directly to the semifinals
2. the contest number $y$ of the VIP participant, if there is such a participant among those registered

# Input data

The input file `talent.in` contains the first line and contains the number $n$ of participants, and each of the following $n$ lines contains a natural number representing the contest number of a participant.

# Output data

The output file `talent.out` will contain on the first line the two values $x$ and $y$, separated by a single space, in this order. If there are no participants admitted directly to the semifinals, then the first line of the file will contain two null values, separated by a single space: $0 \\ 0$.

# Constraints and clarifications

* $0 \lt n \leq 15\ 000$
* the contest numbers are distinct in pairs and are less than or equal to $2\ 000\ 000\ 000$
* a palindrome number is a natural number that is equal to the natural number obtained by writing its digits in reverse order (for example, the number $12021$ is a palindrome number)
* for correctly solving the first task, $50\\%$ of the score is awarded, and for correctly solving the second task, $50\\%$ of the score is awarded.

# Example

`talent.in`
```
8
17864
9900
90321
4704
351
83181
46476
7432
```

`talent.out`
```
3 46476
```

## Explanation

There are $3$ participants admitted directly to the semifinals. Their contest numbers are numbers whose digits can be rearranged to form a palindrome: $9900$ (formed from $2$ distinct digits), $83181$ (formed from $3$ distinct digits) and $46476$ (formed from $3$ distinct digits). Among these, the smallest number formed from a maximum number of distinct digits is $46476$ representing the contest number of the VIP participant.