Safe

Miruna has gotten into a big mess. Because she was about to have an exam in algorithms and data structures, she decided to break into her professor's apartment to get her hands on the exam subjects. She started off well, but now she finds herself in front of the safe that holds the coveted exam subjects. To get past this last obstacle, Miruna needs to enter a secret code. She found out from reliable sources that this code has a length greater than or equal to a number $K$. Moreover, she obtained from the professor's office 2 strings of uppercase letters of lengths $N$ and $M$. Miruna suspects that the secret password that opens the safe is a common subsequence of the 2 strings, as lexicographically large as possible.

## Task

Knowing the 2 strings and the number $K$, find the common subsequence of length greater than or equal to $K$ that is lexicographically largest.

## Input data

The first line of the input file `seif.in` contains an integer $T$, representing the number of tests. Each test consists of 3 lines: the first line contains an integer $K$, and the next 2 lines contain the character strings.

## Output data

The output file `seif.out` will contain $T$ lines, each line containing the desired subsequence for each test case.

## Constraints and clarifications

$1 \leq T \leq 10$

$1 \leq N, M \leq 1000$

$0 \leq K \leq \min(N, M)$

A string $(x_{1}, x_{2} \dots x_{N})$ is lexicographically larger than another string $(y_{1}, y_{2} \dots y_{M})$ if there exists a position $p$ such that $x_{p} > y_{p}$ and $x_{1} = y_{1}$, $x_{2} = y_{2}  \dots  x_{p-1} = y_{p-1}$.

There is always a solution for the test data.

## Example

`seif.in`
```
2
2
AAZ
AZA
1
ZAZ
ZBZ
```

`seif.out`
```
AZ
ZZ
```