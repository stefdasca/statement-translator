## Task

At the company DOT on the planet CAMP, $n$ people work, numbered from $1$ to $n$. The big boss is organizing a party where all employees will participate. At each table, one or more employees will be seated, respecting the following two rules: the sum of the ages of the employees seated at the same table must not exceed the value $S$; any two people $a$ and $b$, people seated at the same table, either know each other or there are $k$ people at the same table $x_1$, $x_2$, $\dots$, $x_k$ such that $a$ knows $x_1$, $x_1$ knows $x_2$, $\dots$, $x_k$ knows $b$. Since the company is very large, everyone knows only their direct boss and their direct subordinates. The hierarchy in the company is non-contradictory, meaning there is no chain of the form $x_1$ is the boss of $x_2$, $x_2$ is the boss of $x_3$, $\dots$, $x_{k-1}$ is the boss of $x_k$, $x_k$ is the boss of $x_1$.

## Input data

The first line of the input file `mese.in` contains the numbers $n$ and $S$, separated by a space. The next $n$ lines contain two integers separated by a space; the first number on line $i+1$ represents the direct boss of $i$, the second number represents the age of $i$. There is a single line, corresponding to the big boss, where the direct boss is $0$.

## Output data

The output file `mese.out` will contain a single line which will contain the minimum number of tables necessary for the party.

## Constraints and clarifications

$2 \leq n \leq 100\,000$

Ages are integers in the interval $[1 \dots 255]$

$2 \leq S \leq 30\,000$

No age exceeds the value of $S$

## Example

`mese.in`

```
6 10
5 9
3 4
0 2
2 4
3 7
2 2
```

`mese.out`

```
3
```

## Explanation:

A possible arrangement at the $3$ tables:

$(3 \, 5)$

$(2 \, 4 \, 6)$

$(1)$