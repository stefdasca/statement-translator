
Scrat and Scratte are two acorn-devouring squirrels. They live in a tall oak tree and gather acorns from its $N$ branches. The squirrels will organize a competition: whoever gathers the most acorns in $K$ turns. In a turn, each squirrel will travel from the burrow to a branch of the oak tree, gather as many acorns as possible, but no more than $M$ acorns, and then return to the burrow. The squirrels will alternately take $K$ turns each, starting with Scratte.

Upset that he will not start first in the competition, Scrat decides to train separately and see how many acorns he would gather in $K$ turns if he were alone.

# Task

Create a program that determines:

1. How many acorns Scrat collects during training;
2. How many acorns each squirrel collects during the competition.

# Input data

The input file `ghinde.in` contains on the first line a natural number $C$. For all tests, $C$ can only take the values $1$ or $2$. The second line contains the numbers $N$, $M$, and $K$ representing the number of branches of the oak tree, the maximum number of acorns gathered in a turn, respectively the number of turns. On the following $N$ lines, the number of acorns on each branch is found.

# Output data

If the value of $C$ is $1$, only the first point of the task will be solved. In this case, the output file `ghinde.out` will contain the total number of acorns gathered by Scrat during training.

If the value of $C$ is $2$, only the second point of the task will be solved. In this case, the output file `ghinde.out` will contain on the same line two natural numbers, separated by a space, representing in order, the number of acorns gathered by Scratte and Scrat during the competition.

# Constraints and clarifications

* $1 \leq N \leq 500\ 000$
* $1 \leq K \leq 2\ 000\ 000\ 000$
* $1 \leq M \leq 500\ 000$
* $0 \leq$ number of acorns on a branch $\leq 500\ 000$
* For the correct resolution of the first task, $20$ points are awarded, and for the correct resolution of the second task, $80$ points are awarded

# Example 1

`ghinde.in`
```
1
3 10 3
13
19
4
```

`ghinde.out`
```
29
```

## Explanation

Scrat gathers $10$ acorns from the first branch, then $10$ from the second branch and another $9$ from the second branch, meaning $10 + 10 + 9 = 29$

# Example 2

`ghinde.in`
```
2
4 10 3
13
19
4
7
```

`ghinde.out`
```
23 20
```

## Explanation

Scratte: $10$ from the second branch;
Scrat: $10$ from the first branch;
Scratte: $9$ from the second branch;
Scrat: $7$ from the fourth branch;
Scratte: $4$ from the third branch;
Scrat: $3$ from the first branch;
Scratte: $10+9+4=23$
Scrat: $10+7+3=20$
```

