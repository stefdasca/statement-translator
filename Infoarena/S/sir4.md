## Task

Consider the sequence $X_i$ defined by the following initialization variables: $X_0$, $A$, $B$, $M$ such that:

$X_0$ is the first element of the sequence.

$X_i = (A * X_{i-1} + B) \% M$, for any $i \geq 1 \ (x \% y \ represents \ the \ remainder \ of \ the \ integer \ division \ of \ x \ by \ y)$.

Answer $Q$ questions of the form: Given the position $P_i$ of an element in the sequence, determine its value, $X_{P_i}$.

Given the initialization variables $X_0$, $A$, $B$, $M$, determine the answer for each of the $Q$ questions.

## Input data

The program reads data from the file `sir4.in`.

The first line contains the natural numbers $X_0$, $A$, $B$, $M$, and $Q$ separated by a space.

Each of the following $Q$ lines contains, in order, one of the numbers $P_1$, $P_2$, $\dots$, $P_Q$, representing positions of terms in the sequence.

## Output data

The program writes to the first line of the file `sir4.out`, $Q$ numbers representing the answers, in order, to the given questions. The numbers will be separated by a space. After the last number, print the end-of-line character.

## Constraints and clarifications

$1 \leq M \leq 2\ 10^6$

$M$ is a prime number

$1 \leq X_0, A, B < M$

$Q \leq 10^3$

$0 \leq P_i < 10^{10000}$

## Example

`sir4.in`

`7 5 21 23 5`

`0`

`1`

`2`

`3`

`4`

`sir4.out`

`7 10 2 8 15`

## Explanation

The first 5 terms of the sequence $X$ are: $7$, $10$, $2$, $8$, and $15$.