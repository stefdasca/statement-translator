## Task

Mona and Lisa are avid gamblers. Every evening, they try their luck at a special electronic roulette wheel, which displays a lowercase English alphabet letter with each turn. The two girls played $N$ turns last night, betting on exactly one letter each turn. Because they lost a significant amount of money (in dollars), the girls suspect that the roulette wheel might be rigged and want to scientifically prove it. They wrote down $N$ characters on a sheet, where the $i$-th character represents the letter displayed by the roulette wheel in the $i$-th turn. Mona observes that some sequences of characters in consecutive positions are periodic, meaning they are formed by concatenating the same string at least twice. For example, the strings $abcabc$ and $ananan$ are periodic, but $abac$ is not. Lisa realizes that the roulette is rigged if it generated many periodic sequences. Lisa thus selects $M$ sequences for which she wants to determine whether they are periodic or not. If a sequence is periodic, Lisa wants to know in how many ways it can be obtained by concatenating the same string.

## Input data

The input file `perioada.in` contains the number $N$ on the first line. The second line contains $N$ characters, as described. The third line contains the number $M$ of sequences to be tested. Each of the following $M$ lines contains a pair of natural numbers $x$ $y$, separated by exactly one space.

## Output data

The output file `perioada.out` will contain $M$ integers, with the value on the $i$-th line representing the number of ways the $i$-th sequence from the input file can be considered a concatenation.

## Constraints and clarifications

$1 \leq N, M \leq 100\,000$

$1 \leq x < y \leq N$

## Example

`perioada.in`:
```
10
ranananvvv
3
2 7
1 6
8 10
```

`perioada.out`:
```
3
0
1
```

## Explanation

The sequence $ananan$ is formed by repeating the string $an$ $3$ times. 

The sequence $ranana$ is not periodic.