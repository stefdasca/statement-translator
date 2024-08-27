# ADN 2

Aurel is very passionate about biology. He particularly likes to analyze the structure of DNA sequences. A DNA sequence is represented as a string of characters from the set $A, G, C$, and $T$. Aurel has identified $M$ interesting DNA sequences. He would like to answer the following question: How many DNA sequences of length $N$ exist, which contain each of the $M$ DNA sequences as a subarray? Help Aurel answer this question.

## Input data

The input file `adn2.in` will contain on the first line $T$, the number of tests. Each test will contain on its first line two natural numbers, $N$ and $M$, with the meaning given in the statement. On the next $M$ lines, there will be one DNA sequence each.

## Output data

In the output file `adn2.out`, $T$ lines will be printed, with the answer for test $i$ found on line $i$, modulo $666013$.

## Constraints and clarifications

$T = 5$

$N \leq 300$

$M \leq 8$

The maximum length of a DNA sequence in the input file is $20$.

## Example

`adn2.in`

```
1
14 5
ACT
CTA
GA
AAC
ACG
```

`adn2.out`

```
545749
```