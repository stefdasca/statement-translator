# Brasov

One week before the start of the national stage of the Informatics Olympiad, a devoted fan of this competition, Georgel Tractorescu, reminisces about the past years with friends over a glass of juice in the Old Town of Brasov. He fondly remembers every moment spent in this favorable environment for both academic and personal development, and he wishes to raise a glass of water in honor of the organizers. However, as nothing is perfect, Georgel realizes a flaw in the competition's rules and wants to exploit it to manipulate future results and, who knows, maybe even give you the 1st place. But being too busy relaxing, he proposes the following deal: anyone who helps Georgel complete his plan will receive $100$ points in the "Adolescent Grigore Moisil" contest and possibly $300$ points in the next edition of the national informatics Olympiad, and those who don't will have to settle for a Guinness. Since Georgel is not easily fooled (be like Georgel!), he won’t give away the actual flaw in the rules but will ask you to implement a program that answers a set of tasks. Knowing that initially, we start with a function defined on the empty set, the tasks are as follows:

$1 \ a \ b$ - insert the interval $[a, b]$ into the domain of the function $(Domain = Domain \cup [a, b])$

$0 \ a \ b$ - delete the interval $(a, b)$ from the domain of the function $(Domain = Domain \setminus (a, b))$

MAX - determine the maximum length of a maximal continuous interval in the domain, and if there is no interval, display $-1$

MIN - determine the minimum length of a maximal continuous interval in the domain, and if there is no interval, display $-1$

Diff_min - determine the minimum difference between the lengths of two maximal continuous intervals in the domain, and if there are not at least two intervals, display $-1$

Diff_max - determine the maximum difference between the lengths of two maximal continuous intervals in the domain, and if there are not at least two intervals, display $-1$

$2 \ x \ y$ - determine how many maximal continuous intervals have lengths in the range $[x, y]$

## Input Data

The input file `brasov.in` contains on the first line the number $q \ $, representing the number of tasks. Each of the next $q \ $ lines describes one of the types of tasks presented above.

## Output Data

The output file `brasov.out` will contain the answers for each task, each answer on a separate line in the order in which the tasks were read.

## Constraints and Clarifications

$1 \leq q \leq 500.000$

$-100.000.000 \leq a \leq 100.000.000$

$-100.000.000 \leq b \leq 100.000.000$

$0 \leq x \leq 1.000.000.000$

$0 \leq y \leq 1.000.000.000$

It is guaranteed that for each task of type $1$ the following relation is valid: $a \leq b$

It is guaranteed that for each task of type $0$ the following relation is valid: $a + 1 \leq b$

It is guaranteed that there will not be more than $200.000$ tasks of type $1$ and $2$

An interval $J$ is considered continuous if and only if it can be written as $[a, b]$

A continuous interval $J$ is considered maximal if and only if there is no other continuous interval $[x, y]$ in the domain such that $[a, b]$ is included in $[x, y]$

## Example

`brasov.in` `brasov.out`

```
9
1 -1 2
MIN
MAX
Diff_min
Diff_max
2 0 3
0 -1 2
Diff_min
Diff_max
```

```
3
3
-1
-1
1
0
3
3
-1
-1
1
0
0
```

## Explanation

After the first task, the domain becomes: Domain = $[-1, 2]$

After the seventh task, the domain becomes: Domain = $[-1, -1] \cup [2, 2]$