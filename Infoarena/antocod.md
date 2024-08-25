# Antocod

Antonia is a hyperactive little girl. To keep her daughter busy, Antonela, Antonia's mother, gave her a code consisting of $N$ boxes and a list of $M$ distinct numbers that she can enter into the boxes (a number can be entered into multiple boxes). For a configuration of the code, Antonela defined the antocod as the number formed by multiplying the numbers in the $N$ boxes that make up the code. Antonela asked her daughter to determine the sum of the antocods of all possible configurations, modulo $666013$. Since she is too busy preparing her daughter's birthday, she doesn't have time to do the calculations, so she asks you to tell her the answer in order to check if her daughter answered correctly. Two configurations $V_1$ and $V_2$ of the code are considered different if there is at least one box $i$ $(1 \leq i \leq N)$, for which $V_1[i] \neq V_2[i]$.

## Task

The input file `antocod.in` contains on the first line two natural numbers $N$ and $M$ representing the number of boxes and the number of distinct numbers respectively, and on the next line, $M$ natural numbers representing the numbers that can be found in the boxes of the code.

## Output data

The output file `antocod.out` will contain a single natural number, representing the answer to Antonela's query, modulo $666013$.

## Constraints and clarifications

$1 \leq N \leq 10^9$

$1 \leq M \leq 10^5$

$1 \leq X \leq 10^9$, where $X$ is a number from the list Antonela provided to Antonia.

The $M$ numbers are pairwise distinct.

## Example

`antocod.in`

```
2 3
2 3 1
```

`antocod.out`

```
36
```

## Explanation

We have the configurations:

$(2, 2) $, with a total of $4$;

$(2, 3)$, $(2, 1)$, $(3, 2)$, $(1, 2)$, with a total of $16$;

$(3, 3)$, $(3, 1)$, $(1, 3)$, $(1, 1)$, with a total of $16$.

In total, we will have: $4 + 16 + 16 = 36$.