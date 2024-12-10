

A natural number $N$ composed of $m$ digits and all the $m - 1$ numbers that can be successively formed starting from the initial number $N$ are considered by moving the most significant digit of the current combination to its end, as can be seen from the examples below.

$N = 12035 \rightarrow 20351 \rightarrow 03512 \rightarrow 35120 \rightarrow 51203$ ($4$ combinations). The zero at the beginning of $03512$ is cut and the number remains $3512$.

$N = 2121 \rightarrow 1212 \rightarrow 2121 \rightarrow 1212$ ($3$ combinations, $3$ numbers)

# Task

Write a program that reads the number $N$, constructs the $m - 1$ numbers and determines:

1. the number with the highest number of divisors among these $m$ numbers; if there are multiple such numbers among the $m$, all these numbers will be written in the output file.
2. the largest number that is a proper divisor for at least one of these $m$ numbers, and if there is no such divisor (all $m$ numbers are prime), the value $0$ will be displayed.

# Input data

The `divizor.in` file contains a single line which contains the natural number $N$.

# Output data

The `divizor.out` file will contain:

* the first line will contain the number or numbers with the maximum number of divisors, separated by a space
* the second line will contain a natural number representing the largest number that is a proper divisor for at least one of these $m$ numbers or $0$, if all $m$ numbers are prime

# Constraints and clarifications

* $1 \leq N < 1 \ 000 \ 000$;
* According to the combination forming procedure, it may happen that the same number is obtained multiple times. All possible combinations will be considered, even if there are repeating numbers.
* The digit $0$ written at the beginning of a number is considered negligible and does not need to be displayed in the final result.
* The initial number is also considered in all requirements.
* A proper divisor of a number is a divisor different from $1$ and the number itself.
* Partial scores are awarded: requirement a) 60% of the points, requirement b) 40% of the points

# Example

`divizor.in`
```
212
```

`divizor.out`
```
212
106
```

## Explanation

The obtained numbers: $212$ (initial), $122$, $221$. $212$ has $6$ divisors, $122$ and $221$ have $4$ divisors each. Thus, the number with the highest number of divisors is $212$. The largest proper divisor is $106$ (divisor of the number $212$).
