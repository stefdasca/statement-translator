# Alcohol

Mescheriakov wants to become an alcohol producer. And what product has a higher percentage of alcohol than spirit? Thus, Mescheriakov bought a spirit factory, and he wants to start production as soon as possible, but he needs a reliable assistant. He wants to test you with the following problem: "Given a parenthesis sequence of length $N$ and any number of colors, $M$, color each parenthesis with a color from the $M$ colors, with the property that two parentheses that are part of the same pair or are adjacent cannot have the same color. The number of valid colorings of this parenthesis sequence modulo $666013$ is required." Mescheriakov wants to choose as his assistant the one who can answer the above problem after drinking a maximum amount of spirit. Since you want to ensure that you get the position, you need the help of a computer!

## Task

Write a program that solves Mescheriakov's problem!

## Input data

The input file `spirt.in` contains on the first line two natural numbers $N$ and $M$, with the meaning given in the statement. The second line of the input file will contain a sequence of parentheses of length $N$, describing Mescheriakov's parenthesis sequence.

## Output data

In the output file `spirt.out`, you must print a single number, the answer to the problem, modulo $666013$.

## Constraints and clarifications

$1 \leq N \leq 100\ 000$

$3 \leq M \leq 100\ 000$

For 20% of tests

$1 \leq N \leq 30$

$1 \le\q M \leq 10$

For another 20% of tests

$1 \leq N, M \leq 100$

It is guaranteed that the parenthesis sequence from the statement is correct (each open parenthesis has a matching closed parenthesis following it).

The author of this problem, despite being in contradiction with Mescheriakov, advises you not to drink spirit!

## Example

`spirt.in`
```
2 4
()
```
`spirt.out`
```
12
```

`spirt.in`
```
4 4
(())
```
`spirt.out`
```
84
```

`spirt.in`
```
4 4
()()
```
`spirt.out`
```
108
```