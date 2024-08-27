# Loto2

Tired of spending money on Loto 6/49, O'Bitica decides to try his luck with a new lottery, 1/2,000,000,000,000. Wanting to be sure of his success, he goes to Guru Lotolica to find out the winning number. Guru Lotolica does not want to reveal the winning number directly but tells him the following: "I will give you a sequence of $N$ natural numbers, each less than $2\ 000\ 000\ 000$. The winning number will have the following two properties: It will be larger than all the numbers in the sequence I will give you. It will not be divisible by any of the numbers in the sequence I will give you."

## Input data

The input file `loto2.in` contains the natural number $N$ on the first line, and on the second line contains $N$ natural numbers, representing the sequence given by Lotolica.

## Output data

The output file `loto2.out` will contain a single natural number, representing the winning number.

## Constraints and clarifications

$1 \leq N \leq 100\ 000$

$1 \leq A[i] \leq 2\ 000\ 000\ 000$

It is guaranteed that a solution exists. If there are multiple solutions, any of them can be displayed. As the name of the game suggests, the winning number must be between $1$ and $2\ 000\ 000\ 000$.

## Example

`loto2.in`

```
4
4 3 10 5
```

`loto2.out`

```
14
```